from . import FinTS3SegmentOLD, FinTS3Segment

from ..fields import DataElementGroupField
from ..formals import KTZ1, Account3

class HKSPA(FinTS3SegmentOLD):
    """
    HKSPA (SEPA-Kontoverbindung anfordern)
    Section C.10.1.3
    """
    type = 'HKSPA'
    version = 1

    def __init__(self, segno, accno, subaccfeature, blz):
        data = [
            ':'.join([
                accno, subaccfeature,
                self.country_code, blz
            ]) if accno is not None else ''
        ]
        super().__init__(segno, data)

class HKSPA1(FinTS3Segment):
    """SEPA-Kontoverbindung anfordern, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle 
    """
    accounts = DataElementGroupField(type=Account3, max_count=999, required=False, _d="Kontoverbindung")

class HISPA1(FinTS3Segment):
    """SEPA-Kontoverbindung rückmelden, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle 
    """
    accounts = DataElementGroupField(type=KTZ1, max_count=999, required=False, _d="SEPA-Kontoverbindung")

