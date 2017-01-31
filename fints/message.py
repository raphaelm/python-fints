import random
import re

from .segments.message import HNHBK, HNHBS, HNSHA, HNSHK, HNVSD, HNVSK


class FinTSMessage:
    def __init__(self, blz, username, pin, systemid, dialogid, msgno, encrypted_segments, tan_mechs=None):
        self.blz = blz
        self.username = username
        self.pin = pin
        self.systemid = systemid
        self.dialogid = dialogid
        self.msgno = msgno
        self.segments = []
        self.encrypted_segments = []

        if tan_mechs and '999' not in tan_mechs:
            self.profile_version = 2
            self.security_function = tan_mechs[0]
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

        sig_end = HNSHA(cur_count, self.secref, self.pin)
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


class FinTSResponse:
    RE_UNWRAP = re.compile('HNVSD:\d+:\d+\+@\d+@(.+)\'\'')
    RE_SEGMENTS = re.compile("'(?=[A-Z]{4,}:\d|')")
    RE_SYSTEMID = re.compile("HISYN:\d+:\d+:\d+\+(.+)")
    RE_TANMECH = re.compile('\d{3}')

    def __init__(self, data):
        self.response = self._unwrap(data)
        self.segments = self.RE_SEGMENTS.split(data)

    def __str__(self):
        return self.response

    def _unwrap(self, data):
        m = self.RE_UNWRAP.match(data)
        if m:
            return m.group(1)
        else:
            return data

    def is_success(self):
        summary = self.get_summary_by_segment('HIRMG')
        for code, msg in summary.items():
            if code[0] == "9":
                return False
        return True

    def _get_segment_index(self, idx, seg):
        seg = seg.split('+')
        if len(seg) > idx - 1:
            return seg[idx - 1]
        return None

    def get_dialog_id(self):
        seg = self._find_segment('HNHBK')
        if not seg:
            raise ValueError('Invalid response, no HNHBK segment')

        return self._get_segment_index(4, seg)

    def get_bank_name(self):
        seg = self._find_segment('HIBPA')
        if seg:
            seg = seg.split('+')
            if len(seg) > 3:
                return seg[3]

    def get_systemid(self):
        seg = self._find_segment('HISYN')
        m = self.RE_SYSTEMID.match(seg)
        if not m:
            raise ValueError('Could not find systemid')
        return m.group(1)

    def get_summary_by_segment(self, name):
        if name not in ('HIRMS', 'HIRMG'):
            raise ValueError('Unsupported segment for message summary')

        res = {}
        seg = self._find_segment(name)
        seg = seg.split('+')[1:]
        for de in seg:
            de = de.split(':')
            res[de[0]] = de[2]
        return res

    def get_hkkaz_max_version(self):
        return self._get_segment_max_version('HIKAZS')

    def get_hksal_max_version(self):
        return self._get_segment_max_version('HISALS')

    def get_supported_tan_mechanisms(self):
        segs = self._find_segments('HIRMS')
        for s in segs:
            seg = s.split('+')[1:]
            for s in seg:
                id, msg = s.split('::', 1)
                if id == "3920":
                    m = self.RE_TANMECH.search(msg)
                    if m:
                        return [m.group(0)]
        return False

    def _find_segment_for_reference(self, name, ref):
        segs = self._find_segments(name)
        for seg in segs:
            segsplit = seg.split('+')[0].split(':')
            if segsplit[3] == str(ref.segmentno):
                return seg

    def get_touchdowns(self, msg: FinTSMessage):
        touchdown = {}
        for msgseg in msg.encrypted_segments:
            seg = self._find_segment_for_reference('HIRMS', msgseg)
            if seg:
                parts = seg.split('+')[1:]
                for p in parts:
                    psplit = p.split(':')
                    if psplit[0] == "3040":
                        td = psplit[3]
                        touchdown[msgseg.type] = td
        return touchdown

    def _get_segment_max_version(self, name):
        v = 3
        segs = self._find_segments(name)
        for s in segs:
            parts = s.split('+')
            segheader = parts[0].split(':')
            curver = int(segheader[2])
            if curver > v:
                v = curver
        return v

    def _find_segment(self, name):
        return self._find_segments(name, True)

    def _find_segments(self, name, one=False):
        found = [] if not one else ''
        for s in self.segments:
            spl = s.split(':', 1)
            if spl[0] == name:
                if one:
                    return s
                found.append(s)
        return found
