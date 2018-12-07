from fints.fields import DataElementField, DataElementGroupField
from fints.formals import (
    KTI1, Account2, Account3, Amount1, Balance1, Balance2, Timestamp1,
)

from .base import FinTS3Segment


class HKSAL5(FinTS3Segment):
    """Saldenabfrage, version 5

    Source: HBCI Homebanking-Computer-Interface, Schnittstellenspezifikation"""
    account = DataElementGroupField(type=Account2, _d="Kontoverbindung Auftraggeber")
    all_accounts = DataElementField(type='jn', _d="Alle Konten")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HISAL5(FinTS3Segment):
    """Saldenrückmeldung, version 5

    Source: HBCI Homebanking-Computer-Interface, Schnittstellenspezifikation"""
    account = DataElementGroupField(type=Account2, _d="Kontoverbindung Auftraggeber")
    account_product = DataElementField(type='an', max_length=30, _d="Kontoproduktbezeichnung")
    currency = DataElementField(type='cur', _d="Kontowährung")
    balance_booked = DataElementGroupField(type=Balance1, _d="Gebuchter Saldo")
    balance_pending = DataElementGroupField(type=Balance1, required=False, _d="Saldo der vorgemerkten Umsätze")
    line_of_credit = DataElementGroupField(type=Amount1, required=False, _d="Kreditlinie")
    available_amount = DataElementGroupField(type=Amount1, required=False, _d="Verfügbarer Betrag")
    used_amount = DataElementGroupField(type=Amount1, required=False, _d="Bereits verfügter Betrag")
    booking_date = DataElementField(type='dat', required=False, _d="Buchungsdatum des Saldos")
    booking_time = DataElementField(type='tim', required=False, _d="Buchungsuhrzeit des Saldos")
    date_due = DataElementField(type='dat', required=False, _d="Fälligkeit")


class HKSAL6(FinTS3Segment):
    """Saldenabfrage, version 6

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=Account3, _d="Kontoverbindung Auftraggeber")
    all_accounts = DataElementField(type='jn', _d="Alle Konten")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HISAL6(FinTS3Segment):
    """Saldenrückmeldung, version 6

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=Account3, _d="Kontoverbindung Auftraggeber")
    account_product = DataElementField(type='an', max_length=30, _d="Kontoproduktbezeichnung")
    currency = DataElementField(type='cur', _d="Kontowährung")
    balance_booked = DataElementGroupField(type=Balance2, _d="Gebuchter Saldo")
    balance_pending = DataElementGroupField(type=Balance2, required=False, _d="Saldo der vorgemerkten Umsätze")
    line_of_credit = DataElementGroupField(type=Amount1, required=False, _d="Kreditlinie")
    available_amount = DataElementGroupField(type=Amount1, required=False, _d="Verfügbarer Betrag")
    used_amount = DataElementGroupField(type=Amount1, required=False, _d="Bereits verfügter Betrag")
    overdraft = DataElementGroupField(type=Amount1, required=False, _d="Überziehung")
    booking_timestamp = DataElementGroupField(type=Timestamp1, required=False, _d="Buchungszeitpunkt")
    date_due = DataElementField(type='dat', required=False, _d="Fälligkeit")


class HKSAL7(FinTS3Segment):
    """Saldenabfrage, version 7

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    all_accounts = DataElementField(type='jn', _d="Alle Konten")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HISAL7(FinTS3Segment):
    """Saldenrückmeldung, version 7

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle """
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    account_product = DataElementField(type='an', max_length=30, _d="Kontoproduktbezeichnung")
    currency = DataElementField(type='cur', _d="Kontowährung")
    balance_booked = DataElementGroupField(type=Balance2, _d="Gebuchter Saldo")
    balance_pending = DataElementGroupField(type=Balance2, required=False, _d="Saldo der vorgemerkten Umsätze")
    line_of_credit = DataElementGroupField(type=Amount1, required=False, _d="Kreditlinie")
    available_amount = DataElementGroupField(type=Amount1, required=False, _d="Verfügbarer Betrag")
    used_amount = DataElementGroupField(type=Amount1, required=False, _d="Bereits verfügter Betrag")
    overdraft = DataElementGroupField(type=Amount1, required=False, _d="Überziehung")
    booking_timestamp = DataElementGroupField(type=Timestamp1, required=False, _d="Buchungszeitpunkt")
    date_due = DataElementField(type='dat', required=False, _d="Fälligkeit")
