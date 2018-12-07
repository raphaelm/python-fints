from fints.fields import DataElementField, DataElementGroupField
from fints.formals import KTI1, Account2, Account3, QueryCreditCardStatements2

from .base import FinTS3Segment, ParameterSegment


class HKKAZ5(FinTS3Segment):
    """Kontoumsätze anfordern/Zeitraum, version 5

    Source: HBCI Homebanking-Computer-Interface, Schnittstellenspezifikation"""
    account = DataElementGroupField(type=Account2, _d="Kontoverbindung Auftraggeber")
    all_accounts = DataElementField(type='jn', _d="Alle Konten")
    date_start = DataElementField(type='dat', required=False, _d="Von Datum")
    date_end = DataElementField(type='dat', required=False, _d="Bis Datum")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HIKAZ5(FinTS3Segment):
    """Kontoumsätze rückmelden/Zeitraum, version 5

    Source: HBCI Homebanking-Computer-Interface, Schnittstellenspezifikation"""
    statement_booked = DataElementField(type='bin', _d="Gebuchte Umsätze")
    statement_pending = DataElementField(type='bin', required=False, _d="Nicht gebuchte Umsätze")


class HKKAZ6(FinTS3Segment):
    """Kontoumsätze anfordern/Zeitraum, version 6

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=Account3, _d="Kontoverbindung Auftraggeber")
    all_accounts = DataElementField(type='jn', _d="Alle Konten")
    date_start = DataElementField(type='dat', required=False, _d="Von Datum")
    date_end = DataElementField(type='dat', required=False, _d="Bis Datum")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HIKAZ6(FinTS3Segment):
    """Kontoumsätze rückmelden/Zeitraum, version 6

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    statement_booked = DataElementField(type='bin', _d="Gebuchte Umsätze")
    statement_pending = DataElementField(type='bin', required=False, _d="Nicht gebuchte Umsätze")


class HKKAZ7(FinTS3Segment):
    """Kontoumsätze anfordern/Zeitraum, version 7

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    all_accounts = DataElementField(type='jn', _d="Alle Konten")
    date_start = DataElementField(type='dat', required=False, _d="Von Datum")
    date_end = DataElementField(type='dat', required=False, _d="Bis Datum")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HIKAZ7(FinTS3Segment):
    """Kontoumsätze rückmelden/Zeitraum, version 7

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    statement_booked = DataElementField(type='bin', _d="Gebuchte Umsätze")
    statement_pending = DataElementField(type='bin', required=False, _d="Nicht gebuchte Umsätze")


class DKKKU2(FinTS3Segment):
    """Kreditkartenumsätze anfordern, version 2

    Source: Reverse engineered"""
    account = DataElementGroupField(type=Account2, _d="Kontoverbindung Auftraggeber")
    credit_card_number = DataElementField(type='an', _d="Kreditkartennummer")
    subaccount = DataElementField(type='an', required=False, _d="Subaccount?")
    date_start = DataElementField(type='dat', required=False, _d="Von Datum")
    date_end = DataElementField(type='dat', required=False, _d="Bis Datum")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class DIKKU2(FinTS3Segment):
    """Kreditkartenumsätze rückmelden, version 2

    Source: Reverse engineered"""

class DIKKUS2(ParameterSegment):
    """Kreditkartenumsätze anfordern Parameter, version 2

    Source: Reverse engineered"""
    parameter = DataElementGroupField(type=QueryCreditCardStatements2, _d="Parameter Kreditkartenumsätze anfordern")
