from ..fields import CodeField, DataElementField, DataElementGroupField
from ..formals import (
    KTI1, Amount1, QueryScheduledBatchDebitParameter1,
    QueryScheduledDebitParameter1, QueryScheduledDebitParameter2,
    ScheduledBatchDebitParameter1, ScheduledBatchDebitParameter2,
    ScheduledCOR1BatchDebitParameter1, ScheduledCOR1DebitParameter1,
    ScheduledDebitParameter1, ScheduledDebitParameter2, SEPACCode1,
    StatusSEPATask1, SupportedSEPAPainMessages1,
)
from .base import FinTS3Segment, ParameterSegment


class BatchDebitBase(FinTS3Segment):
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    sum_amount = DataElementGroupField(type=Amount1, _d="Summenfeld")
    request_single_booking = DataElementField(type='jn', _d="Einzelbuchung gewünscht")
    sepa_descriptor = DataElementField(type='an', max_length=256, _d="SEPA Descriptor")
    sepa_pain_message = DataElementField(type='bin', _d="SEPA pain message")


class DebitResponseBase(FinTS3Segment):
    task_id = DataElementField(type='an', max_length=99, required=False, _d="Auftragsidentifikation")


class HKDSE1(FinTS3Segment):
    """Terminierte SEPA-Einzellastschrift einreichen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    sepa_descriptor = DataElementField(type='an', max_length=256, _d="SEPA Descriptor")
    sepa_pain_message = DataElementField(type='bin', _d="SEPA pain message")


class HIDSE1(DebitResponseBase):
    """Einreichung terminierter SEPA-Einzellastschrift bestätigen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """


class HIDSES1(ParameterSegment):
    """Terminierte SEPA-Einzellastschrift einreichen Parameter, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    parameter = DataElementGroupField(type=ScheduledDebitParameter1, _d="Parameter terminierte SEPA-Sammellastschrift einreichen")


class HKDSE2(FinTS3Segment):
    """Terminierte SEPA-Einzellastschrift einreichen, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    sepa_descriptor = DataElementField(type='an', max_length=256, _d="SEPA Descriptor")
    sepa_pain_message = DataElementField(type='bin', _d="SEPA pain message")


class HIDSE2(DebitResponseBase):
    """Einreichung terminierter SEPA-Einzellastschrift bestätigen, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """


class HIDSES2(ParameterSegment):
    """Terminierte SEPA-Einzellastschrift einreichen Parameter, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    parameter = DataElementGroupField(type=ScheduledDebitParameter2, _d="Parameter terminierte SEPA-Sammellastschrift einreichen")


class HKDME1(BatchDebitBase):
    """Einreichung terminierter SEPA-Sammellastschrift, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """


class HIDME1(DebitResponseBase):
    """Einreichung terminierter SEPA-Sammellastschrift bestätigen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """


class HIDMES1(ParameterSegment):
    """Terminierte SEPA-Sammellastschrift einreichen Parameter, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    parameter = DataElementGroupField(type=ScheduledBatchDebitParameter1, _d="Parameter terminierte SEPA-Sammellastschrift einreichen")


class HKDME2(BatchDebitBase):
    """Einreichung terminierter SEPA-Sammellastschrift, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """


class HIDME2(DebitResponseBase):
    """Einreichung terminierter SEPA-Sammellastschrift bestätigen, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """


class HIDMES2(ParameterSegment):
    """Terminierte SEPA-Sammellastschrift einreichen Parameter, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    parameter = DataElementGroupField(type=ScheduledBatchDebitParameter2, _d="Parameter terminierte SEPA-Sammellastschrift einreichen")


class HKDSC1(FinTS3Segment):
    """Terminierte SEPA-COR1-Einzellastschrift einreichen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    sepa_descriptor = DataElementField(type='an', max_length=256, _d="SEPA Descriptor")
    sepa_pain_message = DataElementField(type='bin', _d="SEPA pain message")


class HIDSC1(DebitResponseBase):
    """Einreichung terminierter SEPA-COR1-Einzellastschrift bestätigen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """


class HIDSCS1(ParameterSegment):
    """Terminierte SEPA-COR1-Einzellastschrift Parameter, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    parameter = DataElementGroupField(type=ScheduledCOR1DebitParameter1, _d="Parameter terminierte SEPA-COR1-Einzellastschrift")


