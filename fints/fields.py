import datetime
import re
import warnings
from contextlib import suppress

import fints.types
from fints.utils import (
    DocTypeMixin, FieldRenderFormatStringMixin,
    FixedLengthMixin, Password, SubclassesMixin,
)


class Field:
    def __init__(self, length=None, min_length=None, max_length=None, count=None, min_count=None, max_count=None, required=True, _d=None):
        if length is not None and (min_length is not None or max_length is not None):
            raise ValueError("May not specify both 'length' AND 'min_length'/'max_length'")
        if count is not None and (min_count is not None or max_count is not None):
            raise ValueError("May not specify both 'count' AND 'min_count'/'max_count'")

        self.length = length
        self.min_length = min_length
        self.max_length = max_length
        self.count = count
        self.min_count = min_count
        self.max_count = max_count
        self.required = required

        if not self.count and not self.min_count and not self.max_count:
            self.count = 1

        self.__doc__ = _d

    def _default_value(self):
        return None

    def __get__(self, instance, owner):
        if self not in instance._values:
            self.__set__(instance, None)

        return instance._values[self]

    def __set__(self, instance, value):
        if value is None:
            if self.count == 1:
                instance._values[self] = self._default_value()
            else:
                instance._values[self] = fints.types.ValueList(parent=self)
        else:
            if self.count == 1:
                value_ = self._parse_value(value)
                self._check_value(value_)
            else:
                value_ = fints.types.ValueList(parent=self)
                for i, v in enumerate(value):
                    value_[i] = v

            instance._values[self] = value_

    def __delete__(self, instance):
        self.__set__(instance, None)

    def _parse_value(self, value):
        raise NotImplementedError('Needs to be implemented in subclass')

    def _render_value(self, value):
        raise NotImplementedError('Needs to be implemented in subclass')

    def _check_value(self, value):
        with suppress(NotImplementedError):
            self._render_value(value)

    def _check_value_length(self, value):
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError("Value {!r} cannot be rendered: max_length={} exceeded".format(value, self.max_length))

        if self.min_length is not None and len(value) < self.min_length:
            raise ValueError("Value {!r} cannot be rendered: min_length={} not reached".format(value, self.min_length))

        if self.length is not None and len(value) != self.length:
            raise ValueError("Value {!r} cannot be rendered: length={} not satisfied".format(value, self.length))

    def render(self, value):
        if value is None:
            return None

        return self._render_value(value)

    def _inline_doc_comment(self, value):
        if self.__doc__:
            d = self.__doc__.splitlines()[0].strip()
            if d:
                return " # {}".format(d)
        return ""

class TypedField(Field, SubclassesMixin):
    flat_length = 1

    def __new__(cls, *args, **kwargs):
        target_cls = None
        fallback_cls = None
        for subcls in cls._all_subclasses():
            if getattr(subcls, 'type', '') is None:
                fallback_cls = subcls
            if getattr(subcls, 'type', None) == kwargs.get('type', None):
                target_cls = subcls
                break
        if target_cls is None and fallback_cls is not None and issubclass(fallback_cls, cls):
            target_cls = fallback_cls
        retval = object.__new__(target_cls or cls)
        return retval

    def __init__(self, type=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.type = type or getattr(self.__class__, 'type', None)


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

    @property
    def flat_length(self):
        result = 0
        for name, field in self.type._fields.items():
            if field.count is None:
                raise TypeError("Cannot compute flat length of field {}.{} with variable count".format(self.__class__.__name__, name))
            result = result + field.count * field.flat_length
        return result
    

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
            return fints.types.Container()
        else:
            return self.type()
    
    def _parse_value(self, value):
        if self.type is None:
            warnings.warn("Generic field used for type {!r} value {!r}".format(self.type, value))
        return value

class TextField(FieldRenderFormatStringMixin, DataElementField):
    type = 'txt'
    _DOC_TYPE = str
    _FORMAT_STRING = "{}"  ## FIXME Restrict CRLF

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
            raise TypeError("Leading zeroes not allowed for value of type 'num': {!r}".format(value))
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

class FloatField(FieldRenderFormatStringMixin, DataElementField):
    type = 'float'
    ## FIXME: Not implemented, no one uses this?

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
            if addendum and not addendum is value.__class__.__doc__:
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
    type = 'dat' # FIXME Need test
    _DOC_TYPE = datetime.date
    _FIXED_LENGTH = [8]

    def _parse_value(self, value):
        val = super()._parse_value(value)
        val = str(val)
        return datetime.date(int(val[0:4]), int(val[4:6]), int(val[6:8]))

    def _render_value(self, value):
        val = "{:04d}{:02d}{:02d}".format(value.year, value.month, value.day)
        val = int(val)
        return super()._render_value(val)

class TimeField(FixedLengthMixin, DigitsField):
    type = 'tim' # FIXME Need test
    _DOC_TYPE = datetime.time
    _FIXED_LENGTH = [6]

    def _parse_value(self, value):
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
        if isinstance(value, fints.types.SegmentSequence):
            return value
        else:
            return fints.types.SegmentSequence(value)

    def _render_value(self, value):
        return value.render_bytes()
