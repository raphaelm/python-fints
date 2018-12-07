import re

from fints.fields import *
from fints.types import *
from fints.utils import RepresentableEnum, ShortReprMixin

CUSTOMER_ID_ANONYMOUS = '9999999999'


class DataElementGroup(Container):
    pass


class SegmentHeader(ShortReprMixin, DataElementGroup):
    """Segmentkopf"""
    type = AlphanumericField(max_length=6, _d='Segmentkennung')
    number = NumericField(max_length=3, _d='Segmentnummer')
    version = NumericField(max_length=3, _d='Segmentversion')
    reference = NumericField(max_length=3, required=False, _d='Bezugssegment')


class ReferenceMessage(DataElementGroup):
    dialog_id = DataElementField(type='id')
    message_number = NumericField(max_length=4)


class SecurityMethod(RepresentableEnum):
    DDV = 'DDV'
    RAH = 'RAH'
    RDH = 'RDH'
    PIN = 'PIN'


class SecurityProfile(DataElementGroup):
    """Sicherheitsprofil"""
    security_method = CodeField(enum=SecurityMethod, length=3, _d="Sicherheitsverfahren")
    security_method_version = DataElementField(type='num', _d="Version des Sicherheitsverfahrens")


class IdentifiedRole(RepresentableEnum):
    MS = '1' #: Message Sender
    MR = '2' #: Message Receiver


class SecurityIdentificationDetails(DataElementGroup):
    identified_role = CodeField(IdentifiedRole, max_length=3)
    cid = DataElementField(type='bin', max_length=256)
    identifier = DataElementField(type='id')


class DateTimeType(RepresentableEnum):
    STS = '1'  #: Sicherheitszeitstempel
    CRT = '6'  #: Certificate Revocation Time


class SecurityDateTime(DataElementGroup):
    date_time_type = CodeField(DateTimeType, max_length=3)
    date = DataElementField(type='dat', required=False)
    time = DataElementField(type='tim', required=False)


class UsageEncryption(RepresentableEnum):
    OSY = '2'  #: Owner Symmetric


class OperationMode(RepresentableEnum):
    CBC = '2'  #: Cipher Block Chaining
    ISO_9796_1 = '16'  #: ISO 9796-1 (bei RDH)
    ISO_9796_2_RANDOM = '17'  #: ISO 9796-2 mit Zufallszahl (bei RDH)
    PKCS1V15 = '18'  #: RSASSA-PKCS#1 V1.5 (bei RDH); RSAES-PKCS#1 V1.5 (bei RAH, RDH)
    PSS = '19'  #: RSASSA-PSS (bei RAH, RDH)
    ZZZ = '999'  #: Gegenseitig vereinbart (DDV: Retail-MAC)


class EncryptionAlgorithmCoded(RepresentableEnum):
    TWOKEY3DES = '13' #: 2-Key-Triple-DES
    AES256 = '14' #: AES-256


class AlgorithmParameterName(RepresentableEnum):
    KYE = '5' #: Symmetrischer Schlüssel, verschlüsselt mit symmetrischem Schlüssel
    KYP = '6' #: Symmetrischer Schlüssel, verschlüsselt mit öffentlichem Schlüssel


class AlgorithmParameterIVName(RepresentableEnum):
    IVC = '1' #: Initialization value, clear text


class EncryptionAlgorithm(DataElementGroup):
    usage_encryption = CodeField(UsageEncryption, max_length=3)
    operation_mode = CodeField(OperationMode, max_length=3)
    encryption_algorithm = CodeField(EncryptionAlgorithmCoded, max_length=3)
    algorithm_parameter_value = DataElementField(type='bin', max_length=512)
    algorithm_parameter_name = CodeField(AlgorithmParameterName, max_length=3)
    algorithm_parameter_iv_name = CodeField(AlgorithmParameterIVName, max_length=3)
    algorithm_parameter_iv_value = DataElementField(type='bin', max_length=512, required=False)


class HashAlgorithm(DataElementGroup):
    usage_hash = DataElementField(type='code', max_length=3)
    hash_algorithm = DataElementField(type='code', max_length=3)
    algorithm_parameter_name = DataElementField(type='code', max_length=3)
    algorithm_parameter_value = DataElementField(type='bin', max_length=512, required=False)


class SignatureAlgorithm(DataElementGroup):
    usage_signature = DataElementField(type='code', max_length=3)
    signature_algorithm = DataElementField(type='code', max_length=3)
    operation_mode = DataElementField(type='code', max_length=3)


class BankIdentifier(DataElementGroup):
    COUNTRY_ALPHA_TO_NUMERIC = {
        # Kapitel E.4 der SEPA-Geschäftsvorfälle
        'BE': '056',
        'BG': '100',
        'DK': '208',
        'DE': '280',
        'FI': '246',
        'FR': '250',
        'GR': '300',
        'GB': '826',
        'IE': '372',
        'IS': '352',
        'IT': '380',
        'JP': '392',
        'CA': '124',
        'HR': '191',
        'LI': '438',
        'LU': '442',
        'NL': '528',
        'AT': '040',
        'PL': '616',
        'PT': '620',
        'RO': '642',
        'RU': '643',
        'SE': '752',
        'CH': '756',
        'SK': '703',
        'SI': '705',
        'ES': '724',
        'CZ': '203',
        'TR': '792',
        'HU': '348',
        'US': '840',
        'EU': '978'
    }
    COUNTRY_NUMERIC_TO_ALPHA = {v: k for k, v in COUNTRY_ALPHA_TO_NUMERIC.items()}
    COUNTRY_NUMERIC_TO_ALPHA['276'] = 'DE'  # not yet in use by banks, but defined by ISO

    country_identifier = DataElementField(type='ctr')
    bank_code = DataElementField(type='an', max_length=30)


class KeyType(RepresentableEnum):
    """Schlüsselart"""
    D = 'D'  #: Schlüssel zur Erzeugung digitaler Signaturen
    S = 'S'  #: Signierschlüssel
    V = 'V'  #: Chiffrierschlüssel


class KeyName(DataElementGroup):
    bank_identifier = DataElementGroupField(type=BankIdentifier)
    user_id = DataElementField(type='id')
    key_type = CodeField(KeyType, length=1, _d="Schlüsselart")
    key_number = DataElementField(type='num', max_length=3)
    key_version = DataElementField(type='num', max_length=3)


