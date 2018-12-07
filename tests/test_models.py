from io import StringIO

import pytest
from fints.formals import (
    AlphanumericField, DataElementField, GenericField,
    NumericField, SegmentHeader, SegmentSequence,
)
from fints.segments.base import FinTS3Segment
from fints.segments.message import HNHBK3, HNHBS1


def test_metaclass_foo():
    a = HNHBK3()

    assert list(a._fields) == ['header', 'message_size', 'hbci_version', 'dialog_id', 'message_number', 'reference_message']
    assert a._fields['header']


def test_fints3_only_de_and_deg():
    from fints.formals import Field, Container, DataElementGroupField

    with pytest.raises(TypeError, match="b=.* is not DataElementField or DataElementGroupField"):
        class Foo(FinTS3Segment):
            a = NumericField()
            b = Field()

    class A(Container):
        a = Field()

    class B(Container):
        b = DataElementGroupField(type=A)

    with pytest.raises(TypeError, match="a=.* is not DataElementField or DataElementGroupField"):
        class Foo(FinTS3Segment):
            c = DataElementGroupField(type=B)


def test_segment_subclassing():
    class Base1(FinTS3Segment):
        a = NumericField()

    class Base2(Base1):
        b = NumericField()

    class ISUBTST1(Base2):
        c = NumericField()

    assert list(ISUBTST1._fields.keys()) == ['header', 'a', 'b', 'c']


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


def test_nested_output_evalable():
    import fints.segments, fints.formals

    a = SegmentSequence([fints.segments.message.HNHBK3(header=fints.formals.SegmentHeader('HNHBK', 1, 3, None), message_size='000000000428', hbci_version=300,
                                                       dialog_id='430711670077=043999659571CN9D=', message_number=2,
                                                       reference_message=fints.formals.ReferenceMessage(dialog_id='430711670077=043999659571CN9D=',
                                                                                                        message_number=2)),
                         fints.segments.message.HNVSK3(header=fints.formals.SegmentHeader('HNVSK', 998, 3, None),
                                                       security_profile=fints.formals.SecurityProfile(security_method='PIN', security_method_version=1),
                                                       security_function='998', security_role='1',
                                                       security_identification_details=fints.formals.SecurityIdentificationDetails(identified_role='2',
                                                                                                                                   cid=None,
                                                                                                                                   identifier='oIm3BlHv6mQBAADYgbPpp+kWrAQA'),
                                                       security_datetime=fints.formals.SecurityDateTime(date_time_type='1', date=None, time=None),
                                                       encryption_algorithm=fints.formals.EncryptionAlgorithm(usage_encryption='2', operation_mode='2',
                                                                                                              encryption_algorithm='13',
                                                                                                              algorithm_parameter_value=b'00000000',
                                                                                                              algorithm_parameter_name='5',
                                                                                                              algorithm_parameter_iv_name='1',
                                                                                                              algorithm_parameter_iv_value=None),
                                                       key_name=fints.formals.KeyName(
                                                           bank_identifier=fints.formals.BankIdentifier(country_identifier='280', bank_code='15050500'),
                                                           user_id='hermes', key_type='S', key_number=0, key_version=0), compression_function='0',
                                                       certificate=fints.formals.Certificate(certificate_type=None, certificate_content=None)),
                         fints.segments.message.HNVSD1(header=fints.formals.SegmentHeader('HNVSD', 999, 1, None), data=SegmentSequence([
                                                                                                                                           fints.segments.message.HNSHK4(
                                                                                                                                               header=fints.formals.SegmentHeader(
                                                                                                                                                   'HNSHK', 2,
                                                                                                                                                   4, None),
                                                                                                                                               security_profile=fints.formals.SecurityProfile(
                                                                                                                                                   security_method='PIN',
                                                                                                                                                   security_method_version=1),
                                                                                                                                               security_function='999',
                                                                                                                                               security_reference='9166926',
                                                                                                                                               security_application_area='1',
                                                                                                                                               security_role='1',
                                                                                                                                               security_identification_details=fints.formals.SecurityIdentificationDetails(
                                                                                                                                                   identified_role='2',
                                                                                                                                                   cid=None,
                                                                                                                                                   identifier='oIm3BlHv6mQBAADYgbPpp+kWrAQA'),
                                                                                                                                               security_reference_number=1,
                                                                                                                                               security_datetime=fints.formals.SecurityDateTime(
                                                                                                                                                   date_time_type='1',
                                                                                                                                                   date=None,
                                                                                                                                                   time=None),
                                                                                                                                               hash_algorithm=fints.formals.HashAlgorithm(
                                                                                                                                                   usage_hash='1',
                                                                                                                                                   hash_algorithm='999',
                                                                                                                                                   algorithm_parameter_name='1',
                                                                                                                                                   algorithm_parameter_value=None),
                                                                                                                                               signature_algorithm=fints.formals.SignatureAlgorithm(
                                                                                                                                                   usage_signature='6',
                                                                                                                                                   signature_algorithm='10',
                                                                                                                                                   operation_mode='16'),
                                                                                                                                               key_name=fints.formals.KeyName(
                                                                                                                                                   bank_identifier=fints.formals.BankIdentifier(
                                                                                                                                                       country_identifier='280',
                                                                                                                                                       bank_code='15050500'),
                                                                                                                                                   user_id='hermes',
                                                                                                                                                   key_type='S',
                                                                                                                                                   key_number=0,
                                                                                                                                                   key_version=0),
                                                                                                                                               certificate=fints.formals.Certificate(
                                                                                                                                                   certificate_type=None,
                                                                                                                                                   certificate_content=None)),
                                                                                                                                           fints.segments.base.FinTS3Segment(
                                                                                                                                               header=fints.formals.SegmentHeader(
                                                                                                                                                   'HIRMG', 3,
                                                                                                                                                   2, None),
                                                                                                                                               _additional_data=[
                                                                                                                                                   ['0010',
                                                                                                                                                    None,
                                                                                                                                                    'Nachricht entgegengenommen.'],
                                                                                                                                                   ['0100',
                                                                                                                                                    None,
                                                                                                                                                    'Dialog beendet.']]),
                                                                                                                                           fints.segments.base.FinTS3Segment(
                                                                                                                                               header=fints.formals.SegmentHeader(
                                                                                                                                                   'HNSHA', 4,
                                                                                                                                                   2, None),
                                                                                                                                               _additional_data=[
                                                                                                                                                   '9166926'])])),
                         fints.segments.message.HNHBS1(header=fints.formals.SegmentHeader('HNHBS', 5, 1, None), message_number=2)])

    output = StringIO()
    a.print_nested(stream=output)

    b = eval(output.getvalue())
    output.close()

    assert len(a.segments) == len(b.segments)

    for s1, s2 in zip(a.segments, b.segments):
        assert type(s1) == type(s2)
