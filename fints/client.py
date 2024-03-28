import datetime
import logging
from abc import ABCMeta, abstractmethod
from base64 import b64decode
from collections import OrderedDict
from contextlib import contextmanager
from decimal import Decimal
from enum import Enum

import bleach
from sepaxml import SepaTransfer

from . import version
from .connection import FinTSHTTPSConnection
from .dialog import FinTSDialog
from .exceptions import *
from .formals import (
    CUSTOMER_ID_ANONYMOUS, KTI1, BankIdentifier, DescriptionRequired,
    SynchronizationMode, TANMediaClass4, TANMediaType2,
    SupportedMessageTypes)
from .message import FinTSInstituteMessage
from .models import SEPAAccount
from .parser import FinTS3Serializer
from .security import (
    PinTanDummyEncryptionMechanism, PinTanOneStepAuthenticationMechanism,
    PinTanTwoStepAuthenticationMechanism,
)
from .segments.accounts import HISPA1, HKSPA1
from .segments.auth import HIPINS1, HKTAB4, HKTAB5, HKTAN2, HKTAN3, HKTAN5, HKTAN6, HKTAN7
from .segments.bank import HIBPA3, HIUPA4, HKKOM4
from .segments.debit import (
    HKDBS1, HKDBS2, HKDMB1, HKDMC1, HKDME1, HKDME2,
    HKDSC1, HKDSE1, HKDSE2, DebitResponseBase,
)
from .segments.depot import HKWPD5, HKWPD6
from .segments.dialog import HIRMG2, HIRMS2, HISYN4, HKSYN3
from .segments.journal import HKPRO3, HKPRO4
from .segments.saldo import HKSAL5, HKSAL6, HKSAL7
from .segments.statement import DKKKU2, HKKAZ5, HKKAZ6, HKKAZ7, HKCAZ1
from .segments.transfer import HKCCM1, HKCCS1, HKIPZ1, HKIPM1
from .types import SegmentSequence
from .utils import (
    MT535_Miniparser, Password, SubclassesMixin,
    compress_datablob, decompress_datablob, mt940_to_array,
)

logger = logging.getLogger(__name__)

SYSTEM_ID_UNASSIGNED = '0'
DATA_BLOB_MAGIC = b'python-fints_DATABLOB'
DATA_BLOB_MAGIC_RETRY = b'python-fints_RETRY_DATABLOB'


class FinTSOperations(Enum):
    """This enum is used as keys in the 'supported_operations' member of the get_information() response.

    The enum value is a tuple of transaction types ("Geschäftsvorfälle"). The operation is supported if
    any of the listed transaction types is present/allowed.
    """
    GET_BALANCE = ("HKSAL", )
    GET_TRANSACTIONS = ("HKKAZ", )
    GET_TRANSACTIONS_XML = ("HKCAZ", )
    GET_CREDIT_CARD_TRANSACTIONS = ("DKKKU", )
    GET_STATEMENT = ("HKEKA", )
    GET_STATEMENT_PDF = ("HKEKP", )
    GET_HOLDINGS = ("HKWPD", )
    GET_SEPA_ACCOUNTS = ("HKSPA", )
    GET_SCHEDULED_DEBITS_SINGLE = ("HKDBS", )
    GET_SCHEDULED_DEBITS_MULTIPLE = ("HKDMB", )
    GET_STATUS_PROTOCOL = ("HKPRO", )
    SEPA_TRANSFER_SINGLE = ("HKCCS", )
    SEPA_TRANSFER_MULTIPLE = ("HKCCM", )
    SEPA_DEBIT_SINGLE = ("HKDSE", )
    SEPA_DEBIT_MULTIPLE = ("HKDME", )
    SEPA_DEBIT_SINGLE_COR1 = ("HKDSC", )
    SEPA_DEBIT_MULTIPLE_COR1 = ("HKDMC", )
    SEPA_STANDING_DEBIT_SINGLE_CREATE = ("HKDDE", )
    GET_SEPA_STANDING_DEBITS_SINGLE = ("HKDDB", )
    SEPA_STANDING_DEBIT_SINGLE_DELETE = ("HKDDL", )


class NeedRetryResponse(SubclassesMixin, metaclass=ABCMeta):
    """Base class for Responses that need the operation to be externally retried.

    A concrete subclass of this class is returned, if an operation cannot be completed and needs a retry/completion.
    Typical (and only) example: Requiring a TAN to be provided."""

    @abstractmethod
    def get_data(self) -> bytes:
        """Return a compressed datablob representing this object.

        To restore the object, use :func:`fints.client.NeedRetryResponse.from_data`.
        """
        raise NotImplementedError

    @classmethod
    def from_data(cls, blob):
        """Restore an object instance from a compressed datablob.

        Returns an instance of a concrete subclass."""
        version, data = decompress_datablob(DATA_BLOB_MAGIC_RETRY, blob)

        if version == 1:
            for clazz in cls._all_subclasses():
                if clazz.__name__ == data["_class_name"]:
                    return clazz._from_data_v1(data)

        raise Exception("Invalid data blob data or version")


class ResponseStatus(Enum):
    """Error status of the response"""

    UNKNOWN = 0
    SUCCESS = 1  #: Response indicates Success
    WARNING = 2  #: Response indicates a Warning
    ERROR = 3  #: Response indicates an Error


_RESPONSE_STATUS_MAPPING = {
    '0': ResponseStatus.SUCCESS,
    '3': ResponseStatus.WARNING,
    '9': ResponseStatus.ERROR,
}


class TransactionResponse:
    """Result of a FinTS operation.

    The status member indicates the highest type of errors included in this Response object.
    The responses member lists all individual response lines/messages, there may be multiple (e.g. 'Message accepted' and 'Order executed').
    The data member may contain further data appropriate to the operation that was executed."""
    status = ResponseStatus
    responses = list
    data = dict

    def __init__(self, response_message):
        self.status = ResponseStatus.UNKNOWN
        self.responses = []
        self.data = {}

        for hirms in response_message.find_segments(HIRMS2):
            for resp in hirms.responses:
                self.set_status_if_higher(_RESPONSE_STATUS_MAPPING.get(resp.code[0], ResponseStatus.UNKNOWN))

    def set_status_if_higher(self, status):
        if status.value > self.status.value:
            self.status = status

    def __repr__(self):
        return "<{o.__class__.__name__}(status={o.status!r}, responses={o.responses!r}, data={o.data!r})>".format(o=self)


class FinTSClientMode(Enum):
    OFFLINE = 'offline'
    INTERACTIVE = 'interactive'


