import re
import warnings
from contextlib import suppress
from inspect import getmro
from copy import deepcopy
from collections import OrderedDict

from fints.utils import classproperty, SubclassesMixin

class ValueList:
    def __init__(self, parent):
        self._parent = parent
        self._data = []

    def __getitem__(self, i):
        if i >= len(self._data):
            self.__setitem__(i, None)
        if i < 0:
            raise IndexError("Cannot access negative index")
        return self._data[i]

    def __setitem__(self, i, value):
        if i < 0:
            raise IndexError("Cannot access negative index")

        if self._parent.count is not None:
            if i >= self._parent.count:
                raise IndexError("Cannot access index {} beyond count {}".format(i, self._parent.count))
        elif self._parent.max_count is not None:
            if i >= self._parent.max_count:
                raise IndexError("Cannot access index {} beyound max_count {}".format(i, self._parent.max_count))

        for x in range(len(self._data), i):
            self.__setitem__(x, None)

        if value is None:
            value = self._parent._default_value()
        else:
            value = self._parent._parse_value(value)
            self._parent._check_value(value)

        if i == len(self._data):
            self._data.append(value)
        else:
            self._data[i] = value

    def __delitem__(self, i):
        self.__setitem__(i, None)

    def __len__(self):
        if self._parent.count is not None:
            return self._parent.count
        else:
            retval = len(self._data)
            if self._parent.min_count is not None:
                if self._parent.min_count > retval:
                    retval = self._parent.min_count
            return retval

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __repr__(self):
        return "{!r}".format(list(self))

class Field:
    def __init__(self, length=None, min_length=None, max_length=None, count=None, min_count=None, max_count=None, required=True):
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
                instance._values[self] = ValueList(parent=self)
        else:
            if self.count == 1:
                value_ = self._parse_value(value)
                self._check_value(value_)
            else:
                value_ = ValueList(parent=self)
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


