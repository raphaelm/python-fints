import re

from fints.types import * # The order is important!
from fints.fields import *


class ShortReprMixin:
    def __repr__(self):
        return "{}{}({})".format(
            "{}.".format(self.__class__.__module__),
            self.__class__.__name__,
            ", ".join(
                ("{!r}".format(value) if not name.startswith("_") else "{}={!r}".format(name, value))
                for (name, value) in self._repr_items
            )
        )

    def print_nested(self, stream=None, level=0, indent="    ", prefix="", first_level_indent=True, trailer=""):
        stream.write(
            ( (prefix + level*indent) if first_level_indent else "")
            + "{!r}{}\n".format(self, trailer)
        )

class DataElementGroup(Container):
    pass

class SegmentHeader(ShortReprMixin, DataElementGroup):
    "Segmentkopf"
    type = AlphanumericField(max_length=6, _d='Segmentkennung')
    number = NumericField(max_length=3, _d='Segmentnummer')
    version = NumericField(max_length=3, _d='Segmentversion')
    reference = NumericField(max_length=3, required=False, _d='Bezugssegment')

class ReferenceMessage(DataElementGroup):
    dialogue_id = DataElementField(type='id')
    message_number = NumericField(max_length=4)

class SecurityProfile(DataElementGroup):
    security_method = DataElementField(type='code', length=3)
    security_method_version = DataElementField(type='num')

class SecurityIdentificationDetails(DataElementGroup):
    name_party = DataElementField(type='code', max_length=3)
    cid = DataElementField(type='bin', max_length=256)
    identifier_party = DataElementField(type='id')

class SecurityDateTime(DataElementGroup):
    datetime_type = DataElementField(type='code', max_length=3)
    date = DataElementField(type='dat', required=False)
    time = DataElementField(type='tim', required=False)

class EncryptionAlgorithm(DataElementGroup):
    usage_encryption = DataElementField(type='code', max_length=3)
    operation_mode = DataElementField(type='code', max_length=3)
    encryption_algorithm = DataElementField(type='code', max_length=3)
    algorithm_parameter_value = DataElementField(type='bin', max_length=512)
    algorithm_parameter_name = DataElementField(type='code', max_length=3)
    algorithm_parameter_iv_name = DataElementField(type='code', max_length=3)
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
    country_identifier = DataElementField(type='ctr')
    bank_code = DataElementField(type='an', max_length=30)

class KeyName(DataElementGroup):
    bank_identifier = DataElementGroupField(type=BankIdentifier)
    user_id = DataElementField(type='id')
    key_type = DataElementField(type='code', length=1)
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

class AccountInformation(DataElementGroup):
    account_number = DataElementField(type='id')
    subaccount_number = DataElementField(type='id')
    bank_identifier = DataElementGroupField(type=BankIdentifier)

class AccountLimit(DataElementGroup):
    limit_type = DataElementField(type='code', length=1)
    limit_amount = DataElementField(type='btg', required=False)
    limit_days = DataElementField(type='num', max_length=3, required=False)

class AllowedTransaction(DataElementGroup):
    transaction = DataElementField(type='an', max_length=6)
    required_signatures = DataElementField(type='num', max_length=2)
    limit_type = DataElementField(type='code', length=1, required=False)
    limit_amount = DataElementField(type='btg', required=False)
    limit_days = DataElementField(type='num', max_length=3, required=False)

class TwoStepParametersCommon(DataElementGroup):
    @property
    def VERSION(self):
        return int( re.match(r'^(\D+)(\d+)$', self.__class__.__name__).group(2) )

    security_function = DataElementField(type='code', max_length=3, _d="Sicherheitsfunktion kodiert")
    tan_process = DataElementField(type='code', length=1, _d="TAN-Prozess")
    tech_id = DataElementField(type='id', _d="Technische Identifikation TAN-Verfahren")

class TwoStepParameters1(TwoStepParametersCommon):
    name = DataElementField(type='an', max_length=30, _d="Name des Zwei-Schritt-Verfahrens")
    max_length_input = DataElementField(type='num', max_length=2, _d="Maximale Länge des Eingabewertes im Zwei-Schritt-Verfahren")
    allowed_format = DataElementField(type='code', length=1, _d="Erlaubtes Format im Zwei-Schritt-Verfahren")
    text_return_value = DataElementField(type='an', max_length=30, _d="Text zur Belegung des Rückgabewertes im Zwei-Schritt-Verfahren")
    max_length_return_value = DataElementField(type='num', max_length=3, _d="Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren")
    number_of_supported_lists = DataElementField(type='num', length=1, _d="Anzahl unterstützter aktiver TAN-Listen")
    multiple_tans_allowed = DataElementField(type='jn', _d="Mehrfach-TAN erlaubt")
    tan_time_delayed_allowed = DataElementField(type='jn', _d="TAN zeitversetzt/dialogübergreifend erlaubt")

