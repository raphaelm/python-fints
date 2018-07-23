from . import FinTS3Segment
import datetime

class HKCCS(FinTS3Segment):
    """
    HKCCS (SEPA Überweisung übertragen)
    Section C.2.1.2
    """
    type = 'HKCCS'

    def __init__(self, segno, account, arg):
        self.version = 1
        sepadescriptor = 'urn?:iso?:std?:iso?:20022?:tech?:xsd?:pain.001.001.03'
        painmsg = self.create_pain(account, arg)
        laenge = '@' + str(len(painmsg)) + '@'
        msg = ':'.join([
            account.iban,
            account.bic
        ])
        data = [
            msg,
            sepadescriptor,
            '@{}@{}'.format(len(painmsg), painmsg)
        ]
        super().__init__(segno, data)

    def create_pain(self, account, arg):
        pain = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        pain += '<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pain.001.001.03" ' \
                'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ' \
                'xsi:schemaLocation="urn:iso:std:iso:20022:tech:xsd:pain.001.001.03 pain.001.001.03.xsd">'
        pain += '<CstmrCdtTrfInitn>'
        pain += '<GrpHdr>'
        pain += '<MsgId>' + datetime.datetime.now().isoformat()[:-2] + '</MsgId>'
        pain += '<CreDtTm>' + datetime.datetime.now().replace(microsecond=0).isoformat() + '</CreDtTm>'
        pain += '<NbOfTxs>1</NbOfTxs>'
        pain += '<CtrlSum>' + arg['CtrlSum'] + '</CtrlSum>'
        pain += '<InitgPty><Nm>' + arg['Nm']+ '</Nm></InitgPty>'
        pain += '</GrpHdr>'
        pain += '<PmtInf>'
        pain += '<PmtInfId>' + datetime.datetime.now().isoformat()[:-2] + '</PmtInfId>'
        pain += '<PmtMtd>TRF</PmtMtd><NbOfTxs>1</NbOfTxs>'
        pain += '<CtrlSum>' + arg['CtrlSum'] + '</CtrlSum>'
        pain += '<PmtTpInf><SvcLvl><Cd>SEPA</Cd></SvcLvl></PmtTpInf>'
        pain += '<ReqdExctnDt>1999-01-01</ReqdExctnDt>'
        pain += '<Dbtr><Nm>' + arg['Nm'] + '</Nm></Dbtr>'
        pain += '<DbtrAcct><Id><IBAN>' + account.iban + '</IBAN></Id></DbtrAcct>'
        pain += '<DbtrAgt><FinInstnId><BIC>' + account.bic + '</BIC></FinInstnId></DbtrAgt>'
        pain += '<ChrgBr>SLEV</ChrgBr>'
        pain += '<CdtTrfTxInf>'
        pain += '<PmtId><EndToEndId>NOTPROVIDED</EndToEndId></PmtId>'
        pain += '<Amt><InstdAmt Ccy="EUR">' + arg['CtrlSum'] + '</InstdAmt></Amt>'
        pain += '<CdtrAgt><FinInstnId><BIC>' + arg['DbtrAgt'] + '</BIC></FinInstnId></CdtrAgt>'
        pain += '<Cdtr><Nm>' + arg['Nm'] + '</Nm></Cdtr>'
        pain += '<CdtrAcct><Id><IBAN>' + arg['DbtrAcct'] + '</IBAN></Id></CdtrAcct>'
        pain += '<RmtInf><Ustrd>' + arg['Ustrd'] + '</Ustrd></RmtInf>'
        pain += '</CdtTrfTxInf>'
        pain += '</PmtInf>'
        pain += '</CstmrCdtTrfInitn>'
        pain += '</Document>'

        return pain

class HKTAN(FinTS3Segment):
    """
    HKTAN (TAN-Verfahren festlegen)
    Section C.2.1.2
    """
    type = 'HKTAN'

    def __init__(self, segno, prozess, aref, medium):
        self.version = 3
        if prozess == 4:
            if medium == '':
                data = [
                    prozess
                ]
            else:
                data = [
                    prozess,'','','','','','','', medium
            ]
        else:
            data = [
                prozess,'', aref, '', 'N'
            ]
        super().__init__(segno, data)

class HKTAB(FinTS3Segment):
    """
    HKTAB (Verfügbarre TAN-Medien ermitteln)
    Section C.2.1.2
    """
    type = 'HKTAB'

    def __init__(self, segno):
        self.version = 4
        data = [
            '0','A'
        ]
        super().__init__(segno, data)
