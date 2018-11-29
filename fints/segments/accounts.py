from ..fields import DataElementGroupField
from ..formals import KTZ1, Account3, GetSEPAAccountParameter1
from .base import FinTS3Segment, ParameterSegment


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


class HISPAS1(ParameterSegment):
    """SEPA-Kontoverbindung anfordern, Parameter, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle"""
    parameter = DataElementGroupField(type=GetSEPAAccountParameter1, _d="Parameter SEPA-Kontoverbindung anfordern")
