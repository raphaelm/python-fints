import datetime
import decimal
import re
import warnings

from fints.types import Container, SegmentSequence, TypedField
from fints.utils import (
    DocTypeMixin, FieldRenderFormatStringMixin, FixedLengthMixin, Password,
)


class DataElementField(DocTypeMixin, TypedField):
    pass


class ContainerField(TypedField):
    def _check_value(self, value):
        if self.type:
            if not isinstance(value, self.type):
                raise TypeError("Value {!r} is not of type {!r}".format(value, self.type))
        super()._check_value(value)

    def _default_value(self):
        return self.type()
    

class DataElementGroupField(DocTypeMixin, ContainerField):
    pass


class GenericField(FieldRenderFormatStringMixin, DataElementField):
    type = None
    _FORMAT_STRING = "{}"

    def _parse_value(self, value):
        warnings.warn("Generic field used for type {!r} value {!r}".format(self.type, value))
        return value


class GenericGroupField(DataElementGroupField):
    type = None

    def _default_value(self):
        if self.type is None:
            return Container()
        else:
            return self.type()
    
    def _parse_value(self, value):
        if self.type is None:
            warnings.warn("Generic field used for type {!r} value {!r}".format(self.type, value))
        return value


class TextField(FieldRenderFormatStringMixin, DataElementField):
    type = 'txt'
    _DOC_TYPE = str
    _FORMAT_STRING = "{}"  # FIXME Restrict CRLF

    def _parse_value(self, value): return str(value)


class AlphanumericField(TextField):
    type = 'an'


class DTAUSField(DataElementField):
    type = 'dta'


class NumericField(FieldRenderFormatStringMixin, DataElementField):
    type = 'num'
    _DOC_TYPE = int
    _FORMAT_STRING = "{:d}"

    def _parse_value(self, value): 
        _value = str(value)
        if len(_value) > 1 and _value[0] == '0':
            raise ValueError("Leading zeroes not allowed for value of type 'num': {!r}".format(value))
        return int(_value, 10)


class ZeroPaddedNumericField(NumericField):
    type = ''
    _DOC_TYPE = int

    def __init__(self, *args, **kwargs):
        if not kwargs.get('length', None):
            raise ValueError("ZeroPaddedNumericField needs length argument")
        super().__init__(*args, **kwargs)

    @property
    def _FORMAT_STRING(self):
        return "{:0" + str(self.length) + "d}"

    def _parse_value(self, value):
        _value = str(value)
        return int(_value, 10)


class DigitsField(FieldRenderFormatStringMixin, DataElementField):
    type = 'dig'
    _DOC_TYPE = str
    _FORMAT_STRING = "{}"

    def _parse_value(self, value): 
        _value = str(value)
        if not re.match(r'^\d*$', _value):
            raise TypeError("Only digits allowed for value of type 'dig': {!r}".format(value))
        return _value


class FloatField(DataElementField):
    type = 'float'
    _DOC_TYPE = float
    _FORMAT_STRING = "{:.12f}"  # Warning: Python's float is not exact!
    # FIXME: Needs test

    def _parse_value(self, value):
        if isinstance(value, float):
            return value
        
        if isinstance(value, decimal.Decimal):
            value = str(value.normalize()).replace(".", ",")

        _value = str(value)
        if not re.match(r'^(?:0|[1-9]\d*),(?:\d*[1-9]|)$', _value):
            raise TypeError("Only digits and ',' allowed for value of type 'float', no superfluous leading or trailing zeroes allowed: {!r}".format(value))

        return float(_value.replace(",", "."))

    def _render_value(self, value):
        retval = self._FORMAT_STRING.format(value)
        retval = retval.replace('.', ',').rstrip('0')
        self._check_value_length(retval)
        return retval


class AmountField(FixedLengthMixin, DataElementField):
    type = 'wrt'
    _DOC_TYPE = decimal.Decimal
    _FIXED_LENGTH = [None, None, 15]
    # FIXME Needs test

    def _parse_value(self, value):
        if isinstance(value, float):
            return value

        if isinstance(value, decimal.Decimal):
            return value

        _value = str(value)
        if not re.match(r'^(?:0|[1-9]\d*),(?:\d*[1-9]|)$', _value):
            raise TypeError("Only digits and ',' allowed for value of type 'float', no superfluous leading or trailing zeroes allowed: {!r}".format(value))

        return decimal.Decimal(_value.replace(",", "."))

    def _render_value(self, value):
        retval = str(value)
        retval = retval.replace('.', ',').rstrip('0')
        self._check_value_length(retval)
        return retval


class BinaryField(DataElementField):
    type = 'bin'
    _DOC_TYPE = bytes

    def _render_value(self, value):
        retval = bytes(value)
        self._check_value_length(retval)

        return retval

    def _parse_value(self, value): return bytes(value)


class IDField(FixedLengthMixin, AlphanumericField):
    type = 'id'
    _DOC_TYPE = str
    _FIXED_LENGTH = [None, None, 30]


class BooleanField(FixedLengthMixin, AlphanumericField):
    type = 'jn'
    _DOC_TYPE = bool
    _FIXED_LENGTH = [1]

    def _render_value(self, value):
        return "J" if value else "N"

    def _parse_value(self, value):
        if value is None:
            return None
        if value == "J" or value is True:
            return True
        elif value == "N" or value is False:
            return False
        else:
            raise ValueError("Invalid value {!r} for BooleanField".format(value))


class CodeFieldMixin:
    # FIXME Need tests

    def __init__(self, enum=None, *args, **kwargs):
        if enum:
            self._DOC_TYPE = enum
            self._enum = enum
        else:
            self._enum = None
        super().__init__(*args, **kwargs)

    def _parse_value(self, value):
        retval = super()._parse_value(value)
        if self._enum:
            retval = self._enum(retval)
        return retval

    def _render_value(self, value):
        retval = value
        if self._enum:
            retval = str(value.value)
        return super()._render_value(retval)

    def _inline_doc_comment(self, value):
        retval = super()._inline_doc_comment(value)
        if self._enum:
            addendum = value.__doc__
            if addendum and addendum is not value.__class__.__doc__:
                if not retval:
                    retval = " # "
                else:
                    retval = retval + ": "
                retval = retval + addendum
        return retval


class CodeField(CodeFieldMixin, AlphanumericField):
    type = 'code'
    _DOC_TYPE = str


class IntCodeField(CodeFieldMixin, NumericField):
    type = ''
    _DOC_TYPE = int
    _FORMAT_STRING = "{}"


class CountryField(FixedLengthMixin, DigitsField):
    type = 'ctr'
    _FIXED_LENGTH = [3]


class CurrencyField(FixedLengthMixin, AlphanumericField):
    type = 'cur'
    _FIXED_LENGTH = [3]


class DateField(FixedLengthMixin, NumericField):
    type = 'dat'  # FIXME Need test
    _DOC_TYPE = datetime.date
    _FIXED_LENGTH = [8]

    def _parse_value(self, value):
        if isinstance(value, datetime.date):
            return value
        val = super()._parse_value(value)
        val = str(val)
        return datetime.date(int(val[0:4]), int(val[4:6]), int(val[6:8]))

    def _render_value(self, value):
        val = "{:04d}{:02d}{:02d}".format(value.year, value.month, value.day)
        val = int(val)
        return super()._render_value(val)


class TimeField(FixedLengthMixin, DigitsField):
    type = 'tim'  # FIXME Need test
    _DOC_TYPE = datetime.time
    _FIXED_LENGTH = [6]

    def _parse_value(self, value):
        if isinstance(value, datetime.time):
            return value
        val = super()._parse_value(value)
        return datetime.time(int(val[0:2]), int(val[2:4]), int(val[4:6]))

    def _render_value(self, value):
        val = "{:02d}{:02d}{:02d}".format(value.hour, value.minute, value.second)
        return super()._render_value(val)


class PasswordField(AlphanumericField):
    type = ''
    _DOC_TYPE = Password

    def _parse_value(self, value):
        return Password(value)

    def _render_value(self, value):
        return str(value)


class SegmentSequenceField(DataElementField):
    type = 'sf'

    def _parse_value(self, value):
        if isinstance(value, SegmentSequence):
            return value
        else:
            return SegmentSequence(value)

    def _render_value(self, value):
        return value.render_bytes()
