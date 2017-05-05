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
            # The spec allows the specification of currency and
            # quality of valuations, as shown in the docstring above.
            # However, both 1822direkt and CortalConsors reject the
            # call if these two are present, claiming an invalid input.
            # 'EUR'        # Währung der Depotaufstellung"
            # 2             # Kursqualität
        ]
        super().__init__(segno, data)
