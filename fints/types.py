from collections import Iterable, OrderedDict
from contextlib import suppress

from .utils import SubclassesMixin


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

    def _get_minimal_true_length(self):
        retval = 0
        for i, val in enumerate(self._data):
            if isinstance(val, Container):
                if val.is_unset():
                    continue
            elif val is None:
                continue
            retval = i + 1
        return retval

    def __len__(self):
        if self._parent.count is not None:
            return self._parent.count
        else:
            retval = self._get_minimal_true_length()
            if self._parent.min_count is not None:
                if self._parent.min_count > retval:
                    retval = self._parent.min_count
            return retval

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]

    def __repr__(self):
        return "{!r}".format(list(self))

    def print_nested(self, stream=None, level=0, indent="    ", prefix="", first_level_indent=True, trailer="", print_doc=True, first_line_suffix=""):
        import sys
        stream = stream or sys.stdout

        stream.write(
            ((prefix + level * indent) if first_level_indent else "")
            + "[{}\n".format(first_line_suffix)
        )
        min_true_length = self._get_minimal_true_length()
        skipped_items = 0
        for i, val in enumerate(self):
            if i > min_true_length:
                skipped_items += 1
                continue
            if print_doc:
                docstring = self._parent._inline_doc_comment(val)
            else:
                docstring = ""
            if not hasattr(getattr(val, 'print_nested', None), '__call__'):
                stream.write(
                    (prefix + (level + 1) * indent) + "{!r},{}\n".format(val, docstring)
                )
            else:
                val.print_nested(stream=stream, level=level + 2, indent=indent, prefix=prefix, trailer=",", print_doc=print_doc, first_line_suffix=docstring)
        if skipped_items:
            stream.write((prefix + (level + 1) * indent) + "# {} empty items skipped\n".format(skipped_items))
        stream.write((prefix + level * indent) + "]{}\n".format(trailer))


class SegmentSequence:
    """A sequence of FinTS3Segment objects"""

    def __init__(self, segments=None):
        if isinstance(segments, bytes):
            from .parser import FinTS3Parser
            parser = FinTS3Parser()
            data = parser.explode_segments(segments)
            segments = [parser.parse_segment(segment) for segment in data]
        self.segments = list(segments) if segments else []

    def render_bytes(self) -> bytes:
        from .parser import FinTS3Serializer
        return FinTS3Serializer().serialize_message(self)

    def __repr__(self):
        return "{}.{}({!r})".format(self.__class__.__module__, self.__class__.__name__, self.segments)

    def print_nested(self, stream=None, level=0, indent="    ", prefix="", first_level_indent=True, trailer="", print_doc=True, first_line_suffix=""):
        import sys
        stream = stream or sys.stdout
        stream.write(
            ((prefix + level * indent) if first_level_indent else "")
            + "{}.{}([".format(self.__class__.__module__, self.__class__.__name__)
            + first_line_suffix
            + "\n"
        )
        for segment in self.segments:
            docstring = print_doc and segment.__doc__
            if docstring:
                docstring = docstring.splitlines()[0].strip()
            if docstring:
                docstring = " # {}".format(docstring)
            else:
                docstring = ""
            segment.print_nested(stream=stream, level=level + 1, indent=indent, prefix=prefix, first_level_indent=True, trailer=",", print_doc=print_doc,
                                 first_line_suffix=docstring)
        stream.write((prefix + level * indent) + "]){}\n".format(trailer))

    def find_segments(self, query=None, version=None, callback=None, recurse=True):
        """Yields an iterable of all matching segments.

        :param query: Either a str or class specifying a segment type (such as 'HNHBK', or :class:`~fints.segments.message.HNHBK3`), or a list or tuple of strings or classes.
                     If a list/tuple is specified, segments returning any matching type will be returned.
        :param version: Either an int specifying a segment version, or a list or tuple of ints.
                        If a list/tuple is specified, segments returning any matching version will be returned.
        :param callback: A callable that will be given the segment as its sole argument and must return a boolean indicating whether to return this segment.
        :param recurse: If True (the default), recurse into SegmentSequenceField values, otherwise only look at segments in this SegmentSequence.

        The match results of all given parameters will be AND-combined.
        """

        if query is None:
            query = []
        elif isinstance(query, str) or not isinstance(query, (list, tuple, Iterable)):
            query = [query]

        if version is None:
            version = []
        elif not isinstance(version, (list, tuple, Iterable)):
            version = [version]

        if callback is None:
            callback = lambda s: True

        for s in self.segments:
            if ((not query) or any((isinstance(s, t) if isinstance(t, type) else s.header.type == t) for t in query)) and \
                    ((not version) or any(s.header.version == v for v in version)) and \
                    callback(s):
                yield s

            if recurse:
                for name, field in s._fields.items():
                    val = getattr(s, name)
                    if val and hasattr(val, 'find_segments'):
                        yield from val.find_segments(query=query, version=version, callback=callback, recurse=recurse)

    def find_segment_first(self, *args, **kwargs):
        """Finds the first matching segment.

        Same parameters as find_segments(), but only returns the first match, or None if no match is found."""

        for m in self.find_segments(*args, **kwargs):
            return m

        return None

    def find_segment_highest_version(self, query=None, version=None, callback=None, recurse=True, default=None):
        """Finds the highest matching segment.

        Same parameters as find_segments(), but returns the match with the highest version, or default if no match is found."""
        # FIXME Test

        retval = None

        for s in self.find_segments(query=query, version=version, callback=callback, recurse=recurse):
            if not retval or s.header.version > retval.header.version:
                retval = s

        if retval is None:
            return default

        return retval


class ContainerMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()

    def __new__(cls, name, bases, classdict):
        retval = super().__new__(cls, name, bases, classdict)
        retval._fields = OrderedDict()
        for supercls in reversed(bases):
            if hasattr(supercls, '_fields'):
                retval._fields.update((k, v) for (k, v) in supercls._fields.items())
        retval._fields.update((k, v) for (k, v) in classdict.items() if isinstance(v, Field))
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

        for k, v in init_values.items():
            setattr(self, k, v)

    @classmethod
    def naive_parse(cls, data):
        if data is None:
            raise TypeError("No data provided")
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
                elif isinstance(val, ValueList):
                    if len(val) == 0:
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

    def print_nested(self, stream=None, level=0, indent="    ", prefix="", first_level_indent=True, trailer="", print_doc=True, first_line_suffix=""):
        """Structured nested print of the object to the given stream.

        The print-out is eval()able to reconstruct the object."""
        import sys
        stream = stream or sys.stdout

        stream.write(
            ((prefix + level * indent) if first_level_indent else "")
            + "{}.{}(".format(self.__class__.__module__, self.__class__.__name__)
            + first_line_suffix
            + "\n"
        )
        for name, value in self._repr_items:
            val = getattr(self, name)
            if print_doc and not name.startswith("_"):
                docstring = self._fields[name]._inline_doc_comment(val)
            else:
                docstring = ""
            if not hasattr(getattr(val, 'print_nested', None), '__call__'):
                stream.write(
                    (prefix + (level + 1) * indent) + "{} = {!r},{}\n".format(name, val, docstring)
                )
            else:
                stream.write(
                    (prefix + (level + 1) * indent) + "{} = ".format(name)
                )
                val.print_nested(stream=stream, level=level + 2, indent=indent, prefix=prefix, first_level_indent=False, trailer=",", print_doc=print_doc,
                                 first_line_suffix=docstring)
        stream.write((prefix + level * indent) + "){}\n".format(trailer))
