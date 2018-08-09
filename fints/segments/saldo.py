from . import FinTS3SegmentOLD


class HKSAL(FinTS3SegmentOLD):
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
