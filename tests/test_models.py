import pytest
from fints.segments import FinTS3Segment, HNHBK3, HNHBS1
from fints.formals import SegmentHeader, DataElementField, GenericField, NumericField, AlphanumericField

def test_metaclass_foo():
    a = HNHBK3()

    assert list(a._fields) == ['header', 'message_size', 'hbci_version', 'dialogue_id', 'message_number', 'reference_message']
    assert a._fields['header']

def test_descriptor_subclassing():
    a = DataElementField(type='an')
    assert isinstance(a, AlphanumericField)

    b = AlphanumericField()
    assert b.type == 'an'

    c = DataElementField(type='fnord')
    assert isinstance(c, GenericField)

def test_descriptor_in_use():
    assert isinstance(HNHBS1._fields['message_number'], NumericField)

def test_data_element_constructor():
    a = HNHBS1(message_number='4')

    assert a.message_number == 4

def test_fints3_constructor_auto_segmentheader():
    a = HNHBS1(7)

    assert a.message_number == 7

def test_data_element_constructor_double_arg():
    with pytest.raises(TypeError):
        HNHBS1(8, message_number='9')

def test_data_element_setgetdel():
    a = HNHBS1()

    a.message_number = '5'
    assert a.message_number == 5

    a.message_number = 6
    assert a.message_number == 6

    del a.message_number
    assert not a.message_number

def test_descriptors_independent():
    a = HNHBK3()
    b = HNHBK3()

    a.hbci_version = '300'

    assert a.hbci_version
    assert not b.hbci_version

def test_parse_container():
    a = ['HNHBS', '2', '1', ]

    h = SegmentHeader.naive_parse(a)

    assert h.type == 'HNHBS'
    assert h.version == 1
    assert h.reference is None

def test_segment_class_type_version():
    assert HNHBS1.TYPE == 'HNHBS'
    assert HNHBS1.VERSION == 1

    assert HNHBK3.VERSION == 3

def test_find_subclass():
    a = [
        ['HNHBS', '2', '1', ],
        '3'
    ]

    clazz = FinTS3Segment.find_subclass(a)
    assert clazz is HNHBS1
