from fints.fields import DataElementField, DataElementGroupField
from fints.formals import Account2, Account3

from . import FinTS3Segment, FinTS3SegmentOLD


class HKWPD(FinTS3SegmentOLD):
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

class HKWPD5(FinTS3Segment):
    """Depotaufstellung anfordern, version 5

    Source: HBCI Homebanking-Computer-Interface, Schnittstellenspezifikation"""
    account = DataElementGroupField(type=Account2, _d="Depot")
    currency = DataElementField(type='cur', required=False, _d="Währung der Depotaufstellung")
    quality = DataElementField(type='num', length=1, required=False, _d="Kursqualität")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HIWPD5(FinTS3Segment):
    """Depotaufstellung rückmelden, version 5

    Source: HBCI Homebanking-Computer-Interface, Schnittstellenspezifikation"""
    holdings = DataElementField(type='bin', _d="Depotaufstellung")


class HKWPD6(FinTS3Segment):
    """Depotaufstellung anfordern, version 6

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=Account3, _d="Depot")
    currency = DataElementField(type='cur', required=False, _d="Währung der Depotaufstellung")
    quality = DataElementField(type='code', length=1, required=False, _d="Kursqualität")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HIWPD6(FinTS3Segment):
    """Depotaufstellung rückmelden, version 6

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    holdings = DataElementField(type='bin', _d="Depotaufstellung")