class Certificate(DataElementGroup):
    certificate_type = DataElementField(type='code')
    certificate_content = DataElementField(type='bin', max_length=4096)


class UserDefinedSignature(DataElementGroup):
    pin = PasswordField(max_length=99)
    tan = DataElementField(type='an', max_length=99, required=False)


class Response(DataElementGroup):
    code = DataElementField(type='dig', length=4)
    reference_element = DataElementField(type='an', max_length=7)
    text = DataElementField(type='an', max_length=80)
    parameters = DataElementField(type='an', max_length=35, max_count=10, required=False)


class Amount1(DataElementGroup):
    """Betrag

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    amount = DataElementField(type='wrt', _d="Wert")
    currency = DataElementField(type='cur', _d="Währung")


class AccountInformation(DataElementGroup):
    account_number = DataElementField(type='id')
    subaccount_number = DataElementField(type='id')
    bank_identifier = DataElementGroupField(type=BankIdentifier)


class AccountLimit(DataElementGroup):
    limit_type = DataElementField(type='code', length=1)
    limit_amount = DataElementGroupField(type=Amount1, required=False)
    limit_days = DataElementField(type='num', max_length=3, required=False)


class AllowedTransaction(DataElementGroup):
    transaction = DataElementField(type='an', max_length=6)
    required_signatures = DataElementField(type='num', max_length=2)
    limit_type = DataElementField(type='code', length=1, required=False)
    limit_amount = DataElementGroupField(type=Amount1, required=False)
    limit_days = DataElementField(type='num', max_length=3, required=False)


class TANTimeDialogAssociation(RepresentableEnum):
    NOT_ALLOWED = '1'  #: TAN nicht zeitversetzt / dialogübergreifend erlaubt
    ALLOWED = '2'  #: TAN zeitversetzt / dialogübergreifend erlaubt
    BOTH = '3'  #: beide Verfahren unterstützt
    NOT_APPLICABLE = '4'  #: nicht zutreffend


class AllowedFormat(RepresentableEnum):
    NUMERIC = '1'  #: numerisch
    ALPHANUMERIC = '2'  #: alfanumerisch


class TANListNumberRequired(RepresentableEnum):
    NO = '0'  #: Nein
    YES = '2'  #: Ja


class InitializationMode(RepresentableEnum):
    CLEARTEXT_PIN_NO_TAN = '00'  #: Initialisierungsverfahren mit Klartext-PIN und ohne TAN
    ENCRYPTED_PIN_NO_TAN = '01'  #: Schablone 01: Verschlüsselte PIN und ohne TAN
    MASK_02 = '02'  #: Schablone 02: Reserviert, bei FinTS zur Zeit nicht verwendet


class DescriptionRequired(RepresentableEnum):
    MUST_NOT = '0'  #: Bezeichnung des TAN-Mediums darf nicht angegeben werden
    MAY = '1'  #: Bezeichnung des TAN-Mediums kann angegeben werden
    MUST = '2'  #: Bezeichnung des TAN-Mediums muss angegeben werden


class SMSChargeAccountRequired(RepresentableEnum):
    MUST_NOT = '0'  #: SMS-Abbuchungskonto darf nicht angegeben werden
    MAY = '1'  #: SMS-Abbuchungskonto kann angegeben werden
    MUST = '2'  #: SMS-Abbuchungskonto muss angegeben werden


class PrincipalAccountRequired(RepresentableEnum):
    MUST_NOT = '0'  #: Auftraggeberkonto darf nicht angegeben werden
    MUST = '2'  #: Auftraggeberkonto muss angegeben werden, wenn im Geschäftsvorfall enthalten


class TaskHashAlgorithm(RepresentableEnum):
    NONE = '0'  #: Auftrags-Hashwert nicht unterstützt
    RIPEMD_160 = '1'  #: RIPEMD-160
    SHA_1 = '2'  #: SHA-1


class TwoStepParametersCommon(DataElementGroup):
    @property
    def VERSION(self):
        """TAN mechanism version"""
        return int(re.match(r'^(\D+)(\d+)$', self.__class__.__name__).group(2))

    security_function = DataElementField(type='code', max_length=3, _d="Sicherheitsfunktion kodiert")
    tan_process = DataElementField(type='code', length=1, _d="TAN-Prozess")
    tech_id = DataElementField(type='id', _d="Technische Identifikation TAN-Verfahren")


class TwoStepParameters1(TwoStepParametersCommon):
    name = DataElementField(type='an', max_length=30, _d="Name des Zwei-Schritt-Verfahrens")
    max_length_input = DataElementField(type='num', max_length=2, _d="Maximale Länge des Eingabewertes im Zwei-Schritt-Verfahren")
    allowed_format = CodeField(enum=AllowedFormat, length=1, _d="Erlaubtes Format im Zwei-Schritt-Verfahren")
    text_return_value = DataElementField(type='an', max_length=30, _d="Text zur Belegung des Rückgabewertes im Zwei-Schritt-Verfahren")
    max_length_return_value = DataElementField(type='num', max_length=3, _d="Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren")
    number_of_supported_lists = DataElementField(type='num', length=1, _d="Anzahl unterstützter aktiver TAN-Listen")
    multiple_tans_allowed = DataElementField(type='jn', _d="Mehrfach-TAN erlaubt")
    tan_time_delayed_allowed = DataElementField(type='jn', _d="TAN zeitversetzt/dialogübergreifend erlaubt")


class TwoStepParameters2(TwoStepParametersCommon):
    name = DataElementField(type='an', max_length=30, _d="Name des Zwei-Schritt-Verfahrens")
    max_length_input = DataElementField(type='num', max_length=2, _d="Maximale Länge des Eingabewertes im Zwei-Schritt-Verfahren")
    allowed_format = CodeField(enum=AllowedFormat, length=1, _d="Erlaubtes Format im Zwei-Schritt-Verfahren")
    text_return_value = DataElementField(type='an', max_length=30, _d="Text zur Belegung des Rückgabewertes im Zwei-Schritt-Verfahren")
    max_length_return_value = DataElementField(type='num', max_length=3, _d="Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren")
    number_of_supported_lists = DataElementField(type='num', length=1, _d="Anzahl unterstützter aktiver TAN-Listen")
    multiple_tans_allowed = DataElementField(type='jn', _d="Mehrfach-TAN erlaubt")
    tan_time_dialog_association = CodeField(enum=TANTimeDialogAssociation, length=1, _d="TAN Zeit- und Dialogbezug")
    tan_list_number_required = CodeField(enum=TANListNumberRequired, length=1, _d="TAN-Listennummer erforderlich")
    cancel_allowed = DataElementField(type='jn', _d="Auftragsstorno erlaubt")
    challenge_class_required = DataElementField(type='jn', _d="Challenge-Klasse erforderlich")
    challenge_value_required = DataElementField(type='jn', _d="Challenge-Betrag erforderlich")


class TwoStepParameters3(TwoStepParametersCommon):
    name = DataElementField(type='an', max_length=30, _d="Name des Zwei-Schritt-Verfahrens")
    max_length_input = DataElementField(type='num', max_length=2, _d="Maximale Länge des Eingabewertes im Zwei-Schritt-Verfahren")
    allowed_format = CodeField(enum=AllowedFormat, length=1, _d="Erlaubtes Format im Zwei-Schritt-Verfahren")
    text_return_value = DataElementField(type='an', max_length=30, _d="Text zur Belegung des Rückgabewertes im Zwei-Schritt-Verfahren")
    max_length_return_value = DataElementField(type='num', max_length=3, _d="Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren")
    number_of_supported_lists = DataElementField(type='num', length=1, _d="Anzahl unterstützter aktiver TAN-Listen")
    multiple_tans_allowed = DataElementField(type='jn', _d="Mehrfach-TAN erlaubt")
    tan_time_dialog_association = CodeField(enum=TANTimeDialogAssociation, length=1, _d="TAN Zeit- und Dialogbezug")
    tan_list_number_required = CodeField(enum=TANListNumberRequired, length=1, _d="TAN-Listennummer erforderlich")
    cancel_allowed = DataElementField(type='jn', _d="Auftragsstorno erlaubt")
    challenge_class_required = DataElementField(type='jn', _d="Challenge-Klasse erforderlich")
    challenge_value_required = DataElementField(type='jn', _d="Challenge-Betrag erforderlich")
    initialization_mode = CodeField(enum=InitializationMode, _d="Initialisierungsmodus")
    description_required = CodeField(enum=DescriptionRequired, length=1, _d="Bezeichnung des TAN-Medium erforderlich")
    supported_media_number = DataElementField(type='num', length=1, required=False, _d="Anzahl unterstützter aktiver TAN-Medien")


class TwoStepParameters4(TwoStepParametersCommon):
    zka_id = DataElementField(type='an', max_length=32, _d="ZKA TAN-Verfahren")
    zka_version = DataElementField(type='an', max_length=10, _d="Version ZKA TAN-Verfahren")
    name = DataElementField(type='an', max_length=30, _d="Name des Zwei-Schritt-Verfahrens")
    max_length_input = DataElementField(type='num', max_length=2, _d="Maximale Länge des Eingabewertes im Zwei-Schritt-Verfahren")
    allowed_format = CodeField(enum=AllowedFormat, length=1, _d="Erlaubtes Format im Zwei-Schritt-Verfahren")
    text_return_value = DataElementField(type='an', max_length=30, _d="Text zur Belegung des Rückgabewertes im Zwei-Schritt-Verfahren")
    max_length_return_value = DataElementField(type='num', max_length=3, _d="Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren")
    number_of_supported_lists = DataElementField(type='num', length=1, _d="Anzahl unterstützter aktiver TAN-Listen")
    multiple_tans_allowed = DataElementField(type='jn', _d="Mehrfach-TAN erlaubt")
    tan_time_dialog_association = CodeField(enum=TANTimeDialogAssociation, length=1, _d="TAN Zeit- und Dialogbezug")
    tan_list_number_required = CodeField(enum=TANListNumberRequired, length=1, _d="TAN-Listennummer erforderlich")
    cancel_allowed = DataElementField(type='jn', _d="Auftragsstorno erlaubt")
    sms_charge_account_required = DataElementField(type='jn', _d="SMS-Abbuchungskonto erforderlich")
    challenge_class_required = DataElementField(type='jn', _d="Challenge-Klasse erforderlich")
    challenge_value_required = DataElementField(type='jn', _d="Challenge-Betrag erforderlich")
    challenge_structured = DataElementField(type='jn', _d="Challenge strukturiert")
    initialization_mode = CodeField(enum=InitializationMode, _d="Initialisierungsmodus")
    description_required = CodeField(enum=DescriptionRequired, length=1, _d="Bezeichnung des TAN-Medium erforderlich")
    supported_media_number = DataElementField(type='num', length=1, required=False, _d="Anzahl unterstützter aktiver TAN-Medien")


class TwoStepParameters5(TwoStepParametersCommon):
    zka_id = DataElementField(type='an', max_length=32, _d="ZKA TAN-Verfahren")
    zka_version = DataElementField(type='an', max_length=10, _d="Version ZKA TAN-Verfahren")
    name = DataElementField(type='an', max_length=30, _d="Name des Zwei-Schritt-Verfahrens")
    max_length_input = DataElementField(type='num', max_length=2, _d="Maximale Länge des Eingabewertes im Zwei-Schritt-Verfahren")
    allowed_format = CodeField(enum=AllowedFormat, length=1, _d="Erlaubtes Format im Zwei-Schritt-Verfahren")
    text_return_value = DataElementField(type='an', max_length=30, _d="Text zur Belegung des Rückgabewertes im Zwei-Schritt-Verfahren")
    max_length_return_value = DataElementField(type='num', max_length=4, _d="Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren")
    number_of_supported_lists = DataElementField(type='num', length=1, _d="Anzahl unterstützter aktiver TAN-Listen")
    multiple_tans_allowed = DataElementField(type='jn', _d="Mehrfach-TAN erlaubt")
    tan_time_dialog_association = CodeField(enum=TANTimeDialogAssociation, length=1, _d="TAN Zeit- und Dialogbezug")
    tan_list_number_required = CodeField(enum=TANListNumberRequired, length=1, _d="TAN-Listennummer erforderlich")
    cancel_allowed = DataElementField(type='jn', _d="Auftragsstorno erlaubt")
    sms_charge_account_required = CodeField(enum=SMSChargeAccountRequired, length=1, _d="SMS-Abbuchungskonto erforderlich")
    principal_account_required = CodeField(enum=PrincipalAccountRequired, length=1, _d="Auftraggeberkonto erforderlich")
    challenge_class_required = DataElementField(type='jn', _d="Challenge-Klasse erforderlich")
    challenge_structured = DataElementField(type='jn', _d="Challenge strukturiert")
    initialization_mode = CodeField(enum=InitializationMode, _d="Initialisierungsmodus")
    description_required = CodeField(enum=DescriptionRequired, length=1, _d="Bezeichnung des TAN-Medium erforderlich")
    supported_media_number = DataElementField(type='num', length=1, required=False, _d="Anzahl unterstützter aktiver TAN-Medien")


class TwoStepParameters6(TwoStepParametersCommon):
    zka_id = DataElementField(type='an', max_length=32, _d="ZKA TAN-Verfahren")
    zka_version = DataElementField(type='an', max_length=10, _d="Version ZKA TAN-Verfahren")
    name = DataElementField(type='an', max_length=30, _d="Name des Zwei-Schritt-Verfahrens")
    max_length_input = DataElementField(type='num', max_length=2, _d="Maximale Länge des Eingabewertes im Zwei-Schritt-Verfahren")
    allowed_format = CodeField(enum=AllowedFormat, length=1, _d="Erlaubtes Format im Zwei-Schritt-Verfahren")
    text_return_value = DataElementField(type='an', max_length=30, _d="Text zur Belegung des Rückgabewertes im Zwei-Schritt-Verfahren")
    max_length_return_value = DataElementField(type='num', max_length=4, _d="Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren")
    multiple_tans_allowed = DataElementField(type='jn', _d="Mehrfach-TAN erlaubt")
    tan_time_dialog_association = CodeField(enum=TANTimeDialogAssociation, length=1, _d="TAN Zeit- und Dialogbezug")
    cancel_allowed = DataElementField(type='jn', _d="Auftragsstorno erlaubt")
    sms_charge_account_required = CodeField(enum=SMSChargeAccountRequired, length=1, _d="SMS-Abbuchungskonto erforderlich")
    principal_account_required = CodeField(enum=PrincipalAccountRequired, length=1, _d="Auftraggeberkonto erforderlich")
    challenge_class_required = DataElementField(type='jn', _d="Challenge-Klasse erforderlich")
    challenge_structured = DataElementField(type='jn', _d="Challenge strukturiert")
    initialization_mode = CodeField(enum=InitializationMode, _d="Initialisierungsmodus")
    description_required = CodeField(enum=DescriptionRequired, length=1, _d="Bezeichnung des TAN-Medium erforderlich")
    response_hhd_uc_required = DataElementField(type='jn', _d="Antwort HHD_UC erforderlich")
    supported_media_number = DataElementField(type='num', length=1, required=False, _d="Anzahl unterstützter aktiver TAN-Medien")


class ParameterTwostepCommon(DataElementGroup):
    onestep_method_allowed = DataElementField(type='jn')
    multiple_tasks_allowed = DataElementField(type='jn')
    task_hash_algorithm = CodeField(enum=TaskHashAlgorithm, length=1, _d="Auftrags-Hashwertverfahren")


class ParameterTwostepTAN1(ParameterTwostepCommon):
    security_profile_bank_signature = DataElementField(type='code', length=1)
    twostep_parameters = DataElementGroupField(type=TwoStepParameters1, min_count=1, max_count=98)


class ParameterTwostepTAN2(ParameterTwostepCommon):
    twostep_parameters = DataElementGroupField(type=TwoStepParameters2, min_count=1, max_count=98)


class ParameterTwostepTAN3(ParameterTwostepCommon):
    twostep_parameters = DataElementGroupField(type=TwoStepParameters3, min_count=1, max_count=98)


class ParameterTwostepTAN4(ParameterTwostepCommon):
    twostep_parameters = DataElementGroupField(type=TwoStepParameters4, min_count=1, max_count=98)


class ParameterTwostepTAN5(ParameterTwostepCommon):
    twostep_parameters = DataElementGroupField(type=TwoStepParameters5, min_count=1, max_count=98)


class ParameterTwostepTAN6(ParameterTwostepCommon):
    twostep_parameters = DataElementGroupField(type=TwoStepParameters6, min_count=1, max_count=98)


class TransactionTanRequired(DataElementGroup):
    transaction = DataElementField(type='an', max_length=6)
    tan_required = DataElementField(type='jn')


class ParameterPinTan(DataElementGroup):
    min_pin_length = DataElementField(type='num', max_length=2, required=False)
    max_pin_length = DataElementField(type='num', max_length=2, required=False)
    max_tan_length = DataElementField(type='num', max_length=2, required=False)
    user_id_field_text = DataElementField(type='an', max_length=30, required=False)
    customer_id_field_text = DataElementField(type='an', max_length=30, required=False)
    transaction_tans_required = DataElementGroupField(type=TransactionTanRequired, max_count=999, required=False)


class Language2(RepresentableEnum):
    """Dialogsprache

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    DEFAULT = '0'  #: Standard
    DE = '1'  #: Deutsch, 'de', Subset Deutsch, Codeset 1 (Latin 1)
    EN = '2'  #: Englisch, 'en', Subset Englisch, Codeset 1 (Latin 1)
    FR = '3'  #: Französisch, 'fr', Subset Französisch, Codeset 1 (Latin 1)


