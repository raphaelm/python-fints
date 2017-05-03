from . import FinTS3Segment

class HKWPD(FinTS3Segment):
    """
    HKWPD (Depotaufstellung anfordern)
    Section C.4.3.1
    Example: HKWPD:3:7+23456::280:10020030+USD+2'
    """
    type = 'HKWPD'

    def __init__(self, segno, version, account):
        self.version = version
        data = [
            account
            #'EUR'        # Währung der Depotaufstellung"
            #2             # Kursqualität
        ]
        super().__init__(segno, data)

