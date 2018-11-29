import datetime
import random

from fints.exceptions import FinTSError
from .formals import (
    AlgorithmParameterIVName, AlgorithmParameterName, CompressionFunction,
    DateTimeType, EncryptionAlgorithm, EncryptionAlgorithmCoded,
    HashAlgorithm, IdentifiedRole, KeyName, KeyType, OperationMode,
    SecurityApplicationArea, SecurityDateTime,
    SecurityIdentificationDetails, SecurityMethod, SecurityProfile,
    SecurityRole, SignatureAlgorithm, UsageEncryption, UserDefinedSignature,
)
from .message import FinTSMessage
from .segments.message import HNSHA2, HNSHK4, HNVSD1, HNVSK3
from .types import SegmentSequence


class EncryptionMechanism:
    def encrypt(self, message: FinTSMessage):
        raise NotImplemented()

    def decrypt(self, message: FinTSMessage):
        raise NotImplemented()


class AuthenticationMechanism:
    def sign_prepare(self, message: FinTSMessage):
        raise NotImplemented()
    
    def sign_commit(self, message: FinTSMessage):
        raise NotImplemented()
    
    def verify(self, message: FinTSMessage):
        raise NotImplemented()


class PinTanDummyEncryptionMechanism(EncryptionMechanism):
    def __init__(self, security_method_version=1):
        super().__init__()
        self.security_method_version = security_method_version

    def encrypt(self, message: FinTSMessage):
        assert message.segments[0].header.type == 'HNHBK'
        assert message.segments[-1].header.type == 'HNHBS'

        plain_segments = message.segments[1:-1]
        del message.segments[1:-1]

        _now = datetime.datetime.now()

        message.segments.insert(
            1,
            HNVSK3(
                security_profile=SecurityProfile(SecurityMethod.PIN, self.security_method_version),
                security_function='998',
                security_role=SecurityRole.ISS,
                security_identification_details=SecurityIdentificationDetails(
                    IdentifiedRole.MS,
                    identifier=message.dialog.client.system_id,
                ),
                security_datetime=SecurityDateTime(
                    DateTimeType.STS,
                    _now.date(),
                    _now.time(),
                ),
                encryption_algorithm=EncryptionAlgorithm(
                    UsageEncryption.OSY,
                    OperationMode.CBC,
                    EncryptionAlgorithmCoded.TWOKEY3DES,
                    b'\x00'*8,
                    AlgorithmParameterName.KYE,
                    AlgorithmParameterIVName.IVC,
                ),
                key_name=KeyName(
                    message.dialog.client.bank_identifier,
                    message.dialog.client.user_id,
                    KeyType.V,
                    0,
                    0,
                ),
                compression_function=CompressionFunction.NULL,
            )
        )
        message.segments[1].header.number = 998
        message.segments.insert(
            2,
            HNVSD1(
                data=SegmentSequence(segments=plain_segments)
            )
        )
        message.segments[2].header.number = 999

    def decrypt(self, message: FinTSMessage):
        pass


class PinTanAuthenticationMechanism(AuthenticationMechanism):
    def __init__(self, pin):
        self.pin = pin
        self.pending_signature = None
        self.security_function = None

    def sign_prepare(self, message: FinTSMessage):
        _now = datetime.datetime.now()
        rand = random.SystemRandom()

        self.pending_signature = HNSHK4(
            security_profile=SecurityProfile(SecurityMethod.PIN, 1),
            security_function=self.security_function,
            security_reference=rand.randint(1000000, 9999999),
            security_application_area=SecurityApplicationArea.SHM,
            security_role=SecurityRole.ISS,
            security_identification_details=SecurityIdentificationDetails(
                IdentifiedRole.MS,
                identifier=message.dialog.client.system_id,
            ),
            security_reference_number=1,  # FIXME
            security_datetime=SecurityDateTime(
                DateTimeType.STS,
                _now.date(),
                _now.time(),
            ),
            hash_algorithm=HashAlgorithm(
                usage_hash='1',
                hash_algorithm='999',
                algorithm_parameter_name='1',
            ),
            signature_algorithm=SignatureAlgorithm(
                usage_signature='6',
                signature_algorithm='10',
                operation_mode='16',
            ),
            key_name=KeyName(
                message.dialog.client.bank_identifier,
                message.dialog.client.user_id,
                KeyType.S,
                0,
                0,
            ),

        )

        message += self.pending_signature

    def _get_tan(self):
        return None

    def sign_commit(self, message: FinTSMessage):
        if not self.pending_signature:
            raise FinTSError("No signature is pending")

        if self.pending_signature not in message.segments:
            raise FinTSError("Cannot sign a message that was not prepared")

        signature = HNSHA2(
            security_reference=self.pending_signature.security_reference,
            user_defined_signature=UserDefinedSignature(
                pin=self.pin,
                tan=self._get_tan(),
            ),
        )

        self.pending_signature = None
        message += signature

    def verify(self, message: FinTSMessage):
        pass


class PinTanOneStepAuthenticationMechanism(PinTanAuthenticationMechanism):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.security_function = '999'


class PinTanTwoStepAuthenticationMechanism(PinTanAuthenticationMechanism):
    def __init__(self, client, security_function, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = client
        self.security_function = security_function

    def _get_tan(self):
        retval = self.client._pending_tan
        self.client._pending_tan = None
        return retval
