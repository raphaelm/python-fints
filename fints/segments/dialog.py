from ..fields import CodeField, DataElementField, DataElementGroupField
from ..formals import Response, SynchronizationMode
from .base import FinTS3Segment


class HKSYN3(FinTS3Segment):
    """Synchronisierung, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    synchronization_mode = CodeField(enum=SynchronizationMode, length=1)


class HISYN4(FinTS3Segment):
    """Synchronisierungsantwort"""
    system_id = DataElementField(type='id', _d="Kundensystem-ID")
    message_number = DataElementField(type='num', max_length=4, required=False, _d="Nachrichtennummer")
    security_reference_signature_key = DataElementField(type='num', max_length=16, required=False, _d="Sicherheitsreferenznummer für Signierschlüssel")
    security_reference_digital_signature = DataElementField(type='num', max_length=16, required=False, _d="Sicherheitsreferenznummer für Digitale Signatur")


class HKEND1(FinTS3Segment):
    """Dialogende, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    dialog_id = DataElementField(type='id', _d="Dialog-ID")


class HIRMG2(FinTS3Segment):
    """Rückmeldungen zur Gesamtnachricht"""
    responses = DataElementGroupField(type=Response, min_count=1, max_count=99, _d="Rückmeldung")


class HIRMS2(FinTS3Segment):
    """Rückmeldungen zu Segmenten"""
    responses = DataElementGroupField(type=Response, min_count=1, max_count=99, _d="Rückmeldung")
