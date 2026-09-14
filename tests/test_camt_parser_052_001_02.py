import datetime
from decimal import Decimal

from fints.camt_parser import _join_repeated, camt053_to_dict
from fints.models import Amount

# Modelled on what ING (camt.052.001.02) returns: no Pty wrapper around
# party names, and the remittance information split into one Ustrd per
# field rather than one per 35 characters.
data = b"""<?xml version="1.0" encoding="UTF-8"?>
<Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.052.001.02">
	<BkToCstmrAcctRpt>
		<GrpHdr>
			<MsgId>1</MsgId>
			<CreDtTm>2026-01-15T12:00:00+01:00</CreDtTm>
		</GrpHdr>
		<Rpt>
			<Id>1</Id>
			<CreDtTm>2026-01-15T12:00:00+01:00</CreDtTm>
			<Acct>
				<Id><IBAN>DE02120300000000202051</IBAN></Id>
				<Ccy>EUR</Ccy>
			</Acct>
			<Ntry>
				<Amt Ccy="EUR">30.95</Amt>
				<CdtDbtInd>DBIT</CdtDbtInd>
				<Sts>BOOK</Sts>
				<BookgDt><Dt>2026-01-14</Dt></BookgDt>
				<ValDt><Dt>2026-01-14</Dt></ValDt>
				<NtryDtls>
					<TxDtls>
						<RltdPties>
							<Cdtr>
								<Nm>VISA SUPERMARKT MUSTERSTADT </Nm>
							</Cdtr>
						</RltdPties>
						<RmtInf>
							<Ustrd>NR XXXX 1234 MUSTERSTADT DE</Ustrd>
							<Ustrd>KAUFUMSATZ</Ustrd>
							<Ustrd>12.01 30.95</Ustrd>
							<Ustrd>123456</Ustrd>
							<Ustrd>ARN00000000000000000000000</Ustrd>
						</RmtInf>
					</TxDtls>
				</NtryDtls>
				<AddtlNtryInf>Lastschrifteinzug</AddtlNtryInf>
			</Ntry>
			<Ntry>
				<Amt Ccy="EUR">22.00</Amt>
				<CdtDbtInd>CRDT</CdtDbtInd>
				<Sts>BOOK</Sts>
				<BookgDt><Dt>2026-01-12</Dt></BookgDt>
				<ValDt><Dt>2026-01-12</Dt></ValDt>
				<NtryDtls>
					<TxDtls>
						<RltdPties>
							<Dbtr>
								<Nm>Erika Musterfrau</Nm>
							</Dbtr>
							<DbtrAcct>
								<Id><IBAN>DE02500105170137075030</IBAN></Id>
							</DbtrAcct>
						</RltdPties>
						<RmtInf>
							<Ustrd>Taschengeld Januar</Ustrd>
						</RmtInf>
					</TxDtls>
				</NtryDtls>
				<AddtlNtryInf>Gutschrift</AddtlNtryInf>
			</Ntry>
		</Rpt>
	</BkToCstmrAcctRpt>
</Document>
"""


def test_join_repeated():
    # Fields on separate lines get a space between them.
    assert _join_repeated("NR XXXX 1234 MUSTERSTADT DE", "KAUFUMSATZ") == "NR XXXX 1234 MUSTERSTADT DE KAUFUMSATZ"
    # A chunk that already ends in whitespace is left alone.
    assert _join_repeated("CRED: ", "DE00ZZZ123456789") == "CRED: DE00ZZZ123456789"
    assert _join_repeated("CRED:", " DE00ZZZ123456789") == "CRED: DE00ZZZ123456789"
    # Missing text does not raise and adds nothing.
    assert _join_repeated("abc", None) == "abc"
    assert _join_repeated(None, "abc") == "abc"


def test_parse_without_party_wrapper():
    debit, credit = camt053_to_dict(data)

    assert debit["amount"] == Amount(Decimal("-30.95"), "EUR")
    assert debit["applicant_name"] == "VISA SUPERMARKT MUSTERSTADT "
    assert debit["purpose"] == "NR XXXX 1234 MUSTERSTADT DE KAUFUMSATZ 12.01 30.95 123456 ARN00000000000000000000000"
    assert debit["AdditionalEntryInformation"] == "Lastschrifteinzug"
    assert debit["entry_date"] == datetime.date(2026, 1, 14)

    assert credit["amount"] == Amount(Decimal("22.00"), "EUR")
    assert credit["applicant_name"] == "Erika Musterfrau"
    assert credit["applicant_iban"] == "DE02500105170137075030"
    assert credit["purpose"] == "Taschengeld Januar"
    assert credit["AdditionalEntryInformation"] == "Gutschrift"
