import re

from fints.fields import CodeField, IntCodeField
from fints.formals import (
    KTZ1, AccountInformation, AccountLimit, AllowedTransaction, BankIdentifier,
    Certificate, CompressionFunction, Container, ContainerMeta,
    DataElementField, DataElementGroupField, EncryptionAlgorithm, HashAlgorithm,
    KeyName, ParameterPinTan, ParameterTwostepTAN1, ParameterTwostepTAN2,
    ParameterTwostepTAN3, ParameterTwostepTAN4, ParameterTwostepTAN5,
    ParameterTwostepTAN6, ReferenceMessage, Response, SecurityApplicationArea,
    SecurityClass, SecurityDateTime, SecurityIdentificationDetails,
    SecurityProfile, SecurityRole, SegmentHeader, SegmentSequenceField,
    SignatureAlgorithm, SupportedHBCIVersions2, SupportedLanguages2, UPDUsage,
    UserDefinedSignature, Language2, CommunicationParameter2,
)
from fints.utils import SubclassesMixin, classproperty

TYPE_VERSION_RE = re.compile(r'^([A-Z]+)(\d+)$')

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

class HKKOM4(FinTS3Segment):
    """Kommunikationszugang anfordern, version 4

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    start_bank_identifier = DataElementGroupField(type=BankIdentifier, required=False, _d="Von Kreditinstitutskennung")
    end_bank_identifier = DataElementGroupField(type=BankIdentifier, required=False, _d="Bis Kreditinstitutskennung")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")

class HIKOM4(FinTS3Segment):
    """Kommunikationszugang rückmelden, version 4

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    bank_identifier = DataElementGroupField(type=BankIdentifier, _d="Kreditinstitutskennung")
    default_language = CodeField(enum=Language2, max_length=3, _d="Standardsprache")
    communication_parameters = DataElementGroupField(type=CommunicationParameter2, min_count=1, max_count=9, _d="Kommunikationsparameter")

from . import (
    accounts, auth, debit, depot, dialog, message, saldo, statement, transfer,
)
