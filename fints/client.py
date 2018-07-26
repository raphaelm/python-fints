import datetime
import logging
import re
from decimal import Decimal

from mt940.models import Balance
from sepaxml import SepaTransfer

from fints.segments.debit import HKDSE, HKDME
from .connection import FinTSHTTPSConnection
from .dialog import FinTSDialog
from .message import FinTSMessage
from .models import SEPAAccount, TANMethod, TANChallenge6, TANChallenge5, TANChallenge3, TANChallenge4, TANChallenge
from .segments.accounts import HKSPA
from .segments.auth import HKTAN, HKTAB
from .segments.depot import HKWPD
from .segments.saldo import HKSAL
from .segments.statement import HKKAZ
from .segments.transfer import HKCCS, HKCCM
from .utils import mt940_to_array, MT535_Miniparser, split_for_data_groups, split_for_data_elements, Password

logger = logging.getLogger(__name__)


class FinTS3Client:
    version = 300

    def __init__(self):
        self.accounts = []

    def _new_dialog(self):
        raise NotImplemented()

    def _new_message(self, dialog: FinTSDialog, segments, tan=None):
        raise NotImplemented()

    def get_sepa_accounts(self):
        """
        Returns a list of SEPA accounts

        :return: List of SEPAAccount objects.
        """
        dialog = self._new_dialog()
        dialog.sync()
        dialog.init()

        def _get_msg():
            return self._new_message(dialog, [
                HKSPA(3, None, None, None)
            ])

        with self.pin.protect():
            logger.debug('Sending HKSPA: {}'.format(_get_msg()))

        resp = dialog.send(_get_msg())
        logger.debug('Got HKSPA response: {}'.format(resp))
        dialog.end()

        accounts = resp._find_segment('HISPA')
        accountlist = accounts.split('+')[1:]
        self.accounts = []
        for acc in accountlist:
            arr = acc.split(':')
            self.accounts.append(SEPAAccount(
                iban=arr[1], bic=arr[2], accountnumber=arr[3], subaccount=arr[4], blz=arr[6]
            ))

        return self.accounts

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

        re_data = re.compile(r'[^@]*@([0-9]+)@(.+)', flags=re.MULTILINE | re.DOTALL)
        statement = []
        for resp in responses:
            seg = resp._find_segment('HIKAZ')
            if seg:
                m = re_data.match(seg)
                if m:
                    statement += mt940_to_array(m.group(2))

        logger.debug('Statement: {}'.format(statement))

        dialog.end()
        return statement

    def _create_statement_message(self, dialog: FinTSDialog, account: SEPAAccount, start_date, end_date, touchdown):
        hversion = dialog.hkkazversion

        if hversion in (4, 5, 6):
            acc = ':'.join([
                account.accountnumber, account.subaccount, str(280), account.blz
            ])
        elif hversion == 7:
            acc = ':'.join([
                account.iban, account.bic, account.accountnumber, account.subaccount, str(280), account.blz
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
        # init dialog
        dialog = self._new_dialog()
        dialog.sync()
        dialog.init()

        # execute job
        def _get_msg():
            return self._create_balance_message(dialog, account)

        with self.pin.protect():
            logger.debug('Sending HKSAL: {}'.format(_get_msg()))

        resp = dialog.send(_get_msg())
        logger.debug('Got HKSAL response: {}'.format(resp))

        # end dialog
        dialog.end()

        # find segment and split up to balance part
        seg = resp._find_segment('HISAL')
        arr = split_for_data_elements(split_for_data_groups(seg)[4])

        # get balance date
        date = datetime.datetime.strptime(arr[3], "%Y%m%d").date()

        # return balance
        return Balance(arr[0], arr[1], date, currency=arr[2])

    def _create_balance_message(self, dialog: FinTSDialog, account: SEPAAccount):
        hversion = dialog.hksalversion

        if hversion in (1, 2, 3, 4, 5, 6):
            acc = ':'.join([
                account.accountnumber, account.subaccount, str(280), account.blz
            ])
        elif hversion == 7:
            acc = ':'.join([
                account.iban, account.bic, account.accountnumber, account.subaccount, str(280), account.blz
            ])
        else:
            raise ValueError('Unsupported HKSAL version {}'.format(hversion))

        return self._new_message(dialog, [
            HKSAL(
                3,
                hversion,
                acc
            )
        ])

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

    def _create_get_holdings_message(self, dialog: FinTSDialog, account: SEPAAccount):
        hversion = dialog.hksalversion

        if hversion in (1, 2, 3, 4, 5, 6):
            acc = ':'.join([
                account.accountnumber, account.subaccount, str(280), account.blz
            ])
        elif hversion == 7:
            acc = ':'.join([
                account.iban, account.bic, account.accountnumber, account.subaccount, str(280), account.blz
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

    def _create_send_tan_message(self, dialog: FinTSDialog, challenge: TANChallenge, tan):
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

    def start_simple_sepa_transfer(self, account: SEPAAccount, tan_method: TANMethod, iban: str, bic: str,
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
        s = split_for_data_groups(seg)
        spl = split_for_data_elements(s[0])
        if spl[2] == '3':
            model = TANChallenge3
        elif spl[2] == '4':
            model = TANChallenge4
        elif spl[2] == '5':
            model = TANChallenge5
        elif spl[2] == '6':
            model = TANChallenge6
        else:
            raise NotImplementedError(
                "HITAN segment version {} is currently not implemented".format(
                    spl[2]
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

    def _create_get_tan_description_message(self, dialog: FinTSDialog):
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
        deg = split_for_data_groups(seg)

        return deg[2]


class FinTS3PinTanClient(FinTS3Client):

    def __init__(self, blz, username, pin, server):
        self.username = username
        self.blz = blz
        self.pin = Password(pin)
        self.connection = FinTSHTTPSConnection(server)
        self.systemid = 0
        super().__init__()

    def _new_dialog(self):
        dialog = FinTSDialog(self.blz, self.username, self.pin, self.systemid, self.connection)
        return dialog

    def _new_message(self, dialog: FinTSDialog, segments, tan=None):
        return FinTSMessage(self.blz, self.username, self.pin, dialog.systemid, dialog.dialogid, dialog.msgno,
                            segments, dialog.tan_mechs, tan)
