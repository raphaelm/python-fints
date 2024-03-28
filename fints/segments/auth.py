from fints.fields import CodeField, DataElementField, DataElementGroupField
from fints.formals import (
    KTI1, BankIdentifier, ChallengeValidUntil, Language2,
    ParameterChallengeClass, ParameterPinTan, ParameterTwostepTAN1,
    ParameterTwostepTAN2, ParameterTwostepTAN3, ParameterTwostepTAN4,
    ParameterTwostepTAN5, ParameterTwostepTAN6, ResponseHHDUC,
    SystemIDStatus, TANMedia4, TANMedia5, TANMediaClass3,
    TANMediaClass4, TANMediaType2, TANUsageOption, ParameterTwostepTAN7,
)

from .base import FinTS3Segment, ParameterSegment


class HKIDN2(FinTS3Segment):
    """Identifikation, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    bank_identifier = DataElementGroupField(type=BankIdentifier, _d="Kreditinstitutskennung")
    customer_id = DataElementField(type='id', _d="Kunden-ID")
    system_id = DataElementField(type='id', _d="Kundensystem-ID")
    system_id_status = CodeField(enum=SystemIDStatus, length=1, _d="Kundensystem-Status")


class HKVVB3(FinTS3Segment):
    """Verarbeitungsvorbereitung, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    bpd_version = DataElementField(type='num', max_length=3, _d="BPD-Version")
    upd_version = DataElementField(type='num', max_length=3, _d="UPD-Version")
    language = CodeField(enum=Language2, max_length=3, _d="Dialogsprache")
    product_name = DataElementField(type='an', max_length=25, _d="Produktbezeichnung")
    product_version = DataElementField(type='an', max_length=5, _d="Produktversion")


class HKTAN2(FinTS3Segment):
    """Zwei-Schritt-TAN-Einreichung, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""
    tan_process = DataElementField(type='code', length=1, _d="TAN-Prozess")
    task_hash_value = DataElementField(type='bin', max_length=256, required=False, _d="Auftrags-Hashwert")
    task_reference = DataElementField(type='an', max_length=35, required=False, _d="Auftragsreferenz")
    tan_list_number = DataElementField(type='an', max_length=20, required=False, _d="TAN-Listennummer")
    further_tan_follows = DataElementField(type='jn', length=1, required=False, _d="Weitere TAN folgt")
    cancel_task = DataElementField(type='jn', length=1, required=False, _d="Auftrag stornieren")
    challenge_class = DataElementField(type='num', max_length=2, required=False, _d="Challenge-Klasse")
    parameter_challenge_class = DataElementGroupField(type=ParameterChallengeClass, required=False, _d="Parameter Challenge-Klasse")


class HKTAN3(FinTS3Segment):
    """Zwei-Schritt-TAN-Einreichung, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""
    tan_process = DataElementField(type='code', length=1, _d="TAN-Prozess")
    task_hash_value = DataElementField(type='bin', max_length=256, required=False, _d="Auftrags-Hashwert")
    task_reference = DataElementField(type='an', max_length=35, required=False, _d="Auftragsreferenz")
    tan_list_number = DataElementField(type='an', max_length=20, required=False, _d="TAN-Listennummer")
    further_tan_follows = DataElementField(type='jn', length=1, required=False, _d="Weitere TAN folgt")
    cancel_task = DataElementField(type='jn', length=1, required=False, _d="Auftrag stornieren")
    challenge_class = DataElementField(type='num', max_length=2, required=False, _d="Challenge-Klasse")
    parameter_challenge_class = DataElementGroupField(type=ParameterChallengeClass, required=False, _d="Parameter Challenge-Klasse")
    tan_medium_name = DataElementField(type='an', max_length=32, required=False, _d="Bezeichnung des TAN-Mediums")


