from . import FinTS3Segment


class HKKAZ(FinTS3Segment):
    """
    HKKAZ (Kontoumsätze)
    Section C.2.1.1.1.2
    """
    type = 'HKKAZ'

    def __init__(self, segno, version, account, date_start, date_end, touchdown):
        self.version = version

        data = [
            account,
            'N',
            date_start.strftime('%Y%m%d'),
            date_end.strftime('%Y%m%d'),
            '',
            touchdown if touchdown is not None else ''
        ]
        super().__init__(segno, data)
