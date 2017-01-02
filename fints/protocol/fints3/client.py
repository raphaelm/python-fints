from .connection import FinTSHTTPSConnection
from .dialog import FinTSDialog


class FinTS3Client:
    version = 300


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

    def get_sepa_accounts(self):
        dialog = self._new_dialog()
        dialog.sync()

