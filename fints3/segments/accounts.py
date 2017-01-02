from . import FinTS3Segment


class HKSPA(FinTS3Segment):
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
