from fints.utils import fints_escape

from fints.fields import DataElementField, DataElementGroupField
from fints.formals import (
    KTI1, Account3, Account2
)

from . import FinTS3Segment, FinTS3SegmentOLD


class HKKAZ(FinTS3SegmentOLD):
    """
    HKKAZ (Kontoumsätze)

    Refs: http://www.hbci-zka.de/dokumente/spezifikation_deutsch/fintsv3/FinTS_3.0_Messages_Geschaeftsvorfaelle_2015-08-07_final_version.pdf
    Section C.2.1.1.1.2
    """
    type = 'HKKAZ'

    def __init__(self, segno, version, account, date_start, date_end, touchdown):
        self.version = version

        data = [
            account,
            'N',
            date_start.strftime('%Y%m%d'),
            date_end.strftime('%Y%m%d'),
            '',
            fints_escape(touchdown) if touchdown is not None else ''
        ]
        super().__init__(segno, data)

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
