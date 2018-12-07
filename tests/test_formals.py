import pytest
from fints.formals import (
    Container, ContainerField, DataElementField,
    DataElementGroupField, DigitsField, Field, GenericGroupField,
    NumericField, SegmentHeader, SegmentSequence,
)


def test_container_simple():
    class A(Container):
        a = DataElementField(type='an')
        b = DigitsField()

    i1 = A()
    assert isinstance(i1, A)
    assert hasattr(i1, 'a')
    assert i1.a is None

    i1.a = 'abc123'
    i1.b = '007'
    assert i1.a == 'abc123'
    assert i1.b == '007'

    i2 = A(b='0815', a='bcd234')

    assert isinstance(i1, A)
    assert i2.a == 'bcd234'
    assert i2.b == '0815'

    with pytest.raises(TypeError):
        A(b='a')

    del i2.b
    assert i2.b is None


def test_container_nested():
    class A(Container):
        a = NumericField()

    class B(Container):
        b = DataElementGroupField(type=A)

    i1 = B()
    assert isinstance(i1.b, A)

    i1.b.a = '1'
    assert i1.b.a == 1


def test_container_count_exact():
    class A(Container):
        a = NumericField(count=2)

    i1 = A()

    assert len(i1.a) == 2

    assert i1.a[0] is None
    assert i1.a[1] is None

    with pytest.raises(IndexError):
        i1.a[2]

    with pytest.raises(IndexError):
        i1.a[2] = 1

    with pytest.raises(IndexError):
        i1.a[-1]

    with pytest.raises(IndexError):
        i1.a[-1] = 1

    i1.a[0] = '3'
    i1.a[1] = 4

    with pytest.raises(ValueError):
        i1.a[1] = '05'

    assert i1.a[0] == 3
    assert i1.a[1] == 4

    assert len(i1.a) == 2

    del i1.a[1]
    assert i1.a[1] is None


def test_container_count_variable_1():
    class A(Container):
        a = NumericField(min_count=2, max_count=5)

    i1 = A()

    assert len(i1.a) == 2

    assert i1.a[0] is None
    assert i1.a[1] is None
    assert i1.a[3] is None

    assert len(i1.a) == 2

    with pytest.raises(IndexError):
        i1.a[5]

    with pytest.raises(IndexError):
        i1.a[5] = 1

    with pytest.raises(IndexError):
        i1.a[-1]

    i1.a[0] = '3'
    i1.a[1] = 4
    i1.a[3] = 17

    assert i1.a[0] == 3
    assert i1.a[1] == 4
    assert i1.a[2] is None
    assert i1.a[3] == 17

    assert len(i1.a) == 4

    assert i1.a[4] is None

    assert len(i1.a) == 4


def test_container_count_variable_2():
    class A(Container):
        a = NumericField(min_count=2)

    i1 = A()

    assert len(i1.a) == 2


def test_container_count_variable_3():
    class A(Container):
        a = NumericField(max_count=4)

    i1 = A()

    assert len(i1.a) == 0


def test_container_count_variable_iter():
    class A(Container):
        a = NumericField(max_count=4)

    i1 = A()

    assert len(i1.a) == 0

    assert list(i1.a) == []

    i1.a[2] = '3'

    assert list(i1.a) == [None, None, 3]

    assert len(i1.a) == 3


def test_container_init():
    class A(Container):
        a = NumericField()
        b = DigitsField()

    i1 = A(a='3', b='04')

    assert i1.a == 3
    assert i1.b == '04'


def test_container_nested_init():
    class A(Container):
        a = NumericField()

    class B(Container):
        b = DataElementGroupField(type=A)

    i1 = A(a='5')
    i2 = B(b=i1)

    assert isinstance(i2.b, A)
    assert i2.b.a == 5

    class C(Container):
        c = DataElementGroupField(type=B)

    with pytest.raises(TypeError):
        C(c=i1)

    i3 = B()
    assert i3.b.a is None


def test_container_count_init():
    class A(Container):
        a = NumericField(count=4)

    i1 = A(a=[None, '23'])

    assert i1.a[0] is None
    assert i1.a[1] == 23

    assert len(i1.a) == 4


