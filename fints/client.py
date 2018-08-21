import datetime
import logging
from decimal import Decimal

from fints.segments.debit import HKDME, HKDSE
from mt940.models import Balance
from sepaxml import SepaTransfer

from .connection import FinTSHTTPSConnection
from .dialog import FinTSDialog, FinTSDialogOLD
from .formals import (
    KTI1, Account3, BankIdentifier,
    SynchronisationMode, TwoStepParametersCommon,
)
from .message import FinTSMessageOLD
from .models import (
    SEPAAccount, TANChallenge, TANChallenge3,
    TANChallenge4, TANChallenge5, TANChallenge6,
)
from .security import (
    PinTanDummyEncryptionMechanism, PinTanOneStepAuthenticationMechanism,
    PinTanTwoStepAuthenticationMechanism,
)
from .segments import HIBPA3, HIRMS2, HIUPA4
from .segments.accounts import HISPA1, HKSPA, HKSPA1
from .segments.auth import HKTAB, HKTAN
from .segments.depot import HKWPD5, HKWPD6
from .segments.dialog import HISYN4, HKSYN3
from .segments.saldo import HKSAL5, HKSAL6, HKSAL7
from .segments.statement import HKKAZ5, HKKAZ6, HKKAZ7
from .segments.transfer import HKCCM, HKCCS
from .types import SegmentSequence
from .utils import MT535_Miniparser, Password, mt940_to_array

logger = logging.getLogger(__name__)

SYSTEM_ID_UNASSIGNED = '0'

