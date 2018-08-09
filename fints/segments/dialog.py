from . import FinTS3SegmentOLD


class HKEND(FinTS3SegmentOLD):
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
