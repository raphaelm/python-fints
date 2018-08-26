from . import FinTS3Segment
from ..fields import DataElementGroupField
from ..formals import KTZ1, Account3

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
