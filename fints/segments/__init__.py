import re

from fints.formals import (
    AccountInformation, KTZ1, AccountLimit,
    AllowedTransaction, BankIdentifier, Certificate, Container, ContainerMeta,
    DataElementField, DataElementGroupField, EncryptionAlgorithm,
    HashAlgorithm, KeyName, ParameterPinTan, ParameterTwostepTAN1,
    ParameterTwostepTAN2, ParameterTwostepTAN3, ParameterTwostepTAN4,
    ParameterTwostepTAN5, ParameterTwostepTAN6, ReferenceMessage, Response,
    SecurityDateTime, SecurityIdentificationDetails, SecurityProfile, SecurityRole,
    SegmentHeader, SegmentSequenceField, SignatureAlgorithm,
    SupportedHBCIVersions2, SupportedLanguages2, UserDefinedSignature,
    CompressionFunction, SecurityApplicationArea, SecurityClass, UPDUsage
)
from fints.fields import CodeField, IntCodeField
from fints.utils import SubclassesMixin, classproperty

TYPE_VERSION_RE = re.compile(r'^([A-Z]+)(\d+)$')

class FinTS3SegmentOLD:
    type = '???'
    country_code = 280
    version = 2
    def __init__(self, segmentno, data):
        self.segmentno = segmentno
        self.data = data
    def __str__(self):
        res = '{}:{}:{}'.format(self.type, self.segmentno, self.version)
        for d in self.data:
            res += '+' + str(d)
        return res + "'"

class FinTS3SegmentMeta(ContainerMeta):
    @staticmethod
    def _check_fields_recursive(instance):
        for name, field in instance._fields.items():
            if not isinstance(field, (DataElementField, DataElementGroupField)):
                raise TypeError("{}={!r} is not DataElementField or DataElementGroupField".format(name, field))
            if isinstance(field, DataElementGroupField):
                FinTS3SegmentMeta._check_fields_recursive(field.type)

    def __new__(cls, name, bases, classdict):
        retval = super().__new__(cls, name, bases, classdict)
        FinTS3SegmentMeta._check_fields_recursive(retval)
        return retval

class FinTS3Segment(Container, SubclassesMixin, metaclass=FinTS3SegmentMeta):
    header = DataElementGroupField(type=SegmentHeader, _d="Segmentkopf")

    @classproperty
    def TYPE(cls):
        match = TYPE_VERSION_RE.match(cls.__name__)
        if match:
            return match.group(1)

    @classproperty
    def VERSION(cls):
        match = TYPE_VERSION_RE.match(cls.__name__)
        if match:
            return int( match.group(2) )

    def __init__(self, *args, **kwargs):
        if 'header' not in kwargs:
            kwargs['header'] = SegmentHeader(self.TYPE, None, self.VERSION)

        args = (kwargs.pop('header'), ) + args

        return super().__init__(*args, **kwargs)

    @classmethod
    def find_subclass(cls, segment):
        h = SegmentHeader.naive_parse(segment[0])
        target_cls = None

        for possible_cls in cls._all_subclasses():
            if getattr(possible_cls, 'TYPE', None) == h.type and getattr(possible_cls, 'VERSION', None) == h.version:
                target_cls = possible_cls

        if not target_cls:
            target_cls = cls

        return target_cls


class HNVSD1(FinTS3Segment):
    "Verschlüsselte Daten"
    data = SegmentSequenceField(_d="Daten, verschlüsselt")

class HNVSK3(FinTS3Segment):
    "Verschlüsselungskopf"
    security_profile = DataElementGroupField(type=SecurityProfile, _d="Sicherheitsprofil")
    security_function = DataElementField(type='code', max_length=3, _d="Sicherheitsfunktion, kodiert")
    security_role = CodeField(SecurityRole, max_length=3, _d="Rolle des Sicherheitslieferanten, kodiert")
    security_identification_details = DataElementGroupField(type=SecurityIdentificationDetails, _d="Sicherheitsidentifikation, Details")
    security_datetime = DataElementGroupField(type=SecurityDateTime, _d="Sicherheitsdatum und -uhrzeit")
    encryption_algorithm = DataElementGroupField(type=EncryptionAlgorithm, _d="Verschlüsselungsalgorithmus")
    key_name = DataElementGroupField(type=KeyName, _d="Schlüsselname")
    compression_function = CodeField(CompressionFunction, max_length=3, _d="Komprimierungsfunktion")
    certificate = DataElementGroupField(type=Certificate, required=False, _d="Zertifikat")

class HNSHK4(FinTS3Segment):
    "Signaturkopf"
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
    "Signaturabschluss"
    security_reference = DataElementField(type='an', max_length=14, _d="Sicherheitskontrollreferenz")
    validation_result = DataElementField(type='bin', max_length=512, required=False, _d="Validierungsresultat")
    user_defined_signature = DataElementGroupField(type=UserDefinedSignature, required=False, _d="Benutzerdefinierte Signatur")