class FinTS3Client:
    def __init__(self,
                 bank_identifier, user_id, customer_id=None,
                 from_data: bytes=None,
                 product_id=None, product_version=version[:5],
                 mode=FinTSClientMode.INTERACTIVE):
        self.accounts = []
        if isinstance(bank_identifier, BankIdentifier):
            self.bank_identifier = bank_identifier
        elif isinstance(bank_identifier, str):
            self.bank_identifier = BankIdentifier(BankIdentifier.COUNTRY_ALPHA_TO_NUMERIC['DE'], bank_identifier)
        else:
            raise TypeError("bank_identifier must be BankIdentifier or str (BLZ)")
        self.system_id = SYSTEM_ID_UNASSIGNED
        if not product_id:
            raise TypeError("The product_id keyword argument is mandatory starting with python-fints version 4. See "
                            "https://python-fints.readthedocs.io/en/latest/upgrading_3_4.html for more information.")

        self.user_id = user_id
        self.customer_id = customer_id or user_id
        self.bpd_version = 0
        self.bpa = None
        self.bpd = SegmentSequence()
        self.upd_version = 0
        self.upa = None
        self.upd = SegmentSequence()
        self.product_name = product_id
        self.product_version = product_version
        self.response_callbacks = []
        self.mode = mode
        self.init_tan_response = None
        self._standing_dialog = None

        if from_data:
            self.set_data(bytes(from_data))

    def _new_dialog(self, lazy_init=False):
        raise NotImplemented()

    def _ensure_system_id(self):
        raise NotImplemented()

    def _process_response(self, dialog, segment, response):
        pass

    def process_response_message(self, dialog, message: FinTSInstituteMessage, internal_send=True):
        bpa = message.find_segment_first(HIBPA3)
        if bpa:
            self.bpa = bpa
            self.bpd_version = bpa.bpd_version
            self.bpd = SegmentSequence(
                message.find_segments(
                    callback=lambda m: len(m.header.type) == 6 and m.header.type[1] == 'I' and m.header.type[5] == 'S'
                )
            )

        upa = message.find_segment_first(HIUPA4)
        if upa:
            self.upa = upa
            self.upd_version = upa.upd_version
            self.upd = SegmentSequence(
                message.find_segments('HIUPD')
            )

        for seg in message.find_segments(HIRMG2):
            for response in seg.responses:
                if not internal_send:
                    self._log_response(None, response)

                    self._call_callbacks(None, response)

                self._process_response(dialog, None, response)

        for seg in message.find_segments(HIRMS2):
            for response in seg.responses:
                segment = None  # FIXME: Provide segment

                if not internal_send:
                    self._log_response(segment, response)

                    self._call_callbacks(segment, response)

                self._process_response(dialog, segment, response)

    def _send_with_possible_retry(self, dialog, command_seg, resume_func):
        response = dialog._send(command_seg)
        return resume_func(command_seg, response)

    def __enter__(self):
        if self._standing_dialog:
            raise Exception("Cannot double __enter__() {}".format(self))
        self._standing_dialog = self._get_dialog()
        self._standing_dialog.__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        if self._standing_dialog:
            if exc_type is not None and issubclass(exc_type, FinTSSCARequiredError):
                # In case of SCARequiredError, the dialog has already been closed by the bank
                self._standing_dialog.open = False
            else:
                self._standing_dialog.__exit__(exc_type, exc_value, traceback)
        else:
            raise Exception("Cannot double __exit__() {}".format(self))

        self._standing_dialog = None

    def _get_dialog(self, lazy_init=False):
        if lazy_init and self._standing_dialog:
            raise Exception("Cannot _get_dialog(lazy_init=True) with _standing_dialog")

        if self._standing_dialog:
            return self._standing_dialog

        if not lazy_init:
            self._ensure_system_id()

        return self._new_dialog(lazy_init=lazy_init)

    def _set_data_v1(self, data):
        self.system_id = data.get('system_id', self.system_id)

        if all(x in data for x in ('bpd_bin', 'bpa_bin', 'bpd_version')):
            if data['bpd_version'] >= self.bpd_version and data['bpa_bin']:
                self.bpd = SegmentSequence(data['bpd_bin'])
                self.bpa = SegmentSequence(data['bpa_bin']).segments[0]
                self.bpd_version = data['bpd_version']

        if all(x in data for x in ('upd_bin', 'upa_bin', 'upd_version')):
            if data['upd_version'] >= self.upd_version and data['upa_bin']:
                self.upd = SegmentSequence(data['upd_bin'])
                self.upa = SegmentSequence(data['upa_bin']).segments[0]
                self.upd_version = data['upd_version']

    def _deconstruct_v1(self, including_private=False):
        data = {
            "system_id": self.system_id,
            "bpd_bin": self.bpd.render_bytes(),
            "bpa_bin": FinTS3Serializer().serialize_message(self.bpa) if self.bpa else None,
            "bpd_version": self.bpd_version,
        }

        if including_private:
            data.update({
                "upd_bin": self.upd.render_bytes(),
                "upa_bin": FinTS3Serializer().serialize_message(self.upa) if self.upa else None,
                "upd_version": self.upd_version,
            })

        return data

    def deconstruct(self, including_private: bool=False) -> bytes:
        """Return state of this FinTSClient instance as an opaque datablob. You should not
        use this object after calling this method.

        Information about the connection is implicitly retrieved from the bank and
        cached in the FinTSClient. This includes: system identifier, bank parameter
        data, user parameter data. It's not strictly required to retain this information
        across sessions, but beneficial. If possible, an API user SHOULD use this method
        to serialize the client instance before destroying it, and provide the serialized
        data next time an instance is constructed.

        Parameter `including_private` should be set to True, if the storage is sufficiently
        secure (with regards to confidentiality) to include private data, specifically,
        account numbers and names. Most often this is the case.

        Note: No connection information is stored in the datablob, neither is the PIN.
        """
        data = self._deconstruct_v1(including_private=including_private)
        return compress_datablob(DATA_BLOB_MAGIC, 1, data)

    def set_data(self, blob: bytes):
        """Restore a datablob created with deconstruct().

        You should only call this method once, and only immediately after constructing
        the object and before calling any other method or functionality (e.g. __enter__()).
        For convenience, you can pass the `from_data` parameter to __init__()."""
        decompress_datablob(DATA_BLOB_MAGIC, blob, self)

    def _log_response(self, segment, response):
        if response.code[0] in ('0', '1'):
            log_target = logger.info
        elif response.code[0] in ('3',):
            log_target = logger.warning
        else:
            log_target = logger.error

        log_target("Dialog response: {} - {}{}".format(
            response.code,
            response.text,
            " ({!r})".format(response.parameters) if response.parameters else ""),
            extra={
                'fints_response_code': response.code,
                'fints_response_text': response.text,
                'fints_response_parameters': response.parameters,
            }
        )

    def get_information(self):
        """
        Return information about the connected bank.

        Note: Can only be filled after the first communication with the bank.
        If in doubt, use a construction like::

            f = FinTS3Client(...)
            with f:
                info = f.get_information()

        Returns a nested dictionary::

            bank:
                name: Bank Name
                supported_operations: dict(FinTSOperations -> boolean)
                supported_formats: dict(FinTSOperation -> ['urn:iso:std:iso:20022:tech:xsd:pain.001.003.03', ...])
                supported_sepa_formats: ['urn:iso:std:iso:20022:tech:xsd:pain.001.003.03', ...]
            accounts:
                - iban: IBAN
                  account_number: Account Number
                  subaccount_number: Sub-Account Number
                  bank_identifier: fints.formals.BankIdentifier(...)
                  customer_id: Customer ID
                  type: Account type
                  currency: Currency
                  owner_name: ['Owner Name 1', 'Owner Name 2 (optional)']
                  product_name: Account product name
                  supported_operations: dict(FinTSOperations -> boolean)
                - ...

        """
        retval = {
            'bank': {},
            'accounts': [],
            'auth': {},
        }
        if self.bpa:
            retval['bank']['name'] = self.bpa.bank_name
        if self.bpd.segments:
            retval['bank']['supported_operations'] = {
                op: any(self.bpd.find_segment_first(cmd[0]+'I'+cmd[2:]+'S') for cmd in op.value)
                for op in FinTSOperations
            }
            retval['bank']['supported_formats'] = {}
            for op in FinTSOperations:
                for segment in (self.bpd.find_segment_first(cmd[0] + 'I' + cmd[2:] + 'S') for cmd in op.value):
                    if not hasattr(segment, 'parameter'):
                        continue
                    formats = getattr(segment.parameter, 'supported_sepa_formats', [])
                    retval['bank']['supported_formats'][op] = list(
                        set(retval['bank']['supported_formats'].get(op, [])).union(set(formats))
                    )
            hispas = self.bpd.find_segment_first('HISPAS')
            if hispas:
                retval['bank']['supported_sepa_formats'] = list(hispas.parameter.supported_sepa_formats)
            else:
                retval['bank']['supported_sepa_formats'] = []
        if self.upd.segments:
            for upd in self.upd.find_segments('HIUPD'):
                acc = {}
                acc['iban'] = upd.iban
                acc['account_number'] = upd.account_information.account_number
                acc['subaccount_number'] = upd.account_information.subaccount_number
                acc['bank_identifier'] = upd.account_information.bank_identifier
                acc['customer_id'] = upd.customer_id
                acc['type'] = upd.account_type
                acc['currency'] = upd.account_currency
                acc['extension'] = upd.extension
                acc['owner_name'] = []
                if upd.name_account_owner_1:
                    acc['owner_name'].append(upd.name_account_owner_1)
                if upd.name_account_owner_2:
                    acc['owner_name'].append(upd.name_account_owner_2)
                acc['product_name'] = upd.account_product_name
                acc['supported_operations'] = {
                    op: any(allowed_transaction.transaction in op.value for allowed_transaction in upd.allowed_transactions)
                    for op in FinTSOperations
                }
                retval['accounts'].append(acc)
        return retval

    def _get_sepa_accounts(self, command_seg, response):
        self.accounts = []
        for seg in response.find_segments(HISPA1, throw=True):
            self.accounts.extend(seg.accounts)

        return [a for a in [acc.as_sepa_account() for acc in self.accounts] if a]

    def get_sepa_accounts(self):
        """
        Returns a list of SEPA accounts

        :return: List of SEPAAccount objects.
        """

        seg = HKSPA1()
        with self._get_dialog() as dialog:
            return self._send_with_possible_retry(dialog, seg, self._get_sepa_accounts)

    def _continue_fetch_with_touchdowns(self, command_seg, response):
        for resp in response.response_segments(command_seg, *self._touchdown_args, **self._touchdown_kwargs):
            self._touchdown_responses.append(resp)

        touchdown = None
        for response in response.responses(command_seg, '3040'):
            touchdown = response.parameters[0]
            break

        if touchdown:
            logger.info('Fetching more results ({})...'.format(self._touchdown_counter))

        self._touchdown_counter += 1
        if touchdown:
            seg = self._touchdown_segment_factory(touchdown)
            return self._send_with_possible_retry(self._touchdown_dialog, seg, self._continue_fetch_with_touchdowns)
        else:
            return self._touchdown_response_processor(self._touchdown_responses)

    def _fetch_with_touchdowns(self, dialog, segment_factory, response_processor, *args, **kwargs):
        """Execute a sequence of fetch commands on dialog.
        segment_factory must be a callable with one argument touchdown. Will be None for the
        first call and contains the institute's touchdown point on subsequent calls.
        segment_factory must return a command segment.
        response_processor can be a callable that will be passed the return value of this function and can
        return a new value instead.
        Extra arguments will be passed to FinTSMessage.response_segments.
        Return value is a concatenated list of the return values of FinTSMessage.response_segments().
        """
        self._touchdown_responses = []
        self._touchdown_counter = 1
        self._touchdown = None
        self._touchdown_dialog = dialog
        self._touchdown_segment_factory = segment_factory
        self._touchdown_response_processor = response_processor
        self._touchdown_args = args
        self._touchdown_kwargs = kwargs
        seg = segment_factory(self._touchdown)
        return self._send_with_possible_retry(dialog, seg, self._continue_fetch_with_touchdowns)

    def _find_highest_supported_command(self, *segment_classes, **kwargs):
        """Search the BPD for the highest supported version of a segment."""
        return_parameter_segment = kwargs.get("return_parameter_segment", False)

        parameter_segment_name = "{}I{}S".format(segment_classes[0].TYPE[0], segment_classes[0].TYPE[2:])
        version_map = dict((clazz.VERSION, clazz) for clazz in segment_classes)
        max_version = self.bpd.find_segment_highest_version(parameter_segment_name, version_map.keys())
        if not max_version:
            raise FinTSUnsupportedOperation('No supported {} version found. I support {}, bank supports {}.'.format(
                parameter_segment_name,
                tuple(version_map.keys()),
                tuple(v.header.version for v in self.bpd.find_segments(parameter_segment_name))
            ))

        if return_parameter_segment:
            return max_version, version_map.get(max_version.header.version)
        else:
            return version_map.get(max_version.header.version)

    def get_transactions(self, account: SEPAAccount, start_date: datetime.date = None, end_date: datetime.date = None):
        """
        Fetches the list of transactions of a bank account in a certain timeframe.

        :param account: SEPA
        :param start_date: First day to fetch
        :param end_date: Last day to fetch
        :return: A list of mt940.models.Transaction objects
        """

        with self._get_dialog() as dialog:
            hkkaz = self._find_highest_supported_command(HKKAZ5, HKKAZ6, HKKAZ7)

            logger.info('Start fetching from {} to {}'.format(start_date, end_date))
            response = self._fetch_with_touchdowns(
                dialog,
                lambda touchdown: hkkaz(
                    account=hkkaz._fields['account'].type.from_sepa_account(account),
                    all_accounts=False,
                    date_start=start_date,
                    date_end=end_date,
                    touchdown_point=touchdown,
                ),
                lambda responses: mt940_to_array(''.join([seg.statement_booked.decode('iso-8859-1') for seg in responses])),
                'HIKAZ',
                # Note 1: Some banks send the HIKAZ data in arbitrary splits.
                # So better concatenate them before MT940 parsing.
                # Note 2: MT940 messages are encoded in the S.W.I.F.T character set,
                # which is a subset of ISO 8859. There are no character in it that
                # differ between ISO 8859 variants, so we'll arbitrarily chose 8859-1.
            )
            logger.info('Fetching done.')

        return response

    @staticmethod
    def _response_handler_get_transactions_xml(responses):
        booked_streams = []
        pending_streams = []
        for seg in responses:
            booked_streams.extend(seg.statement_booked.camt_statements)
            pending_streams.append(seg.statement_pending)
        return booked_streams, pending_streams

    def get_transactions_xml(self, account: SEPAAccount, start_date: datetime.date = None,
                             end_date: datetime.date = None) -> list:
        """
        Fetches the list of transactions of a bank account in a certain timeframe as camt.052.001.02 XML files.
        Returns both booked and pending transactions.

        :param account: SEPA
        :param start_date: First day to fetch
        :param end_date: Last day to fetch
        :return: Two lists of bytestrings containing XML documents, possibly empty: first one for booked transactions,
            second for pending transactions
        """

        with self._get_dialog() as dialog:
            hkcaz = self._find_highest_supported_command(HKCAZ1)

            logger.info('Start fetching from {} to {}'.format(start_date, end_date))
            responses = self._fetch_with_touchdowns(
                dialog,
                lambda touchdown: hkcaz(
                    account=hkcaz._fields['account'].type.from_sepa_account(account),
                    all_accounts=False,
                    date_start=start_date,
                    date_end=end_date,
                    touchdown_point=touchdown,
                    supported_camt_messages=SupportedMessageTypes(['urn:iso:std:iso:20022:tech:xsd:camt.052.001.02']),
                ),
                FinTS3Client._response_handler_get_transactions_xml,
                'HICAZ'
            )
            logger.info('Fetching done.')

        return responses

    def get_credit_card_transactions(self, account: SEPAAccount, credit_card_number: str, start_date: datetime.date = None, end_date: datetime.date = None):
        # FIXME Reverse engineered, probably wrong
        with self._get_dialog() as dialog:
            dkkku = self._find_highest_supported_command(DKKKU2)

            responses = self._fetch_with_touchdowns(
                dialog,
                lambda touchdown: dkkku(
                    account=dkkku._fields['account'].type.from_sepa_account(account) if account else None,
                    credit_card_number=credit_card_number,
                    date_start=start_date,
                    date_end=end_date,
                    touchdown_point=touchdown,
                ),
                lambda responses: responses,
                'DIKKU'
            )

        return responses

    def _get_balance(self, command_seg, response):
        for resp in response.response_segments(command_seg, 'HISAL'):
            return resp.balance_booked.as_mt940_Balance()

    def get_balance(self, account: SEPAAccount):
        """
        Fetches an accounts current balance.

        :param account: SEPA account to fetch the balance
        :return: A mt940.models.Balance object
        """

        with self._get_dialog() as dialog:
            hksal = self._find_highest_supported_command(HKSAL5, HKSAL6, HKSAL7)

            seg = hksal(
                account=hksal._fields['account'].type.from_sepa_account(account),
                all_accounts=False,
            )

            response = self._send_with_possible_retry(dialog, seg, self._get_balance)
            return response

    def get_holdings(self, account: SEPAAccount):
        """
        Retrieve holdings of an account.

        :param account: SEPAAccount to retrieve holdings for.
        :return: List of Holding objects
        """
        # init dialog
        with self._get_dialog() as dialog:
            hkwpd = self._find_highest_supported_command(HKWPD5, HKWPD6)

            responses = self._fetch_with_touchdowns(
                dialog,
                lambda touchdown: hkwpd(
                    account=hkwpd._fields['account'].type.from_sepa_account(account),
                    touchdown_point=touchdown,
                ),
                lambda responses: responses,  # TODO
                'HIWPD'
            )

        if isinstance(responses, NeedTANResponse):
            return responses

        holdings = []
        for resp in responses:
            if type(resp.holdings) == bytes:
                holding_str = resp.holdings.decode()
            else:
                holding_str = resp.holdings

            mt535_lines = str.splitlines(holding_str)
            # The first line is empty - drop it.
            del mt535_lines[0]
            mt535 = MT535_Miniparser()
            holdings.extend(mt535.parse(mt535_lines))

        if not holdings:
            logger.debug('No HIWPD response segment found - maybe account has no holdings?')
        return holdings

    def get_scheduled_debits(self, account: SEPAAccount, multiple=False):
        with self._get_dialog() as dialog:
            if multiple:
                command_classes = (HKDMB1, )
                response_type = "HIDMB"
            else:
                command_classes = (HKDBS1, HKDBS2)
                response_type = "HKDBS"

            hkdbs = self._find_highest_supported_command(*command_classes)

            responses = self._fetch_with_touchdowns(
                dialog,
                lambda touchdown: hkdbs(
                    account=hkdbs._fields['account'].type.from_sepa_account(account),
                    touchdown_point=touchdown,
                ),
                lambda responses: responses,
                response_type,
            )

        return responses

    def get_status_protocol(self):
        with self._get_dialog() as dialog:
            hkpro = self._find_highest_supported_command(HKPRO3, HKPRO4)

            responses = self._fetch_with_touchdowns(
                dialog,
                lambda touchdown: hkpro(
                    touchdown_point=touchdown,
                ),
                lambda responses: responses,
                'HIPRO',
            )

        return responses

    def get_communication_endpoints(self):
        with self._get_dialog() as dialog:
            hkkom = self._find_highest_supported_command(HKKOM4)

            responses = self._fetch_with_touchdowns(
                dialog,
                lambda touchdown: hkkom(
                    touchdown_point=touchdown,
                ),
                lambda responses: responses,
                'HIKOM'
            )

        return responses

    def _find_supported_sepa_version(self, candidate_versions):
        hispas = self.bpd.find_segment_first('HISPAS')
        if not hispas:
            logger.warning("Could not determine supported SEPA versions, is the dialogue open? Defaulting to first candidate: %s.", candidate_versions[0])
            return candidate_versions[0]

        bank_supported = list(hispas.parameter.supported_sepa_formats)

        for candidate in candidate_versions:
            if "urn:iso:std:iso:20022:tech:xsd:{}".format(candidate) in bank_supported:
                return candidate
            if "urn:iso:std:iso:20022:tech:xsd:{}.xsd".format(candidate) in bank_supported:
                return candidate

        logger.warning("No common supported SEPA version. Defaulting to first candidate and hoping for the best: %s.", candidate_versions[0])
        return candidate_versions[0]

    def simple_sepa_transfer(self, account: SEPAAccount, iban: str, bic: str,
                             recipient_name: str, amount: Decimal, account_name: str, reason: str, instant_payment=False,
                             endtoend_id='NOTPROVIDED'):
        """
        Simple SEPA transfer.

        :param account: SEPAAccount to start the transfer from.
        :param iban: Recipient's IBAN
        :param bic: Recipient's BIC
        :param recipient_name: Recipient name
        :param amount: Amount as a ``Decimal``
        :param account_name: Sender account name
        :param reason: Transfer reason
        :param instant_payment: Whether to use instant payment (defaults to ``False``)
        :param endtoend_id: End-to-end-Id (defaults to ``NOTPROVIDED``)
        :return: Returns either a NeedRetryResponse or TransactionResponse
        """
        config = {
            "name": account_name,
            "IBAN": account.iban,
            "BIC": account.bic,
            "batch": False,
            "currency": "EUR",
        }
        version = self._find_supported_sepa_version(['pain.001.001.03', 'pain.001.003.03'])
        sepa = SepaTransfer(config, version)
        payment = {
            "name": recipient_name,
            "IBAN": iban,
            "BIC": bic,
            "amount": round(Decimal(amount) * 100),  # in cents
            "execution_date": datetime.date(1999, 1, 1),
            "description": reason,
            "endtoend_id": endtoend_id,
        }
        sepa.add_payment(payment)
        xml = sepa.export().decode()
        return self.sepa_transfer(account, xml, pain_descriptor="urn:iso:std:iso:20022:tech:xsd:"+version, instant_payment=instant_payment)

    def sepa_transfer(self, account: SEPAAccount, pain_message: str, multiple=False,
                      control_sum=None, currency='EUR', book_as_single=False,
                      pain_descriptor='urn:iso:std:iso:20022:tech:xsd:pain.001.001.03', instant_payment=False):
        """
        Custom SEPA transfer.

        :param account: SEPAAccount to send the transfer from.
        :param pain_message: SEPA PAIN message containing the transfer details.
        :param multiple: Whether this message contains multiple transfers.
        :param control_sum: Sum of all transfers (required if there are multiple)
        :param currency: Transfer currency
        :param book_as_single: Kindly ask the bank to put multiple transactions as separate lines on the bank statement (defaults to ``False``)
        :param pain_descriptor: URN of the PAIN message schema used.
        :param instant_payment: Whether this is an instant transfer (defaults to ``False``)
        :return: Returns either a NeedRetryResponse or TransactionResponse
        """

        with self._get_dialog() as dialog:
            if multiple:
                command_class = HKIPM1 if instant_payment else HKCCM1
            else:
                command_class = HKIPZ1 if instant_payment else HKCCS1

            hiccxs, hkccx = self._find_highest_supported_command(
                command_class,
                return_parameter_segment=True
            )

            seg = hkccx(
                account=hkccx._fields['account'].type.from_sepa_account(account),
                sepa_descriptor=pain_descriptor,
                sepa_pain_message=pain_message.encode(),
            )

            # if instant_payment:
            #     seg.allow_convert_sepa_transfer = True

            if multiple:
                if hiccxs.parameter.sum_amount_required and control_sum is None:
                    raise ValueError("Control sum required.")
                if book_as_single and not hiccxs.parameter.single_booking_allowed:
                    raise FinTSUnsupportedOperation("Single booking not allowed by bank.")

                if control_sum:
                    seg.sum_amount.amount = control_sum
                    seg.sum_amount.currency = currency

                if book_as_single:
                    seg.request_single_booking = True

            return self._send_with_possible_retry(dialog, seg, self._continue_sepa_transfer)

    def _continue_sepa_transfer(self, command_seg, response):
        retval = TransactionResponse(response)

        for seg in response.find_segments(HIRMS2):
            for resp in seg.responses:
                retval.set_status_if_higher(_RESPONSE_STATUS_MAPPING.get(resp.code[0], ResponseStatus.UNKNOWN))
                retval.responses.append(resp)

        return retval

    def _continue_dialog_initialization(self, command_seg, response):
        return response

    def sepa_debit(self, account: SEPAAccount, pain_message: str, multiple=False, cor1=False,
                   control_sum=None, currency='EUR', book_as_single=False,
                   pain_descriptor='urn:iso:std:iso:20022:tech:xsd:pain.008.003.01'):
        """
        Custom SEPA debit.

        :param account: SEPAAccount to send the debit from.
        :param pain_message: SEPA PAIN message containing the debit details.
        :param multiple: Whether this message contains multiple debits.
        :param cor1: Whether to use COR1 debit (lead time reduced to 1 day)
        :param control_sum: Sum of all debits (required if there are multiple)
        :param currency: Debit currency
        :param book_as_single: Kindly ask the bank to put multiple transactions as separate lines on the bank statement (defaults to ``False``)
        :param pain_descriptor: URN of the PAIN message schema used. Defaults to ``urn:iso:std:iso:20022:tech:xsd:pain.008.003.01``.
        :return: Returns either a NeedRetryResponse or TransactionResponse (with data['task_id'] set, if available)
        """

        with self._get_dialog() as dialog:
            if multiple:
                if cor1:
                    command_candidates = (HKDMC1, )
                else:
                    command_candidates = (HKDME1, HKDME2)
            else:
                if cor1:
                    command_candidates = (HKDSC1, )
                else:
                    command_candidates = (HKDSE1, HKDSE2)

            hidxxs, hkdxx = self._find_highest_supported_command(
                *command_candidates,
                return_parameter_segment=True
            )

            seg = hkdxx(
                account=hkdxx._fields['account'].type.from_sepa_account(account),
                sepa_descriptor=pain_descriptor,
                sepa_pain_message=pain_message.encode(),
            )

            if multiple:
                if hidxxs.parameter.sum_amount_required and control_sum is None:
                    raise ValueError("Control sum required.")
                if book_as_single and not hidxxs.parameter.single_booking_allowed:
                    raise FinTSUnsupportedOperation("Single booking not allowed by bank.")

                if control_sum:
                    seg.sum_amount.amount = control_sum
                    seg.sum_amount.currency = currency

                if book_as_single:
                    seg.request_single_booking = True

            return self._send_with_possible_retry(dialog, seg, self._continue_sepa_debit)

    def _continue_sepa_debit(self, command_seg, response):
        retval = TransactionResponse(response)

        for seg in response.find_segments(HIRMS2):
            for resp in seg.responses:
                retval.set_status_if_higher(_RESPONSE_STATUS_MAPPING.get(resp.code[0], ResponseStatus.UNKNOWN))
                retval.responses.append(resp)

        for seg in response.find_segments(DebitResponseBase):
            if seg.task_id:
                retval.data['task_id'] = seg.task_id

        if not 'task_id' in retval.data:
            for seg in response.find_segments('HITAN'):
                if hasattr(seg, 'task_reference') and seg.task_reference:
                    retval.data['task_id'] = seg.task_reference

        return retval

    def add_response_callback(self, cb):
        # FIXME document
        self.response_callbacks.append(cb)

    def remove_response_callback(self, cb):
        # FIXME document
        self.response_callbacks.remove(cb)

    def set_product(self, product_name, product_version):
        """Set the product name and version that is transmitted as part of our identification

        According to 'FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals',
        version 3.0, section C.3.1.3, you should fill this with useful information about the
        end-user product, *NOT* the FinTS library."""

        self.product_name = product_name
        self.product_version = product_version

    def _call_callbacks(self, *cb_data):
        for cb in self.response_callbacks:
            cb(*cb_data)

    def pause_dialog(self):
        """Pause a standing dialog and return the saved dialog state.

        Sometimes, for example in a web app, it's not possible to keep a context open
        during user input. In some cases, though, it's required to send a response
        within the same dialog that issued the original task (f.e. TAN with TANTimeDialogAssociation.NOT_ALLOWED).
        This method freezes the current standing dialog (started with FinTS3Client.__enter__()) and
        returns the frozen state.

        Commands MUST NOT be issued in the dialog after calling this method.

        MUST be used in conjunction with deconstruct()/set_data().

        Caller SHOULD ensure that the dialog is resumed (and properly ended) within a reasonable amount of time.

        :Example:

        ::

            client = FinTS3PinTanClient(..., from_data=None)
            with client:
                challenge = client.sepa_transfer(...)

                dialog_data = client.pause_dialog()

                # dialog is now frozen, no new commands may be issued
                # exiting the context does not end the dialog

            client_data = client.deconstruct()

            # Store dialog_data and client_data out-of-band somewhere
            # ... Some time passes ...
            # Later, possibly in a different process, restore the state

            client = FinTS3PinTanClient(..., from_data=client_data)
            with client.resume_dialog(dialog_data):
                client.send_tan(...)

                # Exiting the context here ends the dialog, unless frozen with pause_dialog() again.
        """
        if not self._standing_dialog:
            raise Exception("Cannot pause dialog, no standing dialog exists")
        return self._standing_dialog.pause()

    @contextmanager
    def resume_dialog(self, dialog_data):
        # FIXME document, test,    NOTE NO UNTRUSTED SOURCES
        if self._standing_dialog:
            raise Exception("Cannot resume dialog, existing standing dialog")
        self._standing_dialog = FinTSDialog.create_resume(self, dialog_data)
        with self._standing_dialog:
            yield self
        self._standing_dialog = None


