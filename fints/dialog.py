import logging

from .message import FinTSMessage, FinTSResponse
from .segments.auth import HKIDN, HKSYN, HKVVB
from .segments.dialog import HKEND

logger = logging.getLogger(__name__)


class FinTSDialogError(Exception):
    pass


class FinTSDialog:
    def __init__(self, blz, username, pin, systemid, connection):
        self.blz = blz
        self.username = username
        self.pin = pin
        self.systemid = systemid
        self.connection = connection
        self.msgno = 1
        self.dialogid = 0
        self.hksalversion = 6
        self.hkkazversion = 6
        self.tan_mechs = []

    def sync(self):
        logger.info('Initialize SYNC')

        seg_identification = HKIDN(3, self.blz, self.username, 0)
        seg_prepare = HKVVB(4)
        seg_sync = HKSYN(5)

        msg_sync = FinTSMessage(self.blz, self.username, self.pin, self.systemid, self.dialogid, self.msgno, [
            seg_identification,
            seg_prepare,
            seg_sync
        ])

        logger.debug('Sending SYNC: {}'.format(msg_sync))
        resp = self.send(msg_sync)
        logger.debug('Got SYNC response: {}'.format(resp))
        self.systemid = resp.get_systemid()
        self.dialogid = resp.get_dialog_id()
        self.bankname = resp.get_bank_name()
        self.hksalversion = resp.get_hksal_max_version()
        self.hkkazversion = resp.get_hkkaz_max_version()
        self.tan_mechs = resp.get_supported_tan_mechanisms()

        logger.debug('Bank name: {}'.format(self.bankname))
        logger.debug('System ID: {}'.format(self.systemid))
        logger.debug('Dialog ID: {}'.format(self.dialogid))
        logger.debug('HKKAZ max version: {}'.format(self.hkkazversion))
        logger.debug('HKSAL max version: {}'.format(self.hksalversion))
        logger.debug('TAN mechanisms: {}'.format(', '.join(self.tan_mechs)))
        self.end()

    def init(self):
        logger.info('Initialize Dialog')

        seg_identification = HKIDN(3, self.blz, self.username, self.systemid)
        seg_prepare = HKVVB(4)

        msg_init = FinTSMessage(self.blz, self.username, self.pin, self.systemid, self.dialogid, self.msgno, [
            seg_identification,
            seg_prepare,
        ], self.tan_mechs)
        logger.debug('Sending INIT: {}'.format(msg_init))
        resp = self.send(msg_init)
        logger.debug('Got INIT response: {}'.format(resp))

        self.dialogid = resp.get_dialog_id()
        logger.info('Received dialog ID: {}'.format(self.dialogid))

        return self.dialogid

    def end(self):
        logger.info('Initialize END')

        msg_end = FinTSMessage(self.blz, self.username, self.pin, self.systemid, self.dialogid, self.msgno, [
            HKEND(3, self.dialogid)
        ])
        logger.debug('Sending END: {}'.format(msg_end))
        resp = self.send(msg_end)
        logger.debug('Got END response: {}'.format(resp))
        logger.info('Resetting dialog ID and message number count')
        self.dialogid = 0
        self.msgno = 1
        return resp

    def send(self, msg):
        logger.info('Sending Message')
        msg.msgno = self.msgno
        msg.dialogid = self.dialogid

        try:
            resp = FinTSResponse(self.connection.send(msg))
            if not resp.is_success():
                raise FinTSDialogError(resp.get_summary_by_segment('HIRMG'))
            self.msgno += 1
            return resp
        except:
            # TODO: Error handling
            raise
