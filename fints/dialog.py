import logging

from .formals import (
    BankIdentifier, Language2, SynchronisationMode, SystemIDStatus,
)
from .message import (
    FinTSCustomerMessage, FinTSMessage, FinTSMessageOLD, MessageDirection,
)
from .segments.auth import HKIDN, HKIDN2, HKSYN, HKVVB, HKVVB3
from .segments.dialog import HKEND, HKEND1
from .segments.message import HNHBK3, HNHBS1

logger = logging.getLogger(__name__)

DIALOGUE_ID_UNASSIGNED = '0'

class FinTSDialogError(Exception):
    pass


class FinTSDialog:
    def __init__(self, client=None, lazy_init=False, enc_mechanism=None, auth_mechanisms=[]):
        self.client = client
        self.next_message_number = dict((v, 1) for v in  MessageDirection)
        self.messages = dict((v, {}) for v in MessageDirection)
        self.auth_mechanisms = auth_mechanisms
        self.enc_mechanism = enc_mechanism
        self.open = False
        self.need_init = True
        self.lazy_init = lazy_init
        self.dialogue_id = DIALOGUE_ID_UNASSIGNED

    def __enter__(self):
        if not self.lazy_init:
            self.init()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.end()

    def init(self, *extra_segments):
        if self.need_init and not self.open:
            segments = [
                HKIDN2(
                    self.client.bank_identifier,
                    self.client.customer_id,
                    self.client.system_id,
                    SystemIDStatus.ID_NECESSARY
                ),
                HKVVB3(
                    self.client.bpd_version,
                    self.client.upd_version,
                    Language2.DE,
                    self.client.product_name,
                    self.client.product_version
                )
            ]
            for s in extra_segments:
                segments.append(s)

            try:
                self.open = True
                retval = self.send(*segments)
                self.need_init = False
                return retval
            except:
                self.open = False
                raise
            finally:
                self.lazy_init = False

    def end(self):
        if self.open:
            self.send(HKEND1(self.dialogue_id))
            self.open = False

    def send(self, *segments):
        if not self.open:
            if self.lazy_init and self.need_init:
                self.init()

        if not self.open:
            raise Exception("Cannot send on dialog that is not open")

        message = self.new_customer_message()
        for s in segments:
            message += s
        self.finish_message(message)

        assert message.segments[0].message_number == self.next_message_number[message.DIRECTION]
        self.messages[message.segments[0].message_number] = message
        self.next_message_number[message.DIRECTION] += 1

        response = self.client.connection.send(message)

        ##assert response.segments[0].message_number == self.next_message_number[response.DIRECTION]
        # FIXME Better handling of HKEND in exception case
        self.messages[response.segments[0].message_number] = message
        self.next_message_number[response.DIRECTION] += 1

        if self.enc_mechanism:
            self.enc_mechanism.decrypt(message)

        for auth_mech in self.auth_mechanisms:
            auth_mech.verify(message)

        if self.dialogue_id == DIALOGUE_ID_UNASSIGNED:
            seg = response.find_segment_first(HNHBK3)
            if not seg:
                raise ValueError('Could not find dialogue_id')
            self.dialogue_id = seg.dialogue_id

        self.client.process_institute_response(response)

        return response

    def new_customer_message(self):
        message = FinTSCustomerMessage(self)
        message += HNHBK3(0, 300, self.dialogue_id, self.next_message_number[message.DIRECTION])
        
        for auth_mech in self.auth_mechanisms:
            auth_mech.sign_prepare(message)
        
        return message

    def finish_message(self, message):
        # Create signature(s) in reverse order: from inner to outer
        for auth_mech in reversed(self.auth_mechanisms):
            auth_mech.sign_commit(message)

        message += HNHBS1(message.segments[0].message_number)

        if self.enc_mechanism:
            self.enc_mechanism.encrypt(message)

        message.segments[0].message_size = len(message.render_bytes())


class FinTSDialogOLD:
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

    def _get_msg_sync(self):
        seg_identification = HKIDN(3, self.blz, self.username, 0)
        seg_prepare = HKVVB(4)
        seg_sync = HKSYN(5)

        return FinTSMessageOLD(self.blz, self.username, self.pin, self.systemid, self.dialogid, self.msgno, [
            seg_identification,
            seg_prepare,
            seg_sync
        ])

    def _get_msg_init(self):
        seg_identification = HKIDN(3, self.blz, self.username, self.systemid)
        seg_prepare = HKVVB(4)

        return FinTSMessageOLD(self.blz, self.username, self.pin, self.systemid, self.dialogid, self.msgno, [
            seg_identification,
            seg_prepare,
        ], self.tan_mechs)

    def _get_msg_end(self):
        return FinTSMessageOLD(self.blz, self.username, self.pin, self.systemid, self.dialogid, self.msgno, [
            HKEND(3, self.dialogid)
        ])

    def sync(self):
        logger.info('Initialize SYNC')

        with self.pin.protect():
            logger.debug('Sending SYNC: {}'.format(self._get_msg_sync()))

        resp = self.send(self._get_msg_sync())
        logger.debug('Got SYNC response: {}'.format(resp))
        self.systemid = resp.get_systemid()
        self.dialogid = resp.get_dialog_id()
        self.bankname = resp.get_bank_name()
        self.hksalversion = resp.get_segment_max_version('HIKAZS')
        self.hkkazversion = resp.get_segment_max_version('HISALS')
        self.hktanversion = resp.get_segment_max_version('HKTAN')
        self.tan_mechs = resp.get_supported_tan_mechanisms()

        logger.debug('Bank name: {}'.format(self.bankname))
        logger.debug('System ID: {}'.format(self.systemid))
        logger.debug('Dialog ID: {}'.format(self.dialogid))
        logger.debug('HKKAZ max version: {}'.format(self.hkkazversion))
        logger.debug('HKSAL max version: {}'.format(self.hksalversion))
        logger.debug('HKTAN max version: {}'.format(self.hktanversion))
        logger.debug('TAN mechanisms: {}'.format(', '.join(str(t) for t in self.tan_mechs)))
        self.end()

    def init(self):
        logger.info('Initialize Dialog')

        with self.pin.protect():
            logger.debug('Sending INIT: {}'.format(self._get_msg_init()))

        res = self.send(self._get_msg_init())
        logger.debug('Got INIT response: {}'.format(res))

        self.dialogid = res.get_dialog_id()
        logger.info('Received dialog ID: {}'.format(self.dialogid))

        return self.dialogid

    def end(self):
        logger.info('Initialize END')

        with self.pin.protect():
            logger.debug('Sending END: {}'.format(self._get_msg_end()))

        resp = self.send(self._get_msg_end())
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
            resp = self.connection.send(msg)
            if not resp.is_success():
                raise FinTSDialogError(
                    resp.get_summary_by_segment()
                )
            self.msgno += 1
            return resp
        except:
            # TODO: Error handling
            raise