class NeedTANResponse(NeedRetryResponse):
    challenge_raw = None  #: Raw challenge as received by the bank
    challenge = None  #: Textual challenge to be displayed to the user
    challenge_html = None  #: HTML-safe challenge text, possibly with formatting
    challenge_hhduc = None  #: HHD_UC challenge to be transmitted to the TAN generator
    challenge_matrix = None  #: Matrix code challenge: tuple(mime_type, data)
    decoupled = None  #: Use decoupled process

    def __init__(self, command_seg, tan_request, resume_method=None, tan_request_structured=False, decoupled=False):
        self.command_seg = command_seg
        self.tan_request = tan_request
        self.tan_request_structured = tan_request_structured
        self.decoupled = decoupled
        if hasattr(resume_method, '__func__'):
            self.resume_method = resume_method.__func__.__name__
        else:
            self.resume_method = resume_method
        self._parse_tan_challenge()

    def __repr__(self):
        return '<o.__class__.__name__(command_seg={o.command_seg!r}, tan_request={o.tan_request!r})>'.format(o=self)

    @classmethod
    def _from_data_v1(cls, data):
        if data["version"] == 1:
            if "init_tan" in data:
                segs = SegmentSequence(data['segments_bin']).segments
                return cls(None, segs[0], data['resume_method'], data['tan_request_structured'])
            else:
                segs = SegmentSequence(data['segments_bin']).segments
                return cls(segs[0], segs[1], data['resume_method'], data['tan_request_structured'])

        raise Exception("Wrong blob data version")

    def get_data(self) -> bytes:
        """Return a compressed datablob representing this object.

        To restore the object, use :func:`fints.client.NeedRetryResponse.from_data`.
        """
        if self.command_seg:
            data = {
                "_class_name": self.__class__.__name__,
                "version": 1,
                "segments_bin": SegmentSequence([self.command_seg, self.tan_request]).render_bytes(),
                "resume_method": self.resume_method,
                "tan_request_structured": self.tan_request_structured,
            }
        else:
            data = {
                "_class_name": self.__class__.__name__,
                "version": 1,
                "init_tan": True,
                "segments_bin": SegmentSequence([self.tan_request]).render_bytes(),
                "resume_method": self.resume_method,
                "tan_request_structured": self.tan_request_structured,
            }
        return compress_datablob(DATA_BLOB_MAGIC_RETRY, 1, data)

    def _parse_tan_challenge(self):
        self.challenge_raw = self.tan_request.challenge
        self.challenge = self.challenge_raw
        self.challenge_html = None
        self.challenge_hhduc = None
        self.challenge_matrix = None

        if hasattr(self.tan_request, 'challenge_hhduc'):
            if self.tan_request.challenge_hhduc:
                if len(self.tan_request.challenge_hhduc) < 256:
                    self.challenge_hhduc = self.tan_request.challenge_hhduc.decode('us-ascii')
                else:
                    data = self.tan_request.challenge_hhduc
                    type_len_field, data = data[:2], data[2:]
                    if len(type_len_field) == 2:
                        type_len = type_len_field[0]*256 + type_len_field[1]
                        type_data, data = data[:type_len], data[type_len:]

                        content_len_field, data = data[:2], data[2:]
                        if len(content_len_field) == 2:
                            content_len = content_len_field[0]*256 + content_len_field[1]
                            content_data, data = data[:content_len], data[content_len:]

                            self.challenge_matrix = (type_data.decode('us-ascii', 'replace'), content_data)

        if self.challenge.startswith('CHLGUC  '):
            l = self.challenge[8:12]
            if l.isdigit():
                self.challenge_hhduc = self.challenge[12:(12+int(l,10))]
                self.challenge = self.challenge[(12+int(l,10)):]

                if self.challenge_hhduc.startswith('iVBO'):
                    self.challenge_matrix = ('image/png', b64decode(self.challenge_hhduc))
                    self.challenge_hhduc = None

        if self.challenge.startswith('CHLGTEXT'):
            self.challenge = self.challenge[12:]

        if self.tan_request_structured:
            self.challenge_html = bleach.clean(
                self.challenge,
                tags=['br', 'p', 'b', 'i', 'u', 'ul', 'ol', 'li'],
                attributes={},
            )
        else:
            self.challenge_html = bleach.clean(self.challenge, tags=[])


