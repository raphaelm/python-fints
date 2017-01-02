import logging
import re

from .connection import FinTSHTTPSConnection
from .dialog import FinTSDialog
from .message import FinTSMessage
from .models import SEPAAccount
from .segments.accounts import HKSPA
from .segments.statement import HKKAZ
from .utils import mt940_to_array

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
