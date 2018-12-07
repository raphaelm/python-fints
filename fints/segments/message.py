from fints.fields import (
    CodeField, DataElementField, DataElementGroupField,
    SegmentSequenceField, ZeroPaddedNumericField,
)
from fints.formals import (
    Certificate, CompressionFunction, EncryptionAlgorithm,
    HashAlgorithm, KeyName, ReferenceMessage, SecurityApplicationArea,
    SecurityDateTime, SecurityIdentificationDetails, SecurityProfile,
    SecurityRole, SignatureAlgorithm, UserDefinedSignature,
)

from .base import FinTS3Segment


class HNHBK3(FinTS3Segment):
    """Nachrichtenkopf"""
    message_size = ZeroPaddedNumericField(length=12, _d="Größe der Nachricht (nach Verschlüsselung und Komprimierung)")
    hbci_version = DataElementField(type='num', max_length=3, _d="HBCI-Version")
    dialog_id = DataElementField(type='id', _d="Dialog-ID")
    message_number = DataElementField(type='num', max_length=4, _d="Nachrichtennummer")
    reference_message = DataElementGroupField(type=ReferenceMessage, required=False, _d="Bezugsnachricht")


class HNHBS1(FinTS3Segment):
    """Nachrichtenabschluss"""
    message_number = DataElementField(type='num', max_length=4, _d="Nachrichtennummer")


class HNVSK3(FinTS3Segment):
    """Verschlüsselungskopf, version 3

    Source: FinTS Financial Transaction Services, Sicherheitsverfahren HBCI"""
    security_profile = DataElementGroupField(type=SecurityProfile, _d="Sicherheitsprofil")
    security_function = DataElementField(type='code', max_length=3, _d="Sicherheitsfunktion, kodiert")
    security_role = CodeField(SecurityRole, max_length=3, _d="Rolle des Sicherheitslieferanten, kodiert")
    security_identification_details = DataElementGroupField(type=SecurityIdentificationDetails, _d="Sicherheitsidentifikation, Details")
    security_datetime = DataElementGroupField(type=SecurityDateTime, _d="Sicherheitsdatum und -uhrzeit")
    encryption_algorithm = DataElementGroupField(type=EncryptionAlgorithm, _d="Verschlüsselungsalgorithmus")
    key_name = DataElementGroupField(type=KeyName, _d="Schlüsselname")
    compression_function = CodeField(CompressionFunction, max_length=3, _d="Komprimierungsfunktion")
    certificate = DataElementGroupField(type=Certificate, required=False, _d="Zertifikat")


class HNVSD1(FinTS3Segment):
    """Verschlüsselte Daten, version 1

    Source: FinTS Financial Transaction Services, Sicherheitsverfahren HBCI"""
    data = SegmentSequenceField(_d="Daten, verschlüsselt")


class HNSHK4(FinTS3Segment):
    """Signaturkopf, version 4

    Source: FinTS Financial Transaction Services, Sicherheitsverfahren HBCI"""
    security_profile = DataElementGroupField(type=SecurityProfile, _d="Sicherheitsprofil")
    security_function = DataElementField(type='code', max_length=3, _d="Sicherheitsfunktion, kodiert")
    security_reference = DataElementField(type='an', max_length=14, _d="Sicherheitskontrollreferenz")
    security_application_area = CodeField(SecurityApplicationArea, max_length=3, _d="Bereich der Sicherheitsapplikation, kodiert")
    security_role = CodeField(SecurityRole, max_length=3, _d="Rolle des Sicherheitslieferanten, kodiert")
    security_identification_details = DataElementGroupField(type=SecurityIdentificationDetails, _d="Sicherheitsidentifikation, Details")
    security_reference_number = DataElementField(type='num', max_length=16, _d="Sicherheitsreferenznummer")
    security_datetime = DataElementGroupField(type=SecurityDateTime, _d="Sicherheitsdatum und -uhrzeit")
    hash_algorithm = DataElementGroupField(type=HashAlgorithm, _d="Hashalgorithmus")
    signature_algorithm = DataElementGroupField(type=SignatureAlgorithm, _d="Signaturalgorithmus")
    key_name = DataElementGroupField(type=KeyName, _d="Schlüsselname")
    certificate = DataElementGroupField(type=Certificate, required=False, _d="Zertifikat")


class HNSHA2(FinTS3Segment):
    """Signaturabschluss, version 2

    Source: FinTS Financial Transaction Services, Sicherheitsverfahren HBCI"""
    security_reference = DataElementField(type='an', max_length=14, _d="Sicherheitskontrollreferenz")
    validation_result = DataElementField(type='bin', max_length=512, required=False, _d="Validierungsresultat")
    user_defined_signature = DataElementGroupField(type=UserDefinedSignature, required=False, _d="Benutzerdefinierte Signatur")