def test_container_count_variable_init():
    class A(Container):
        a = NumericField(max_count=4)

    i1 = A(a=[None, '23'])

    assert i1.a[0] is None
    assert i1.a[1] == 23

    assert len(i1.a) == 2


def test_container_naive_parse():
    class A(Container):
        a = NumericField()
        b = DigitsField()

    i1 = A.naive_parse(['23', '42'])

    assert i1.a == 23
    assert i1.b == '42'


def test_invalid_spec():
    with pytest.raises(ValueError):
        class A(Container):
            a = NumericField(length=3, max_length=5)

    with pytest.raises(ValueError):
        class A(Container):
            a = NumericField(count=3, min_count=5)

    with pytest.raises(NotImplementedError):
        class A(Container):
            a = Field()

        A(a=123)


def test_parse_restrictions():
    class A(Container):
        a = NumericField(min_length=2, max_length=3)
        b = DigitsField(length=3)

    i1 = A()
    with pytest.raises(ValueError, match='max_length=3 exceeded'):
        i1.a = '1234'

    i2 = A(a=123)
    with pytest.raises(ValueError, match='max_length=3 exceeded'):
        i2.a = 1234

    with pytest.raises(ValueError, match='length=3 not satisfied'):
        A(b='01')

    with pytest.raises(ValueError, match='min_length=2 not reached'):
        A(a=1)


def test_unset():
    class A(Container):
        a = NumericField()

    class B(Container):
        b = ContainerField(type=A)
        c = NumericField()

    assert A().is_unset()
    assert not A(a=1).is_unset()
    assert A(a=None).is_unset()

    assert B().is_unset()
    assert B(b=A()).is_unset()
    assert not B(c=1).is_unset()


def test_sequence_repr():
    s = SegmentSequence()

    assert repr(s) == 'fints.types.SegmentSequence([])'


def test_valuelist_repr():
    class A(Container):
        a = NumericField(max_count=3)

    i1 = A()
    assert repr(i1.a) == "[]"


def test_empty_list():
    class A(Container):
        a = NumericField(max_count=3)

    i1 = A()
    assert len(i1.a) == 0

    i2 = A(a=[None])
    assert len(i2.a) == 0


def test_segmentheader_short():
    h = SegmentHeader('HNHBS', 5, 1)

    assert repr(h) == "fints.formals.SegmentHeader('HNHBS', 5, 1)"


def test_container_generic():
    class A(Container):
        a = DataElementGroupField()

    assert isinstance(A._fields['a'], GenericGroupField)

    i1 = A()
    assert i1._fields['a'].type is None

    assert i1.a

    with pytest.warns(UserWarning, match=r'Generic field used for type None value \[\]'):
        i2 = A(a=[])


def test_find_1():
    from conftest import TEST_MESSAGES
    from fints.parser import FinTS3Parser
    from fints.segments.message import HNHBS1, HNHBK3

    m = FinTS3Parser().parse_message(TEST_MESSAGES['basic_complicated'])

    assert len(list(m.find_segments('HNHBK'))) == 1
    assert len(list(m.find_segments(['HNHBK', 'HNHBS']))) == 2

    assert len(list(m.find_segments(['HNHBK', 'HNHBS'], 1))) == 1
    assert len(list(m.find_segments(['HNHBK', 'HNHBS'], (1, 3)))) == 2

    assert isinstance(m.find_segment_first('HNHBK'), HNHBK3)
    assert isinstance(m.find_segment_first('HNHBS'), HNHBS1)

    assert m.find_segment_first('ITST') is None

    assert len(m.find_segment_first('HITANS', 1).parameter.twostep_parameters) == 2
    assert len(m.find_segment_first('HITANS', 3).parameter.twostep_parameters) == 6

    assert m.find_segment_first('HITANS', recurse=False) is None


def test_find_by_class():
    from conftest import TEST_MESSAGES
    from fints.parser import FinTS3Parser
    from fints.segments.message import HNHBS1

    m = FinTS3Parser().parse_message(TEST_MESSAGES['basic_complicated'])

    assert list(m.find_segments(HNHBS1))[0].__class__ == HNHBS1

    assert m.find_segment_first(HNHBS1).header.type == 'HNHBS'