class HKTAN5(FinTS3Segment):
    """Zwei-Schritt-TAN-Einreichung, version 5

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""
    tan_process = DataElementField(type='code', length=1, _d="TAN-Prozess")
    segment_type = DataElementField(type='an', max_length=6, required=False, _d="Segmentkennung")
    account = DataElementGroupField(type=KTI1, required=False, _d="Kontoverbindung international Auftraggeber")
    task_hash_value = DataElementField(type='bin', max_length=256, required=False, _d="Auftrags-Hashwert")
    task_reference = DataElementField(type='an', max_length=35, required=False, _d="Auftragsreferenz")
    tan_list_number = DataElementField(type='an', max_length=20, required=False, _d="TAN-Listennummer")
    further_tan_follows = DataElementField(type='jn', length=1, required=False, _d="Weitere TAN folgt")
    cancel_task = DataElementField(type='jn', length=1, required=False, _d="Auftrag stornieren")
    sms_charge_account = DataElementGroupField(type=KTI1, required=False, _d="SMS-Abbuchungskonto")
    challenge_class = DataElementField(type='num', max_length=2, required=False, _d="Challenge-Klasse")
    parameter_challenge_class = DataElementGroupField(type=ParameterChallengeClass, required=False, _d="Parameter Challenge-Klasse")
    tan_medium_name = DataElementField(type='an', max_length=32, required=False, _d="Bezeichnung des TAN-Mediums")


class HKTAN6(FinTS3Segment):
    """Zwei-Schritt-TAN-Einreichung, version 6

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""
    tan_process = DataElementField(type='code', length=1, _d="TAN-Prozess")
    segment_type = DataElementField(type='an', max_length=6, required=False, _d="Segmentkennung")
    account = DataElementGroupField(type=KTI1, required=False, _d="Kontoverbindung international Auftraggeber")
    task_hash_value = DataElementField(type='bin', max_length=256, required=False, _d="Auftrags-Hashwert")
    task_reference = DataElementField(type='an', max_length=35, required=False, _d="Auftragsreferenz")
    further_tan_follows = DataElementField(type='jn', length=1, required=False, _d="Weitere TAN folgt")
    cancel_task = DataElementField(type='jn', length=1, required=False, _d="Auftrag stornieren")
    sms_charge_account = DataElementGroupField(type=KTI1, required=False, _d="SMS-Abbuchungskonto")
    challenge_class = DataElementField(type='num', max_length=2, required=False, _d="Challenge-Klasse")
    parameter_challenge_class = DataElementGroupField(type=ParameterChallengeClass, required=False, _d="Parameter Challenge-Klasse")
    tan_medium_name = DataElementField(type='an', max_length=32, required=False, _d="Bezeichnung des TAN-Mediums")
    response_hhd_uc = DataElementGroupField(type=ResponseHHDUC, required=False, _d="Antwort HHD_UC")


class HKTAN7(FinTS3Segment):
    """Zwei-Schritt-TAN-Einreichung, version 7

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""
    tan_process = DataElementField(type='code', length=1, _d="TAN-Prozess")
    segment_type = DataElementField(type='an', max_length=6, required=False, _d="Segmentkennung")
    account = DataElementGroupField(type=KTI1, required=False, _d="Kontoverbindung international Auftraggeber")
    task_hash_value = DataElementField(type='bin', max_length=256, required=False, _d="Auftrags-Hashwert")
    task_reference = DataElementField(type='an', max_length=35, required=False, _d="Auftragsreferenz")
    further_tan_follows = DataElementField(type='jn', length=1, required=False, _d="Weitere TAN folgt")
    cancel_task = DataElementField(type='jn', length=1, required=False, _d="Auftrag stornieren")
    sms_charge_account = DataElementGroupField(type=KTI1, required=False, _d="SMS-Abbuchungskonto")
    challenge_class = DataElementField(type='num', max_length=2, required=False, _d="Challenge-Klasse")
    parameter_challenge_class = DataElementGroupField(type=ParameterChallengeClass, required=False, _d="Parameter Challenge-Klasse")
    tan_medium_name = DataElementField(type='an', max_length=32, required=False, _d="Bezeichnung des TAN-Mediums")
    response_hhd_uc = DataElementGroupField(type=ResponseHHDUC, required=False, _d="Antwort HHD_UC")


class HITAN2(FinTS3Segment):
    """Zwei-Schritt-TAN-Einreichung Rückmeldung, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""
    tan_process = DataElementField(type='code', length=1, _d="TAN-Prozess")
    task_hash_value = DataElementField(type='bin', max_length=256, required=False, _d="Auftrags-Hashwert")
    task_reference = DataElementField(type='an', max_length=35, required=False, _d="Auftragsreferenz")
    challenge = DataElementField(type='an', max_length=2048, required=False, _d="Challenge")
    challenge_valid_until = DataElementGroupField(type=ChallengeValidUntil, required=False, _d="Gültigkeitsdatum und -uhrzeit für Challenge")
    tan_list_number = DataElementField(type='an', max_length=20, required=False, _d="TAN-Listennummer")
    ben = DataElementField(type='an', max_length=99, required=False, _d="BEN")


