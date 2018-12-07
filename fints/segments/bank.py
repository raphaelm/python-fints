from fints.fields import CodeField, DataElementField, DataElementGroupField
from fints.formals import (
    AccountInformation, AccountLimit, AllowedTransaction,
    BankIdentifier, CommunicationParameter2, Language2,
    SupportedHBCIVersions2, SupportedLanguages2, UPDUsage,
)

from .base import FinTS3Segment


class HIBPA3(FinTS3Segment):
    """Bankparameter allgemein, version 3

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    bpd_version = DataElementField(type='num', max_length=3, _d="BPD-Version")
    bank_identifier = DataElementGroupField(type=BankIdentifier, _d="Kreditinstitutskennung")
    bank_name = DataElementField(type='an', max_length=60, _d="Kreditinstitutsbezeichnung")
    number_tasks = DataElementField(type='num', max_length=3, _d="Anzahl Geschäftsvorfallarten pro Nachricht")
    supported_languages = DataElementGroupField(type=SupportedLanguages2, _d="Unterstützte Sprachen")
    supported_hbci_version = DataElementGroupField(type=SupportedHBCIVersions2, _d="Unterstützte HBCI-Versionen")
    max_message_length = DataElementField(type='num', max_length=4, required=False, _d="Maximale Nachrichtengröße")
    min_timeout = DataElementField(type='num', max_length=4, required=False, _d="Minimaler Timeout-Wert")
    max_timeout = DataElementField(type='num', max_length=4, required=False, _d="Maximaler Timeout-Wert")


class HIUPA4(FinTS3Segment):
    """Userparameter allgemein"""
    user_identifier = DataElementField(type='id', _d="Benutzerkennung")
    upd_version = DataElementField(type='num', max_length=3, _d="UPD-Version")
    upd_usage = CodeField(UPDUsage, length=1, _d="UPD-Verwendung")
    username = DataElementField(type='an', max_length=35, required=False, _d="Benutzername")
    extension = DataElementField(type='an', max_length=2048, required=False, _d="Erweiterung, allgemein")


class HIUPD6(FinTS3Segment):
    """Kontoinformationen"""
    account_information = DataElementGroupField(type=AccountInformation, required=False, _d="Kontoverbindung")
    iban = DataElementField(type='an', max_length=34, _d="IBAN")
    customer_id = DataElementField(type='id', _d="Kunden-ID")
    account_type = DataElementField(type='num', max_length=2, _d="Kontoart")
    account_currency = DataElementField(type='cur', _d="Kontowährung")
    name_account_owner_1 = DataElementField(type='an', max_length=27, _d="Name des Kontoinhabers 1")
    name_account_owner_2 = DataElementField(type='an', max_length=27, required=False, _d="Name des Kontoinhabers 2")
    account_product_name = DataElementField(type='an', max_length=30, required=False, _d="Kontoproduktbezeichnung")
    account_limit = DataElementGroupField(type=AccountLimit, required=False, _d="Kontolimit")
    allowed_transactions = DataElementGroupField(type=AllowedTransaction, count=999, required=False, _d="Erlaubte Geschäftsvorfälle")
    extension = DataElementField(type='an', max_length=2048, required=False, _d="Erweiterung, kontobezogen")


class HKKOM4(FinTS3Segment):
    """Kommunikationszugang anfordern, version 4

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    start_bank_identifier = DataElementGroupField(type=BankIdentifier, required=False, _d="Von Kreditinstitutskennung")
    end_bank_identifier = DataElementGroupField(type=BankIdentifier, required=False, _d="Bis Kreditinstitutskennung")
    max_number_responses = DataElementField(type='num', max_length=4, required=False, _d="Maximale Anzahl Einträge")
    touchdown_point = DataElementField(type='an', max_length=35, required=False, _d="Aufsetzpunkt")


class HIKOM4(FinTS3Segment):
    """Kommunikationszugang rückmelden, version 4

    Source: FinTS Financial Transaction Services, Schnittstellenspezifikation, Formals"""
    bank_identifier = DataElementGroupField(type=BankIdentifier, _d="Kreditinstitutskennung")
    default_language = CodeField(enum=Language2, max_length=3, _d="Standardsprache")
    communication_parameters = DataElementGroupField(type=CommunicationParameter2, min_count=1, max_count=9, _d="Kommunikationsparameter")
