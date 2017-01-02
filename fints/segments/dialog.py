from . import FinTS3Segment


class HKEND(FinTS3Segment):
    """
    HKEND (Dialogende)
    Section C.4.1.2
    """
    type = 'HKEND'
    version = 1

    def __init__(self, segno, dialogid):
        data = [
            dialogid,
        ]
        super().__init__(segno, data)
