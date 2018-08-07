from enum import Enum
from collections import Iterable
from contextlib import suppress
import re
from .segments import FinTS3Segment
from .formals import DataElementField, DataElementGroupField, SegmentSequence

# 
# FinTS 3.0 structure:
#     Message := ( Segment "'" )+
#     Segment := ( DEG "+" )+
#     DEG     := ( ( DE | DEG ) ":")+
#  
#  First DEG in segment is segment header
#  Many DEG (Data Element Group) on Segment level are just DE (Data Element),
#  Recursion DEG -> DEG must be limited, since no other separator characters
#  are available. In general, a second order DEG must have fixed length but
#  may have a variable repeat count if it is at the end of the segment
#

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

class FinTS3Parser:
    def parse_message(self, data):
        if isinstance(data, bytes):
            data = self.explode_segments(data)

        message = SegmentSequence()
        for segment in data:
            seg = self.parse_segment(segment)
            message.segments.append(seg)
        return message

    def parse_segment(self, segment):
        clazz = FinTS3Segment.find_subclass(segment)
        seg = clazz()

        data = iter(segment)
        for name, field in seg._fields.items():
            try:
                val = next(data)
            except StopIteration:
                if field.required:
                    raise ValueError("Required field {}.{} was not present".format(clazz.__name__, name))
            else:
                deg = self.parse_n_deg(field, val)
                setattr(seg, name, deg)
        seg._additional_data = list(data)

        return seg

    def parse_n_deg(self, field, data):
        if not isinstance(data, Iterable) or isinstance(data, (str, bytes)):
            data = [data]

        data_i = iter(data)
        field_index = 0
        field_length = field.flat_length

        retval = []
        eod = False

        while not eod:
            vals = []
            try:
                for x in range(field_length):
                    vals.append(next(data_i))
            except StopIteration:
                eod = True

            if field.count == 1:
                if isinstance(field, DataElementField):
                    if not len(vals):
                        return
                    return vals[0]
                elif isinstance(field, DataElementGroupField):
                    return self.parse_deg(field.type, vals)
                else:
                    raise Error("Internal error")
                break

            if field_index >= (field.count if field.count is not None else len(data) // field_length):
                break

            if isinstance(field, DataElementField):
                retval.append(vals[0] if len(vals) else None)
            elif isinstance(field, DataElementGroupField):
                retval.append(self.parse_deg(field.type, vals))
            else:
                raise Error("Internal error")

        return retval

    def parse_deg(self, clazz, vals):
        retval = clazz()

        data_i = iter(vals)
        for name, field in retval._fields.items():
            deg = self.parse_n_deg(field, data_i)
            setattr(retval, name, deg)

        return retval


    @staticmethod
    def explode_segments(data: bytes, start=0, end=None):
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

