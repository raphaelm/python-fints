from fints.fields import DataElementField, DataElementGroupField
from fints.formals import KTI1, Amount1, BatchTransferParameter1

from .base import FinTS3Segment, ParameterSegment


class HKCCS1(FinTS3Segment):
    """SEPA Einzelüberweisung, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    sepa_descriptor = DataElementField(type='an', max_length=256, _d="SEPA Descriptor")
    sepa_pain_message = DataElementField(type='bin', _d="SEPA pain message")


class HKCCM1(FinTS3Segment):
    """SEPA-Sammelüberweisung, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    sum_amount = DataElementGroupField(type=Amount1, _d="Summenfeld")
    request_single_booking = DataElementField(type='jn', _d="Einzelbuchung gewünscht")
    sepa_descriptor = DataElementField(type='an', max_length=256, _d="SEPA Descriptor")
    sepa_pain_message = DataElementField(type='bin', _d="SEPA pain message")


class HICCMS1(ParameterSegment):
    """SEPA-Sammelüberweisung Parameter, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    parameter = DataElementGroupField(type=BatchTransferParameter1, _d="Parameter SEPA-Sammelüberweisung")