class TwoStepParameters2(TwoStepParametersCommon):
    name = DataElementField(type='an', max_length=30, _d="Name des Zwei-Schritt-Verfahrens")
    max_length_input = DataElementField(type='num', max_length=2, _d="Maximale Länge des Eingabewertes im Zwei-Schritt-Verfahren")
    allowed_format = DataElementField(type='code', length=1, _d="Erlaubtes Format im Zwei-Schritt-Verfahren")
    text_return_value = DataElementField(type='an', max_length=30, _d="Text zur Belegung des Rückgabewertes im Zwei-Schritt-Verfahren")
    max_length_return_value = DataElementField(type='num', max_length=3, _d="Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren")
    number_of_supported_lists = DataElementField(type='num', length=1, _d="Anzahl unterstützter aktiver TAN-Listen")
    multiple_tans_allowed = DataElementField(type='jn', _d="Mehrfach-TAN erlaubt")
    tan_time_dialog_association = DataElementField(type='code', length=1, _d="TAN Zeit- und Dialogbezug")
    tan_list_number_required = DataElementField(type='code', length=1, _d="TAN-Listennummer erforderlich")
    cancel_allowed = DataElementField(type='jn', _d="Auftragsstorno erlaubt")
    challenge_class_required = DataElementField(type='jn', _d="Challenge-Klasse erforderlich")
    challenge_value_required = DataElementField(type='jn', _d="Challenge-Betrag erforderlich")

class TwoStepParameters3(TwoStepParametersCommon):
    name = DataElementField(type='an', max_length=30, _d="Name des Zwei-Schritt-Verfahrens")
    max_length_input = DataElementField(type='num', max_length=2, _d="Maximale Länge des Eingabewertes im Zwei-Schritt-Verfahren")
    allowed_format = DataElementField(type='code', length=1, _d="Erlaubtes Format im Zwei-Schritt-Verfahren")
    text_return_value = DataElementField(type='an', max_length=30, _d="Text zur Belegung des Rückgabewertes im Zwei-Schritt-Verfahren")
    max_length_return_value = DataElementField(type='num', max_length=3, _d="Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren")
    number_of_supported_lists = DataElementField(type='num', length=1, _d="Anzahl unterstützter aktiver TAN-Listen")
    multiple_tans_allowed = DataElementField(type='jn', _d="Mehrfach-TAN erlaubt")
    tan_time_dialog_association = DataElementField(type='code', length=1, _d="TAN Zeit- und Dialogbezug")
    tan_list_number_required = DataElementField(type='code', length=1, _d="TAN-Listennummer erforderlich")
    cancel_allowed = DataElementField(type='jn', _d="Auftragsstorno erlaubt")
    challenge_class_required = DataElementField(type='jn', _d="Challenge-Klasse erforderlich")
    challenge_value_required = DataElementField(type='jn', _d="Challenge-Betrag erforderlich")
    initialisation_mode = DataElementField(type='code', _d="Initialisierungsmodus")
    description_required = DataElementField(type='code', length=1, _d="Bezeichnung des TAN-Medium erforderlich")
    supported_media_number = DataElementField(type='num', length=1, required=False, _d="Anzahl unterstützter aktiver TAN-Medien")

class TwoStepParameters4(TwoStepParametersCommon):
    zka_id = DataElementField(type='an', max_length=32, _d="ZKA TAN-Verfahren")
    zka_version = DataElementField(type='an', max_length=10, _d="Version ZKA TAN-Verfahren")
    name = DataElementField(type='an', max_length=30, _d="Name des Zwei-Schritt-Verfahrens")
    max_length_input = DataElementField(type='num', max_length=2, _d="Maximale Länge des Eingabewertes im Zwei-Schritt-Verfahren")
    allowed_format = DataElementField(type='code', length=1, _d="Erlaubtes Format im Zwei-Schritt-Verfahren")
    text_return_value = DataElementField(type='an', max_length=30, _d="Text zur Belegung des Rückgabewertes im Zwei-Schritt-Verfahren")
    max_length_return_value = DataElementField(type='num', max_length=3, _d="Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren")
    number_of_supported_lists = DataElementField(type='num', length=1, _d="Anzahl unterstützter aktiver TAN-Listen")
    multiple_tans_allowed = DataElementField(type='jn', _d="Mehrfach-TAN erlaubt")
    tan_time_dialog_association = DataElementField(type='code', length=1, _d="TAN Zeit- und Dialogbezug")
    tan_list_number_required = DataElementField(type='code', length=1, _d="TAN-Listennummer erforderlich")
    cancel_allowed = DataElementField(type='jn', _d="Auftragsstorno erlaubt")
    sms_charge_account_required = DataElementField(type='jn', _d="SMS-Abbuchungskonto erforderlich")
    challenge_class_required = DataElementField(type='jn', _d="Challenge-Klasse erforderlich")
    challenge_value_required = DataElementField(type='jn', _d="Challenge-Betrag erforderlich")
    challenge_structured = DataElementField(type='jn', _d="Challenge strukturiert")
    initialisation_mode = DataElementField(type='code', _d="Initialisierungsmodus")
    description_required = DataElementField(type='code', length=1, _d="Bezeichnung des TAN-Medium erforderlich")
    supported_media_number = DataElementField(type='num', length=1, required=False, _d="Anzahl unterstützter aktiver TAN-Medien")

