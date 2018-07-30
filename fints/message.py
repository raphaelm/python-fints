from enum import Enum
import random
import re

from fints.models import TANMethod1, TANMethod2, TANMethod3, TANMethod4, TANMethod5, TANMethod6
from .segments.message import HNHBK, HNHBS, HNSHA, HNSHK, HNVSD, HNVSK

TOKEN_RE = re.compile(rb"""
                        ^(?:  (?: \? (?P<ECHAR>.) )
                            | (?P<CHAR>[^?:+@']+)
                            | (?P<TOK>[+:'])
                            | (?: @ (?P<BINLEN>[0-9]+) @ )
                         )""", re.X | re.S)

class Token(Enum):
    EOF = 'eof'
    CHAR = 'char'
    BINARY = 'bin'
    PLUS = '+'
    COLON = ':'
    APOSTROPHE = "'"

class ParserState:
    def __init__(self, data: bytes, start=0, end=None, encoding='iso-8859-1'):
        self._token = None
        self._value = None
        self._encoding = encoding
        self._tokenizer = iter(self._tokenize(data, start, end or len(data), encoding))

    def peek(self):
        if not self._token:
            self._token, self._value = next(self._tokenizer)
        return self._token

    def consume(self, token=None):
        self.peek()
        if token and token != self._token:
            raise ValueError
        self._token = None
        return self._value

    @staticmethod
    def _tokenize(data, start, end, encoding):
        pos = start
        unclaimed = []
        last_was = None
        
        while pos < end:
            match = TOKEN_RE.match(data[pos:end])
            if match:
                pos += match.end()
                d = match.groupdict()
                if d['ECHAR'] is not None:
                    unclaimed.append(d['ECHAR'])
                elif d['CHAR'] is not None:
                    unclaimed.append(d['CHAR'])
                else:
                    if unclaimed:
                        if last_was in (Token.BINARY, Token.CHAR):
                            raise ValueError
                        yield Token.CHAR, b''.join(unclaimed).decode(encoding)
                        unclaimed.clear()
                        last_was = Token.CHAR

                    if d['TOK'] is not None:
                        token = Token(d['TOK'].decode('us-ascii'))
                        yield token, d['TOK']
                        last_was = token
                    elif d['BINLEN'] is not None:
                        blen = int(d['BINLEN'].decode('us-ascii'), 10)
                        if last_was in (Token.BINARY, Token.CHAR):
                            raise ValueError
                        yield Token.BINARY, data[pos:pos+blen]
                        pos += blen
                        last_was = Token.BINARY
                    else:
                        raise ValueError
            else:
                raise ValueError

        if unclaimed:
            if last_was in (Token.BINARY, Token.CHAR):
                raise ValueError
            yield Token.CHAR, b''.join(unclaimed).decode(encoding)
            unclaimed.clear()
            last_was = Token.CHAR

        yield Token.EOF, b''


class FinTSMessageBase:
    def __init__(self, *segments):
        self.segments = []
        for segment in segments:
            self.add_segment(segment)

    def add_segment(self, segment):
        self.segments.append(segment)

    @classmethod
    def parse(cls, data: bytes, start=0, end=None):
        return cls(*cls.parse_segments(data, start, end))

    @classmethod
    def parse_segments(cls, data: bytes, start=0, end=None):
        segments = []

        parser = ParserState(data, start, end)

        while parser.peek() != Token.EOF:
            segment = []
            while parser.peek() not in (Token.APOSTROPHE, Token.EOF):
                data = None
                deg = []
                while parser.peek() in (Token.BINARY, Token.CHAR, Token.COLON):
                    if parser.peek() in (Token.BINARY, Token.CHAR):
                        data = parser.consume()

                    elif parser.peek() == Token.COLON:
                        deg.append(data)
                        data = None
                        parser.consume(Token.COLON)

                if data and deg:
                    deg.append(data)
                    data = deg

                segment.append(data)
                if parser.peek() == Token.PLUS:
                    parser.consume(Token.PLUS)

            parser.consume(Token.APOSTROPHE)
            segments.append(segment)

        parser.consume(Token.EOF)

        return segments
 

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


class FinTSResponse(FinTSMessageBase):
    def __init__(self, data):
        self.segments = self.parse_segments(data)
        self.payload = self.segments
        for seg in self.segments:
            if seg[0][0] == 'HNVSD':
                self.payload = self.parse_segments(seg[1])

    def __str__(self):
        return str(self.payload)

    def is_success(self):
        summary = self.get_summary_by_segment('HIRMG')
        for code, msg in summary.items():
            if code[0] == "9":
                return False
        return True

    def get_dialog_id(self):
        seg = self._find_segment('HNHBK')
        if not seg:
            raise ValueError('Invalid response, no HNHBK segment')

        return seg[3]

    def get_bank_name(self):
        seg = self._find_segment('HIBPA')
        if seg:
            if len(seg) > 3:
                return seg[3]

    def get_systemid(self):
        seg = self._find_segment('HISYN')
        if not seg:
            raise ValueError('Could not find systemid')
        return seg[1]

    def get_summary_by_segment(self, name=None):
        if name and name not in ('HIRMS', 'HIRMG'):
            raise ValueError('Unsupported segment for message summary')
        if name:
            names = [name]
        else:
            names = ('HIRMS', 'HIRMG')

        res = {}
        for name in names:
            seg = self._find_segment(name)
            for de in seg[1:]:
                res[de[0]] = de[2]
        return res

    def get_hkkaz_max_version(self):
        return self._get_segment_max_version('HIKAZS')

    def get_hksal_max_version(self):
        return self._get_segment_max_version('HISALS')

    def get_supported_tan_mechanisms(self):
        segs = self._find_segments('HIRMS')
        tan_methods = []
        for seg in segs:
            for deg in seg:
                if deg[0] == '3920':
                    tan_methods.extend( deg[3:] )

        # Get parameters for tan methods
        segs = self._find_segments('HITANS')
        methods = []
        for seg in segs:
            if seg[0][2] == '1':
                model = TANMethod1
            elif seg[0][2] == '2':
                model = TANMethod2
            elif seg[0][2] == '3':
                model = TANMethod3
            elif seg[0][2] == '4':
                model = TANMethod4
            elif seg[0][2] == '5':
                model = TANMethod5
            elif seg[0][2] == '6':
                model = TANMethod6
            else:
                raise NotImplementedError(
                    "HITANS segment version {} is currently not implemented".format(
                        seg[0][2]
                    )
                )

            step = len(model.args)
            tan_params = seg[3][3:]
            for i in range(len(tan_params) // step):
                part = spl[i * step:(i + 1) * step]
                method = model(*part)
                if method.security_feature in tan_methods:
                    methods.append(method)

        return methods

    def _find_segment_for_reference(self, name, ref):
        segs = self._find_segments(name)
        for seg in segs:
            if len(seg[0]) < 4: continue
            if seg[0][3] == str(ref.segmentno):
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

    def _get_segment_max_version(self, name):
        v = 3
        segs = self._find_segments(name)
        for s in segs:
            curver = int(s[0][2])
            if curver > v:
                v = curver
        return v

    def _find_segment(self, name):
        return self._find_segments(name, True)

    def _find_segments(self, name, one=False, in_payload=False):
        found = []
        for s in (self.payload if in_payload else self.segments):
            if s[0][0] == name:
                if one:
                    return s
                found.append(s)
        # FIXME Simple hack: Seach in inner message if no success in outer message
        if not found and not in_payload:
            return self._find_segments(name, one, in_payload=True)
        return found
