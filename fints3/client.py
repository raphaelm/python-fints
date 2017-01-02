import logging

from .segments.accounts import HKSPA
from .connection import FinTSHTTPSConnection
from .dialog import FinTSDialog
from .message import FinTSMessage
from .models import SEPAAccount

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
        return FinTSMessage(self.blz, self.username, self.pin, dialog.systemid, dialog.dialogid, dialog.msgno, segments)

