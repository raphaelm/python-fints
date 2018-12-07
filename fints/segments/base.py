import re

from fints.fields import DataElementField, DataElementGroupField, IntCodeField
from fints.formals import SecurityClass, SegmentHeader
from fints.types import Container, ContainerMeta
from fints.utils import SubclassesMixin, classproperty

TYPE_VERSION_RE = re.compile(r'^([A-Z]+)(\d+)$')


class FinTS3SegmentMeta(ContainerMeta):
    @staticmethod
    def _check_fields_recursive(instance):
        for name, field in instance._fields.items():
            if not isinstance(field, (DataElementField, DataElementGroupField)):
                raise TypeError("{}={!r} is not DataElementField or DataElementGroupField".format(name, field))
            if isinstance(field, DataElementGroupField):
                FinTS3SegmentMeta._check_fields_recursive(field.type)

    def __new__(cls, name, bases, classdict):
        retval = super().__new__(cls, name, bases, classdict)
        FinTS3SegmentMeta._check_fields_recursive(retval)
        return retval


class FinTS3Segment(Container, SubclassesMixin, metaclass=FinTS3SegmentMeta):
    header = DataElementGroupField(type=SegmentHeader, _d="Segmentkopf")

    @classproperty
    def TYPE(cls):
        match = TYPE_VERSION_RE.match(cls.__name__)
        if match:
            return match.group(1)

    @classproperty
    def VERSION(cls):
        match = TYPE_VERSION_RE.match(cls.__name__)
        if match:
            return int(match.group(2))

    def __init__(self, *args, **kwargs):
        if 'header' not in kwargs:
            kwargs['header'] = SegmentHeader(self.TYPE, None, self.VERSION)

        args = (kwargs.pop('header'), ) + args

        super().__init__(*args, **kwargs)

    @classmethod
    def find_subclass(cls, segment):
        h = SegmentHeader.naive_parse(segment[0])
        target_cls = None

        for possible_cls in cls._all_subclasses():
            if getattr(possible_cls, 'TYPE', None) == h.type and getattr(possible_cls, 'VERSION', None) == h.version:
                target_cls = possible_cls

        if not target_cls:
            target_cls = cls

        return target_cls


class ParameterSegment_22(FinTS3Segment):
    max_number_tasks = DataElementField(type='num', max_length=3, _d="Maximale Anzahl Aufträge")
    min_number_signatures = DataElementField(type='num', length=1, _d="Anzahl Signaturen mindestens")


class ParameterSegment(FinTS3Segment):
    max_number_tasks = DataElementField(type='num', max_length=3, _d="Maximale Anzahl Aufträge")
    min_number_signatures = DataElementField(type='num', length=1, _d="Anzahl Signaturen mindestens")
    security_class = IntCodeField(SecurityClass, length=1, _d="Sicherheitsklasse")
