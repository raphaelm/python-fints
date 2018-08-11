from enum import Enum
import random
import re

from .segments.message import HNHBK, HNHBS, HNSHA, HNSHK, HNVSD, HNVSK
from .parser import FinTS3Parser
from .formals import SegmentSequence
from .segments import ParameterSegment

class FinTSMessage:
    def __init__(self, blz, username, pin, systemid, dialogid, msgno, encrypted_segments, tan_mechs=None, tan=None):
        self.blz = blz
        self.username = username
        self.pin = pin
        self.tan = tan
        self.systemid = systemid
        self.dialogid = dialogid
        self.msgno = msgno
        self.segments = []
        self.encrypted_segments = []

        if tan_mechs and '999' not in [t.security_feature for t in tan_mechs]:
            self.profile_version = 2
            self.security_function = tan_mechs[0].security_feature
        else:
            self.profile_version = 1
            self.security_function = '999'

        sig_head = self.build_signature_head()
        enc_head = self.build_encryption_head()
        self.segments.append(enc_head)

        self.enc_envelop = HNVSD(999, '')
        self.segments.append(self.enc_envelop)

        self.append_enc_segment(sig_head)
        for s in encrypted_segments:
            self.append_enc_segment(s)

        cur_count = len(encrypted_segments) + 3

        sig_end = HNSHA(cur_count, self.secref, self.pin, self.tan)
        self.append_enc_segment(sig_end)
        self.segments.append(HNHBS(cur_count + 1, msgno))

    def append_enc_segment(self, seg):
        self.encrypted_segments.append(seg)
        self.enc_envelop.set_data(self.enc_envelop.encoded_data + str(seg))

    def build_signature_head(self):
        rand = random.SystemRandom()
        self.secref = rand.randint(1000000, 9999999)
        return HNSHK(2, self.secref, self.blz, self.username, self.systemid, self.profile_version,
                     self.security_function)

    def build_encryption_head(self):
        return HNVSK(998, self.blz, self.username, self.systemid, self.profile_version)

    def build_header(self):
        l = sum([len(str(s)) for s in self.segments])
        return HNHBK(l, self.dialogid, self.msgno)

    def __str__(self):
        return str(self.build_header()) + ''.join([str(s) for s in self.segments])


class FinTSResponse(SegmentSequence):
    def is_success(self):
        for seg in self.find_segments('HIRMG'):
            for response in seg.responses:
                if response.code.startswith('9'):
                    return False
        return True

    def get_dialog_id(self):
        seg = self.find_segment_first('HNHBK')
        if not seg:
            raise ValueError('Invalid response, no HNHBK segment')

        return seg.dialogue_id

    def get_bank_name(self):
        seg = self.find_segment_first('HIBPA')
        if seg:
            return seg.bank_name

    def get_systemid(self):
        seg = self.find_segment_first('HISYN')
        if not seg:
            raise ValueError('Could not find systemid')
        return seg.customer_system_id

    def get_hkkaz_max_version(self):
        return max((seg.header.version for seg in self.find_segments('HIKAZS')), default=3)

    def get_hksal_max_version(self):
        return max((seg.header.version for seg in self.find_segments('HISALS')), default=3)

    def get_supported_tan_mechanisms(self):
        tan_methods = []
        for seg in self.find_segments('HIRMS'):
            for response in seg.responses:
                if response.code == '3920':
                    tan_methods.extend( response.parameters )

        # Get parameters for tan methods
        methods = []
        for seg in self.find_segments('HITANS'):
            if not isinstance(seg, ParameterSegment):
                raise NotImplementedError(
                    "HITANS segment version {} is currently not implemented".format(
                        seg.header.version
                    )
                )

            if seg.parameters.twostep_parameters.security_function in tan_methods:
                methods.append(method)

        return methods

    def _find_segment_for_reference(self, name, ref):
        for seg in self.find_segments(name):
            if seg.header.reference == int(str(ref.segmentno)):
                return seg

    def get_touchdowns(self, msg: FinTSMessage):
        touchdown = {}
        for msgseg in msg.encrypted_segments:
            seg = self._find_segment_for_reference('HIRMS', msgseg)
            if seg:
                for p in seg[1:]:
                    if p[0] == "3040":
                        touchdown[msgseg.type] = p[3]
        return touchdown
