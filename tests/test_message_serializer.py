from fints.parser import FinTS3Serializer, FinTS3Parser
from fints.segments import FinTS3Segment
from fints.formals import NumericField
import pytest

def test_serialize_1():
    class ITST1(FinTS3Segment):
        a = NumericField(count=3)

    i1 = ITST1(a=[1,3])
    i1.header.number = 42

    serialization = rb"""ITST:42:1+1+3+'"""

    assert FinTS3Serializer().serialize_message(i1) == serialization

def test_implode_1():
    m = [
        [
            ['IIMPTST', '1', '1'],
            '1\'',
            '2+',
            [
                '1@',
                '2:',
                b'5@+\':',
            ],
        ],
        [
            ['IIMPTST', '2', '1'],
            '3?',
            '4',
        ]
    ]

    s = FinTS3Serializer.implode_segments(m)

    assert s == rb"""IIMPTST:1:1+1?'+2?++1?@:2?::@5@5@+':'IIMPTST:2:1+3??+4'"""

    assert FinTS3Parser.explode_segments(s) == m

def test_escape():
    assert b"a" == FinTS3Serializer.escape_value('a')

    assert b"??" == FinTS3Serializer.escape_value('?')

    assert b"??ab?:" == FinTS3Serializer.escape_value('?ab:')

    assert b"@1@c" == FinTS3Serializer.escape_value(b'c')

    with pytest.raises(TypeError):
        FinTS3Serializer.escape_value(1)
