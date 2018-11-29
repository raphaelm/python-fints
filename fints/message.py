from enum import Enum

from .formals import SegmentSequence
from .segments.base import FinTS3Segment
from .segments.dialog import HIRMS2


class MessageDirection(Enum):
    FROM_CUSTOMER = 1
    FROM_INSTITUTE = 2


class FinTSMessage(SegmentSequence):
    DIRECTION = None
    # Auto-Numbering, dialog relation, security base

    def __init__(self, dialog=None, *args, **kwargs):
        self.dialog = dialog
        self.next_segment_number = 1
        super().__init__(*args, **kwargs)

    def __iadd__(self, segment: FinTS3Segment):
        if not isinstance(segment, FinTS3Segment):
            raise TypeError("Can only append FinTS3Segment instances, not {!r}".format(segment))
        segment.header.number = self.next_segment_number
        self.next_segment_number += 1
        self.segments.append(segment)
        return self

    def response_segments(self, ref, *args, **kwargs):
        for segment in self.find_segments(*args, **kwargs):
            if segment.header.reference == ref.header.number:
                yield segment

    def responses(self, ref, code=None):
        for segment in self.response_segments(ref, HIRMS2):
            for response in segment.responses:
                if code is None or response.code == code:
                    yield response


class FinTSCustomerMessage(FinTSMessage):
    DIRECTION = MessageDirection.FROM_CUSTOMER
    # Identification, authentication


class FinTSInstituteMessage(FinTSMessage):
    DIRECTION = MessageDirection.FROM_INSTITUTE
