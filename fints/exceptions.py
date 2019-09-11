class FinTSError(Exception):
    pass


class FinTSClientError(FinTSError):
    pass


class FinTSClientPINError(FinTSClientError):
    pass


class FinTSClientTemporaryAuthError(FinTSClientError):
    pass


class FinTSSCARequiredError(FinTSClientError):
    pass


class FinTSDialogError(FinTSError):
    pass


class FinTSDialogStateError(FinTSDialogError):
    pass


class FinTSDialogOfflineError(FinTSDialogError):
    pass


class FinTSDialogInitError(FinTSDialogError):
    pass


class FinTSConnectionError(FinTSError):
    pass


class FinTSUnsupportedOperation(FinTSError):
    pass


class FinTSNoResponseError(FinTSError):
    pass
