from . import FinTS3Segment
from ..fields import CodeField, DataElementField
from ..formals import SynchronisationMode


class HKSYN3(FinTS3Segment):
    """Synchronisierung, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    synchronisation_mode = CodeField(enum=SynchronisationMode, length=1)    

class HISYN4(FinTS3Segment):
    "Synchronisierungsantwort"
    system_id = DataElementField(type='id', _d="Kundensystem-ID")
    message_number = DataElementField(type='num', max_length=4, required=False, _d="Nachrichtennummer")
    security_reference_signature_key = DataElementField(type='num', max_length=16, required=False, _d="Sicherheitsreferenznummer für Signierschlüssel")
    security_reference_digital_signature = DataElementField(type='num', max_length=16, required=False, _d="Sicherheitsreferenznummer für Digitale Signatur")

class HKEND1(FinTS3Segment):
    """Dialogende, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    dialogue_id = DataElementField(type='id', _d="Dialog-ID")
