from fints.fields import CodeField, DataElementField, DataElementGroupField
from fints.formals import (
    KTI1, Amount1, BatchTransferParameter1
)

from . import FinTS3Segment, ParameterSegment, FinTS3SegmentOLD
from ..models import SEPAAccount


class HKCCS(FinTS3SegmentOLD):
    """
    HKCCS (SEPA Überweisung übertragen)
    Section C.2.1.2
    """
    type = 'HKCCS'

    def __init__(self, segno, account: SEPAAccount, pain_msg):
        self.version = 1
        sepa_descriptor = 'urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain.001.001.03'
        msg = ':'.join([
            account.iban,
            account.bic
        ])
        data = [
            msg,
            sepa_descriptor,
            '@{}@{}'.format(len(pain_msg), pain_msg)
        ]
        super().__init__(segno, data)

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


class HKCCM(FinTS3SegmentOLD):
    """
    HKCCM (SEPA-Sammelüberweisung einreichen)
    Section C.10.3.1.1
    """
    type = 'HKCCM'

    def __init__(self, segno, account: SEPAAccount, pain_msg, control_sum, currency, book_as_single):
        self.version = 1
        sepa_descriptor = 'urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain.001.001.03'
        msg = ':'.join([
            account.iban,
            account.bic
        ])
        data = [
            msg,
            str(control_sum).replace('.', ',') + ':' + currency,
            'J' if book_as_single else '',
            sepa_descriptor,
            '@{}@{}'.format(len(pain_msg), pain_msg)
        ]
        super().__init__(segno, data)
