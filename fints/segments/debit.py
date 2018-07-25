from . import FinTS3Segment
from ..models import SEPAAccount


class HKDSE(FinTS3Segment):
    """
    HKDSE (Einreichung terminierter SEPA-Einzellastschrift)
    Section C.10.2.5.4.1
    """
    type = 'HKDSE'

    def __init__(self, segno, account: SEPAAccount, pain_msg):
        self.version = 1
        sepa_descriptor = 'urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain.008.003.02'
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


class HKDME(FinTS3Segment):
    """
    HKDME (Einreichung terminierter SEPA-Sammellastschrift)
    Section C.10.3.2.2.1
    """
    type = 'HKDME'

    def __init__(self, segno, account: SEPAAccount, pain_msg, control_sum, currency, book_as_single):
        self.version = 1
        sepa_descriptor = 'urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain.008.003.02'
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