class HITAN3(FinTS3Segment):
    """Zwei-Schritt-TAN-Einreichung Rückmeldung, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""
    tan_process = DataElementField(type='code', length=1, _d="TAN-Prozess")
    task_hash_value = DataElementField(type='bin', max_length=256, required=False, _d="Auftrags-Hashwert")
    task_reference = DataElementField(type='an', max_length=35, required=False, _d="Auftragsreferenz")
    challenge = DataElementField(type='an', max_length=2048, required=False, _d="Challenge")
    challenge_valid_until = DataElementGroupField(type=ChallengeValidUntil, required=False, _d="Gültigkeitsdatum und -uhrzeit für Challenge")
    tan_list_number = DataElementField(type='an', max_length=20, required=False, _d="TAN-Listennummer")
    ben = DataElementField(type='an', max_length=99, required=False, _d="BEN")
    tan_medium_name = DataElementField(type='an', max_length=32, required=False, _d="Bezeichnung des TAN-Mediums")


class HITAN5(FinTS3Segment):
    """Zwei-Schritt-TAN-Einreichung Rückmeldung, version 5

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""
    tan_process = DataElementField(type='code', length=1, _d="TAN-Prozess")
    task_hash_value = DataElementField(type='bin', max_length=256, required=False, _d="Auftrags-Hashwert")
    task_reference = DataElementField(type='an', max_length=35, required=False, _d="Auftragsreferenz")
    challenge = DataElementField(type='an', max_length=2048, required=False, _d="Challenge")
    challenge_hhduc = DataElementField(type='bin', required=False, _d="Challenge HHD_UC")
    challenge_valid_until = DataElementGroupField(type=ChallengeValidUntil, required=False, _d="Gültigkeitsdatum und -uhrzeit für Challenge")
    tan_list_number = DataElementField(type='an', max_length=20, required=False, _d="TAN-Listennummer")
    ben = DataElementField(type='an', max_length=99, required=False, _d="BEN")
    tan_medium_name = DataElementField(type='an', max_length=32, required=False, _d="Bezeichnung des TAN-Mediums")


class HITAN6(FinTS3Segment):
    """Zwei-Schritt-TAN-Einreichung Rückmeldung, version 6

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""
    tan_process = DataElementField(type='code', length=1, _d="TAN-Prozess")
    task_hash_value = DataElementField(type='bin', max_length=256, required=False, _d="Auftrags-Hashwert")
    task_reference = DataElementField(type='an', max_length=35, required=False, _d="Auftragsreferenz")
    challenge = DataElementField(type='an', max_length=2048, required=False, _d="Challenge")
    challenge_hhduc = DataElementField(type='bin', required=False, _d="Challenge HHD_UC")
    challenge_valid_until = DataElementGroupField(type=ChallengeValidUntil, required=False, _d="Gültigkeitsdatum und -uhrzeit für Challenge")
    tan_medium_name = DataElementField(type='an', max_length=32, required=False, _d="Bezeichnung des TAN-Mediums")


class HITAN7(FinTS3Segment):
    """Zwei-Schritt-TAN-Einreichung Rückmeldung, version 7

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""
    tan_process = DataElementField(type='code', length=1, _d="TAN-Prozess")
    task_hash_value = DataElementField(type='bin', max_length=256, required=False, _d="Auftrags-Hashwert")
    task_reference = DataElementField(type='an', max_length=35, required=False, _d="Auftragsreferenz")
    challenge = DataElementField(type='an', max_length=2048, required=False, _d="Challenge")
    challenge_hhduc = DataElementField(type='bin', required=False, _d="Challenge HHD_UC")
    challenge_valid_until = DataElementGroupField(type=ChallengeValidUntil, required=False, _d="Gültigkeitsdatum und -uhrzeit für Challenge")
    tan_medium_name = DataElementField(type='an', max_length=32, required=False, _d="Bezeichnung des TAN-Mediums")


class HKTAB4(FinTS3Segment):
    """TAN-Generator/Liste anzeigen Bestand, version 4

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""

    tan_media_type = CodeField(enum=TANMediaType2, _d="TAN-Medium-Art")
    tan_media_class = CodeField(enum=TANMediaClass3, _d="TAN-Medium-Klasse")


class HITAB4(FinTS3Segment):
    """TAN-Generator/Liste anzeigen Bestand Rückmeldung, version 4

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""

    tan_usage_option = CodeField(enum=TANUsageOption, _d="TAN_Einsatzoption")
    tan_media_list = DataElementGroupField(type=TANMedia4, max_count=99, required=False, _d="TAN-Medium-Liste")


class HKTAB5(FinTS3Segment):
    """TAN-Generator/Liste anzeigen Bestand, version 5

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""

    tan_media_type = CodeField(enum=TANMediaType2, _d="TAN-Medium-Art")
    tan_media_class = CodeField(enum=TANMediaClass4, _d="TAN-Medium-Klasse")


class HITAB5(FinTS3Segment):
    """TAN-Generator/Liste anzeigen Bestand Rückmeldung, version 5

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN"""

    tan_usage_option = CodeField(enum=TANUsageOption, _d="TAN_Einsatzoption")
    tan_media_list = DataElementGroupField(type=TANMedia5, max_count=99, required=False, _d="TAN-Medium-Liste")


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


class HITANS7(HITANSBase):
    parameter = DataElementGroupField(type=ParameterTwostepTAN7)


class HIPINS1(ParameterSegment):
    """PIN/TAN-spezifische Informationen, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Sicherheitsverfahren PIN/TAN 
    """
    parameter = DataElementGroupField(type=ParameterPinTan, _d="Parameter PIN/TAN-spezifische Informationen") 
