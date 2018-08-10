Developer documentation/API
===========================

Parsing and serialization
-------------------------

.. autoclass:: fints.parser.FinTS3Parser
   :members:

.. autoclass:: fints.parser.FinTS3Serializer
   :members:

Example usage:

.. code-block:: python

   >>> message = (b'HNHBK:1:3+000000000428+300+430711670077=043999659571CN9D=+2+430711670077=043'
   ...            b"999659571CN9D=:2'HNVSK:998:3+PIN:1+998+1+2::oIm3BlHv6mQBAADYgbPpp?+kWrAQA+1+"
   ...            b"2:2:13:@8@00000000:5:1+280:15050500:hermes:S:0:0+0'HNVSD:999:1+@195@HNSHK:2:"
   ...            b'4+PIN:1+999+9166926+1+1+2::oIm3BlHv6mQBAADYgbPpp?+kWrAQA+1+1+1:999:1+6:10:16'
   ...            b"+280:15050500:hermes:S:0:0'HIRMG:3:2+0010::Nachricht entgegengenommen.+0100:"
   ...            b":Dialog beendet.'HNSHA:4:2+9166926''HNHBS:5:1+2'")
   >>> from fints.parser import FinTS3Parser
   >>> s = FinTS3Parser().parse_message(message)
   >>> s
   SegmentSequence([fints.segments.HNHBK3(header=fints.formals.SegmentHeader('HNHBK', 1, 3), message_size='000000000428', hbci_version=300, dialogue_id='430711670077=043999659571CN9D=', message_number=2, reference_message=fints.formals.ReferenceMessage(dialogue_id='430711670077=043999659571CN9D=', message_number=2)), fints.segments.HNVSK3(header=fints.formals.SegmentHeader('HNVSK', 998, 3), security_profile=fints.formals.SecurityProfile(security_method='PIN', security_method_version=1), security_function='998', security_role='1', security_identification_details=fints.formals.SecurityIdentificationDetails(name_party='2', cid=None, identifier_party='oIm3BlHv6mQBAADYgbPpp+kWrAQA'), security_datetime=fints.formals.SecurityDateTime(datetime_type='1'), encryption_algorithm=fints.formals.EncryptionAlgorithm(usage_encryption='2', operation_mode='2', encryption_algorithm='13', algorithm_parameter_value=b'00000000', algorithm_parameter_name='5', algorithm_parameter_iv_name='1'), key_name=fints.formals.KeyName(bank_identifier=fints.formals.BankIdentifier(country_identifier='280', bank_code='15050500'), user_id='hermes', key_type='S', key_number=0, key_version=0), compression_function='0'), fints.segments.HNVSD1(header=fints.formals.SegmentHeader('HNVSD', 999, 1), data=SegmentSequence([fints.segments.HNSHK4(header=fints.formals.SegmentHeader('HNSHK', 2, 4), security_profile=fints.formals.SecurityProfile(security_method='PIN', security_method_version=1), security_function='999', security_reference='9166926', security_application_area='1', security_role='1', security_identification_details=fints.formals.SecurityIdentificationDetails(name_party='2', cid=None, identifier_party='oIm3BlHv6mQBAADYgbPpp+kWrAQA'), security_reference_number=1, security_datetime=fints.formals.SecurityDateTime(datetime_type='1'), hash_algorithm=fints.formals.HashAlgorithm(usage_hash='1', hash_algorithm='999', algorithm_parameter_name='1'), signature_algorithm=fints.formals.SignatureAlgorithm(usage_signature='6', signature_algorithm='10', operation_mode='16'), key_name=fints.formals.KeyName(bank_identifier=fints.formals.BankIdentifier(country_identifier='280', bank_code='15050500'), user_id='hermes', key_type='S', key_number=0, key_version=0)), fints.segments.HIRMG2(header=fints.formals.SegmentHeader('HIRMG', 3, 2), response=[fints.formals.Response(response_code='0010', reference_element=None, response_text='Nachricht entgegengenommen.'), fints.formals.Response(response_code='0100', reference_element=None, response_text='Dialog beendet.')]), fints.segments.HNSHA2(header=fints.formals.SegmentHeader('HNSHA', 4, 2), security_reference='9166926')])), fints.segments.HNHBS1(header=fints.formals.SegmentHeader('HNHBS', 5, 1), message_number=2)])
   >>> from fints.parser import FinTS3Serializer
   >>> FinTS3Serializer().serialize_message(s)
   b"HNHBK:1:3+000000000428+300+430711670077=043999659571CN9D=+2+430711670077=043999659571CN9D=:2'HNVSK:998:3+PIN:1+998+1+2::oIm3BlHv6mQBAADYgbPpp?+kWrAQA+1+2:2:13:@8@00000000:5:1+280:15050500:hermes:S:0:0+0'HNVSD:999:1+@195@HNSHK:2:4+PIN:1+999+9166926+1+1+2::oIm3BlHv6mQBAADYgbPpp?+kWrAQA+1+1+1:999:1+6:10:16+280:15050500:hermes:S:0:0'HIRMG:3:2+0010::Nachricht entgegengenommen.+0100::Dialog beendet.'HNSHA:4:2+9166926''HNHBS:5:1+2'"


FinTS Segment Sequence
----------------------

A message is a sequence of segments. The :class:`~fints.formals.SegmentSequence` object allows searching for segments by type and version, by default recursing into nested sequences.

.. autoclass:: fints.formals.SegmentSequence
   :members:
   :undoc-members: print_nested


