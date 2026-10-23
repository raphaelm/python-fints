from ..fields import DataElementField, DataElementGroupField
from ..formals import (
    KTI1, ChangeStandingOrderParameter1, CreateStandingOrderParameter1,
    DeleteStandingOrderParameter1, QueryStandingOrdersParameter1,
    StandingOrderDetails3, StandingOrderSuspension3, SupportedSEPAPainMessages1,
)
from .base import FinTS3Segment, ParameterSegment


class HKCDB1(FinTS3Segment):
    """SEPA-Dauerauftragsbestand anfordern, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    supported_sepa_pain_messages = DataElementGroupField(type=SupportedSEPAPainMessages1, _d="Unterstützte SEPA pain messages")
    task_id = DataElementField(type='an', max_length=99, required=False, _d="Auftragsidentifikation")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HICDB1(FinTS3Segment):
    """SEPA-Dauerauftragsbestand rückmelden, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    sepa_descriptor = DataElementField(type='an', max_length=256, _d="SEPA Descriptor")
    sepa_pain_message = DataElementField(type='bin', _d="SEPA pain message")
    task_id = DataElementField(type='an', max_length=99, required=False, _d="Auftragsidentifikation")
    standing_order_details = DataElementGroupField(type=StandingOrderDetails3, _d="Dauerauftragsdetails")
    suspension = DataElementGroupField(type=StandingOrderSuspension3, required=False, _d="Aussetzung")
    task_changeable = DataElementField(type='jn', required=False, _d="Auftrag änderbar")
    task_suspendable = DataElementField(type='jn', required=False, _d="Auftrag aussetzbar")
    task_cancelable = DataElementField(type='jn', required=False, _d="Auftrag löschbar")


class HICDBS1(ParameterSegment):
    """SEPA-Dauerauftragsbestand Parameter, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    parameter = DataElementGroupField(type=QueryStandingOrdersParameter1, _d="Parameter SEPA-Dauerauftragsbestand")


class HKCDL1(FinTS3Segment):
    """SEPA-Dauerauftrag löschen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    sepa_descriptor = DataElementField(type='an', max_length=256, required=False, _d="SEPA Descriptor")
    sepa_pain_message = DataElementField(type='bin', required=False, _d="SEPA pain message")
    execution_date = DataElementField(type='dat', required=False, _d="Ausführungsdatum")
    task_id = DataElementField(type='an', max_length=99, required=False, _d="Auftragsidentifikation")
    standing_order_details = DataElementGroupField(type=StandingOrderDetails3, _d="Dauerauftragsdetails")


class HICDLS1(ParameterSegment):
    """SEPA-Dauerauftrag löschen Parameter, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    parameter = DataElementGroupField(type=DeleteStandingOrderParameter1, _d="Parameter SEPA-Dauerauftrag löschen")


class HKCDE1(FinTS3Segment):
    """SEPA-Dauerauftrag einrichten, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    sepa_descriptor = DataElementField(type='an', max_length=256, _d="SEPA Descriptor")
    sepa_pain_message = DataElementField(type='bin', _d="SEPA pain message")
    standing_order_details = DataElementGroupField(type=StandingOrderDetails3, _d="Dauerauftragsdetails")


class HICDE1(FinTS3Segment):
    """SEPA-Dauerauftragseinrichtung bestätigen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    task_id = DataElementField(type='an', max_length=99, required=False, _d="Auftragsidentifikation")


class HICDES1(ParameterSegment):
    """SEPA-Dauerauftrag einrichten Parameter, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    parameter = DataElementGroupField(type=CreateStandingOrderParameter1, _d="Parameter SEPA-Dauerauftrag einrichten")


class HKCDN1(FinTS3Segment):
    """SEPA-Dauerauftrag ändern, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    sepa_descriptor = DataElementField(type='an', max_length=256, _d="SEPA Descriptor")
    sepa_pain_message = DataElementField(type='bin', _d="SEPA pain message")
    execution_date = DataElementField(type='dat', required=False, _d="Ausführungsdatum")
    task_id = DataElementField(type='an', max_length=99, required=False, _d="Auftragsidentifikation")
    standing_order_details = DataElementGroupField(type=StandingOrderDetails3, required=False, _d="Dauerauftragsdetails")


class HICDN1(FinTS3Segment):
    """SEPA-Dauerauftragsänderung bestätigen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    task_id = DataElementField(type='an', max_length=99, _d="Auftragsidentifikation")
    task_id_old = DataElementField(type='an', max_length=99, required=False, _d="Auftragsidentifikation alt")


class HICDNS1(ParameterSegment):
    """SEPA-Dauerauftrag ändern Parameter, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    parameter = DataElementGroupField(type=ChangeStandingOrderParameter1, _d="Parameter SEPA-Dauerauftrag ändern")
