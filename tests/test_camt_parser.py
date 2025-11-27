import datetime
import pprint
from decimal import Decimal

from fints.camt_parser import _modify_key, camt053_to_dict
from fints.models import Amount


def test_modify_key():
    assert _modify_key("BkTxCd.Domn.Cd") == "BankTransactionCode.Domain.Code"


data = b"""<?xml version="1.0" encoding="ISO-8859-1" ?>
<Document
	xmlns="urn:iso:std:iso:20022:tech:xsd:camt.052.001.08"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="urn:iso:std:iso:20022:tech:xsd:camt.052.001.08 camt.052.001.08.xsd">
	<BkToCstmrAcctRpt>
		<GrpHdr>
			<MsgId>52D20251127T1628589914030N000000000</MsgId>
			<CreDtTm>2025-11-27T16:28:58.0+01:00</CreDtTm>
		</GrpHdr>
		<Rpt>
			<Id>2316C522025112716285899</Id>
			<RptPgntn>
				<PgNb>1</PgNb>
				<LastPgInd>true</LastPgInd>
			</RptPgntn>
			<ElctrncSeqNb>000000000</ElctrncSeqNb>
			<CreDtTm>2025-11-27T16:28:58.0+01:00</CreDtTm>
			<Acct>
				<Id>
					<IBAN>DE1234567890</IBAN>
				</Id>
				<Ccy>EUR</Ccy>
				<Ownr>
					<Nm>Account owner</Nm>
				</Ownr>
				<Svcr>
					<FinInstnId>
						<BICFI>TRODDEF1XXX</BICFI>
						<Nm>Triodos Bank N.V. Deutschland</Nm>
						<Othr>
							<Id>DE 266286897</Id>
							<Issr>UmsStId</Issr>
						</Othr>
					</FinInstnId>
				</Svcr>
			</Acct>
			<Bal>
				<Tp>
					<CdOrPrtry>
						<Cd>OPBD</Cd>
					</CdOrPrtry>
				</Tp>
				<Amt Ccy="EUR">1234.56</Amt>
				<CdtDbtInd>CRDT</CdtDbtInd>
				<Dt>
					<Dt>2025-10-28</Dt>
				</Dt>
			</Bal>
			<Bal>
				<Tp>
					<CdOrPrtry>
						<Cd>CLBD</Cd>
					</CdOrPrtry>
				</Tp>
				<Amt Ccy="EUR">4567.89</Amt>
				<CdtDbtInd>CRDT</CdtDbtInd>
				<Dt>
					<Dt>2025-11-26</Dt>
				</Dt>
			</Bal>
			<Ntry>
				<Amt Ccy="EUR">35.00</Amt>
				<CdtDbtInd>CRDT</CdtDbtInd>
				<Sts>
					<Cd>BOOK</Cd>
				</Sts>
				<BookgDt>
					<Dt>2025-10-28</Dt>
				</BookgDt>
				<ValDt>
					<Dt>2025-10-28</Dt>
				</ValDt>
				<AcctSvcrRef>2025102812344060000</AcctSvcrRef>
				<BkTxCd>
					<Domn>
						<Cd>PMNT</Cd>
						<Fmly>
							<Cd>RRCT</Cd>
							<SubFmlyCd>ESCT</SubFmlyCd>
						</Fmly>
					</Domn>
					<Prtry>
						<Cd>NTRF+168+00931</Cd>
						<Issr>DK</Issr>
					</Prtry>
				</BkTxCd>
				<NtryDtls>
					<TxDtls>
						<Refs>
							<EndToEndId>NOTPROVIDED</EndToEndId>
						</Refs>
						<Amt Ccy="EUR">35.00</Amt>
						<BkTxCd>
							<Domn>
								<Cd>PMNT</Cd>
								<Fmly>
									<Cd>RRCT</Cd>
									<SubFmlyCd>ESCT</SubFmlyCd>
								</Fmly>
							</Domn>
							<Prtry>
								<Cd>NTRF+168+00931</Cd>
								<Issr>DK</Issr>
							</Prtry>
						</BkTxCd>
						<RltdPties>
							<Dbtr>
								<Pty>
									<Nm>Sender</Nm>
								</Pty>
							</Dbtr>
							<DbtrAcct>
								<Id>
									<IBAN>DE999999999</IBAN>
								</Id>
							</DbtrAcct>
							<Cdtr>
								<Pty>
									<Nm>Account owner</Nm>
								</Pty>
							</Cdtr>
							<CdtrAcct>
								<Id>
									<IBAN>DE1234567890</IBAN>
								</Id>
							</CdtrAcct>
						</RltdPties>
						<RltdAgts>
							<DbtrAgt>
								<FinInstnId>
									<BICFI>GENODEM1GLS</BICFI>
								</FinInstnId>
							</DbtrAgt>
						</RltdAgts>
						<RmtInf>
							<Ustrd>Reference</Ustrd>
						</RmtInf>
					</TxDtls>
				</NtryDtls>
				<AddtlNtryInf>\xdcberweisungsgutschr.</AddtlNtryInf>
			</Ntry>
			<Ntry>
				<Amt Ccy="EUR">29.63</Amt>
				<CdtDbtInd>DBIT</CdtDbtInd>
				<Sts>
					<Cd>BOOK</Cd>
				</Sts>
				<BookgDt>
					<Dt>2025-11-07</Dt>
				</BookgDt>
				<ValDt>
					<Dt>2025-11-07</Dt>
				</ValDt>
				<AcctSvcrRef>2025110701433815000</AcctSvcrRef>
				<BkTxCd>
					<Domn>
						<Cd>PMNT</Cd>
						<Fmly>
							<Cd>RDDT</Cd>
							<SubFmlyCd>ESDD</SubFmlyCd>
						</Fmly>
					</Domn>
					<Prtry>
						<Cd>NDDT+105+00931</Cd>
						<Issr>DK</Issr>
					</Prtry>
				</BkTxCd>
				<NtryDtls>
					<TxDtls>
						<Refs>
							<EndToEndId>SD36-1234-1234-1234</EndToEndId>
							<MndtId>1234-1234-1234</MndtId>
						</Refs>
						<Amt Ccy="EUR">29.63</Amt>
						<BkTxCd>
							<Domn>
								<Cd>PMNT</Cd>
								<Fmly>
									<Cd>RDDT</Cd>
									<SubFmlyCd>ESDD</SubFmlyCd>
								</Fmly>
							</Domn>
							<Prtry>
								<Cd>NDDT+105+00931</Cd>
								<Issr>DK</Issr>
							</Prtry>
						</BkTxCd>
						<RltdPties>
							<Dbtr>
								<Pty>
									<Nm>Account owner</Nm>
								</Pty>
							</Dbtr>
							<DbtrAcct>
								<Id>
									<IBAN>DE1234567890</IBAN>
								</Id>
							</DbtrAcct>
							<Cdtr>
								<Pty>
									<Nm>Supplier</Nm>
									<Id>
										<PrvtId>
											<Othr>
												<Id>NL1234567890</Id>
											</Othr>
										</PrvtId>
									</Id>
								</Pty>
							</Cdtr>
							<CdtrAcct>
								<Id>
									<IBAN>DE9999988888</IBAN>
								</Id>
							</CdtrAcct>
							<UltmtCdtr>
								<Pty>
									<Nm>Ultimate Supplier</Nm>
								</Pty>
							</UltmtCdtr>
						</RltdPties>
						<RltdAgts>
							<CdtrAgt>
								<FinInstnId>
									<BICFI>DEUTDEFFXXX</BICFI>
								</FinInstnId>
							</CdtrAgt>
						</RltdAgts>
						<RmtInf>
							<Ustrd>Foobar EREF: SD36-1234-1234-1234 MREF: 1234-12345-1234 CRED: </Ustrd>
							<Ustrd>DE00ZZZ123456789</Ustrd>
						</RmtInf>
					</TxDtls>
				</NtryDtls>
				<AddtlNtryInf>Lastschrift</AddtlNtryInf>
			</Ntry>
		</Rpt>
	</BkToCstmrAcctRpt>
</Document>"""


