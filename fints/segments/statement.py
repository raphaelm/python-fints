from fints.fields import DataElementField, DataElementGroupField, CodeField
from fints.formals import KTI1, Account2, Account3, QueryCreditCardStatements2, SupportedMessageTypes, \
    BookedCamtStatements1, StatementFormat, Confirmation, ReportPeriod2

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


class HKCAZ1(FinTS3Segment):
    """Kontoumsätze anfordern/Zeitraum, version 5

    Source: HBCI Homebanking-Computer-Interface, Schnittstellenspezifikation"""
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    supported_camt_messages = DataElementGroupField(type=SupportedMessageTypes, _d="Kontoverbindung international")
    all_accounts = DataElementField(type='jn', _d="Alle Konten")
    date_start = DataElementField(type='dat', required=False, _d="Von Datum")
    date_end = DataElementField(type='dat', required=False, _d="Bis Datum")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HICAZ1(FinTS3Segment):
    """Kontoumsätze rückmelden/Zeitraum, version 1

    Source: HBCI Homebanking-Computer-Interface, Schnittstellenspezifikation"""
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung Auftraggeber")
    camt_descriptor = DataElementField(type='an', _d="camt-Deskriptor")
    statement_booked = DataElementGroupField(type=BookedCamtStatements1, _d="Gebuchte Umsätze")
    statement_pending = DataElementField(type='bin', required=False, _d="Nicht gebuchte Umsätze")


class HKKAU1(FinTS3Segment):
    """Übersicht Kontoauszüge, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle"""
    account = DataElementGroupField(type=Account3, _d="Kontoverbindung Auftraggeber")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HKKAU2(FinTS3Segment):
    """Übersicht Kontoauszüge, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle"""
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HIKAU1(FinTS3Segment):
    """Übersicht Kontoauszüge, version 1

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle"""
    statement_number = DataElementField(type='num', max_length=5, _d="Kontoauszugsnummer")
    confirmation = CodeField(enum=Confirmation, length=1, _d="Quittierung")
    collection_possible = DataElementField(type='jn', _d="Abholung möglich J/N")
    year = DataElementField(type='num', length=4, required=False, _d="Jahr")
    date_created = DataElementField(type='dat', required=False, _d="Datum der Erstellung")
    time_created = DataElementField(type='tim', required=False, _d="Uhrzeit der Erstellung")
    creation_type = DataElementField(type='an', max_length=30, required=False, _d="Erstellart")


class HIKAU2(FinTS3Segment):
    """Übersicht Kontoauszüge, version 2

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle"""
    statement_number = DataElementField(type='num', max_length=5, _d="Kontoauszugsnummer")
    confirmation = CodeField(enum=Confirmation, length=1, _d="Quittierung")
    collection_possible = DataElementField(type='jn', _d="Abholung möglich J/N")
    year = DataElementField(type='num', length=4, required=False, _d="Jahr")
    date_created = DataElementField(type='dat', required=False, _d="Datum der Erstellung")
    time_created = DataElementField(type='tim', required=False, _d="Uhrzeit der Erstellung")
    creation_type = DataElementField(type='an', max_length=30, required=False, _d="Erstellart")