class HIRMG2(FinTS3Segment):
    "Rückmeldungen zur Gesamtnachricht"
    responses = DataElementGroupField(type=Response, min_count=1, max_count=99, _d="Rückmeldung")

class HIRMS2(FinTS3Segment):
    "Rückmeldungen zu Segmenten"
    responses = DataElementGroupField(type=Response, min_count=1, max_count=99, _d="Rückmeldung")

class HIUPA4(FinTS3Segment):
    "Userparameter allgemein"
    user_identifier = DataElementField(type='id', _d="Benutzerkennung")
    upd_version = DataElementField(type='num', max_length=3, _d="UPD-Version")
    upd_usage = CodeField(UPDUsage, length=1, _d="UPD-Verwendung")
    username = DataElementField(type='an', max_length=35, required=False, _d="Benutzername")
    extension = DataElementField(type='an', max_length=2048, required=False, _d="Erweiterung, allgemein")

class HIUPD6(FinTS3Segment):
    "Kontoinformationen"
    account_information = DataElementGroupField(type=AccountInformation, required=False, _d="Kontoverbindung")
    iban = DataElementField(type='an', max_length=34, _d="IBAN")
    customer_id = DataElementField(type='id', _d="Kunden-ID")
    account_type = DataElementField(type='num', max_length=2, _d="Kontoart")
    account_currency = DataElementField(type='cur', _d="Kontowährung")
    name_account_owner_1 = DataElementField(type='an', max_length=27, _d="Name des Kontoinhabers 1")
    name_account_owner_2 = DataElementField(type='an', max_length=27, required=False, _d="Name des Kontoinhabers 2")
    account_product_name = DataElementField(type='an', max_length=30, required=False, _d="Kontoproduktbezeichnung")
    account_limit = DataElementGroupField(type=AccountLimit, required=False, _d="Kontolimit")
    allowed_transactions = DataElementGroupField(type=AllowedTransaction, max_count=999, required=False, _d="Erlaubte Geschäftsvorfälle")
    extension = DataElementField(type='an', max_length=2048, required=False, _d="Erweiterung, kontobezogen")

class ParameterSegment(FinTS3Segment):
    max_number_tasks = DataElementField(type='num', max_length=3, _d="Maximale Anzahl Aufträge")
    min_number_signatures = DataElementField(type='num', length=1, _d="Anzahl Signaturen mindestens")
    security_class = IntCodeField(SecurityClass, length=1, _d="Sicherheitsklasse")

class HITANSBase(ParameterSegment):
    pass

class HITANS1(HITANSBase):
    parameter = DataElementGroupField(type=ParameterTwostepTAN1)

class HITANS2(HITANSBase):
    parameter = DataElementGroupField(type=ParameterTwostepTAN2)

class HITANS3(HITANSBase):
    parameter = DataElementGroupField(type=ParameterTwostepTAN3)

class HITANS4(HITANSBase):
    parameter = DataElementGroupField(type=ParameterTwostepTAN4)

class HITANS5(HITANSBase):
    parameter = DataElementGroupField(type=ParameterTwostepTAN5)

class HITANS6(HITANSBase):
    parameter = DataElementGroupField(type=ParameterTwostepTAN6)

class HIPINS1(ParameterSegment):
    """PIN/TAN-spezifische Informationen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN 
    """
    parameter = DataElementGroupField(type=ParameterPinTan, _d="Parameter PIN/TAN-spezifische Informationen") 


class HIBPA3(FinTS3Segment):
    """Bankparameter allgemein, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    bpd_version = DataElementField(type='num', max_length=3, _d="BPD-Version")
    bank_identifier = DataElementGroupField(type=BankIdentifier, _d="Kreditinstitutskennung")
    bank_name = DataElementField(type='an', max_length=60, _d="Kreditinstitutsbezeichnung")
    number_tasks = DataElementField(type='num', max_length=3, _d="Anzahl Geschäftsvorfallarten pro Nachricht")
    supported_languages = DataElementGroupField(type=SupportedLanguages2, _d="Unterstützte Sprachen")
    supported_hbci_version = DataElementGroupField(type=SupportedHBCIVersions2, _d="Unterstützte HBCI-Versionen")
    max_message_length = DataElementField(type='num', max_length=4, required=False, _d="Maximale Nachrichtengröße")
    min_timeout = DataElementField(type='num', max_length=4, required=False, _d="Minimaler Timeout-Wert")
    max_timeout = DataElementField(type='num', max_length=4, required=False, _d="Maximaler Timeout-Wert")

from . import accounts, auth, debit, depot, dialog, message, saldo, statement, transfer
