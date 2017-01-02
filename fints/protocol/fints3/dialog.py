import logging

from .segments.auth import HKIDN, HKSYN, HKVVB
from .message import FinTSMessage

logger = logging.getLogger(__name__)


class FinTSDialog:
    def __init__(self, blz, username, pin, systemid, connection):
        self.blz = blz
        self.username = username
        self.pin = pin
        self.systemid = systemid
        self.connection = connection
        self.msgno = 1
        self.dialogid = 0

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

    def send(self, msg):
        logger.info('Sending Message')
        msg.msgno = self.msgno
        msg.dialogid = self.dialogid

        try:
            resp = self.connection.send(msg)
            self.msgno += 1
            return resp
        except:
            # TODO: Error handlign
            raise
