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
   SegmentSequence([fints.segments.HNHBK3(header=fints.formals.SegmentHeader('HNHBK', 1, 3), message_size='000000000428', hbci_version=300, dialog_id='430711670077=043999659571CN9D=', message_number=2, reference_message=fints.formals.ReferenceMessage(dialog_id='430711670077=043999659571CN9D=', message_number=2)), fints.segments.HNVSK3(header=fints.formals.SegmentHeader('HNVSK', 998, 3), security_profile=fints.formals.SecurityProfile(security_method='PIN', security_method_version=1), security_function='998', security_role='1', security_identification_details=fints.formals.SecurityIdentificationDetails(name_party='2', cid=None, identifier_party='oIm3BlHv6mQBAADYgbPpp+kWrAQA'), security_datetime=fints.formals.SecurityDateTime(datetime_type='1'), encryption_algorithm=fints.formals.EncryptionAlgorithm(usage_encryption='2', operation_mode='2', encryption_algorithm='13', algorithm_parameter_value=b'00000000', algorithm_parameter_name='5', algorithm_parameter_iv_name='1'), key_name=fints.formals.KeyName(bank_identifier=fints.formals.BankIdentifier(country_identifier='280', bank_code='15050500'), user_id='hermes', key_type='S', key_number=0, key_version=0), compression_function='0'), fints.segments.HNVSD1(header=fints.formals.SegmentHeader('HNVSD', 999, 1), data=SegmentSequence([fints.segments.HNSHK4(header=fints.formals.SegmentHeader('HNSHK', 2, 4), security_profile=fints.formals.SecurityProfile(security_method='PIN', security_method_version=1), security_function='999', security_reference='9166926', security_application_area='1', security_role='1', security_identification_details=fints.formals.SecurityIdentificationDetails(name_party='2', cid=None, identifier_party='oIm3BlHv6mQBAADYgbPpp+kWrAQA'), security_reference_number=1, security_datetime=fints.formals.SecurityDateTime(datetime_type='1'), hash_algorithm=fints.formals.HashAlgorithm(usage_hash='1', hash_algorithm='999', algorithm_parameter_name='1'), signature_algorithm=fints.formals.SignatureAlgorithm(usage_signature='6', signature_algorithm='10', operation_mode='16'), key_name=fints.formals.KeyName(bank_identifier=fints.formals.BankIdentifier(country_identifier='280', bank_code='15050500'), user_id='hermes', key_type='S', key_number=0, key_version=0)), fints.segments.HIRMG2(header=fints.formals.SegmentHeader('HIRMG', 3, 2), responses=[fints.formals.Response(code='0010', reference_element=None, text='Nachricht entgegengenommen.'), fints.formals.Response(code='0100', reference_element=None, text='Dialog beendet.')]), fints.segments.HNSHA2(header=fints.formals.SegmentHeader('HNSHA', 4, 2), security_reference='9166926')])), fints.segments.HNHBS1(header=fints.formals.SegmentHeader('HNHBS', 5, 1), message_number=2)])
   >>> from fints.parser import FinTS3Serializer
   >>> FinTS3Serializer().serialize_message(s)
   b"HNHBK:1:3+000000000428+300+430711670077=043999659571CN9D=+2+430711670077=043999659571CN9D=:2'HNVSK:998:3+PIN:1+998+1+2::oIm3BlHv6mQBAADYgbPpp?+kWrAQA+1+2:2:13:@8@00000000:5:1+280:15050500:hermes:S:0:0+0'HNVSD:999:1+@195@HNSHK:2:4+PIN:1+999+9166926+1+1+2::oIm3BlHv6mQBAADYgbPpp?+kWrAQA+1+1+1:999:1+6:10:16+280:15050500:hermes:S:0:0'HIRMG:3:2+0010::Nachricht entgegengenommen.+0100::Dialog beendet.'HNSHA:4:2+9166926''HNHBS:5:1+2'"

.. note::

  In general parsing followed by serialization is not idempotent: A message may contain empty list elements at the end, but our serializer will never generate them.
