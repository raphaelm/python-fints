import pytest
from conftest import TEST_MESSAGES
from fints.formals import NumericField
from fints.parser import FinTS3Parser, FinTS3Serializer
from fints.segments.base import FinTS3Segment


def test_serialize_1():
    class ITST1(FinTS3Segment):
        a = NumericField(count=3)

    i1 = ITST1(a=[1, 3])
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


def test_implode_shorten():
    m = [
        [
            ['IIMPTST', '1', '2'],
            [None, None],
            [None, 'a', None],
            [None, None, 'b'],
            [None, 'c', None, 'd'],
            [None, 'e', None, 'f', None],
            [None, 'g', None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
    ]

    s = FinTS3Serializer.implode_segments(m)

    assert s == rb"""IIMPTST:1:2++:a+::b+:c::d+:e::f+:g++'"""


def test_implode_roundtrip_simple():
    segments = FinTS3Parser.explode_segments(TEST_MESSAGES['basic_simple'])
    assert FinTS3Serializer.implode_segments(segments) == TEST_MESSAGES['basic_simple']

    message = FinTS3Parser().parse_message(segments)
    assert FinTS3Serializer().serialize_message(message) == TEST_MESSAGES['basic_simple']


def test_escape():
    assert b"a" == FinTS3Serializer.escape_value('a')

    assert b"??" == FinTS3Serializer.escape_value('?')

    assert b"??ab?:" == FinTS3Serializer.escape_value('?ab:')

    assert b"@1@c" == FinTS3Serializer.escape_value(b'c')

    with pytest.raises(TypeError):
        FinTS3Serializer.escape_value(1)


def test_serialize_2():
    from fints.formals import SegmentSequence
    import fints.segments
    s = SegmentSequence([fints.segments.message.HNHBK3(header=fints.formals.SegmentHeader('HNHBK', 1, 3), message_size='000000000428', hbci_version=300,
                                                       dialog_id='430711670077=043999659571CN9D=', message_number=2,
                                                       reference_message=fints.formals.ReferenceMessage(dialog_id='430711670077=043999659571CN9D=',
                                                                                                        message_number=2)),
                         fints.segments.message.HNVSK3(header=fints.formals.SegmentHeader('HNVSK', 998, 3),
                                                       security_profile=fints.formals.SecurityProfile(security_method='PIN', security_method_version=1),
                                                       security_function='998', security_role='1',
                                                       security_identification_details=fints.formals.SecurityIdentificationDetails(identified_role='2',
                                                                                                                                   cid=None,
                                                                                                                                   identifier='oIm3BlHv6mQBAADYgbPpp+kWrAQA'),
                                                       security_datetime=fints.formals.SecurityDateTime(date_time_type='1'),
                                                       encryption_algorithm=fints.formals.EncryptionAlgorithm(usage_encryption='2', operation_mode='2',
                                                                                                              encryption_algorithm='13',
                                                                                                              algorithm_parameter_value=b'00000000',
                                                                                                              algorithm_parameter_name='5',
                                                                                                              algorithm_parameter_iv_name='1'),
                                                       key_name=fints.formals.KeyName(
                                                           bank_identifier=fints.formals.BankIdentifier(country_identifier='280', bank_code='15050500'),
                                                           user_id='hermes', key_type='S', key_number=0, key_version=0), compression_function='0'),
                         fints.segments.message.HNVSD1(header=fints.formals.SegmentHeader('HNVSD', 999, 1), data=SegmentSequence([fints.segments.message.HNSHK4(
                             header=fints.formals.SegmentHeader('HNSHK', 2, 4),
                             security_profile=fints.formals.SecurityProfile(security_method='PIN', security_method_version=1), security_function='999',
                             security_reference='9166926', security_application_area='1', security_role='1',
                             security_identification_details=fints.formals.SecurityIdentificationDetails(identified_role='2', cid=None,
                                                                                                         identifier='oIm3BlHv6mQBAADYgbPpp+kWrAQA'),
                             security_reference_number=1, security_datetime=fints.formals.SecurityDateTime(date_time_type='1'),
                             hash_algorithm=fints.formals.HashAlgorithm(usage_hash='1', hash_algorithm='999', algorithm_parameter_name='1'),
                             signature_algorithm=fints.formals.SignatureAlgorithm(usage_signature='6', signature_algorithm='10', operation_mode='16'),
                             key_name=fints.formals.KeyName(bank_identifier=fints.formals.BankIdentifier(country_identifier='280', bank_code='15050500'),
                                                            user_id='hermes', key_type='S', key_number=0, key_version=0)), fints.segments.dialog.HIRMG2(
                             header=fints.formals.SegmentHeader('HIRMG', 3, 2),
                             responses=[fints.formals.Response(code='0010', reference_element=None, text='Nachricht entgegengenommen.'),
                                        fints.formals.Response(code='0100', reference_element=None, text='Dialog beendet.')]), fints.segments.message.HNSHA2(
                             header=fints.formals.SegmentHeader('HNSHA', 4, 2), security_reference='9166926')])),
                         fints.segments.message.HNHBS1(header=fints.formals.SegmentHeader('HNHBS', 5, 1), message_number=2)])

    assert FinTS3Serializer().serialize_message(s) == TEST_MESSAGES['basic_simple']


def test_serialize_roundtrips_complex_1():
    from fints.formals import SegmentSequence
    m1 = SegmentSequence(TEST_MESSAGES['basic_complicated'])
    b1 = m1.render_bytes()

    m2 = SegmentSequence(b1)
    b2 = m2.render_bytes()

    m3 = SegmentSequence(b2)
    b3 = m3.render_bytes()

    assert b2 == b3
