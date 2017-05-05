from . import FinTS3Segment


class HKSAL(FinTS3Segment):
    """
    HKSAL (Konto Saldo anfordern)
    Section C.2.1.2
    """
    type = 'HKSAL'

    def __init__(self, segno, version, account):
        self.version = version
        data = [
            account,
            'N'
        ]
        super().__init__(segno, data)