def test_parse():
    result = camt053_to_dict(data)

    expected = [{'AccountServicerReference': '2025102812344060000',
                 'AdditionalEntryInformation': 'Überweisungsgutschr.',
                 'Amount': '35.00',
                 'BankTransactionCode.Domain.Code': 'PMNT',
                 'BankTransactionCode.Domain.Family.Code': 'RRCT',
                 'BankTransactionCode.Domain.Family.SubFamilyCode': 'ESCT',
                 'BankTransactionCode.Proprietary.Code': 'NTRF+168+00931',
                 'BankTransactionCode.Proprietary.Issuer': 'DK',
                 'BookingDate.Date': '2025-10-28',
                 'CreditDebitIndicator': 'CRDT',
                 'EntryDetails.TransactionDetails.Amount': '35.00',
                 'EntryDetails.TransactionDetails.BankTransactionCode.Domain.Code': 'PMNT',
                 'EntryDetails.TransactionDetails.BankTransactionCode.Domain.Family.Code': 'RRCT',
                 'EntryDetails.TransactionDetails.BankTransactionCode.Domain.Family.SubFamilyCode': 'ESCT',
                 'EntryDetails.TransactionDetails.BankTransactionCode.Proprietary.Code': 'NTRF+168+00931',
                 'EntryDetails.TransactionDetails.BankTransactionCode.Proprietary.Issuer': 'DK',
                 'EntryDetails.TransactionDetails.References.EndToEndIdentification': 'NOTPROVIDED',
                 'EntryDetails.TransactionDetails.RelatedAgents.DebtorAgent.FinancialInstitutionIdentification.BICFI': 'GENODEM1GLS',
                 'EntryDetails.TransactionDetails.RelatedParties.Creditor.Party.Name': 'Account '
                                                                                       'owner',
                 'EntryDetails.TransactionDetails.RelatedParties.CreditorAccount.Identification.IBAN': 'DE1234567890',
                 'EntryDetails.TransactionDetails.RelatedParties.Debtor.Party.Name': 'Sender',
                 'EntryDetails.TransactionDetails.RelatedParties.DebtorAccount.Identification.IBAN': 'DE999999999',
                 'EntryDetails.TransactionDetails.RemittanceInformation.Unstructured': 'Reference',
                 'Status.Code': 'BOOK',
                 'ValueDate.Date': '2025-10-28',
                 'amount': Amount(amount=Decimal('35.00'), currency='EUR'),
                 'applicant_creditor_id': None,
                 'applicant_iban': 'DE999999999',
                 'applicant_name': 'Sender',
                 'bank_reference': '2025102812344060000',
                 'currency': 'EUR',
                 'date': datetime.date(2025, 10, 28),
                 'end_to_end_reference': 'NOTPROVIDED',
                 'entry_date': datetime.date(2025, 10, 28),
                 'guessed_entry_date': datetime.date(2025, 10, 28),
                 'id': 'NTRF',
                 'purpose': 'Reference',
                 'purpose_code': 'ESCT',
                 'recipient_name': 'Account owner',
                 'status': 'C'},
                {'AccountServicerReference': '2025110701433815000',
                 'AdditionalEntryInformation': 'Lastschrift',
                 'Amount': '29.63',
                 'BankTransactionCode.Domain.Code': 'PMNT',
                 'BankTransactionCode.Domain.Family.Code': 'RDDT',
                 'BankTransactionCode.Domain.Family.SubFamilyCode': 'ESDD',
                 'BankTransactionCode.Proprietary.Code': 'NDDT+105+00931',
                 'BankTransactionCode.Proprietary.Issuer': 'DK',
                 'BookingDate.Date': '2025-11-07',
                 'CreditDebitIndicator': 'DBIT',
                 'EntryDetails.TransactionDetails.Amount': '29.63',
                 'EntryDetails.TransactionDetails.BankTransactionCode.Domain.Code': 'PMNT',
                 'EntryDetails.TransactionDetails.BankTransactionCode.Domain.Family.Code': 'RDDT',
                 'EntryDetails.TransactionDetails.BankTransactionCode.Domain.Family.SubFamilyCode': 'ESDD',
                 'EntryDetails.TransactionDetails.BankTransactionCode.Proprietary.Code': 'NDDT+105+00931',
                 'EntryDetails.TransactionDetails.BankTransactionCode.Proprietary.Issuer': 'DK',
                 'EntryDetails.TransactionDetails.References.EndToEndIdentification': 'SD36-1234-1234-1234',
                 'EntryDetails.TransactionDetails.References.MandateIdentification': '1234-1234-1234',
                 'EntryDetails.TransactionDetails.RelatedAgents.CreditorAgent.FinancialInstitutionIdentification.BICFI': 'DEUTDEFFXXX',
                 'EntryDetails.TransactionDetails.RelatedParties.Creditor.Party.Identification.PrivateIdentification.Other.Identification': 'NL1234567890',
                 'EntryDetails.TransactionDetails.RelatedParties.Creditor.Party.Name': 'Supplier',
                 'EntryDetails.TransactionDetails.RelatedParties.CreditorAccount.Identification.IBAN': 'DE9999988888',
                 'EntryDetails.TransactionDetails.RelatedParties.Debtor.Party.Name': 'Account '
                                                                                     'owner',
                 'EntryDetails.TransactionDetails.RelatedParties.DebtorAccount.Identification.IBAN': 'DE1234567890',
                 'EntryDetails.TransactionDetails.RelatedParties.UltimateCreditor.Party.Name': 'Ultimate '
                                                                                               'Supplier',
                 'EntryDetails.TransactionDetails.RemittanceInformation.Unstructured': 'Foobar EREF: SD36-1234-1234-1234 MREF: 1234-12345-1234 CRED: DE00ZZZ123456789',
                 'Status.Code': 'BOOK',
                 'ValueDate.Date': '2025-11-07',
                 'amount': Amount(amount=Decimal('-29.63'), currency='EUR'),
                 'applicant_creditor_id': 'NL1234567890',
                 'applicant_iban': 'DE9999988888',
                 'applicant_name': 'Supplier',
                 'bank_reference': '2025110701433815000',
                 'currency': 'EUR',
                 'date': datetime.date(2025, 11, 7),
                 'end_to_end_reference': 'SD36-1234-1234-1234',
                 'entry_date': datetime.date(2025, 11, 7),
                 'guessed_entry_date': datetime.date(2025, 11, 7),
                 'id': 'NDDT',
                 'purpose': 'Foobar EREF: SD36-1234-1234-1234 MREF: 1234-12345-1234 CRED: DE00ZZZ123456789',
                 'purpose_code': 'ESDD',
                 'recipient_name': 'Account owner',
                 'status': 'D'}]
    assert result == expected
