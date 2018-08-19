from . import FinTS3SegmentOLD, FinTS3Segment

from fints.formals import Account3, KTI1, Balance2, Amount1, Timestamp1
from fints.fields import DataElementGroupField, DataElementField


class HKSAL(FinTS3SegmentOLD):
    """
    HKSAL (Konto Saldo anfordern)
    Section C.2.1.2
    """
    type = 'HKSAL'

    def __init__(self, segno, version, account):
        self.version = version
        data = [
            account,
            'N'
        ]
        super().__init__(segno, data)

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
    booking_time = DataElementGroupField(type=Timestamp1, required=False, _d="Buchungszeitpunkt")
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
    booking_time = DataElementGroupField(type=Timestamp1, required=False, _d="Buchungszeitpunkt")
    date_due = DataElementField(type='dat', required=False, _d="Fälligkeit")
