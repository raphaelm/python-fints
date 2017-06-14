import logging
import re
import datetime

from .connection import FinTSHTTPSConnection
from .dialog import FinTSDialog
from .message import FinTSMessage
from .models import SEPAAccount
from .segments.accounts import HKSPA
from .segments.statement import HKKAZ
from .segments.saldo import HKSAL
from .segments.depot import HKWPD
from .utils import mt940_to_array, MT535_Miniparser, split_for_data_groups, split_for_data_elements
from mt940.models import Balance

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

        msg_spa = self._new_message(dialog, [
            HKSPA(3, None, None, None)
        ])
        logger.debug('Sending HKSPA: {}'.format(msg_spa))
        resp = dialog.send(msg_spa)
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

        msg = self._create_statement_message(dialog, account, start_date, end_date, None)
        logger.debug('Send message: {}'.format(msg))
        resp = dialog.send(msg)
        touchdowns = resp.get_touchdowns(msg)
        responses = [resp]
        touchdown_counter = 1

        while HKKAZ.type in touchdowns:
            logger.info('Fetching more results ({})...'.format(touchdown_counter))
            msg = self._create_statement_message(dialog, account, start_date, end_date, touchdowns[HKKAZ.type])
            logger.debug('Send message: {}'.format(msg))

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
        msg = self._create_balance_message(dialog, account)
        logger.debug('Sending HKSAL: {}'.format(msg))
        resp = dialog.send(msg)
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
        msg = self._create_get_holdings_message(dialog, account)
        logger.debug('Sending HKWPD: {}'.format(msg))
        resp = dialog.send(msg)
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


class FinTS3PinTanClient(FinTS3Client):

    def __init__(self, blz, username, pin, server):
        self.username = username
        self.blz = blz
        self.pin = pin
        self.connection = FinTSHTTPSConnection(server)
        self.systemid = 0
        super().__init__()

    def _new_dialog(self):
        dialog = FinTSDialog(self.blz, self.username, self.pin, self.systemid, self.connection)
        return dialog

    def _new_message(self, dialog: FinTSDialog, segments):
        return FinTSMessage(self.blz, self.username, self.pin, dialog.systemid, dialog.dialogid, dialog.msgno,
                            segments, dialog.tan_mechs)
