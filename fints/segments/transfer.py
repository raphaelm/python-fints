from . import FinTS3Segment
from ..models import SEPAAccount


class HKCCS(FinTS3Segment):
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
