import re
import warnings
from collections.abc import Iterable
from enum import Enum

from .formals import (
    Container, DataElementGroupField, SegmentSequence, ValueList,
)
# Ensure that all segment types are loaded (otherwise the subclass find won't see them)
from .segments import (  # noqa
    accounts, auth, bank, base, debit, depot, dialog,
    journal, message, saldo, statement, transfer,
)
from .segments.base import FinTS3Segment

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
#  Parsing:
#    The message after detokenization/exploding is up to three levels deep:
#    1. level: Sequence of Segments
#    2. level: Sequence of Data Elements or Data Element Groups
#    3. level: Flat sequence of possibly nested Data Element or Data Element Groups
# 
#    On level 2 each item can be either a single item (a single Data Element), or
#    a sequence. A sequence on level 2 can be either a repeated Data Element, or
#    a flat representation of a Data Element Group or repeated Data Element Group.
#    An item on level 3 is always a Data Element, but which Data Element it is depends
#    on which fields have been consumed in the sequence before it.


#: Operate the parser in "robust mode". In this mode, errors during segment parsing
#: will be turned into a FinTSParserWarning and a generic FinTS3Segment (not a subclass)
#: will be constructed. This allows for all syntactically correct FinTS messages to be
#: consumed, even in the presence of errors in this library.
robust_mode = True


class FinTSParserWarning(UserWarning):
    pass


class FinTSParserError(ValueError):
    pass


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
    """Parser for FinTS/HBCI 3.0 messages
    """

    def parse_message(self, data: bytes) -> SegmentSequence:
        """Takes a FinTS 3.0 message as byte array, and returns a parsed segment sequence"""
        if isinstance(data, bytes):
            data = self.explode_segments(data)

        message = SegmentSequence()
        for segment in data:
            seg = self.parse_segment(segment)
            message.segments.append(seg)
        return message

    def parse_segment(self, segment):
        clazz = FinTS3Segment.find_subclass(segment)

        try:
            return self._parse_segment_as_class(clazz, segment)
        except FinTSParserError as e:
            if robust_mode:
                warnings.warn("Ignoring parser error and returning generic object: {}. Turn off robust_mode to see Exception.".format(str(e)), FinTSParserWarning)
                return self._parse_segment_as_class(FinTS3Segment, segment)
            else:
                raise

    def _parse_segment_as_class(self, clazz, segment):
        seg = clazz()

        data = iter(segment)
        for name, field in seg._fields.items():
            repeat = field.count != 1
            constructed = isinstance(field, DataElementGroupField)
            
            if not repeat:
                try:
                    val = next(data)
                except StopIteration:
                    if field.required:
                        raise FinTSParserError("Required field {}.{} was not present".format(seg.__class__.__name__, name))
                    break

                try:
                    if not constructed:
                        setattr(seg, name, val)
                    else:
                        deg = self.parse_deg_noniter(field.type, val, field.required)
                        setattr(seg, name, deg)
                except ValueError as e:
                    raise FinTSParserError("Wrong input when setting {}.{}".format(seg.__class__.__name__, name)) from e
            else:
                i = 0
                while True:
                    try:
                        val = next(data)
                    except StopIteration:
                        break

                    try:
                        if not constructed:
                            getattr(seg, name)[i] = val
                        else:
                            deg = self.parse_deg_noniter(field.type, val, field.required)
                            getattr(seg, name)[i] = deg
                    except ValueError as e:
                        raise FinTSParserError("Wrong input when setting {}.{}".format(seg.__class__.__name__, name)) from e

                    i = i + 1

                    if field.count is not None and i >= field.count:
                        break
                    if field.max_count is not None and i >= field.max_count:
                        break

        seg._additional_data = list(data)

        return seg

    def parse_deg_noniter(self, clazz, data, required):
        if not isinstance(data, Iterable) or isinstance(data, (str, bytes)):
            data = [data]

        data_i = iter(data)

        retval = self.parse_deg(clazz, data_i, required)

        remainder = list(data_i)
        if remainder:
            raise FinTSParserError("Unparsed data {!r} after parsing {!r}".format(remainder, clazz))

        return retval

    def parse_deg(self, clazz, data_i, required=True):
        retval = clazz()

        for number, (name, field) in enumerate(retval._fields.items()):
            repeat = field.count != 1
            constructed = isinstance(field, DataElementGroupField)
            is_last = number == len(retval._fields)-1

            if not repeat:
                try:
                    if not constructed:
                        try:
                            setattr(retval, name, next(data_i))
                        except StopIteration:
                            if required and field.required:
                                raise FinTSParserError("Required field {}.{} was not present".format(retval.__class__.__name__, name))
                            break
                    else:
                        deg = self.parse_deg(field.type, data_i, required and field.required)
                        setattr(retval, name, deg)
                except ValueError as e:
                    raise FinTSParserError("Wrong input when setting {}.{}".format(retval.__class__.__name__, name)) from e
            else:
                i = 0
                while True:
                    try:
                        if not constructed:
                            try:
                                getattr(retval, name)[i] = next(data_i)
                            except StopIteration:
                                break

                        else:
                            require_last = (field.max_count is None) if is_last else True
                            deg = self.parse_deg(field.type, data_i, require_last and required and field.required)
                            getattr(retval, name)[i] = deg

                    except ValueError as e:
                        raise FinTSParserError("Wrong input when setting {}.{}".format(retval.__class__.__name__, name)) from e

                    i = i + 1

                    if field.count is not None and i >= field.count:
                        break
                    if field.max_count is not None and i >= field.max_count:
                        break

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

                if deg:
                    data = deg

                segment.append(data)
                if parser.peek() == Token.PLUS:
                    parser.consume(Token.PLUS)

            parser.consume(Token.APOSTROPHE)
            segments.append(segment)

        parser.consume(Token.EOF)

        return segments


