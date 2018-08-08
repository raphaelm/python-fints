from fints.message import FinTSResponse
from fints.parser import FinTS3Parser
#from fints.segments.message import HNHBK
import pytest

from conftest import COMPLICATED_EXAMPLE, SIMPLE_EXAMPLE

def test_basic_message():
    segments = FinTS3Parser.explode_segments(SIMPLE_EXAMPLE)
    assert len(segments) == 4

def test_explode_complicated():
    segments = FinTS3Parser.explode_segments(COMPLICATED_EXAMPLE)
    assert len(segments) == 4

def test_legacy_response():
    data = SIMPLE_EXAMPLE
    m = FinTSResponse(data)
    assert len(m.segments) == 4
    assert len(m.payload) == 3

def test_parse_simple():
    m = FinTS3Parser().parse_message(SIMPLE_EXAMPLE)
    assert len(m.segments) == 4
    assert m.segments[0].__class__.__name__ == "HNHBK3"
    m.print_nested()

def test_parse_complicated():
    m = FinTS3Parser().parse_message(COMPLICATED_EXAMPLE)
    assert len(m.segments) == 4
    assert m.segments[3].__class__.__name__ == "HNHBS1"
    m.print_nested()

def test_parse_counted():
    from fints.segments import FinTS3Segment
    from fints.formals import NumericField, Container, ContainerField

    class ITST1(FinTS3Segment):
        a = NumericField(count=3)

    m1 = FinTS3Parser().parse_message(b"ITST:1:1+1+2+3'")
    assert m1.segments[0].header.type == 'ITST'
    assert len(m1.segments[0].a) == 3
    assert m1.segments[0].a[0] == 1
    assert m1.segments[0].a[1] == 2
    assert m1.segments[0].a[2] == 3

    class ITST2(FinTS3Segment):
        a = NumericField(max_count=3)

    m2 = FinTS3Parser().parse_message(b"ITST:1:2+1+2+3'")
    assert m2.segments[0].a[2] == 3

    m3 = FinTS3Parser().parse_message(b"ITST:1:2+1+2+3+4'")
    assert m3.segments[0]._additional_data == ['4']

    m4 = FinTS3Parser().parse_message(b"ITST:1:2+1+2'")
    assert len(m4.segments[0].a) == 2
    assert m4.segments[0].a[1] == 2

    class InnerTest(Container):
        a = NumericField(max_count=3)

    class ITST3(FinTS3Segment):
        b = ContainerField(type=InnerTest, max_count=99)


    m5 = FinTS3Parser().parse_message(b"ITST:1:3+12:42+345+61:62:63'")
    m5.print_nested()
    assert m5.segments[0].b[0].a[0] == 12
    assert m5.segments[0].b[0].a[1] == 42
    assert m5.segments[0].b[0].a[2] is None
    assert m5.segments[0].b[1].a[0] == 345
    assert m5.segments[0].b[2].a[0] == 61
    assert m5.segments[0].b[2].a[1] == 62
    assert m5.segments[0].b[2].a[2] == 63


def test_parse_HIRMG2():
    d = b"HIRMG:3:2+0010::Nachricht entgegengenommen.+0100::Dialog beendet.'"
    m = FinTS3Parser().parse_message(d)
    
    seg = m.segments[0]
    assert seg.header.type == 'HIRMG'
    assert seg.response[0].response_code == '0010'
    assert seg.response[1].response_code == '0100'
    assert len(seg.response) == 2

def test_invalid():
    message1 = rb"""12"""

    with pytest.raises(ValueError):
        FinTS3Parser.explode_segments(message1)

    message2 = rb"""@2@12ab'"""

    with pytest.raises(ValueError):
        FinTS3Parser.explode_segments(message2)

    message3 = rb"""ab@2@12'"""

    with pytest.raises(ValueError):
        FinTS3Parser.explode_segments(message3)

    message4 = rb"""ab@@'"""

    with pytest.raises(ValueError):
        FinTS3Parser.explode_segments(message4)

    message5 = rb"""@2@12ab"""

    with pytest.raises(ValueError):
        FinTS3Parser.explode_segments(message5)

    message6 = rb"""HNHBS:5:1'"""
    with pytest.raises(ValueError, match='^Required field'):
        m = FinTS3Parser().parse_message(message6)

