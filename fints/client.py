import datetime
import logging
import re
from decimal import Decimal

from mt940.models import Balance
from sepaxml import SepaTransfer

from .connection import FinTSHTTPSConnection
from .dialog import FinTSDialog
from .message import FinTSMessage
from .message import FinTSResponse
from .models import SEPAAccount, TANMethod, TANChallenge6, TANChallenge5, TANChallenge3, TANChallenge4
from .segments.accounts import HKSPA
from .segments.auth import HKTAN, HKTAB
from .segments.depot import HKWPD
from .segments.saldo import HKSAL
from .segments.statement import HKKAZ
from .segments.transfer import HKCCS
from .utils import mt940_to_array, MT535_Miniparser, split_for_data_groups, split_for_data_elements, Password

logger = logging.getLogger(__name__)


class FinTS3Client:
    version = 300

    def __init__(self):
        self.accounts = []

    def _new_dialog(self):
        raise NotImplemented()

    def _new_message(self, dialog: FinTSDialog, segments):
        raise NotImplemented()

    def get_sepa_accounts(self):
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

    def get_statement(self, account, start_date, end_date):
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

    def get_balance(self, account):
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

    def get_holdings(self, account):
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

    def send_tan(self, arg):
        data = str(arg['response'])

        res = FinTSResponse(data)
        seg = res._find_segment('HITAN')
        seg = split_for_data_groups(seg)
        aref = seg[3]
        segTAN = HKTAN(3, 2, aref, '')

        self.blz = arg['dialog'].blz
        self.username = arg['dialog'].username
        self.pin = arg['dialog'].pin
        self.systemid = arg['dialog'].systemid
        self.dialogid = arg['dialog'].dialogid
        self.msgno = arg['dialog'].msgno
        self.tan_mechs = []
        self.tan_mechs = [arg['TAN-Verfahren']]
        self.pintan = ':'.join([self.pin, arg['tan']])
        msg = FinTSMessage(self.blz, self.username, self.pintan, self.systemid, self.dialogid, self.msgno, [
            segTAN
        ], self.tan_mechs)

        res = arg['dialog'].send(msg)
        arg['dialog'].end()

        return 'Ok'

    def start_simple_sepa_transfer(self, account: SEPAAccount, tan_method: TANMethod, iban: str, bic: str,
                                   recipient_name: str, amount: Decimal, account_name: str, reason: str,
                                   endtoend_id='NOTPROVIDED', tan_description=''):
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
            "execution_date": datetime.date.today(),
            "description": reason,
            "endtoend_id": endtoend_id,
        }
        sepa.add_payment(payment)
        xml = sepa.export().decode()
        return self.start_sepa_transfer(account, xml, tan_method, tan_description)

    def _get_start_sepa_transfer_message(self, dialog, account: SEPAAccount, pain_message: str, tan_description):
        segHKCCS = HKCCS(3, account, pain_message)
        segHKTAN = HKTAN(4, 4, '', tan_description)
        return self._new_message(dialog, [
            segHKCCS,
            segHKTAN
        ])

    def start_sepa_transfer(self, account: SEPAAccount, pain_message: str, tan_method, tan_description=''):
        dialog = self._new_dialog()
        dialog.sync()
        dialog.tan_mechs = [tan_method]
        dialog.init()

        with self.pin.protect():
            logger.debug('Sending HKCCS: {}'.format(self._get_start_sepa_transfer_message(
                dialog, account, pain_message, tan_description
            )))

        resp = dialog.send(self._get_start_sepa_transfer_message(dialog, account, pain_message, tan_description))
        logger.debug('Got HKCCS response: {}'.format(resp))

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
        dialog = self._new_dialog()
        dialog.sync()
        dialog.init()
        return dialog.tan_mechs

    def _create_get_tan_description_message(self, dialog: FinTSDialog):
        return self._new_message(dialog, [
            HKTAB(3)
        ])

    def get_tan_description(self):
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

    def _new_message(self, dialog: FinTSDialog, segments):
        return FinTSMessage(self.blz, self.username, self.pin, dialog.systemid, dialog.dialogid, dialog.msgno,
                            segments, dialog.tan_mechs)
