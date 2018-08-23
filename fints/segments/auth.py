from fints.fields import CodeField, DataElementField, DataElementGroupField
from fints.formals import (
    BankIdentifier, Language2, SynchronisationMode, SystemIDStatus,
    TANMediaType2, TANMediaClass4, TANMedia5, TANMediaClass3, TANMedia4, TANUsageOption,
    KTI1, ParameterChallengeClass, ResponseHHDUC, ChallengeValidUntil
)
from fints.utils import fints_escape

from . import FinTS3Segment, FinTS3SegmentOLD


class HKIDN(FinTS3SegmentOLD):
    """
    HKIDN (Identifikation)
    Section C.3.1.2
    """
    type = 'HKIDN'
    version = 2

    def __init__(self, segmentno, blz, username, systemid=0, customerid=1):
        data = [
            '{}:{}'.format(self.country_code, blz),
            fints_escape(username),
            systemid,
            customerid
        ]
        super().__init__(segmentno, data)

class HKIDN2(FinTS3Segment):
    """Identifikation, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    bank_identifier = DataElementGroupField(type=BankIdentifier, _d="Kreditinstitutskennung")
    customer_id = DataElementField(type='id', _d="Kunden-ID")
    system_id = DataElementField(type='id', _d="Kundensystem-ID")
    system_id_status = CodeField(enum=SystemIDStatus, length=1, _d="Kundensystem-Status")


class HKVVB(FinTS3SegmentOLD):
    """
    HKVVB (Verarbeitungsvorbereitung)
    Section C.3.1.3
    """
    type = 'HKVVB'
    version = 3

    LANG_DE = 1
    LANG_EN = 2
    LANG_FR = 3

    PRODUCT_NAME = 'pyfints'
    PRODUCT_VERSION = '0.1'

    def __init__(self, segmentno, lang=LANG_DE):
        data = [
            0, 0, lang, fints_escape(self.PRODUCT_NAME), fints_escape(self.PRODUCT_VERSION)
        ]
        super().__init__(segmentno, data)

class HKVVB3(FinTS3Segment):
    """Verarbeitungsvorbereitung, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    bpd_version = DataElementField(type='num', max_length=3, _d="BPD-Version")
    upd_version = DataElementField(type='num', max_length=3, _d="UPD-Version")
    language = CodeField(enum=Language2, max_length=3, _d="Dialogsprache")
    product_name = DataElementField(type='an', max_length=25, _d="Produktbezeichnung")
    product_version = DataElementField(type='an', max_length=5, _d="Produktversion")

class HKSYN(FinTS3SegmentOLD):
    """
    HKSYN (Synchronisation)
    Section C.8.1.2
    """
    type = 'HKSYN'
    version = 3

    SYNC_MODE_NEW_CUSTOMER_ID = 0
    SYNC_MODE_LAST_MSG_NUMBER = 1
    SYNC_MODE_SIGNATURE_ID = 2

    def __init__(self, segmentno, mode=SYNC_MODE_NEW_CUSTOMER_ID):
        data = [
            mode
        ]
        super().__init__(segmentno, data)


class HKTAN(FinTS3SegmentOLD):
    """
    HKTAN (TAN-Verfahren festlegen)
    Section B.5.1
    """
    type = 'HKTAN'

    def __init__(self, segno, process, aref, medium, version):
        self.version = version

        if process not in ('2', '4'):
            raise NotImplementedError("HKTAN process {} currently not implemented.".format(process))
        if version not in (3, 4, 5, 6):
            raise NotImplementedError("HKTAN version {} currently not implemented.".format(version))

        if process == '4':
            if medium:
                if version == 3:
                    data = [process, '', '', '', '', '', '', '', medium]
                elif version == 4:
                    data = [process, '', '', '', '', '', '', '', '', medium]
                elif version == 5:
                    data = [process, '', '', '', '', '', '', '', '', '', '', medium]
                elif version == 6:
                    data = [process, '', '', '', '', '', '', '', '', '', medium]
            else:
                data = [process]
        elif process == '2':
            if version == 6:
                data = [process, '', '', '', aref, 'N']
            elif version == 5:
                data = [process, '', '', '', aref, '', 'N']
            elif version in (3, 4):
                data = [process, '', aref, '', 'N']
        super().__init__(segno, data)


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


class HKTAB(FinTS3SegmentOLD):
    """
    HKTAB (Verfügbarre TAN-Medien ermitteln)
    Section C.2.1.2
    """
    type = 'HKTAB'

    def __init__(self, segno):
        self.version = 5
        data = [
            '0', 'A'
        ]
        super().__init__(segno, data)

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
