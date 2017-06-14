from fints.utils import fints_escape
from . import FinTS3Segment


class HKKAZ(FinTS3Segment):
    """
    HKKAZ (Kontoumsätze)

    Refs: http://www.hbci-zka.de/dokumente/spezifikation_deutsch/fintsv3/FinTS_3.0_Messages_Geschaeftsvorfaelle_2015-08-07_final_version.pdf
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
            fints_escape(touchdown) if touchdown is not None else ''
        ]
        super().__init__(segno, data)
