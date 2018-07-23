import logging
import re
import datetime

from .connection import FinTSHTTPSConnection
from .dialog import FinTSDialog
from .message import FinTSMessage
from .models import SEPAAccount, TANMethod5, TANMethod6
from .segments.auth import HKTAN, HKTAB
from .segments.accounts import HKSPA
from .segments.statement import HKKAZ
from .segments.saldo import HKSAL
from .segments.depot import HKWPD
from .segments.transfer import HKCCS
from .message import FinTSResponse
from .utils import mt940_to_array, MT535_Miniparser, split_for_data_groups, split_for_data_elements, Password
from mt940.models import Balance

logger = logging.getLogger(__name__)


class FinTS3Client:
    version = 300

    def __init__(self):
        self.accounts = []

    def _new_dialog(self):
        raise NotImplemented()

    def _new_message(self, dialog: FinTSDialog, segments):
        raise NotImplemented()

    def get_sepa_accounts(self):
        dialog = self._new_dialog()
        dialog.sync()
        dialog.init()

        def _get_msg():
            return self._new_message(dialog, [
                HKSPA(3, None, None, None)
            ])

        with self.pin.protect():
            logger.debug('Sending HKSPA: {}'.format(_get_msg()))

        resp = dialog.send(_get_msg())
        logger.debug('Got HKSPA response: {}'.format(resp))
        dialog.end()

        accounts = resp._find_segment('HISPA')
        accountlist = accounts.split('+')[1:]
        self.accounts = []
        for acc in accountlist:
            arr = acc.split(':')
            self.accounts.append(SEPAAccount(
                iban=arr[1], bic=arr[2], accountnumber=arr[3], subaccount=arr[4], blz=arr[6]
            ))

        return self.accounts

    def get_statement(self, account, start_date, end_date):
        logger.info('Start fetching from {} to {}'.format(start_date, end_date))

        dialog = self._new_dialog()
        dialog.sync()
        dialog.init()

        def _get_msg():
            return self._create_statement_message(dialog, account, start_date, end_date, None)

        with self.pin.protect():
            logger.debug('Send message: {}'.format(_get_msg()))

        msg = _get_msg()
        resp = dialog.send(msg)
        touchdowns = resp.get_touchdowns(msg)
        responses = [resp]
        touchdown_counter = 1

        while HKKAZ.type in touchdowns:
            logger.info('Fetching more results ({})...'.format(touchdown_counter))

            with self.pin.protect():
                logger.debug('Send message: {}'.format(
                    self._create_statement_message(dialog, account, start_date, end_date, touchdowns[HKKAZ.type])
                ))

            msg = self._create_statement_message(dialog, account, start_date, end_date, touchdowns[HKKAZ.type])
            resp = dialog.send(msg)
            responses.append(resp)
            touchdowns = resp.get_touchdowns(msg)

            touchdown_counter += 1

        logger.info('Fetching done.')

        re_data = re.compile(r'[^@]*@([0-9]+)@(.+)', flags=re.MULTILINE | re.DOTALL)
        statement = []
        for resp in responses:
            seg = resp._find_segment('HIKAZ')
            if seg:
                m = re_data.match(seg)
                if m:
                    statement += mt940_to_array(m.group(2))

        logger.debug('Statement: {}'.format(statement))

        dialog.end()
        return statement

    def _create_statement_message(self, dialog: FinTSDialog, account: SEPAAccount, start_date, end_date, touchdown):
        hversion = dialog.hkkazversion

        if hversion in (4, 5, 6):
            acc = ':'.join([
                account.accountnumber, account.subaccount, str(280), account.blz
            ])
        elif hversion == 7:
            acc = ':'.join([
                account.iban, account.bic, account.accountnumber, account.subaccount, str(280), account.blz
            ])
        else:
            raise ValueError('Unsupported HKKAZ version {}'.format(hversion))

        return self._new_message(dialog, [
            HKKAZ(
                3,
                hversion,
                acc,
                start_date,
                end_date,
                touchdown
            )
        ])

    def get_balance(self, account):
        # init dialog
        dialog = self._new_dialog()
        dialog.sync()
        dialog.init()

        # execute job
        def _get_msg():
            return self._create_balance_message(dialog, account)

        with self.pin.protect():
            logger.debug('Sending HKSAL: {}'.format(_get_msg()))

        resp = dialog.send(_get_msg())
        logger.debug('Got HKSAL response: {}'.format(resp))

        # end dialog
        dialog.end()

        # find segment and split up to balance part
        seg = resp._find_segment('HISAL')
        arr = split_for_data_elements(split_for_data_groups(seg)[4])

        # get balance date
        date = datetime.datetime.strptime(arr[3], "%Y%m%d").date()

        # return balance
        return Balance(arr[0], arr[1], date, currency=arr[2])

    def _create_balance_message(self, dialog: FinTSDialog, account: SEPAAccount):
        hversion = dialog.hksalversion

        if hversion in (1, 2, 3, 4, 5, 6):
            acc = ':'.join([
                account.accountnumber, account.subaccount, str(280), account.blz
            ])
        elif hversion == 7:
            acc = ':'.join([
                account.iban, account.bic, account.accountnumber, account.subaccount, str(280), account.blz
            ])
        else:
            raise ValueError('Unsupported HKSAL version {}'.format(hversion))

        return self._new_message(dialog, [
            HKSAL(
                3,
                hversion,
                acc
            )
        ])

    def get_holdings(self, account):
        # init dialog
        dialog = self._new_dialog()
        dialog.sync()
        dialog.init()

        # execute job
        def _get_msg():
            return self._create_get_holdings_message(dialog, account)

        with self.pin.protect():
            logger.debug('Sending HKWPD: {}'.format(_get_msg()))

        resp = dialog.send(_get_msg())
        logger.debug('Got HIWPD response: {}'.format(resp))

        # end dialog
        dialog.end()

        # find segment and split up to balance part
        seg = resp._find_segment('HIWPD')
        if seg:
            mt535_lines = str.splitlines(seg)
            # The first line contains a FinTS HIWPD header - drop it.
            del mt535_lines[0]
            mt535 = MT535_Miniparser()
            return mt535.parse(mt535_lines)
        else:
            logger.debug('No HIWPD response segment found - maybe account has no holdings?')
            return []

    def _create_get_holdings_message(self, dialog: FinTSDialog, account: SEPAAccount):
        hversion = dialog.hksalversion

        if hversion in (1, 2, 3, 4, 5, 6):
            acc = ':'.join([
                account.accountnumber, account.subaccount, str(280), account.blz
            ])
        elif hversion == 7:
            acc = ':'.join([
                account.iban, account.bic, account.accountnumber, account.subaccount, str(280), account.blz
            ])
        else:
            raise ValueError('Unsupported HKSAL version {}'.format(hversion))

        return self._new_message(dialog, [
            HKWPD(
                3,
                hversion,
                acc,
            )
        ])

    def send_tan(self, arg):
        data = str(arg['response'])

        res = FinTSResponse(data)
        seg = res._find_segment('HITAN')
        seg = split_for_data_groups(seg)
        aref = seg[3]
        segTAN = HKTAN(3, 2, aref, '')

        self.blz = arg['dialog'].blz
        self.username = arg['dialog'].username
        self.pin = arg['dialog'].pin
        self.systemid = arg['dialog'].systemid
        self.dialogid = arg['dialog'].dialogid
        self.msgno = arg['dialog'].msgno
        self.tan_mechs = []
        self.tan_mechs = [arg['TAN-Verfahren']]
        self.pintan = ':'.join([self.pin, arg['tan']])
        msg = FinTSMessage(self.blz, self.username, self.pintan, self.systemid, self.dialogid, self.msgno, [
            segTAN
        ], self.tan_mechs)

        res = arg['dialog'].send(msg)
        arg['dialog'].end()

        return 'Ok'

    def create_sepa_transfer(self, account, arg):
        # Diese Funktion erstellt eine neue SEPA-Überweisung
        self.tan_bezeichnung = arg['TAN-Bezeichnung']
        dialog = self._new_dialog()
        dialog.sync()

        # TAN-Verfahren für Dialoginitialisierung ändern
        dialog.tan_mechs = [arg['TAN-Verfahren']]

        dialog.init()

        def _get_msg():
            segHKCCS = HKCCS(3, account, arg)
            segHKTAN = HKTAN(4, 4, '', self.tan_bezeichnung)
            return self._new_message(dialog, [
                segHKCCS,
                segHKTAN
            ])

        with self.pin.protect():
            logger.debug('Sending HKCCS: {}'.format(_get_msg()))

        resp = dialog.send(_get_msg())
        logger.debug('Got HKCCS response: {}'.format(resp))

        response = {}
        response['response'] = resp
        response['dialog'] = dialog

        return response

    def get_tan_methods(self):
        dialog = self._new_dialog()
        dialog.init()

        # Get tan methods
        res = FinTSResponse(str(dialog.bpd))
        seg = res._find_segment('HIRMS')
        deg = split_for_data_groups(seg)
        tan_methods = []
        for de in deg:
            if de[0:4] == '3920':
                d = split_for_data_elements(de)
                for i in range(3, len(d)):
                    tan_methods.append(d[i])

        # Get parameters for tan methods
        seg = res._find_segments('HITANS')
        methods = []
        for s in seg:
            spl = split_for_data_elements(s)
            if spl[2] == '5':
                model = TANMethod5
            elif spl[2] == '6':
                model = TANMethod6
            else:
                raise NotImplementedError(
                    "HITANS segment version {} is currently not implemented".format(
                        spl[2]
                    )
                )

            step = len(model._fields)
            for i in range(len(spl) // step):
                part = spl[6 + i * step:6 + (i + 1) * step]
                method = model(*part)
                if method.security_feature in tan_methods:
                    methods.append(method)

        return methods

    def get_tan_description(self):
        dialog = self._new_dialog()
        dialog.sync()
        dialog.init()

        def _get_msg():
            return self._new_message(dialog, [
                HKTAB(3)
            ])

        with self.pin.protect():
            logger.debug('Sending HKTAB: {}'.format(_get_msg()))

        resp = dialog.send(_get_msg())
        logger.debug('Got HKTAB response: {}'.format(resp))
        dialog.end()

        seg = resp._find_segment('HITAB')
        deg = split_for_data_groups(seg)

        return deg[2]


class FinTS3PinTanClient(FinTS3Client):

    def __init__(self, blz, username, pin, server):
        self.username = username
        self.blz = blz
        self.pin = Password(pin)
        self.connection = FinTSHTTPSConnection(server)
        self.systemid = 0
        super().__init__()

    def _new_dialog(self):
        dialog = FinTSDialog(self.blz, self.username, self.pin, self.systemid, self.connection)
        return dialog

    def _new_message(self, dialog: FinTSDialog, segments):
        return FinTSMessage(self.blz, self.username, self.pin, dialog.systemid, dialog.dialogid, dialog.msgno,
                            segments, dialog.tan_mechs)