class FinTS3Serializer:
    """Serializer for FinTS/HBCI 3.0 messages
    """

    def serialize_message(self, message: SegmentSequence) -> bytes:
        """Serialize a message (as SegmentSequence, list of FinTS3Segment, or FinTS3Segment) into a byte array"""
        if isinstance(message, FinTS3Segment):
            message = SegmentSequence([message])
        if isinstance(message, (list, tuple, Iterable)):
            message = SegmentSequence(list(message))

        result = []

        for segment in message.segments:
            result.append(self.serialize_segment(segment))

        return self.implode_segments(result)

    def serialize_segment(self, segment):

        seg = []
        filler = []

        for name, field in segment._fields.items():
            repeat = field.count != 1
            constructed = isinstance(field, DataElementGroupField)

            val = getattr(segment, name)
            empty = False
            if not field.required:
                if isinstance(val, Container):
                    if val.is_unset():
                        empty = True
                elif isinstance(val, ValueList):
                    if len(val) == 0:
                        empty = True
                elif val is None:
                    empty = True

            if empty:
                filler.append(None)
                continue
            else:
                if filler:
                    seg.extend(filler)
                    filler.clear()

            if not constructed:
                if repeat:
                    seg.extend(field.render(val) for val in getattr(segment, name))
                else:
                    seg.append(field.render(getattr(segment, name)))
            else:
                if repeat:
                    for val in getattr(segment, name):
                        seg.append(self.serialize_deg(val))
                else:
                    seg.append(self.serialize_deg(getattr(segment, name), allow_skip=True))

        if segment._additional_data:
            seg.extend(segment._additional_data)
            
        return seg

    def serialize_deg(self, deg, allow_skip=False):
        result = []
        filler = []

        for name,field in deg._fields.items():
            repeat = field.count != 1
            constructed = isinstance(field, DataElementGroupField)

            val = getattr(deg, name)
            empty = False
            if field.count == 1 and not field.required:
                if isinstance(val, Container):
                    if val.is_unset():
                        empty = True
                elif isinstance(val, ValueList):
                    if len(val) == 0:
                        empty = True
                elif val is None:
                    empty = True

            if empty:
                if allow_skip:
                    filler.append(None)
                else:
                    result.append(None)
                continue
            else:
                if filler:
                    result.extend(filler)
                    filler.clear()

            if not constructed:
                if repeat:
                    result.extend(field.render(val) for val in getattr(deg, name))
                else:
                    result.append(field.render(getattr(deg, name)))
            else:
                if repeat:
                    for val in getattr(deg, name):
                        result.extend(self.serialize_deg(val))
                else:
                    result.extend(self.serialize_deg(getattr(deg, name)))

        return result

    @staticmethod
    def implode_segments(message: list):
        level1 = []

        for segment in message:
            level2 = []
            for deg in segment:
                if isinstance(deg, (list, tuple)):
                    highest_index = max(((i+1) for (i, e) in enumerate(deg) if e != b'' and e is not None), default=0)
                    level2.append(
                        b":".join(FinTS3Serializer.escape_value(de) for de in deg[:highest_index])
                    )
                else:
                    level2.append(FinTS3Serializer.escape_value(deg))
            level1.append(b"+".join(level2))

        return b"'".join(level1) + b"'"

    @staticmethod
    def escape_value(val):
        if isinstance(val, str):
            return re.sub(r"([+:'@?])", r"?\1", val).encode('iso-8859-1')
        elif isinstance(val, bytes):
            return "@{}@".format(len(val)).encode('us-ascii') + val
        elif val is None:
            return b''
        else:
            raise TypeError("Can only escape str, bytes and None")
