from . import FinTS3Segment
from ..models import SEPAAccount
from ..fields import DataElementField, DataElementGroupField
from ..formals import ScheduledCOR1BatchDebitParameter1, KTI1, Amount1, ScheduledBatchDebitParameter1, ScheduledBatchDebitParameter2, ScheduledDebitParameter1, ScheduledDebitParameter2
from . import ParameterSegment

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