class TypedField(Field, SubclassesMixin):
    flat_length = 1

    def __new__(cls, *args, **kwargs):
        target_cls = None
        fallback_cls = None
        if 'type' in kwargs:
            for subcls in cls._all_subclasses():
                if getattr(subcls, 'type', '') is None:
                    fallback_cls = subcls
                if getattr(subcls, 'type', None) == kwargs['type']:
                    target_cls = subcls
                    break
        if target_cls is None and fallback_cls is not None and issubclass(fallback_cls, cls):
            target_cls = fallback_cls
        retval = object.__new__(target_cls or cls)
        return retval

    def __init__(self, type=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.type = type or getattr(self.__class__, 'type', None)


class DataElementField(TypedField):
    pass

class FieldRenderFormatStringMixin:
    FORMAT_STRING = None

    def _render_value(self, value):
        retval = self.FORMAT_STRING.format(value)
        self._check_value_length(retval)

        return retval

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
    

class DataElementGroupField(ContainerField):
    pass

class GenericField(FieldRenderFormatStringMixin, DataElementField):
    type = None
    FORMAT_STRING = "{}"

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
    FORMAT_STRING = "{}"  ## FIXME Restrict CRLF

    def _parse_value(self, value): return str(value)

class AlphanumericField(TextField):
    type = 'an'
    
class DTAUSField(DataElementField):
    type = 'dta'

class NumericField(FieldRenderFormatStringMixin, DataElementField):
    type = 'num'
    FORMAT_STRING = "{:d}"

    def _parse_value(self, value): 
        _value = str(value)
        if len(_value) > 1 and _value[0] == '0':
            raise TypeError("Leading zeroes not allowed for value of type 'num': {!r}".format(value))
        return int(_value, 10)

class DigitsField(FieldRenderFormatStringMixin, DataElementField):
    type = 'dig'
    FORMAT_STRING = "{}"

    def _parse_value(self, value): 
        _value = str(value)
        if not re.match(r'^\d*$', _value):
            raise TypeError("Only digits allowed for value of type 'dig': {!r}".format(value))
        return _value

class FloatField(FieldRenderFormatStringMixin, DataElementField):
    type = 'float'

class BinaryField(DataElementField):
    type = 'bin'

    def _render_value(self, value):
        retval = bytes(value)
        self._check_value_length(retval)

        return retval

    def _parse_value(self, value): return bytes(value)


class SegmentSequence:
    def __init__(self, segments = None):
        if isinstance(segments, bytes):
            from .parser import FinTS3Parser
            parser = FinTS3Parser()
            data = parser.explode_segments(segments)
            segments = [parser.parse_segment(segment) for segment in data]
        self.segments = segments or []

    def __repr__(self):
        return "{}({!r})".format(self.__class__.__name__, self.segments)

    def print_nested(self, stream=None, level=0, indent="    ", prefix="", first_level_indent=True, trailer=""):
        import sys
        stream = stream or sys.stdout
        stream.write(
            ( (prefix + level*indent) if first_level_indent else "")
            + "{}([".format(self.__class__.__name__) + "\n"
        )
        for segment in self.segments:
            segment.print_nested(stream=stream, level=level+1, indent=indent, prefix=prefix, first_level_indent=True, trailer=",")
        stream.write( (prefix + level*indent) + "]){}\n".format(trailer) )

class SegmentSequenceField(DataElementField):
    type = 'sf'

    def _parse_value(self, value):
        if isinstance(value, SegmentSequence):
            return value
        else:
            return SegmentSequence(value)


class ContainerMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()

    def __new__(cls, name, bases, classdict):
        retval = super().__new__(cls, name, bases, classdict)
        retval._fields = OrderedDict()
        for supercls in reversed(bases):
            retval._fields.update((k,v) for (k,v) in supercls.__dict__.items() if isinstance(v, Field))
        retval._fields.update((k,v) for (k,v) in classdict.items() if isinstance(v, Field))
        return retval

class Container(metaclass=ContainerMeta):
    def __init__(self, *args, **kwargs):
        init_values = OrderedDict()

        additional_data = kwargs.pop("_additional_data", [])

        for init_value, field_name in zip(args, self._fields):
            init_values[field_name] = init_value
        args = ()
        
        for field_name in self._fields:
            if field_name in kwargs:
                if field_name in init_values:
                    raise TypeError("__init__() got multiple values for argument {}".format(field_name))
                init_values[field_name] = kwargs.pop(field_name)
        
        super().__init__(*args, **kwargs)
        self._values = {}
        self._additional_data = additional_data

        for k,v in init_values.items():
            setattr(self, k, v)

    @classmethod
    def naive_parse(cls, data):
        retval = cls()
        for ((name, field), value) in zip(retval._fields.items(), data):
            setattr(retval, name, value)
        return retval

    def is_unset(self):
        for name in self._fields.keys():
            val = getattr(self, name)
            if isinstance(val, Container):
                if not val.is_unset():
                    return False
            elif val is not None:
                return False
        return True

    @property
    def _repr_items(self):
        for name, field in self._fields.items():
            val = getattr(self, name)
            if not field.required:
                if isinstance(val, Container):
                    if val.is_unset():
                        continue
                elif val is None:
                    continue
            yield (name, val)

        if self._additional_data:
            yield ("_additional_data", self._additional_data)

    def __repr__(self):
        return "{}.{}({})".format(
            self.__class__.__module__,
            self.__class__.__name__,
            ", ".join(
                "{}={!r}".format(name, val) for (name, val) in self._repr_items
            )
        )

    def print_nested(self, stream=None, level=0, indent="    ", prefix="", first_level_indent=True, trailer=""):
        import sys
        stream = stream or sys.stdout

        stream.write(
            ( (prefix + level*indent) if first_level_indent else "")
            + "{}.{}(".format(self.__class__.__module__, self.__class__.__name__) + "\n"
        )
        for name, value in self._repr_items:
            val = getattr(self, name)
            if not hasattr( getattr(val, 'print_nested', None), '__call__'):
                stream.write(
                    (prefix + (level+1)*indent) + "{} = {!r},\n".format(name, val)
                )
            else:
                stream.write(
                    (prefix + (level+1)*indent) + "{} = ".format(name)
                )
                val.print_nested(stream=stream, level=level+2, indent=indent, prefix=prefix, first_level_indent=False, trailer=",")
        stream.write( (prefix + level*indent) + "){}\n".format(trailer) )

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

    def print_nested(self, stream=None, level=0, indent="    ", prefix="", first_level_indent=True, trailer=""):
        stream.write(
            ( (prefix + level*indent) if first_level_indent else "")
            + "{!r}{}\n".format(self, trailer)
        )

class DataElementGroup(Container):
    pass

class SegmentHeader(ShortReprMixin, DataElementGroup):
    type = AlphanumericField(max_length=6)
    number = NumericField(max_length=3)
    version = NumericField(max_length=3)
    reference = NumericField(max_length=3, required=False)

class ReferenceMessage(DataElementGroup):
    dialogue_id = DataElementField(type='id')
    message_number = NumericField(max_length=4)

class SecurityProfile(DataElementGroup):
    security_method = DataElementField(type='code', length=3)
    security_method_version = DataElementField(type='num')

class SecurityIdentificationDetails(DataElementGroup):
    name_party = DataElementField(type='code', max_length=3)
    cid = DataElementField(type='bin', max_length=256)
    identifier_party = DataElementField(type='id')

class SecurityDateTime(DataElementGroup):
    datetime_type = DataElementField(type='code', max_length=3)
    date = DataElementField(type='dat')
    time = DataElementField(type='tim')

class EncryptionAlgorithm(DataElementGroup):
    usage_encryption = DataElementField(type='code', max_length=3)
    operation_mode = DataElementField(type='code', max_length=3)
    encryption_algorithm = DataElementField(type='code', max_length=3)
    algorithm_parameter_value = DataElementField(type='bin', max_length=512)
    algorithm_parameter_name = DataElementField(type='code', max_length=3)
    algorithm_parameter_iv_name = DataElementField(type='code', max_length=3)
    algorithm_parameter_iv_value = DataElementField(type='bin', max_length=512)

class HashAlgorithm(DataElementGroup):
    usage_hash = DataElementField(type='code', max_length=3)
    hash_algorithm = DataElementField(type='code', max_length=3)
    algorithm_parameter_name = DataElementField(type='code', max_length=3)
    algorithm_parameter_value = DataElementField(type='bin', max_length=512)

class SignatureAlgorithm(DataElementGroup):
    usage_signature = DataElementField(type='code', max_length=3)
    signature_algorithm = DataElementField(type='code', max_length=3)
    operation_mode = DataElementField(type='code', max_length=3)

class BankIdentifier(DataElementGroup):
    country_identifier = DataElementField(type='ctr')
    bank_code = DataElementField(type='an', max_length=30)

class KeyName(DataElementGroup):
    bank_identifier = DataElementGroupField(type=BankIdentifier)
    user_id = DataElementField(type='id')
    key_type = DataElementField(type='code', length=1)
    key_number = DataElementField(type='num', max_length=3)
    key_version = DataElementField(type='num', max_length=3) 

class Certificate(DataElementGroup):
    certificate_type = DataElementField(type='code')
    certificate_content = DataElementField(type='bin', max_length=4096)

class UserDefinedSignature(DataElementGroup):
    pin = DataElementField(type='an', max_length=99)
    tan = DataElementField(type='an', max_length=99, required=False)

class Response(DataElementGroup):
    response_code = DataElementField(type='dig', length=4)
    reference_element = DataElementField(type='an', max_length=7)
    response_text = DataElementField(type='an', max_length=80)
    parameters = DataElementField(type='an', max_length=35, max_count=10)
