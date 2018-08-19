from collections import Iterable, OrderedDict

import fints.fields


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
            retval = 0
            for i, val in enumerate(self._data):
                if isinstance(val, Container):
                    if val.is_unset():
                        continue
                elif val is None:
                    continue
                retval = i+1
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
            ( (prefix + level*indent) if first_level_indent else "")
            + "[{}\n".format(first_line_suffix)
        )
        for val in self:
            if print_doc:
                docstring = self._parent._inline_doc_comment(val)
            else:
                docstring = ""
            if not hasattr( getattr(val, 'print_nested', None), '__call__'):
                stream.write(
                    (prefix + (level+1)*indent) + "{!r},{}\n".format(val, docstring)
                )
            else:
                val.print_nested(stream=stream, level=level+2, indent=indent, prefix=prefix, trailer=",", print_doc=print_doc, first_line_suffix=docstring)
        stream.write( (prefix + level*indent) + "]{}\n".format(trailer) )

class SegmentSequence:
    """A sequence of FinTS3Segment objects"""

    def __init__(self, segments = None):
        if isinstance(segments, bytes):
            from .parser import FinTS3Parser
            parser = FinTS3Parser()
            data = parser.explode_segments(segments)
            segments = [parser.parse_segment(segment) for segment in data]
        self.segments = segments or []

    def render_bytes(self) -> bytes:
        from .parser import FinTS3Serializer
        return FinTS3Serializer().serialize_message(self)

    def __repr__(self):
        return "{}.{}({!r})".format(self.__class__.__module__, self.__class__.__name__, self.segments)

    def print_nested(self, stream=None, level=0, indent="    ", prefix="", first_level_indent=True, trailer="", print_doc=True, first_line_suffix=""):
        import sys
        stream = stream or sys.stdout
        stream.write(
            ( (prefix + level*indent) if first_level_indent else "")
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
            segment.print_nested(stream=stream, level=level+1, indent=indent, prefix=prefix, first_level_indent=True, trailer=",", print_doc=print_doc, first_line_suffix=docstring)
        stream.write( (prefix + level*indent) + "]){}\n".format(trailer) )

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
            if ((not query) or any( (isinstance(s, t) if isinstance(t, type) else s.header.type == t) for t in query)) and \
                ((not version) or any(s.header.version == v for v in version)) and \
                callback(s):
                yield s

            if recurse:
                for name, field in s._fields.items():
                    if isinstance(field, fints.fields.SegmentSequenceField):
                        val = getattr(s, name)
                        if val:
                            yield from val.find_segments(query=query, version=version, callback=callback, recurse=recurse)

    def find_segment_first(self, *args, **kwargs):
        """Finds the first matching segment.

        Same parameters as find_segments(), but only returns the first match, or None if no match is found."""

        for m in self.find_segments(*args, **kwargs):
            return m

        return None

class ContainerMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()

    def __new__(cls, name, bases, classdict):
        retval = super().__new__(cls, name, bases, classdict)
        retval._fields = OrderedDict()
        for supercls in reversed(bases):
            if hasattr(supercls, '_fields'):
                retval._fields.update((k,v) for (k,v) in supercls._fields.items())
        retval._fields.update((k,v) for (k,v) in classdict.items() if isinstance(v, fints.fields.Field))
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
            ( (prefix + level*indent) if first_level_indent else "")
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
            if not hasattr( getattr(val, 'print_nested', None), '__call__'):
                stream.write(
                    (prefix + (level+1)*indent) + "{} = {!r},{}\n".format(name, val, docstring)
                )
            else:
                stream.write(
                    (prefix + (level+1)*indent) + "{} = ".format(name)
                )
                val.print_nested(stream=stream, level=level+2, indent=indent, prefix=prefix, first_level_indent=False, trailer=",", print_doc=print_doc, first_line_suffix=docstring)
        stream.write( (prefix + level*indent) + "){}\n".format(trailer) )