class TwoStepParameters5(TwoStepParametersCommon):
    zka_id = DataElementField(type='an', max_length=32, _d="ZKA TAN-Verfahren")
    zka_version = DataElementField(type='an', max_length=10, _d="Version ZKA TAN-Verfahren")
    name = DataElementField(type='an', max_length=30, _d="Name des Zwei-Schritt-Verfahrens")
    max_length_input = DataElementField(type='num', max_length=2, _d="Maximale Länge des Eingabewertes im Zwei-Schritt-Verfahren")
    allowed_format = DataElementField(type='code', length=1, _d="Erlaubtes Format im Zwei-Schritt-Verfahren")
    text_return_value = DataElementField(type='an', max_length=30, _d="Text zur Belegung des Rückgabewertes im Zwei-Schritt-Verfahren")
    max_length_return_value = DataElementField(type='num', max_length=3, _d="Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren")
    number_of_supported_lists = DataElementField(type='num', length=1, _d="Anzahl unterstützter aktiver TAN-Listen")
    multiple_tans_allowed = DataElementField(type='jn', _d="Mehrfach-TAN erlaubt")
    tan_time_dialog_association = DataElementField(type='code', length=1, _d="TAN Zeit- und Dialogbezug")
    tan_list_number_required = DataElementField(type='code', length=1, _d="TAN-Listennummer erforderlich")
    cancel_allowed = DataElementField(type='jn', _d="Auftragsstorno erlaubt")
    sms_charge_account_required = DataElementField(type='code', length=1, _d="SMS-Abbuchungskonto erforderlich")
    principal_account_required = DataElementField(type='code', length=1, _d="Auftraggeberkonto erforderlich")
    challenge_class_required = DataElementField(type='jn', _d="Challenge-Klasse erforderlich")
    challenge_structured = DataElementField(type='jn', _d="Challenge strukturiert")
    initialisation_mode = DataElementField(type='code', _d="Initialisierungsmodus")
    description_required = DataElementField(type='code', length=1, _d="Bezeichnung des TAN-Medium erforderlich")
    supported_media_number = DataElementField(type='num', length=1, required=False, _d="Anzahl unterstützter aktiver TAN-Medien")

class TwoStepParameters6(TwoStepParametersCommon):
    zka_id = DataElementField(type='an', max_length=32, _d="ZKA TAN-Verfahren")
    zka_version = DataElementField(type='an', max_length=10, _d="Version ZKA TAN-Verfahren")
    name = DataElementField(type='an', max_length=30, _d="Name des Zwei-Schritt-Verfahrens")
    max_length_input = DataElementField(type='num', max_length=2, _d="Maximale Länge des Eingabewertes im Zwei-Schritt-Verfahren")
    allowed_format = DataElementField(type='code', length=1, _d="Erlaubtes Format im Zwei-Schritt-Verfahren")
    text_return_value = DataElementField(type='an', max_length=30, _d="Text zur Belegung des Rückgabewertes im Zwei-Schritt-Verfahren")
    max_length_return_value = DataElementField(type='num', max_length=3, _d="Maximale Länge des Rückgabewertes im Zwei-Schritt-Verfahren")
    multiple_tans_allowed = DataElementField(type='jn', _d="Mehrfach-TAN erlaubt")
    tan_time_dialog_association = DataElementField(type='code', length=1, _d="TAN Zeit- und Dialogbezug")
    cancel_allowed = DataElementField(type='jn', _d="Auftragsstorno erlaubt")
    sms_charge_account_required = DataElementField(type='code', length=1, _d="SMS-Abbuchungskonto erforderlich")
    principal_account_required = DataElementField(type='code', length=1, _d="Auftraggeberkonto erforderlich")
    challenge_class_required = DataElementField(type='jn', _d="Challenge-Klasse erforderlich")
    challenge_structured = DataElementField(type='jn', _d="Challenge strukturiert")
    initialisation_mode = DataElementField(type='code', _d="Initialisierungsmodus")
    description_required = DataElementField(type='code', length=1, _d="Bezeichnung des TAN-Medium erforderlich")
    response_hhd_uc_required = DataElementField(type='jn', _d="Antwort HHD_UC erforderlich")
    supported_media_number = DataElementField(type='num', length=1, required=False, _d="Anzahl unterstützter aktiver TAN-Medien")

class ParameterTwostepCommon(DataElementGroup):
    onestep_method_allowed = DataElementField(type='jn')
    multiple_tasks_allowed = DataElementField(type='jn')
    hash_algorithm = DataElementField(type='code', length=1)

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

class SupportedLanguages2(DataElementGroup):
    languages = DataElementField(type='code', max_length=3, min_count=1, max_count=9)

class SupportedHBCIVersions2(DataElementGroup):
    versions = DataElementField(type='code', max_length=3, min_count=1, max_count=9)

class AccountInternational(DataElementGroup):
    is_sepa = DataElementField(type='jn')
    iban = DataElementField(type='an', max_length=34)
    bic = DataElementField(type='an', max_length=11)
    account_number = DataElementField(type='id')
    subaccount_number = DataElementField(type='id')
    bank_identifier = DataElementGroupField(type=BankIdentifier)