class FinTS3Client:
    def __init__(self, bank_identifier, user_id, customer_id=None):
        self.accounts = []
        if isinstance(bank_identifier, BankIdentifier):
            self.bank_identifier = bank_identifier
        elif isinstance(bank_identifier, str):
            self.bank_identifier = BankIdentifier('280', bank_identifier)
        else:
            raise TypeError("bank_identifier must be BankIdentifier or str (BLZ)")
        self.system_id = SYSTEM_ID_UNASSIGNED
        self.user_id = user_id
        self.customer_id = customer_id or user_id
        self.bpd_version = 0
        self.bpa = None
        self.bpd = SegmentSequence()
        self.upd_version = 0
        self.upa = None
        self.upd = SegmentSequence()
        self.allowed_security_functions = []
        self.selected_security_function = None
        self.product_name = 'pyfints'
        self.product_version = '0.2'
        self._standing_dialog = None

    def _new_dialog(self, lazy_init=False):
        raise NotImplemented()

    def _new_message(self, dialog: FinTSDialogOLD, segments, tan=None):
        raise NotImplemented()

    def _ensure_system_id(self):
        raise NotImplemented()

    def __enter__(self):
        if self._standing_dialog:
            raise Error("Cannot double __enter__() {}".format(self))
        self._standing_dialog = self._get_dialog()
        self._standing_dialog.__enter__()

    def __exit__(self, exc_type, exc_value, traceback):
        if self._standing_dialog:
            self._standing_dialog.__exit__(exc_type, exc_value, traceback)
        else:
            raise Error("Cannot double __exit__() {}".format(self))

        self._standing_dialog = None

    def _get_dialog(self, lazy_init=False):
        if lazy_init and self._standing_dialog:
            raise Error("Cannot _get_dialog(lazy_init=True) with _standing_dialog")

        if self._standing_dialog:
            return self._standing_dialog

        if not lazy_init:
            self._ensure_system_id()

        return self._new_dialog(lazy_init=lazy_init)

    def process_institute_response(self, message):
        bpa = message.find_segment_first(HIBPA3)
        if bpa:
            self.bpa = bpa
            self.bpd_version = bpa.bpd_version
            self.bpd = SegmentSequence(
                message.find_segments(
                    callback = lambda m: len(m.header.type) == 6 and m.header.type[1] == 'I' and m.header.type[5] == 'S'
                )
            )

        upa = message.find_segment_first(HIUPA4)
        if upa:
            self.upa = upa
            self.upd_version = upa.upd_version
            self.upd = SegmentSequence(
                message.find_segments('HIUPD')
            )

        for seg in message.find_segments(HIRMS2):
            for response in seg.responses:
                if response.code == '3920':
                    self.allowed_security_functions = response.parameters
                    if self.selected_security_function is None:
                        self.selected_security_function = self.allowed_security_functions[0]

    def get_sepa_accounts(self):
        """
        Returns a list of SEPA accounts

        :return: List of SEPAAccount objects.
        """

        with self._get_dialog() as dialog:
            response = dialog.send(HKSPA1())
            
        self.accounts = []
        for seg in response.find_segments(HISPA1):
            self.accounts.extend(seg.accounts)

        return [a for a in [acc.as_sepa_account() for acc in self.accounts] if a]

    def _fetch_with_touchdowns(self, dialog, segment_factory, *args, **kwargs):
        """Execute a sequence of fetch commands on dialog.
        segment_factory must be a callable with one argument touchdown. Will be None for the
        first call and contains the institute's touchdown point on subsequent calls.
        segment_factory must return a command segment.
        Extra arguments will be passed to FinTSMessage.response_segments.
        Return value is a concatenated list of the return values of FinTSMessage.response_segments().
        """
        responses = []
        touchdown_counter = 1
        touchdown = None

        while touchdown or touchdown_counter == 1:
            seg = segment_factory(touchdown)

            rm = dialog.send(seg)

            for resp in rm.response_segments(seg, *args, **kwargs):
                responses.append(resp)

            touchdown = None
            for response in rm.responses(seg, '3040'):
                touchdown = response.parameters[0]
                break

            if touchdown:
                logger.info('Fetching more results ({})...'.format(touchdown_counter))

            touchdown_counter += 1

        return responses

    def _find_highest_supported_command(self, *segment_classes):
        """Search the BPD for the highest supported version of a segment."""
        parameter_segment_name = "{}I{}S".format(segment_classes[0].TYPE[0], segment_classes[0].TYPE[2:])
        version_map = dict((clazz.VERSION, clazz) for clazz in segment_classes)
        max_version = self.bpd.find_segment_highest_version(parameter_segment_name, version_map.keys())
        if not max_version:
            raise ValueError('No supported {} version found'.format(parameter_segment_name))

        return version_map.get(max_version.header.version)


    def get_statement(self, account: SEPAAccount, start_date: datetime.date, end_date: datetime.date):
        """
        Fetches the statement of a bank account in a certain timeframe.

        :param account: SEPA
        :param start_date: First day to fetch
        :param end_date: Last day to fetch
        :return: A list of mt940.models.Transaction objects
        """

        with self._get_dialog() as dialog:
            hkkaz = self._find_highest_supported_command(HKKAZ5, HKKAZ6, HKKAZ7)

            logger.info('Start fetching from {} to {}'.format(start_date, end_date))
            responses = self._fetch_with_touchdowns(
                dialog,
                lambda touchdown: hkkaz(
                    account=hkkaz._fields['account'].type.from_sepa_account(account),
                    all_accounts=False,
                    date_start=start_date,
                    date_end=end_date,
                    touchdown_point=touchdown,
                ),
                'HIKAZ'
            )
            logger.info('Fetching done.')

        statement = []
        for seg in responses:
            ## FIXME What is the encoding of MT940 messages?
            statement += mt940_to_array(seg.statement_booked.decode('iso-8859-1'))

        logger.debug('Statement: {}'.format(statement))

        return statement

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

            response = dialog.send(seg)

            for resp in response.response_segments(seg, 'HISAL'):
                return resp.balance_booked.as_mt940_Balance()

    def get_holdings(self, account: SEPAAccount):
        """
        Retrieve holdings of an account.

        :param account: SEPAAccount to retrieve holdings for.
        :return: List of Holding objects
        """
        # init dialog
        with self._get_dialog() as dialog:
            hkwpd = self._find_highest_supported_command(HKWPD5, HKWPD6)

            seg = hkwpd(
                account=hkwpd._fields['account'].type.from_sepa_account(account),
            )

            response = dialog.send(seg)

            for resp in response.response_segments(seg, 'HIWPD'):
                ## FIXME BROKEN
                mt535_lines = str.splitlines(resp)
                # The first line contains a FinTS HIWPD header - drop it.
                del mt535_lines[0]
                mt535 = MT535_Miniparser()
                return mt535.parse(mt535_lines)

            logger.debug('No HIWPD response segment found - maybe account has no holdings?')
            return []

    def _create_send_tan_message(self, dialog: FinTSDialogOLD, challenge: TANChallenge, tan):
        return self._new_message(dialog, [
            HKTAN(3, '2', challenge.reference, '', challenge.version)
        ], tan)

    def send_tan(self, challenge: TANChallenge, tan: str):
        """
        Sends a TAN to confirm a pending operation.

        :param challenge: TANChallenge to respond to
        :param tan: TAN value
        :return: Currently no response
        """
        if challenge.tan_process != '4':
            raise NotImplementedError("TAN process {} currently not implemented".format(challenge.tan_process))
        with self.pin.protect():
            logger.debug('Sending HKTAN: {}'.format(self._create_send_tan_message(
                challenge.dialog, challenge, tan
            )))

        resp = challenge.dialog.send(self._create_send_tan_message(
            challenge.dialog, challenge, tan
        ))
        logger.debug('Got HKTAN response: {}'.format(resp))

        challenge.dialog.end()

    def start_simple_sepa_transfer(self, account: SEPAAccount, tan_method: TwoStepParametersCommon, iban: str, bic: str,
                                   recipient_name: str, amount: Decimal, account_name: str, reason: str,
                                   endtoend_id='NOTPROVIDED', tan_description=''):
        """
        Start a simple SEPA transfer.

        :param account: SEPAAccount to start the transfer from.
        :param tan_method: TANMethod object to use.
        :param iban: Recipient's IBAN
        :param bic: Recipient's BIC
        :param recipient_name: Recipient name
        :param amount: Amount as a ``Decimal``
        :param account_name: Sender account name
        :param reason: Transfer reason
        :param endtoend_id: End-to-end-Id (defaults to ``NOTPROVIDED``)
        :param tan_description: TAN medium description (if required)
        :return: Returns a TANChallenge object
        """
        config = {
            "name": account_name,
            "IBAN": account.iban,
            "BIC": account.bic,
            "batch": False,
            "currency": "EUR",
        }
        sepa = SepaTransfer(config, 'pain.001.001.03')
        payment = {
            "name": recipient_name,
            "IBAN": iban,
            "BIC": bic,
            "amount": int(Decimal(amount) * 100),  # in cents
            "execution_date": datetime.date(1999, 1, 1),
            "description": reason,
            "endtoend_id": endtoend_id,
        }
        sepa.add_payment(payment)
        xml = sepa.export().decode()
        return self.start_sepa_transfer(account, xml, tan_method, tan_description)

    def _get_start_sepa_transfer_message(self, dialog, account: SEPAAccount, pain_message: str, tan_method,
                                         tan_description, multiple, control_sum, currency, book_as_single):
        if multiple:
            if not control_sum:
                raise ValueError("Control sum required.")
            segreq = HKCCM(3, account, pain_message, control_sum, currency, book_as_single)
        else:
            segreq = HKCCS(3, account, pain_message)
        segtan = HKTAN(4, '4', '', tan_description, tan_method.version)
        return self._new_message(dialog, [
            segreq,
            segtan
        ])

    def start_sepa_transfer(self, account: SEPAAccount, pain_message: str, tan_method, tan_description='',
                            multiple=False, control_sum=None, currency='EUR', book_as_single=False):
        """
        Start a custom SEPA transfer.

        :param account: SEPAAccount to send the transfer from.
        :param pain_message: SEPA PAIN message containing the transfer details.
        :param tan_method: TANMethod object to use.
        :param tan_description: TAN medium description (if required)
        :param multiple: Whether this message contains multiple transfers.
        :param control_sum: Sum of all transfers (required if there are multiple)
        :param currency: Transfer currency
        :param book_as_single: Kindly ask the bank to put multiple transactions as separate lines on the bank statement (defaults to ``False``)
        :return: Returns a TANChallenge object
        """
        dialog = self._get_dialog()
        dialog.sync()
        dialog.tan_mechs = [tan_method]
        dialog.init()

        with self.pin.protect():
            logger.debug('Sending: {}'.format(self._get_start_sepa_transfer_message(
                dialog, account, pain_message, tan_method, tan_description, multiple, control_sum, currency,
                book_as_single
            )))

        resp = dialog.send(self._get_start_sepa_transfer_message(
            dialog, account, pain_message, tan_method, tan_description, multiple, control_sum, currency,
            book_as_single
        ))
        logger.debug('Got response: {}'.format(resp))
        return self._tan_requiring_response(dialog, resp)

    def _get_start_sepa_debit_message(self, dialog, account: SEPAAccount, pain_message: str, tan_method,
                                      tan_description, multiple, control_sum, currency, book_as_single):
        if multiple:
            if not control_sum:
                raise ValueError("Control sum required.")
            segreq = HKDME(3, account, pain_message, control_sum, currency, book_as_single)
        else:
            segreq = HKDSE(3, account, pain_message)
        segtan = HKTAN(4, '4', '', tan_description, tan_method.version)
        return self._new_message(dialog, [
            segreq,
            segtan
        ])

    def start_sepa_debit(self, account: SEPAAccount, pain_message: str, tan_method, tan_description='',
                         multiple=False, control_sum=None, currency='EUR', book_as_single=False):
        """
        Start a custom SEPA debit.

        :param account: SEPAAccount to send the debit from.
        :param pain_message: SEPA PAIN message containing the debit details.
        :param tan_method: TANMethod object to use.
        :param tan_description: TAN medium description (if required)
        :param multiple: Whether this message contains multiple debits.
        :param control_sum: Sum of all debits (required if there are multiple)
        :param currency: Debit currency
        :param book_as_single: Kindly ask the bank to put multiple transactions as separate lines on the bank statement (defaults to ``False``)
        :return: Returns a TANChallenge object
        """
        dialog = self._get_dialog()
        dialog.sync()
        dialog.tan_mechs = [tan_method]
        dialog.init()

        with self.pin.protect():
            logger.debug('Sending: {}'.format(self._get_start_sepa_debit_message(
                dialog, account, pain_message, tan_method, tan_description, multiple, control_sum, currency,
                book_as_single
            )))

        resp = dialog.send(self._get_start_sepa_debit_message(
            dialog, account, pain_message, tan_method, tan_description, multiple, control_sum, currency,
            book_as_single
        ))
        logger.debug('Got response: {}'.format(resp))
        return self._tan_requiring_response(dialog, resp)

    def _tan_requiring_response(self, dialog, resp):
        seg = resp._find_segment('HITAN')
        if seg[0][2] == '3':
            model = TANChallenge3
        elif seg[0][2] == '4':
            model = TANChallenge4
        elif seg[0][2] == '5':
            model = TANChallenge5
        elif seg[0][2] == '6':
            model = TANChallenge6
        else:
            raise NotImplementedError(
                "HITAN segment version {} is currently not implemented".format(
                    seg[0][2]
                )
            )
        return model(dialog, *s[1:1 + len(model.args)])

    def get_tan_methods(self):
        """
        Returns a list of TAN methods.

        :return: List of TANMethod objects
        """
        dialog = self._get_dialog()
        dialog.sync()
        dialog.init()
        dialog.end()
        return dialog.tan_mechs

    def _create_get_tan_description_message(self, dialog: FinTSDialogOLD):
        return self._new_message(dialog, [
            HKTAB(3)
        ])

    def get_tan_description(self):
        """
        TAN method meta data, currently unparsed

        :return: str
        """
        dialog = self._get_dialog()
        dialog.sync()
        dialog.init()

        with self.pin.protect():
            logger.debug('Sending HKTAB: {}'.format(self._create_get_tan_description_message(dialog)))

        resp = dialog.send(self._create_get_tan_description_message(dialog))
        logger.debug('Got HKTAB response: {}'.format(resp))
        dialog.end()

        seg = resp._find_segment('HITAB')

        return seg[2]