class SupportedLanguages2(DataElementGroup):
    languages = CodeField(enum=Language2, max_length=3, min_count=1, max_count=9)


class SupportedHBCIVersions2(DataElementGroup):
    versions = DataElementField(type='code', max_length=3, min_count=1, max_count=9)


class KTZ1(DataElementGroup):
    """Kontoverbindung ZV international, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    is_sepa = DataElementField(type='jn', _d="Kontoverwendung SEPA")
    iban = DataElementField(type='an', max_length=34, _d="IBAN")
    bic = DataElementField(type='an', max_length=11, _d="BIC")
    account_number = DataElementField(type='id', _d="Konto-/Depotnummer")
    subaccount_number = DataElementField(type='id', _d="Unterkontomerkmal")
    bank_identifier = DataElementGroupField(type=BankIdentifier, _d="Kreditinstitutskennung")

    def as_sepa_account(self):
        from fints.models import SEPAAccount
        if not self.is_sepa:
            return None
        return SEPAAccount(self.iban, self.bic, self.account_number, self.subaccount_number, self.bank_identifier.bank_code)

    @classmethod
    def from_sepa_account(cls, acc):
        return cls(
            is_sepa=True,
            iban=acc.iban,
            bic=acc.bic,
            account_number=acc.accountnumber,
            subaccount_number=acc.subaccount,
            bank_identifier=BankIdentifier(
                country_identifier=BankIdentifier.COUNTRY_ALPHA_TO_NUMERIC[acc.bic[4:6]],
                bank_code=acc.blz
            )
        )


class KTI1(DataElementGroup):
    """Kontoverbindung international, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    iban = DataElementField(type='an', max_length=34, required=False, _d="IBAN")
    bic = DataElementField(type='an', max_length=11, required=False, _d="BIC")
    account_number = DataElementField(type='id', required=False, _d="Konto-/Depotnummer")
    subaccount_number = DataElementField(type='id', required=False, _d="Unterkontomerkmal")
    bank_identifier = DataElementGroupField(type=BankIdentifier, required=False, _d="Kreditinstitutskennung")

    @classmethod
    def from_sepa_account(cls, acc):
        return cls(
            iban=acc.iban,
            bic=acc.bic,
        )


class Account2(DataElementGroup):
    """Kontoverbindung, version 2

    Source: HBCI Homebanking-Computer-Interface, Schnittstellenspezifikation"""
    account_number = DataElementField(type='id', _d="Konto-/Depotnummer")
    subaccount_number = DataElementField(type='id', _d="Unterkontomerkmal")
    country_identifier = DataElementField(type='ctr', _d="Länderkennzeichen")
    bank_code = DataElementField(type='an', max_length=30, _d="Kreditinstitutscode")

    @classmethod
    def from_sepa_account(cls, acc):
        return cls(
            account_number=acc.accountnumber,
            subaccount_number=acc.subaccount,
            country_identifier=BankIdentifier.COUNTRY_ALPHA_TO_NUMERIC[acc.bic[4:6]],
            bank_code=acc.blz,
        )


class Account3(DataElementGroup):
    """Kontoverbindung, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account_number = DataElementField(type='id', _d="Konto-/Depotnummer")
    subaccount_number = DataElementField(type='id', _d="Unterkontomerkmal")
    bank_identifier = DataElementGroupField(type=BankIdentifier, _d="Kreditinstitutskennung")

    @classmethod
    def from_sepa_account(cls, acc):
        return cls(
            account_number=acc.accountnumber,
            subaccount_number=acc.subaccount,
            bank_identifier=BankIdentifier(
                country_identifier=BankIdentifier.COUNTRY_ALPHA_TO_NUMERIC[acc.bic[4:6]],
                bank_code=acc.blz
            )
        )


class SecurityRole(RepresentableEnum):
    """Rolle des Sicherheitslieferanten, kodiert, version 2

    Kodierte Information über das Verhältnis desjenigen, der bezüglich der zu si-chernden Nachricht die Sicherheit gewährleistet.
    Die Wahl ist von der bankfachlichen Auslegung der Signatur, respektive vom vertraglichen Zustand zwischen Kunde und Kreditinstitut abhängig.

    Source: FinTS Financial Transaction Services, Sicherheitsverfahren HBCI"""
    ISS = '1'  #: Erfasser, Erstsignatur
    CON = '3'  #: Unterstützer, Zweitsignatur
    WIT = '4'  #: Zeuge/Übermittler, nicht Erfasser


class CompressionFunction(RepresentableEnum):
    """Komprimierungsfunktion, version 2

    Source: FinTS Financial Transaction Services, Sicherheitsverfahren HBCI"""
    NULL = '0'  #: Keine Kompression
    LZW = '1'  #: Lempel, Ziv, Welch
    COM = '2'  #: Optimized LZW
    LZSS = '3'  #: Lempel, Ziv
    LZHuf = '4'  #: LZ + Huffman Coding
    ZIP = '5'  #: PKZIP
    GZIP = '6'  #: deflate (http://www.gzip.org/zlib)
    BZIP2 = '7'  #: bzip2 (http://sourceware.cygnus.com/bzip2/)
    ZZZ = '999'  #: Gegenseitig vereinbart


class SecurityApplicationArea(RepresentableEnum):
    """Bereich der Sicherheitsapplikation, kodiert, version 2

    Informationen darüber, welche Daten vom kryptographischen Prozess verarbeitet werden.

    Source: FinTS Financial Transaction Services, Sicherheitsverfahren HBCI"""
    SHM = '1'  #: Signaturkopf und HBCI-Nutzdaten
    SHT = '2'  #: Von Signaturkopf bis Signaturabschluss


class SecurityClass(RepresentableEnum):
    """Sicherheitsklasse, version 1

    Die Sicherheitsklasse gibt für jede Signatur den erforderlichen Sicherheitsdienst an.

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    NONE = 0  #: Kein Sicherheitsdienst erforderlich
    AUTH = 1  #: Sicherheitsdienst 'Authentikation'
    AUTH_ADV = 2  #: Sicherheitsdienst 'Authentikation' mit fortgeschrittener elektronischer Signatur, optionaler Zertifikatsprüfung
    NON_REPUD = 3  #: Sicherheitsdienst 'Non-Repudiation' mit fortgeschrittener elektronischer Signatur, optionaler Zertifikatsprüfung
    NON_REPUD_QUAL = 4  #: Sicherheitsdienst 'Non-Repudiation' mit fortgeschrittener bzw. qualifizierter elektronischer Signatur, zwingende Zertifikatsprüfung


class UPDUsage(RepresentableEnum):
    """UPD-Verwendung, version 2

    Kennzeichen dafür, wie diejenigen Geschäftsvorfälle zu interpretieren sind, die bei der Beschreibung der Kontoinformationen nicht unter den erlaubten Geschäftsvorfällen aufgeführt sind.

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    UPD_CONCLUSIVE = '0'  #: Die nicht aufgeführten Geschäftsvorfälle sind gesperrt
    UPD_INCONCLUSIVE = '1'  #: Bei nicht aufgeführten Geschäftsvorfällen ist keine Aussage möglich, ob diese erlaubt oder gesperrt sind


class SystemIDStatus(RepresentableEnum):
    """Kundensystem-Status, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    ID_UNNECESSARY = '0'  #: Kundensystem-ID wird nicht benötigt
    ID_NECESSARY = '1'  #: Kundensystem-ID wird benötigt


class SynchronizationMode(RepresentableEnum):
    """Synchronisierungsmodus, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    NEW_SYSTEM_ID = '0'  #: Neue Kundensystem-ID zurückmelden
    LAST_MESSAGE = '1'  #: Letzte verarbeitete Nachrichtennummer zurückmelden
    SIGNATURE_ID = '2'  #: Signatur-ID zurückmelden


class CreditDebit2(RepresentableEnum):
    """Soll-Haben-Kennzeichen, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    CREDIT = 'C'  #: Haben
    DEBIT = 'D'  #: Soll


class Balance1(DataElementGroup):
    """Saldo, version 1

    Source: HBCI Homebanking-Computer-Interface, Schnittstellenspezifikation"""
    credit_debit = CodeField(enum=CreditDebit2, length=1, _d="Soll-Haben-Kennzeichen")
    amount = DataElementField(type='wrt', _d="Wert")
    currency = DataElementField(type='cur', _d="Währung")
    date = DataElementField(type='dat', _d="Datum")
    time = DataElementField(type='tim', required=False, _d="Uhrzeit")

    def as_mt940_Balance(self):
        from mt940.models import Balance
        return Balance(
            self.credit_debit.value,
            "{:.12f}".format(self.amount).rstrip('0'),
            self.date,
            currency=self.currency
        )


class Balance2(DataElementGroup):
    """Saldo, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    credit_debit = CodeField(enum=CreditDebit2, length=1, _d="Soll-Haben-Kennzeichen")
    amount = DataElementGroupField(type=Amount1, _d="Betrag")
    date = DataElementField(type='dat', _d="Datum")
    time = DataElementField(type='tim', required=False, _d="Uhrzeit")

    def as_mt940_Balance(self):
        from mt940.models import Balance
        return Balance(
            self.credit_debit.value,
            "{:.12f}".format(self.amount.amount).rstrip('0'),
            self.date,
            currency=self.amount.currency
        )


class Timestamp1(DataElementGroup):
    """Zeitstempel

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    date = DataElementField(type='dat', _d="Datum")
    time = DataElementField(type='tim', required=False, _d="Uhrzeit")


class TANMediaType2(RepresentableEnum):
    """TAN-Medium-Art

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""

    ALL = '0'  #: Alle
    ACTIVE = '1'  #: Aktiv
    AVAILABLE = '2'  #: Verfügbar


class TANMediaClass3(RepresentableEnum):
    """TAN-Medium-Klasse, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""

    ALL = 'A'  #: Alle Medien
    LIST = 'L'  #: Liste
    GENERATOR = 'G'  #: TAN-Generator
    MOBILE = 'M'  #: Mobiltelefon mit mobileTAN
    SECODER = 'S'  #: Secoder


class TANMediaClass4(RepresentableEnum):
    """TAN-Medium-Klasse, version 4

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""

    ALL = 'A'  #: Alle Medien
    LIST = 'L'  #: Liste
    GENERATOR = 'G'  #: TAN-Generator
    MOBILE = 'M'  #: Mobiltelefon mit mobileTAN
    SECODER = 'S'  #: Secoder
    BILATERAL = 'B'  #: Bilateral vereinbart


class TANMediumStatus(RepresentableEnum):
    """Status

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""

    ACTIVE = '1'  #: Aktiv
    AVAILABLE = '2'  #: Verfügbar
    ACTIVE_SUCCESSOR = '3'  #: Aktiv Folgekarte
    AVAILABLE_SUCCESSOR = '4'  #: Verfügbar Folgekarte


class TANMedia4(DataElementGroup):
    """TAN-Medium-Liste, version 4

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""

    tan_medium_class = CodeField(enum=TANMediaClass3, _d="TAN-Medium-Klasse")
    status = CodeField(enum=TANMediumStatus, _d="Status")
    card_number = DataElementField(type='id', required=False, _d="Kartennummer")
    card_sequence = DataElementField(type='id', required=False, _d="Kartenfolgenummer")
    card_type = DataElementField(type='num', required=False, _d="Kartenart")
    account = DataElementGroupField(type=Account3, required=False, _d="Kontonummer Auftraggeber")
    valid_from = DataElementField(type='dat', required=False, _d="Gültig ab")
    valid_until = DataElementField(type='dat', required=False, _d="Gültig bis")
    tan_list_number = DataElementField(type='an', max_length=20, required=False, _d="TAN-Listennummer")
    tan_medium_name = DataElementField(type='an', max_length=32, required=False, _d="Bezeichnung des TAN-Mediums")
    mobile_number_masked = DataElementField(type='an', max_length=35, required=False, _d="Mobiltelefonnummer, verschleiert")
    mobile_number = DataElementField(type='an', max_length=35, required=False, _d="Mobiltelefonnummer")
    sms_charge_account = DataElementGroupField(type=KTI1, required=False, _d="SMS-Abbuchungskonto")
    number_free_tans = DataElementField(type='num', max_length=3, required=False, _d="Anzahl freie TANs")
    last_use = DataElementField(type='dat', required=False, _d="Letzte Benutzung")
    active_since = DataElementField(type='dat', required=False, _d="Freigeschaltet am")


class TANMedia5(DataElementGroup):
    """TAN-Medium-Liste, version 5

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""

    tan_medium_class = CodeField(enum=TANMediaClass4, _d="TAN-Medium-Klasse")
    status = CodeField(enum=TANMediumStatus, _d="Status")
    security_function = DataElementField(type='num', required=False, _d="Sicherheitsfunktion, kodiert")
    card_number = DataElementField(type='id', required=False, _d="Kartennummer")
    card_sequence = DataElementField(type='id', required=False, _d="Kartenfolgenummer")
    card_type = DataElementField(type='num', required=False, _d="Kartenart")
    account = DataElementGroupField(type=Account3, required=False, _d="Kontonummer Auftraggeber")
    valid_from = DataElementField(type='dat', required=False, _d="Gültig ab")
    valid_until = DataElementField(type='dat', required=False, _d="Gültig bis")
    tan_list_number = DataElementField(type='an', max_length=20, required=False, _d="TAN-Listennummer")
    tan_medium_name = DataElementField(type='an', max_length=32, required=False, _d="Bezeichnung des TAN-Mediums")
    mobile_number_masked = DataElementField(type='an', max_length=35, required=False, _d="Mobiltelefonnummer, verschleiert")
    mobile_number = DataElementField(type='an', max_length=35, required=False, _d="Mobiltelefonnummer")
    sms_charge_account = DataElementGroupField(type=KTI1, required=False, _d="SMS-Abbuchungskonto")
    number_free_tans = DataElementField(type='num', max_length=3, required=False, _d="Anzahl freie TANs")
    last_use = DataElementField(type='dat', required=False, _d="Letzte Benutzung")
    active_since = DataElementField(type='dat', required=False, _d="Freigeschaltet am")


class TANUsageOption(RepresentableEnum):
    """TAN-Einsatzoption

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""

    ALL_ACTIVE = '0'  #: Kunde kann alle "aktiven" Medien parallel nutzen
    EXACTLY_ONE = '1'  #: Kunde kann genau ein Medium zu einer Zeit nutzen
    MOBILE_AND_GENERATOR = '2'  #: Kunde kann ein Mobiltelefon und einen TAN-Generator parallel nutzen


class ParameterChallengeClass(DataElementGroup):
    """Parameter Challenge-Klasse

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""
    parameters = DataElementField(type='an', max_length=999, count=9, required=False)


class ResponseHHDUC(DataElementGroup):
    """Antwort HHD_UC

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""
    atc = DataElementField(type='an', max_length=5, _d="ATC")
    ac = DataElementField(type='bin', max_length=256, _d="Application Cryptogram AC")
    ef_id_data = DataElementField(type='bin', max_length=256, _d="EF_ID Data")
    cvr = DataElementField(type='bin', max_length=256, _d="CVR")
    version_info_chiptan = DataElementField(type='bin', max_length=256, _d="Versionsinfo der chipTAN-Applikation")


class ChallengeValidUntil(DataElementGroup):
    """Gültigkeitsdatum und -uhrzeit für Challenge

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""
    date = DataElementField(type='dat', _d="Datum")
    time = DataElementField(type='tim', _d="Uhrzeit")


class BatchTransferParameter1(DataElementGroup):
    """Parameter SEPA-Sammelüberweisung, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    max_transfer_count = DataElementField(type='num', max_length=7, _d="Maximale Anzahl CreditTransferTransactionInformation")
    sum_amount_required = DataElementField(type='jn', _d="Summenfeld benötigt")
    single_booking_allowed = DataElementField(type='jn', _d="Einzelbuchung erlaubt")


class ServiceType2(RepresentableEnum):
    T_ONLINE = 1  #: T-Online
    TCP_IP = 2  #: TCP/IP (Protokollstack SLIP/PPP)
    HTTPS = 3  #: https


class CommunicationParameter2(DataElementGroup):
    """Kommunikationsparameter, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    service_type = IntCodeField(enum=ServiceType2, max_length=2, _d="Kommunikationsdienst")
    address = DataElementField(type='an', max_length=512, _d="Kommunikationsadresse")
    address_adjunct = DataElementField(type='an', max_length=512, required=False, _d="Kommunikationsadresszusatz")
    filter_function = DataElementField(type='an', length=3, required=False, _d="Filterfunktion")
    filter_function_version = DataElementField(type='num', max_length=3, required=False, _d="Version der Filterfunktion")


class ScheduledDebitParameter1(DataElementGroup):
    """Parameter terminierte SEPA-Einzellastschrift einreichen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    min_advance_notice_FNAL_RCUR = DataElementField(type='num', max_length=4, _d="Minimale Vorlaufzeit FNAL/RCUR")
    max_advance_notice_FNAL_RCUR = DataElementField(type='num', max_length=4, _d="Maximale Vorlaufzeit FNAL/RCUR")
    min_advance_notice_FRST_OOFF = DataElementField(type='num', max_length=4, _d="Minimale Vorlaufzeit FRST/OOFF")
    max_advance_notice_FRST_OOFF = DataElementField(type='num', max_length=4, _d="Maximale Vorlaufzeit FRST/OOFF")


class ScheduledDebitParameter2(DataElementGroup):
    """Parameter terminierte SEPA-Einzellastschrift einreichen, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    min_advance_notice = DataElementField(type='an', max_length=99, _d="Minimale Vorlaufzeit SEPA-Lastschrift")
    max_advance_notice = DataElementField(type='an', max_length=99, _d="Maximale Vorlaufzeit SEPA-Lastschrift")
    allowed_purpose_codes = DataElementField(type='an', max_length=4096, required=False, _d="Zulässige purpose codes")
    supported_sepa_formats = DataElementField(type='an', max_length=256, max_count=9, required=False, _d="Unterstützte SEPA-Datenformate")


class ScheduledBatchDebitParameter1(DataElementGroup):
    """Parameter terminierte SEPA-Sammellastschrift einreichen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    min_advance_notice_FNAL_RCUR = DataElementField(type='num', max_length=4, _d="Minimale Vorlaufzeit FNAL/RCUR")
    max_advance_notice_FNAL_RCUR = DataElementField(type='num', max_length=4, _d="Maximale Vorlaufzeit FNAL/RCUR")
    min_advance_notice_FRST_OOFF = DataElementField(type='num', max_length=4, _d="Minimale Vorlaufzeit FRST/OOFF")
    max_advance_notice_FRST_OOFF = DataElementField(type='num', max_length=4, _d="Maximale Vorlaufzeit FRST/OOFF")
    max_debit_count = DataElementField(type='num', max_length=7, _d="Maximale Anzahl DirectDebitTransfer TransactionInformation")
    sum_amount_required = DataElementField(type='jn', _d="Summenfeld benötigt")
    single_booking_allowed = DataElementField(type='jn', _d="Einzelbuchung erlaubt")


class ScheduledBatchDebitParameter2(DataElementGroup):
    """Parameter terminierte SEPA-Sammellastschrift einreichen, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    min_advance_notice = DataElementField(type='an', max_length=99, _d="Minimale Vorlaufzeit SEPA-Lastschrift")
    max_advance_notice = DataElementField(type='an', max_length=99, _d="Maximale Vorlaufzeit SEPA-Lastschrift")
    max_debit_count = DataElementField(type='num', max_length=7, _d="Maximale Anzahl DirectDebitTransfer TransactionInformation")
    sum_amount_required = DataElementField(type='jn', _d="Summenfeld benötigt")
    single_booking_allowed = DataElementField(type='jn', _d="Einzelbuchung erlaubt")
    allowed_purpose_codes = DataElementField(type='an', max_length=4096, required=False, _d="Zulässige purpose codes")
    supported_sepa_formats = DataElementField(type='an', max_length=256, max_count=9, required=False, _d="Unterstützte SEPA-Datenformate")


class ScheduledCOR1DebitParameter1(DataElementGroup):
    """Parameter terminierte SEPA-COR1-Einzellastschrift, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    min_advance_notice_FNAL_RCUR = DataElementField(type='num', max_length=4, _d="Minimale Vorlaufzeit FNAL/RCUR")
    max_advance_notice_FNAL_RCUR = DataElementField(type='num', max_length=4, _d="Maximale Vorlaufzeit FNAL/RCUR")
    min_advance_notice_FRST_OOFF = DataElementField(type='num', max_length=4, _d="Minimale Vorlaufzeit FRST/OOFF")
    max_advance_notice_FRST_OOFF = DataElementField(type='num', max_length=4, _d="Maximale Vorlaufzeit FRST/OOFF")
    allowed_purpose_codes = DataElementField(type='an', max_length=4096, required=False, _d="Zulässige purpose codes")
    supported_sepa_formats = DataElementField(type='an', max_length=256, max_count=9, required=False, _d="Unterstützte SEPA-Datenformate")


class ScheduledCOR1BatchDebitParameter1(DataElementGroup):
    """Parameter terminierte SEPA-COR1-Sammellastschrift, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    max_debit_count = DataElementField(type='num', max_length=7, _d="Maximale Anzahl DirectDebitTransfer TransactionInformation")
    sum_amount_required = DataElementField(type='jn', _d="Summenfeld benötigt")
    single_booking_allowed = DataElementField(type='jn', _d="Einzelbuchung erlaubt")
    min_advance_notice_FNAL_RCUR = DataElementField(type='num', max_length=4, _d="Minimale Vorlaufzeit FNAL/RCUR")
    max_advance_notice_FNAL_RCUR = DataElementField(type='num', max_length=4, _d="Maximale Vorlaufzeit FNAL/RCUR")
    min_advance_notice_FRST_OOFF = DataElementField(type='num', max_length=4, _d="Minimale Vorlaufzeit FRST/OOFF")
    max_advance_notice_FRST_OOFF = DataElementField(type='num', max_length=4, _d="Maximale Vorlaufzeit FRST/OOFF")
    allowed_purpose_codes = DataElementField(type='an', max_length=4096, required=False, _d="Zulässige purpose codes")
    supported_sepa_formats = DataElementField(type='an', max_length=256, max_count=9, required=False, _d="Unterstützte SEPA-Datenformate")


class SupportedSEPAPainMessages1(DataElementGroup):
    """Unterstützte SEPA pain messages, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    sepa_descriptors = DataElementField(type='an', max_length=256, max_count=99, _d="SEPA Descriptor")


class QueryScheduledDebitParameter1(DataElementGroup):
    """Parameter Bestand terminierter SEPA-Einzellastschriften, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    date_range_allowed = DataElementField(type='jn', _d="Zeitraum möglich")
    max_number_responses_allowed = DataElementField(type='jn', _d="Eingabe Anzahl Einträge erlaubt")


class QueryScheduledDebitParameter2(DataElementGroup):
    """Parameter Bestand terminierter SEPA-Einzellastschriften, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    max_number_responses_allowed = DataElementField(type='jn', _d="Eingabe Anzahl Einträge erlaubt")
    date_range_allowed = DataElementField(type='jn', _d="Zeitraum möglich")
    supported_sepa_formats = DataElementField(type='an', max_length=256, max_count=9, required=False, _d="Unterstützte SEPA-Datenformate")


class QueryScheduledBatchDebitParameter1(DataElementGroup):
    """Parameter Bestand terminierter SEPA-Sammellastschriften, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    max_number_responses_allowed = DataElementField(type='jn', _d="Eingabe Anzahl Einträge erlaubt")
    date_range_allowed = DataElementField(type='jn', _d="Zeitraum möglich")


class QueryCreditCardStatements2(DataElementGroup):
    """Parameter Kreditkartenumsätze anfordern, version 2

    Source: reverse engineered"""
    cutoff_days = DataElementField(type='num', max_length=4, _d="Maximale Vorhaltezeit der Umsätze")
    max_number_responses_allowed = DataElementField(type='jn', _d="Eingabe Anzahl Einträge erlaubt")
    date_range_allowed = DataElementField(type='jn', _d="Zeitraum möglich")


class SEPACCode1(RepresentableEnum):
    REVERSAL = '1'  #: Reversal
    REVOCATION = '2'  #: Revocation
    DELETION = '3'  #: Delete


class StatusSEPATask1(RepresentableEnum):
    PENDING = '1'  #: In Terminierung
    DECLINED = '2'  #: Abgelehnt von erster Inkassostelle
    IN_PROGRESS = '3'  #: in Bearbeitung
    PROCESSED = '4'  #: Creditoren-seitig verarbeitet, Buchung veranlasst
    REVOKED = '5'  #: R-Transaktion wurde veranlasst


class GetSEPAAccountParameter1(DataElementGroup):
    """Parameter SEPA-Kontoverbindung anfordern, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    single_account_query_allowed = DataElementField(type='jn', _d="Einzelkontenabruf erlaubt")
    national_account_allowed = DataElementField(type='jn', _d="Nationale Kontoverbindung erlaubt")
    structured_purpose_allowed = DataElementField(type='jn', _d="Strukturierter Verwendungszweck erlaubt")
    supported_sepa_formats = DataElementField(type='an', max_length=256, max_count=99, required=False, _d="Unterstützte SEPA-Datenformate")