FinTS Segments
--------------
A segment is the core communication workhorse in FinTS. Each segment has a header of fixed format, which includes the segment type ("Segmentkennung"), number within the message, version, and, optionally, the number of the segment of another message it is in response or relation to ("Bezugssegment").

The header is followed by a nested structure of fields and groups of fields, the exact specification of which depends on the segment type and version.

All segment classes derive from  :class:`~fints.segments.FinTS3Segment`, which specifies the ``header`` attribute of :class:`~fints.formals.SegmentHeader` type.

.. autoclass:: fints.segments.FinTS3Segment
   :members:
   :inherited-members: print_nested

   .. attribute:: TYPE

      Segment type. Will be determined from the class name in subclasses, if the class name consists only of uppercase characters followed by decimal digits. Subclasses may explicitly set a class attribute instead.

   .. attribute:: VERSION

      Segment version. Will be determined from the class name in subclasses, if the class name consists only of uppercase characters followed by decimal digits. Subclasses may explicitly set a class attribute instead.

   .. classmethod:: find_subclass(segment: list)

      Parse the given ``segment`` parameter as a :class:`~fints.formals.SegmentHeader` and return a subclass with matching type and version class attributes.

.. autoclass:: fints.formals.SegmentHeader
   :members:

The :class:`~fints.segments.FinTS3Segment` class and its base classes employ a number of dynamic programming techniques so that derived classes need only specify the name, order and type of fields and all type conversion, construction etc. will take place automatically. All derived classes basically should behave "as expected", returning only native Python datatypes.

Consider this example segment class:

.. code-block:: python

    class HNHBS1(FinTS3Segment):
        message_number = DataElementField(type='num', max_length=4)

Calling ``print_nested`` on an instance of this class might yield:

.. code-block:: python

    fints.segments.HNHBS1(
        header = fints.formals.SegmentHeader('HNHBS', 4, 1),
        message_number = 1,
    )

Working with Segments
~~~~~~~~~~~~~~~~~~~~~

Objects of :class:`~fints.segments.FinTS3Segment` or a subclass can be created by calling their constructor. The constructor takes optional arguments for all fields of the class. Setting and getting fields and subfields works, and consumes and returns Python objects as appropriate:

.. code-block:: python

    >>> from fints.segments import HNHBS1
    >>> s = HNHBS1()
    >>> s
    fints.segments.HNHBS1(header=fints.formals.SegmentHeader('HNHBS', None, 1), message_number=None)
    >>> s.header.number = 3
    >>> s.header
    fints.formals.SegmentHeader('HNHBS', 3, 1)

When setting a value, format and length restrictions will be checked, if possible:

.. code-block:: python

    >>> s.message_number = 'abc'
    ValueError: invalid literal for int() with base 10: 'abc'
    >>> s.message_number = 12345
    ValueError: Value '12345' cannot be rendered: max_length=4 exceeded

The only exception is: Every field can be set to ``None`` in order to clear the field and make it unset, recursively. No checking is performed whether all fields that are required (or conditionally required) by the specification are set.

.. code-block:: python

    >>> s.header = None
    >>> s
    fints.segments.HNHBS1(header=fints.formals.SegmentHeader(None, None, None), message_number=None)

When calling the constructor with non-keyword arguments, fields are assigned in order, with the exception of ``header`` in :class:`~fints.segments.FinTS3Segment` subclasses, which can only be given as a keyword argument. When no ``header`` argument is present, a :class:`~fints.formals.SegmentHeader` is automatically constructed with default values (and no ``number``). It's generally not required to construct the ``header`` parameter manually.

**FIXME** The ``number`` should in the future be generated automatically within in sequence (at least before serializing).

.. code-block:: python

    >>> HNHBS1(42)
    fints.segments.HNHBS1(header=fints.formals.SegmentHeader('HNHBS', None, 1), message_number=42)
    >>> HNHBS1(42, header=SegmentHeader('FOO'))
    fints.segments.HNHBS1(header=fints.formals.SegmentHeader('FOO', None, None), message_number=42)


Some segment fields have a variable number of values. These are always treated as a list, and minimum/maximum list length is obeyed. Setting a value beyond the end of the list results in an exception. Empty values are added to maintain the correct minimum number of values.

.. code-block:: python

    >>> from fints.segments import HIRMG2
    >>> s = HIRMG2()
    >>> s
    fints.segments.HIRMG2(header=fints.formals.SegmentHeader('HIRMG', None, 2), response=[fints.formals.Response(response_code=None, reference_element=None, response_text=None)])
    >>> s.response[0].response_code = '0010'
    >>> s.response[1].response_code = '0100'
    >>> s.print_nested()
    fints.segments.HIRMG2(
        header = fints.formals.SegmentHeader('HIRMG', None, 2),
        response = [
                    fints.formals.Response(
                        response_code = '0010',
                        reference_element = None,
                        response_text = None,
                    ),
                    fints.formals.Response(
                        response_code = '0100',
                        reference_element = None,
                        response_text = None,
                    ),
            ],
    )
    >>> HIRMG2(response=[fints.formals.Response('2342')]).print_nested()
    fints.segments.HIRMG2(
        header = fints.formals.SegmentHeader('HIRMG', None, 2),
        response = [
                    fints.formals.Response(
                        response_code = '2342',
                        reference_element = None,
                        response_text = None,
                    ),
            ],
    )


All Segments
____________

.. automodule:: fints.segments
    :members:
    :inherited-members:
