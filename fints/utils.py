import base64
import inspect
import json
import re
import zlib
from contextlib import contextmanager
from datetime import datetime
from enum import Enum

import mt940

from .models import Holding


def mt940_to_array(data):
    data = data.replace("@@", "\r\n")
    data = data.replace("-0000", "+0000")
    transactions = mt940.models.Transactions()
    return transactions.parse(data)


def classproperty(f):
    class fx:
        def __init__(self, getter):
            self.getter = getter
        def __get__(self, obj, type=None):
            return self.getter(type)
    return fx(f)


def compress_datablob(magic: bytes, version: int, data: dict):
    data = dict(data)
    for k, v in data.items():
        if k.endswith("_bin"):
            if v:
                data[k] = base64.b64encode(v).decode("us-ascii")
    serialized = json.dumps(data).encode('utf-8')
    compressed = zlib.compress(serialized, 9)
    return b';'.join([magic, b'1', str(version).encode('us-ascii'), compressed])


def decompress_datablob(magic: bytes, blob: bytes, obj: object = None):
    if not blob.startswith(magic):
        raise ValueError("Incorrect data blob")
    s = blob.split(b';', 3)
    if len(s) != 4:
        raise ValueError("Incorrect data blob")
    if not s[1].isdigit() or not s[2].isdigit():
        raise ValueError("Incorrect data blob")
    encoding_version = int(s[1].decode('us-ascii'), 10)
    blob_version = int(s[2].decode('us-ascii'), 10)

    if encoding_version != 1:
        raise ValueError("Unsupported encoding version {}".format(encoding_version))

    decompressed = zlib.decompress(s[3])
    data = json.loads(decompressed.decode('utf-8'))
    for k, v in data.items():
        if k.endswith("_bin"):
            if v:
                data[k] = base64.b64decode(v.encode('us-ascii'))

    if obj:
        setfunc = getattr(obj, "_set_data_v{}".format(blob_version), None)
        if not setfunc:
            raise ValueError("Unknown data blob version")

        setfunc(data)
    else:
        return blob_version, data


class SubclassesMixin:
    @classmethod
    def _all_subclasses(cls):
        for subcls in cls.__subclasses__():
            yield from subcls._all_subclasses()
        yield cls


class DocTypeMixin:
    _DOC_TYPE = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        type_ = self._DOC_TYPE
        if type_ is None:
            if isinstance(getattr(self, 'type', None), type):
                type_ = getattr(self, 'type')

        if type_ is not None:
            if not self.__doc__:
                self.__doc__ = ""

            name = type_.__name__
            if type_.__module__ != 'builtins':
                name = "{}.{}".format(type_.__module__, name)

            self.__doc__ = self.__doc__ + "\n\n:type: :class:`{}`".format(name)


class FieldRenderFormatStringMixin:
    _FORMAT_STRING = None

    def _render_value(self, value):
        retval = self._FORMAT_STRING.format(value)
        self._check_value_length(retval)

        return retval


class FixedLengthMixin:
    _FIXED_LENGTH = [None, None, None]
    _DOC_TYPE = str

    def __init__(self, *args, **kwargs):
        for i, a in enumerate(('length', 'min_length', 'max_length')):
            kwargs[a] = self._FIXED_LENGTH[i] if len(self._FIXED_LENGTH) > i else None

        super().__init__(*args, **kwargs)


class ShortReprMixin:
    def __repr__(self):
        return "{}{}({})".format(
            "{}.".format(self.__class__.__module__),
            self.__class__.__name__,
            ", ".join(
                ("{!r}".format(value) if not name.startswith("_") else "{}={!r}".format(name, value))
                for (name, value) in self._repr_items
            )
        )

    def print_nested(self, stream=None, level=0, indent="    ", prefix="", first_level_indent=True, trailer="", print_doc=True, first_line_suffix=""):
        stream.write(
            ( (prefix + level*indent) if first_level_indent else "")
            + "{!r}{}{}\n".format(self, trailer, first_line_suffix)
        )


