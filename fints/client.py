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
from .segments.depot import HKWPD
from .segments.dialog import HISYN4, HKSYN3
from .segments.saldo import HISAL5, HISAL6, HISAL7, HKSAL5, HKSAL6, HKSAL7
from .segments.statement import HKKAZ
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

    def _new_dialog(self, lazy_init=False):
        raise NotImplemented()

    def _new_message(self, dialog: FinTSDialogOLD, segments, tan=None):
        raise NotImplemented()

    def _ensure_system_id(self):
        raise NotImplemented()

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

        with self._new_dialog() as dialog:
            response = dialog.send(HKSPA1())
            
        self.accounts = []
        for seg in response.find_segments(HISPA1):
            self.accounts.extend(seg.accounts)

        return [a for a in [acc.as_sepa_account() for acc in self.accounts] if a]

    def get_statement(self, account: SEPAAccount, start_date: datetime.datetime, end_date: datetime.date):
        """
        Fetches the statement of a bank account in a certain timeframe.

        :param account: SEPA
        :param start_date: First day to fetch
        :param end_date: Last day to fetch
        :return: A list of mt940.models.Transaction objects
        """
        logger.info('Start fetching from {} to {}'.format(start_date, end_date))

        dialog = self._new_dialog()
        dialog.sync()
        dialog.init()

        def _get_msg():
            return self._create_statement_message(dialog, account, start_date, end_date, None)

        with self.pin.protect():
            logger.debug('Send message: {}'.format(_get_msg()))

        msg = _get_msg()
        resp = dialog.send(msg)
        touchdowns = resp.get_touchdowns(msg)
        responses = [resp]
        touchdown_counter = 1

        while HKKAZ.type in touchdowns:
            logger.info('Fetching more results ({})...'.format(touchdown_counter))

            with self.pin.protect():
                logger.debug('Send message: {}'.format(
                    self._create_statement_message(dialog, account, start_date, end_date, touchdowns[HKKAZ.type])
                ))

            msg = self._create_statement_message(dialog, account, start_date, end_date, touchdowns[HKKAZ.type])
            resp = dialog.send(msg)
            responses.append(resp)
            touchdowns = resp.get_touchdowns(msg)

            touchdown_counter += 1

        logger.info('Fetching done.')

        statement = []
        for resp in responses:
            seg = resp._find_segment('HIKAZ')
            ## FIXME What is the encoding of MT940 messages?
            statement += mt940_to_array(seg[1].decode('iso-8859-1'))

        logger.debug('Statement: {}'.format(statement))

        dialog.end()
        return statement

    def _create_statement_message(self, dialog: FinTSDialogOLD, account: SEPAAccount, start_date, end_date, touchdown):
        hversion = dialog.hkkazversion

        if hversion in (4, 5, 6):
            acc = ':'.join([
                account.accountnumber, account.subaccount or '', str(280), account.blz
            ])
        elif hversion == 7:
            acc = ':'.join([
                account.iban, account.bic, account.accountnumber, account.subaccount or '', str(280), account.blz
            ])
        else:
            raise ValueError('Unsupported HKKAZ version {}'.format(hversion))

        return self._new_message(dialog, [
            HKKAZ(
                3,
                hversion,
                acc,
                start_date,
                end_date,
                touchdown
            )
        ])

    def get_balance(self, account: SEPAAccount):
        """
        Fetches an accounts current balance.

        :param account: SEPA account to fetch the balance
        :return: A mt940.models.Balance object
        """

        with self._new_dialog() as dialog:
            max_hisals = self.bpd.find_segment_highest_version('HISALS', (5, 6, 7))
            if not max_hisals:
                raise ValueError('No supported HISALS version found')

            hksal = {
                5: HKSAL5,
                6: HKSAL6,
                7: HKSAL7,
            }.get(max_hisals.header.version, None)

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
        dialog = self._new_dialog()
        dialog.sync()
        dialog.init()

        # execute job
        def _get_msg():
            return self._create_get_holdings_message(dialog, account)

        with self.pin.protect():
            logger.debug('Sending HKWPD: {}'.format(_get_msg()))

        resp = dialog.send(_get_msg())
        logger.debug('Got HIWPD response: {}'.format(resp))

        # end dialog
        dialog.end()


        ## FIXME BROKEN
        # find segment and split up to balance part
        seg = resp._find_segment('HIWPD')
        if seg:
            mt535_lines = str.splitlines(seg)
            # The first line contains a FinTS HIWPD header - drop it.
            del mt535_lines[0]
            mt535 = MT535_Miniparser()
            return mt535.parse(mt535_lines)
        else:
            logger.debug('No HIWPD response segment found - maybe account has no holdings?')
            return []

    def _create_get_holdings_message(self, dialog: FinTSDialogOLD, account: SEPAAccount):
        hversion = dialog.hksalversion

        if hversion in (1, 2, 3, 4, 5, 6):
            acc = ':'.join([
                account.accountnumber, account.subaccount or '', str(280), account.blz
            ])
        elif hversion == 7:
            acc = ':'.join([
                account.iban, account.bic, account.accountnumber, account.subaccount or '', str(280), account.blz
            ])
        else:
            raise ValueError('Unsupported HKSAL version {}'.format(hversion))

        return self._new_message(dialog, [
            HKWPD(
                3,
                hversion,
                acc,
            )
        ])

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
        dialog = self._new_dialog()
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
        dialog = self._new_dialog()
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
        dialog = self._new_dialog()
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
        dialog = self._new_dialog()
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
        if not lazy_init:
            self._ensure_system_id()

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

        with self._new_dialog(lazy_init=True) as dialog:
            response = dialog.init(
                HKSYN3(SynchronisationMode.NEW_SYSTEM_ID),
            )
            
        seg = response.find_segment_first(HISYN4)
        if not seg:
            raise ValueError('Could not find system_id')
        self.system_id = seg.system_id
