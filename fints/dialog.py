import io
import logging
import pickle

from .connection import FinTSConnectionError
from .exceptions import *
from .formals import CUSTOMER_ID_ANONYMOUS, Language2, SystemIDStatus
from .message import FinTSCustomerMessage, MessageDirection
from .segments.auth import HKIDN2, HKVVB3
from .segments.dialog import HKEND1
from .segments.message import HNHBK3, HNHBS1
from .utils import compress_datablob, decompress_datablob

logger = logging.getLogger(__name__)

DIALOG_ID_UNASSIGNED = '0'
DATA_BLOB_MAGIC = b'python-fints_DIALOG_DATABLOB'


class FinTSDialog:
    def __init__(self, client=None, lazy_init=False, enc_mechanism=None, auth_mechanisms=None):
        self.client = client
        self.next_message_number = dict((v, 1) for v in MessageDirection)
        self.messages = dict((v, {}) for v in MessageDirection)
        self.auth_mechanisms = auth_mechanisms or []
        self.enc_mechanism = enc_mechanism
        self.open = False
        self.need_init = True
        self.lazy_init = lazy_init
        self.dialog_id = DIALOG_ID_UNASSIGNED
        self.paused = False
        self._context_count = 0

    def __enter__(self):
        if self._context_count == 0:
            if not self.lazy_init:
                self.init()
        self._context_count += 1
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self._context_count -= 1
        if not self.paused:
            if self._context_count == 0:
                self.end()

    def init(self, *extra_segments):
        if self.paused:
            raise FinTSDialogStateError("Cannot init() a paused dialog")

        if self.need_init and not self.open:
            segments = [
                HKIDN2(
                    self.client.bank_identifier,
                    self.client.customer_id,
                    self.client.system_id,
                    SystemIDStatus.ID_NECESSARY if self.client.customer_id != CUSTOMER_ID_ANONYMOUS else SystemIDStatus.ID_UNNECESSARY
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
                retval = self.send(*segments, internal_send=True)
                self.need_init = False
                return retval
            except Exception as e:
                self.open = False
                if isinstance(e, (FinTSConnectionError, FinTSClientError)):
                    raise
                else:
                    raise FinTSDialogInitError("Couldn't establish dialog with bank, Authentication data wrong?") from e
            finally:
                self.lazy_init = False

    def end(self):
        if self.paused:
            raise FinTSDialogStateError("Cannot end() on a paused dialog")

        if self.open:
            response = self.send(HKEND1(self.dialog_id), internal_send=True)
            self.open = False

    def send(self, *segments, **kwargs):
        internal_send = kwargs.pop('internal_send', False)

        if self.paused:
            raise FinTSDialogStateError("Cannot send() on a paused dialog")

        if not self.open:
            if self.lazy_init and self.need_init:
                self.init()

        if not self.open:
            raise FinTSDialogStateError("Cannot send on dialog that is not open")

        message = self.new_customer_message()
        for s in segments:
            message += s
        self.finish_message(message)

        assert message.segments[0].message_number == self.next_message_number[message.DIRECTION]
        self.messages[message.DIRECTION][message.segments[0].message_number] = message
        self.next_message_number[message.DIRECTION] += 1

        response = self.client.connection.send(message)

        # assert response.segments[0].message_number == self.next_message_number[response.DIRECTION]
        # FIXME Better handling of HKEND in exception case
        self.messages[response.DIRECTION][response.segments[0].message_number] = response
        self.next_message_number[response.DIRECTION] += 1

        if self.enc_mechanism:
            self.enc_mechanism.decrypt(message)

        for auth_mech in self.auth_mechanisms:
            auth_mech.verify(message)

        if self.dialog_id == DIALOG_ID_UNASSIGNED:
            seg = response.find_segment_first(HNHBK3)
            if not seg:
                raise FinTSDialogError('Could not find dialog_id')
            self.dialog_id = seg.dialog_id

        self.client.process_response_message(self, response, internal_send=internal_send)

        return response

    def new_customer_message(self):
        if self.paused:
            raise FinTSDialogStateError("Cannot call new_customer_message() on a paused dialog")

        message = FinTSCustomerMessage(self)
        message += HNHBK3(0, 300, self.dialog_id, self.next_message_number[message.DIRECTION])
        
        for auth_mech in self.auth_mechanisms:
            auth_mech.sign_prepare(message)
        
        return message

    def finish_message(self, message):
        if self.paused:
            raise FinTSDialogStateError("Cannot call finish_message() on a paused dialog")

        # Create signature(s) in reverse order: from inner to outer
        for auth_mech in reversed(self.auth_mechanisms):
            auth_mech.sign_commit(message)

        message += HNHBS1(message.segments[0].message_number)

        if self.enc_mechanism:
            self.enc_mechanism.encrypt(message)

        message.segments[0].message_size = len(message.render_bytes())

    def pause(self):
        # FIXME Document, test
        if self.paused:
            raise FinTSDialogStateError("Cannot pause a paused dialog")

        external_dialog = self
        external_client = self.client

        class SmartPickler(pickle.Pickler):
            def persistent_id(self, obj):
                if obj is external_dialog:
                    return "dialog"
                if obj is external_client:
                    return "client"
                return None

        pickle_out = io.BytesIO()
        SmartPickler(pickle_out, protocol=4).dump({
            k: getattr(self, k) for k in [
                'next_message_number',
                'messages',
                'auth_mechanisms',
                'enc_mechanism',
                'open',
                'need_init',
                'lazy_init',
                'dialog_id',
            ]
        })

        data_pickled = pickle_out.getvalue()

        self.paused = True

        return compress_datablob(DATA_BLOB_MAGIC, 1, {'data_bin': data_pickled})

    @classmethod
    def create_resume(cls, client, blob):
        retval = cls(client=client)
        decompress_datablob(DATA_BLOB_MAGIC, blob, retval)
        return retval

    def _set_data_v1(self, data):
        external_dialog = self
        external_client = self.client

        class SmartUnpickler(pickle.Unpickler):
            def persistent_load(self, pid):
                if pid == 'dialog':
                    return external_dialog
                if pid == 'client':
                    return external_client
                raise pickle.UnpicklingError("unsupported persistent object")

        pickle_in = io.BytesIO(data['data_bin'])
        data_unpickled = SmartUnpickler(pickle_in).load()

        for k, v in data_unpickled.items():
            setattr(self, k, v)