class MT535_Miniparser:
    re_identification = re.compile(r"^:35B:ISIN\s(.*)\|(.*)\|(.*)$")
    re_marketprice = re.compile(r"^:90B::MRKT\/\/ACTU\/([A-Z]{3})(\d*),{1}(\d*)$")
    re_pricedate = re.compile(r"^:98A::PRIC\/\/(\d*)$")
    re_pieces = re.compile(r"^:93B::AGGR\/\/UNIT\/(\d*),(\d*)$")
    re_totalvalue = re.compile(r"^:19A::HOLD\/\/([A-Z]{3})(\d*),{1}(\d*)$")
    re_acquisitionprice = re.compile(r"^:70E::HOLD\/\/\d*STK\|2(\d*?),{1}(\d*?)\+([A-Z]{3})$")

    def parse(self, lines):
        retval = []
        # First: Collapse multiline clauses into one clause
        clauses = self.collapse_multilines(lines)
        # Second: Scan sequence of clauses for financial instrument
        # sections
        finsegs = self.grab_financial_instrument_segments(clauses)
        # Third: Extract financial instrument data
        for finseg in finsegs:
            isin, name, market_price, price_symbol, price_date, pieces, acquisitionprice = (None,)*7
            for clause in finseg:
                # identification of instrument
                # e.g. ':35B:ISIN LU0635178014|/DE/ETF127|COMS.-MSCI EM.M.T.U.ETF I'
                m = self.re_identification.match(clause)
                if m:
                    isin = m.group(1)
                    name = m.group(3)
                # current market price
                # e.g. ':90B::MRKT//ACTU/EUR38,82'
                m = self.re_marketprice.match(clause)
                if m:
                    price_symbol = m.group(1)
                    market_price = float(m.group(2) + "." + m.group(3))
                # date of market price
                # e.g. ':98A::PRIC//20170428'
                m = self.re_pricedate.match(clause)
                if m:
                    price_date = datetime.strptime(m.group(1), "%Y%m%d").date()
                # number of pieces
                # e.g. ':93B::AGGR//UNIT/16,8211'
                m = self.re_pieces.match(clause)
                if m:
                    pieces = float(m.group(1) + "." + m.group(2))
                # total value of holding
                # e.g. ':19A::HOLD//EUR970,17'
                m = self.re_totalvalue.match(clause)
                if m:
                    total_value = float(m.group(2) + "." + m.group(3))
                # Acquisition price
                # e.g ':70E::HOLD//1STK23,968293+EUR'
                m = self.re_acquisitionprice.match(clause)
                if m:
                    acquisitionprice = float(m.group(1) + '.' + m.group(2))

            # processed all clauses
            retval.append(
                Holding(
                    ISIN=isin, name=name, market_value=market_price,
                    value_symbol=price_symbol, valuation_date=price_date,
                    pieces=pieces, total_value=total_value,
                    acquisitionprice=acquisitionprice))
        return retval

    def collapse_multilines(self, lines):
        clauses = []
        prevline = ""
        for line in lines:
            if line.startswith(":"):
                if prevline != "":
                    clauses.append(prevline)
                prevline = line
            elif line.startswith("-"):
                # last line
                clauses.append(prevline)
                clauses.append(line)
            else:
                prevline += "|{}".format(line)
        return clauses

    def grab_financial_instrument_segments(self, clauses):
        retval = []
        stack = []
        within_financial_instrument = False
        for clause in clauses:
            if clause.startswith(":16R:FIN"):
                # start of financial instrument
                within_financial_instrument = True
            elif clause.startswith(":16S:FIN"):
                # end of financial instrument - move stack over to
                # return value
                retval.append(stack)
                stack = []
                within_financial_instrument = False
            else:
                if within_financial_instrument:
                    stack.append(clause)
        return retval


class Password(str):
    protected = False

    def __init__(self, value):
        self.value = value
        self.blocked = False

    @classmethod
    @contextmanager
    def protect(cls):
        try:
            cls.protected = True
            yield None
        finally:
            cls.protected = False

    def block(self):
        self.blocked = True

    def __str__(self):
        if self.blocked and not self.protected:
            raise Exception("Refusing to use PIN after block")
        return '***' if self.protected else str(self.value)

    def __repr__(self):
        return self.__str__().__repr__()

    def __add__(self, other):
        return self.__str__().__add__(other)

    def replace(self, *args, **kwargs):
        return self.__str__().replace(*args, **kwargs)


class RepresentableEnum(Enum):
    def __init__(self, *args, **kwargs):
        Enum.__init__(self)

        # Hack alert: Try to parse the docstring from the enum source, if available. Fail softly.
        # FIXME Needs test
        try:
            val_1 = val_2 = repr(args[0])
            if val_1.startswith("'"):
                val_2 = '"' + val_1[1:-1] + '"'
            elif val_1.startswith('"'):
                val_2 = "'" + val_1[1:-1] + "'"
            regex = re.compile(r"^.*?\S+\s*=\s*(?:(?:{})|(?:{}))\s*#:\s*(\S.*)$".format(
                        re.escape(val_1), re.escape(val_2)))
            for line in inspect.getsourcelines(self.__class__)[0]:
                m = regex.match(line)
                if m:
                    self.__doc__ = m.group(1).strip()
                    break
        except:
            raise

    def __repr__(self):
        return "{}.{}.{}".format(self.__class__.__module__, self.__class__.__name__, self.name)

    def __str__(self):
        return self.value