class HKDMC1(BatchDebitBase):
    """Terminierte SEPA-COR1-Sammellastschrift einreichen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """


class HIDMC1(DebitResponseBase):
    """Einreichung terminierter SEPA-COR1-Sammellastschrift bestätigen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """


class HIDMCS1(ParameterSegment):
    """Terminierte SEPA-COR1-Sammellastschrift Parameter, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    parameter = DataElementGroupField(type=ScheduledCOR1BatchDebitParameter1, _d="Parameter terminierte SEPA-COR1-Sammellastschrift")


class HKDBS1(FinTS3Segment):
    """Bestand terminierter SEPA-Einzellastschriften anfordern, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    supported_sepa_pain_messages = DataElementGroupField(type=SupportedSEPAPainMessages1, _d="Unterstützte SEPA pain messages")
    date_start = DataElementField(type='dat', required=False, _d="Von Datum")
    date_end = DataElementField(type='dat', required=False, _d="Bis Datum")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HIDBS1(FinTS3Segment):
    """Bestand terminierter SEPA-Einzellastschriften rückmelden, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    sepa_descriptor = DataElementField(type='an', max_length=256, _d="SEPA Descriptor")
    sepa_pain_message = DataElementField(type='bin', _d="SEPA pain message")
    task_id = DataElementField(type='an', max_length=99, required=False, _d="Auftragsidentifikation")
    task_cancelable = DataElementField(type='jn', required=False, _d="Auftrag löschbar")
    task_changeable = DataElementField(type='jn', required=False, _d="Auftrag änderbar")


class HIDBSS1(ParameterSegment):
    """Bestand terminierter SEPA-Einzellastschriften Parameter, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    parameter = DataElementGroupField(type=QueryScheduledDebitParameter1, _d="Parameter Bestand terminierter SEPA-Einzellastschriften")


class HKDBS2(FinTS3Segment):
    """Bestand terminierter SEPA-Einzellastschriften anfordern, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    supported_sepa_pain_messages = DataElementGroupField(type=SupportedSEPAPainMessages1, _d="Unterstützte SEPA pain messages")
    date_start = DataElementField(type='dat', required=False, _d="Von Datum")
    date_end = DataElementField(type='dat', required=False, _d="Bis Datum")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HIDBS2(FinTS3Segment):
    """Bestand terminierter SEPA-Einzellastschriften rückmelden, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    sepa_descriptor = DataElementField(type='an', max_length=256, _d="SEPA Descriptor")
    sepa_pain_message = DataElementField(type='bin', _d="SEPA pain message")
    task_id = DataElementField(type='an', max_length=99, required=False, _d="Auftragsidentifikation")
    sepa_c_code = CodeField(enum=SEPACCode1, _d="SEPA-C-Code")
    task_changeable = DataElementField(type='jn', required=False, _d="Auftrag änderbar")
    status_sepa_task = CodeField(enum=StatusSEPATask1, _d="Status SEPA-Auftrag")


class HIDBSS2(ParameterSegment):
    """Bestand terminierter SEPA-Einzellastschriften Parameter, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    parameter = DataElementGroupField(type=QueryScheduledDebitParameter2, _d="Parameter Bestand terminierter SEPA-Einzellastschriften")


class HKDMB1(FinTS3Segment):
    """Bestand terminierter SEPA-Sammellastschriften anfordern, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    date_start = DataElementField(type='dat', required=False, _d="Von Datum")
    date_end = DataElementField(type='dat', required=False, _d="Bis Datum")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HIDMB1(FinTS3Segment):
    """Bestand terminierter SEPA-Sammellastschriften rückmelden, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    task_id = DataElementField(type='an', max_length=99, required=False, _d="Auftragsidentifikation")
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    date_entered = DataElementField(type='dat', required=False, _d="Einreichungsdatum")
    date_booked = DataElementField(type='dat', required=False, _d="Ausführungsdatum")
    debit_count = DataElementField(type='num', max_length=6, _d="Anzahl der Aufträge")
    sum_amount = DataElementGroupField(type=Amount1, _d="Summe der Beträge")


class HIDMBS1(ParameterSegment):
    """Bestand terminierter SEPA-Sammellastschriften Parameter, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    parameter = DataElementGroupField(type=QueryScheduledBatchDebitParameter1, _d="Parameter Bestand terminierter SEPA-Sammellastschriften")
