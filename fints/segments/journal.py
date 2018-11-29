from fints.fields import DataElementField, DataElementGroupField
from fints.formals import ReferenceMessage, Response

from .base import FinTS3Segment, ParameterSegment, ParameterSegment_22


class HKPRO3(FinTS3Segment):
    """Statusprotokoll anfordern, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    date_start = DataElementField(type='dat', required=False, _d="Von Datum")
    date_end = DataElementField(type='dat', required=False, _d="Bis Datum")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HIPRO3(FinTS3Segment):
    """Statusprotokoll rückmelden, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    reference_message = DataElementGroupField(type=ReferenceMessage, _d="Bezugsnachricht")
    reference = DataElementField(type='num', max_length=3, required=False, _d='Bezugssegment')
    date = DataElementField(type='dat', _d="Datum")
    time = DataElementField(type='tim', _d="Uhrzeit")
    responses = DataElementGroupField(type=Response, _d="Rückmeldung")


class HIPROS3(ParameterSegment_22):
    """Statusprotokoll Parameter, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""


class HKPRO4(FinTS3Segment):
    """Statusprotokoll anfordern, version 4

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    date_start = DataElementField(type='dat', required=False, _d="Von Datum")
    date_end = DataElementField(type='dat', required=False, _d="Bis Datum")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HIPRO4(FinTS3Segment):
    """Statusprotokoll rückmelden, version 4

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    reference_message = DataElementGroupField(type=ReferenceMessage, _d="Bezugsnachricht")
    reference = DataElementField(type='num', max_length=3, required=False, _d='Bezugssegment')
    date = DataElementField(type='dat', _d="Datum")
    time = DataElementField(type='tim', _d="Uhrzeit")
    responses = DataElementGroupField(type=Response, _d="Rückmeldung")


class HIPROS4(ParameterSegment):
    """Statusprotokoll Parameter, version 4

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