class HKEKA3(FinTS3Segment):
    """Kontoauszug anfordern, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle"""
    account = DataElementGroupField(type=Account3, _d="Kontoverbindung Auftraggeber")
    statement_format = CodeField(enum=StatementFormat, length=1, required=False, _d="Kontoauszugsformat")
    statement_number = DataElementField(type='num', max_length=5, _d="Kontoauszugsnummer")
    statement_year = DataElementField(type='num', length=4, _d="Kontoauszugsjahr")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HKEKA4(FinTS3Segment):
    """Kontoauszug anfordern, version 4

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle"""
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    statement_format = CodeField(enum=StatementFormat, length=1, required=False, _d="Kontoauszugsformat")
    statement_number = DataElementField(type='num', max_length=5, _d="Kontoauszugsnummer")
    statement_year = DataElementField(type='num', length=4, _d="Kontoauszugsjahr")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HKEKA5(FinTS3Segment):
    """Kontoauszug anfordern, version 5

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle"""
    account = DataElementGroupField(type=KTI1, _d="Kontoverbindung international")
    statement_format = CodeField(enum=StatementFormat, length=1, required=False, _d="Kontoauszugsformat")
    statement_number = DataElementField(type='num', max_length=5, _d="Kontoauszugsnummer")
    statement_year = DataElementField(type='num', length=4, _d="Kontoauszugsjahr")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HIEKA3(FinTS3Segment):
    """Kontoauszug, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle"""
    statement_format = CodeField(enum=StatementFormat, length=1, required=False, _d="Kontoauszugsformat")
    statement_period = DataElementGroupField(type=ReportPeriod2, _d="Berichtszeitraum")
    data = DataElementField(type='bin', _d="Gebuchte Umsätze")
    statement_info = DataElementField(type='txt', max_length=65536, required=False, _d="Informationen zum Rechnungsabschluss")
    customer_info = DataElementField(type='txt', max_length=65536, required=False,
                                      _d="Informationen zu Kundenbedingungen")
    advertising_text = DataElementField(type='txt', max_length=65536, required=False, _d="Werbetext")
    account_iban = DataElementField(type='an', max_length=34, required=False, _d="IBAN Konto")
    account_bic = DataElementField(type='an', max_length=11, required=False, _d="BIC Konto")
    statement_name_1 = DataElementField(type='an', max_length=35, required=False, _d="Auszugsname 1")
    statement_name_2 = DataElementField(type='an', max_length=35, required=False, _d="Auszugsname 2")
    statement_name_extra = DataElementField(type='an', max_length=35, required=False, _d="Namenszusatz")
    confirmation_code = DataElementField(type='bin', required=False, _d="Quittungscode")


class HIEKA4(FinTS3Segment):
    """Kontoauszug, version 4

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle"""
    statement_format = CodeField(enum=StatementFormat, length=1, required=False, _d="Kontoauszugsformat")
    statement_period = DataElementGroupField(type=ReportPeriod2, _d="Berichtszeitraum")
    data = DataElementField(type='bin', _d="Gebuchte Umsätze")
    statement_info = DataElementField(type='txt', max_length=65536, required=False, _d="Informationen zum Rechnungsabschluss")
    customer_info = DataElementField(type='txt', max_length=65536, required=False,
                                      _d="Informationen zu Kundenbedingungen")
    advertising_text = DataElementField(type='txt', max_length=65536, required=False, _d="Werbetext")
    account_iban = DataElementField(type='an', max_length=34, required=False, _d="IBAN Konto")
    account_bic = DataElementField(type='an', max_length=11, required=False, _d="BIC Konto")
    statement_name_1 = DataElementField(type='an', max_length=35, required=False, _d="Auszugsname 1")
    statement_name_2 = DataElementField(type='an', max_length=35, required=False, _d="Auszugsname 2")
    statement_name_extra = DataElementField(type='an', max_length=35, required=False, _d="Namenszusatz")
    confirmation_code = DataElementField(type='bin', required=False, _d="Quittungscode")


class HIEKA5(FinTS3Segment):
    """Kontoauszug, version 5

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Messages -- Multibankfähige Geschäftsvorfälle"""
    statement_format = CodeField(enum=StatementFormat, length=1, required=False, _d="Kontoauszugsformat")
    statement_period = DataElementGroupField(type=ReportPeriod2, _d="Berichtszeitraum")
    date_created = DataElementField(type='dat', required=False, _d="Erstellungsdatum Kontoauszug")
    statement_year = DataElementField(type='num', length=4, required=False, _d="Kontoauszugsjahr")
    statement_number = DataElementField(type='num', max_length=5, required=False, _d="Kontoauszugsnummer")
    data = DataElementField(type='bin', _d="Gebuchte Umsätze")
    statement_info = DataElementField(type='txt', max_length=65536, required=False, _d="Informationen zum Rechnungsabschluss")
    customer_info = DataElementField(type='txt', max_length=65536, required=False,
                                      _d="Informationen zu Kundenbedingungen")
    advertising_text = DataElementField(type='txt', max_length=65536, required=False, _d="Werbetext")
    account_iban = DataElementField(type='an', max_length=34, required=False, _d="IBAN Konto")
    account_bic = DataElementField(type='an', max_length=11, required=False, _d="BIC Konto")
    statement_name_1 = DataElementField(type='an', max_length=35, required=False, _d="Auszugsname 1")
    statement_name_2 = DataElementField(type='an', max_length=35, required=False, _d="Auszugsname 2")
    statement_name_extra = DataElementField(type='an', max_length=35, required=False, _d="Namenszusatz")
    confirmation_code = DataElementField(type='bin', required=False, _d="Quittungscode")