# Note: Implementing HKTAN#6 implies support for Strong Customer Authentication (SCA)
#  which may require TANs for many more operations including dialog initialization.
#  We do not currently support that.
IMPLEMENTED_HKTAN_VERSIONS = {
    2: HKTAN2,
    3: HKTAN3,
    5: HKTAN5,
    6: HKTAN6,
    7: HKTAN7,
}


class FinTS3PinTanClient(FinTS3Client):

    def __init__(self, bank_identifier, user_id, pin, server, customer_id=None, *args, **kwargs):
        self.pin = Password(pin) if pin is not None else pin
        self._pending_tan = None
        self.connection = FinTSHTTPSConnection(server)
        self.allowed_security_functions = []
        self.selected_security_function = None
        self.selected_tan_medium = None
        self._bootstrap_mode = True
        super().__init__(bank_identifier=bank_identifier, user_id=user_id, customer_id=customer_id, *args, **kwargs)

    def _new_dialog(self, lazy_init=False):
        if self.pin is None:
            enc = None
            auth = []
        elif not self.selected_security_function or self.selected_security_function == '999':
            enc = PinTanDummyEncryptionMechanism(1)
            auth = [PinTanOneStepAuthenticationMechanism(self.pin)]
        else:
            enc = PinTanDummyEncryptionMechanism(2)
            auth = [PinTanTwoStepAuthenticationMechanism(
                self,
                self.selected_security_function,
                self.pin,
            )]

        return FinTSDialog(
            self,
            lazy_init=lazy_init,
            enc_mechanism=enc,
            auth_mechanisms=auth,
        )

    def fetch_tan_mechanisms(self):
        self.set_tan_mechanism('999')
        self._ensure_system_id()
        if self.get_current_tan_mechanism():
            # We already got a reply through _ensure_system_id
            return self.get_current_tan_mechanism()
        with self._new_dialog():
            return self.get_current_tan_mechanism()

    def _ensure_system_id(self):
        if self.system_id != SYSTEM_ID_UNASSIGNED or self.user_id == CUSTOMER_ID_ANONYMOUS:
            return

        with self._get_dialog(lazy_init=True) as dialog:
            response = dialog.init(
                HKSYN3(SynchronizationMode.NEW_SYSTEM_ID),
            )
            self.process_response_message(dialog, response, internal_send=True)
            seg = response.find_segment_first(HISYN4)
            if not seg:
                raise ValueError('Could not find system_id')
            self.system_id = seg.system_id

    def _set_data_v1(self, data):
        super()._set_data_v1(data)
        self.selected_tan_medium = data.get('selected_tan_medium', self.selected_tan_medium)
        self.selected_security_function = data.get('selected_security_function', self.selected_security_function)
        self.allowed_security_functions = data.get('allowed_security_functions', self.allowed_security_functions)

    def _deconstruct_v1(self, including_private=False):
        data = super()._deconstruct_v1(including_private=including_private)
        data.update({
            "selected_security_function": self.selected_security_function,
            "selected_tan_medium": self.selected_tan_medium,
        })

        if including_private:
            data.update({
                "allowed_security_functions": self.allowed_security_functions,
            })

        return data

    def is_tan_media_required(self):
        tan_mechanism = self.get_tan_mechanisms()[self.get_current_tan_mechanism()]
        return getattr(tan_mechanism, 'supported_media_number', None) is not None and \
                tan_mechanism.supported_media_number > 1 and \
                tan_mechanism.description_required == DescriptionRequired.MUST

    def _get_tan_segment(self, orig_seg, tan_process, tan_seg=None):
        tan_mechanism = self.get_tan_mechanisms()[self.get_current_tan_mechanism()]

        hktan = IMPLEMENTED_HKTAN_VERSIONS.get(tan_mechanism.VERSION)

        seg = hktan(tan_process=tan_process)

        if tan_process == '1':
            seg.segment_type = orig_seg.header.type
            account_ = getattr(orig_seg, 'account', None)
            if isinstance(account_, KTI1):
                seg.account = account_
            raise NotImplementedError("TAN-Process 1 not implemented")

        if tan_process in ('1', '3', '4') and self.is_tan_media_required():
            if self.selected_tan_medium:
                seg.tan_medium_name = self.selected_tan_medium
            else:
                seg.tan_medium_name = 'DUMMY'

        if tan_process == '4' and tan_mechanism.VERSION >= 6:
            seg.segment_type = orig_seg.header.type

        if tan_process in ('2', '3', 'S'):
            seg.task_reference = tan_seg.task_reference

        if tan_process in ('1', '2', 'S'):
            seg.further_tan_follows = False

        return seg

    def _need_twostep_tan_for_segment(self, seg):
        if not self.selected_security_function or self.selected_security_function == '999':
            return False
        else:
            hipins = self.bpd.find_segment_first(HIPINS1)
            if not hipins:
                return False
            else:
                for requirement in hipins.parameter.transaction_tans_required:
                    if seg.header.type == requirement.transaction:
                        return requirement.tan_required

        return False

    def _send_with_possible_retry(self, dialog, command_seg, resume_func):
        with dialog:
            if self._need_twostep_tan_for_segment(command_seg):
                tan_seg = self._get_tan_segment(command_seg, '4')

                response = dialog.send(command_seg, tan_seg)

                for resp in response.responses(tan_seg):
                    if resp.code in ('0030', '3955'):
                        return NeedTANResponse(
                            command_seg,
                            response.find_segment_first('HITAN'),
                            resume_func,
                            self.is_challenge_structured(),
                            resp.code == '3955',
                        )
                    if resp.code.startswith('9'):
                        raise Exception("Error response: {!r}".format(response))
            else:
                response = dialog.send(command_seg)

            return resume_func(command_seg, response)

    def is_challenge_structured(self):
        param = self.get_tan_mechanisms()[self.get_current_tan_mechanism()]
        if hasattr(param, 'challenge_structured'):
            return param.challenge_structured
        return False

    def send_tan(self, challenge: NeedTANResponse, tan: str):
        """
        Sends a TAN to confirm a pending operation.

        If ``NeedTANResponse.decoupled`` is ``True``, the ``tan`` parameter is ignored and can be kept empty.
        If the operation was not yet confirmed using the decoupled app, this method will again return a
        ``NeedTANResponse``.

        :param challenge: NeedTANResponse to respond to
        :param tan: TAN value
        :return: New response after sending TAN
        """

        with self._get_dialog() as dialog:
            if challenge.decoupled:
                tan_seg = self._get_tan_segment(challenge.command_seg, 'S', challenge.tan_request)
            else:
                tan_seg = self._get_tan_segment(challenge.command_seg, '2', challenge.tan_request)
                self._pending_tan = tan

            response = dialog.send(tan_seg)

            if challenge.decoupled:
                # TAN process = S
                status_segment = response.find_segment_first('HITAN')
                if not status_segment:
                    raise FinTSClientError(
                        "No TAN status received."
                    )
                for resp in response.responses(tan_seg):
                    if resp.code == '3956':
                        return NeedTANResponse(
                            challenge.command_seg,
                            challenge.tan_request,
                            challenge.resume_method,
                            challenge.tan_request_structured,
                            challenge.decoupled,
                        )

            resume_func = getattr(self, challenge.resume_method)
            return resume_func(challenge.command_seg, response)

    def _process_response(self, dialog, segment, response):
        if response.code == '3920':
            self.allowed_security_functions = list(response.parameters)
            if self.selected_security_function is None or not self.selected_security_function in self.allowed_security_functions:
                # Select the first available twostep security_function that we support
                for security_function, parameter in self.get_tan_mechanisms().items():
                    if security_function == '999':
                        # Skip onestep TAN
                        continue
                    if parameter.tan_process != '2':
                        # Only support process variant 2 for now
                        continue
                    try:
                        self.set_tan_mechanism(parameter.security_function)
                        break
                    except NotImplementedError:
                        pass
                else:
                    # Fall back to onestep
                    self.set_tan_mechanism('999')

        if response.code == '9010':
            raise FinTSClientError("Error during dialog initialization, could not fetch BPD. Please check that you "
                                   "passed the correct bank identifier to the HBCI URL of the correct bank.")

        if ((not dialog.open and response.code.startswith('9')) and not self._bootstrap_mode)  or response.code in ('9340', '9910', '9930', '9931', '9942'):
            # Assume all 9xxx errors in a not-yet-open dialog refer to the PIN or authentication
            # During a dialog also listen for the following codes which may explicitly indicate an
            # incorrect pin: 9340, 9910, 9930, 9931, 9942
            # Fail-safe block all further attempts with this PIN
            if self.pin:
                self.pin.block()
            raise FinTSClientPINError("Error during dialog initialization, PIN wrong?")

        if response.code == '3938':
            # Account locked, e.g. after three wrong password attempts. Theoretically, the bank might allow us to
            # send a HKPSA with a TAN to unlock, but since the library currently doesn't implement it and there's only
            # one chance to get it right, let's rather error iout.
            if self.pin:
                self.pin.block()
            raise FinTSClientTemporaryAuthError("Account is temporarily locked.")

        if response.code == '9075':
            if self._bootstrap_mode:
                if self._standing_dialog:
                    self._standing_dialog.open = False
            else:
                raise FinTSSCARequiredError("This operation requires strong customer authentication.")

    def get_tan_mechanisms(self):
        """
        Get the available TAN mechanisms.

        Note: Only checks for HITANS versions listed in IMPLEMENTED_HKTAN_VERSIONS.

        :return: Dictionary of security_function: TwoStepParameters objects.
        """

        retval = OrderedDict()

        for version in sorted(IMPLEMENTED_HKTAN_VERSIONS.keys()):
            for seg in self.bpd.find_segments('HITANS', version):
                for parameter in seg.parameter.twostep_parameters:
                    if parameter.security_function in self.allowed_security_functions:
                        retval[parameter.security_function] = parameter

        return retval

    def get_current_tan_mechanism(self):
        return self.selected_security_function

    def set_tan_mechanism(self, security_function):
        if self._standing_dialog:
            raise Exception("Cannot change TAN mechanism with a standing dialog")
        self.selected_security_function = security_function

    def set_tan_medium(self, tan_medium):
        if self._standing_dialog:
            raise Exception("Cannot change TAN medium with a standing dialog")
        self.selected_tan_medium = tan_medium.tan_medium_name

    def get_tan_media(self, media_type = TANMediaType2.ALL, media_class = TANMediaClass4.ALL):
        """Get information about TAN lists/generators.

        Returns tuple of fints.formals.TANUsageOption and a list of fints.formals.TANMedia4 or fints.formals.TANMedia5 objects."""
        if self.connection.url == 'https://hbci.postbank.de/banking/hbci.do':
            # see https://github.com/raphaelm/python-fints/issues/101#issuecomment-572486099
            context = self._new_dialog(lazy_init=True)
            method = lambda dialog: dialog.init
        else:
            context = self._get_dialog()
            method = lambda dialog: dialog.send


        with context as dialog:
            hktab = self._find_highest_supported_command(HKTAB4, HKTAB5)

            seg = hktab(
                tan_media_type=media_type,
                tan_media_class=str(media_class),
            )
            # The specification says we should send a dummy HKTAN object but apparently it seems to do more harm than
            # good.

            try:
                self._bootstrap_mode = True
                response = method(dialog)(seg)
            finally:
                self._bootstrap_mode = False

            for resp in response.response_segments(seg, 'HITAB'):
                return resp.tan_usage_option, list(resp.tan_media_list)

    def get_information(self):
        retval = super().get_information()
        retval['auth'] = {
            'current_tan_mechanism': self.get_current_tan_mechanism(),
            'tan_mechanisms': self.get_tan_mechanisms(),
        }
        return retval