class FinTS3PinTanClient(FinTS3Client):

    def __init__(self, bank_identifier, user_id, pin, server, customer_id=None):
        self.pin = Password(pin)
        self.connection = FinTSHTTPSConnection(server)
        super().__init__(bank_identifier=bank_identifier, user_id=user_id, customer_id=customer_id)

    def _new_dialog(self, lazy_init=False):
        if not self.selected_security_function or self.selected_security_function == '999':
            enc = PinTanDummyEncryptionMechanism(1)
            auth = PinTanOneStepAuthenticationMechanism(self.pin)
        else:
            enc = PinTanDummyEncryptionMechanism(2)
            auth = PinTanTwoStepAuthenticationMechanism(
                self,
                self.selected_security_function,
                self.pin,
            )

        return FinTSDialog(self, 
            lazy_init=lazy_init,
            enc_mechanism=enc,
            auth_mechanisms=[auth],
        )

    def _new_message(self, dialog: FinTSDialogOLD, segments, tan=None):
        return FinTSMessageOLD(self.blz, self.username, self.pin, dialog.systemid, dialog.dialogid, dialog.msgno,
                            segments, dialog.tan_mechs, tan)

    def _ensure_system_id(self):
        if self.system_id != SYSTEM_ID_UNASSIGNED:
            return

        with self._get_dialog(lazy_init=True) as dialog:
            response = dialog.init(
                HKSYN3(SynchronisationMode.NEW_SYSTEM_ID),
            )
            
        seg = response.find_segment_first(HISYN4)
        if not seg:
            raise ValueError('Could not find system_id')
        self.system_id = seg.system_id
