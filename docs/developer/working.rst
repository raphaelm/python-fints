Working with Segments
~~~~~~~~~~~~~~~~~~~~~

Objects of :class:`~fints.segments.base.FinTS3Segment` or a subclass can be created by calling their constructor. The constructor takes optional arguments for all fields of the class. Setting and getting fields and subfields works, and consumes and returns Python objects as appropriate:

.. code-block:: python

    >>> from fints.segments import HNHBS1
    >>> s = HNHBS1()
    >>> s
    fints.segments.HNHBS1(header=fints.formals.SegmentHeader('HNHBS', None, 1), message_number=None)
    >>> s.header.number = 3
    >>> s.header
    fints.formals.SegmentHeader('HNHBS', 3, 1)

When setting a value, format and length restrictions will be checked, if possible:

.. code-block:: python

    >>> s.message_number = 'abc'
    ValueError: invalid literal for int() with base 10: 'abc'
    >>> s.message_number = 12345
    ValueError: Value '12345' cannot be rendered: max_length=4 exceeded

The only exception is: Every field can be set to ``None`` in order to clear the field and make it unset, recursively. No checking is performed whether all fields that are required (or conditionally required) by the specification are set. For convenience, an unset constructed field will still be filled with an instance of the field's value type, so that subfield accessing will always work, without encountering ``None`` values on the way.

.. code-block:: python

    >>> s.header = None
    >>> s
    fints.segments.HNHBS1(header=fints.formals.SegmentHeader(None, None, None), message_number=None)

When calling the constructor with non-keyword arguments, fields are assigned in order, with the exception of ``header`` in :class:`~fints.segments.base.FinTS3Segment` subclasses, which can only be given as a keyword argument. When no ``header`` argument is present, a :class:`~fints.formals.SegmentHeader` is automatically constructed with default values (and no ``number``). It's generally not required to construct the ``header`` parameter manually.

.. code-block:: python

    >>> HNHBS1(42)
    fints.segments.HNHBS1(header=fints.formals.SegmentHeader('HNHBS', None, 1), message_number=42)
    >>> HNHBS1(42, header=SegmentHeader('FOO'))
    fints.segments.HNHBS1(header=fints.formals.SegmentHeader('FOO', None, None), message_number=42)


Some segment fields have a variable number of values. These are always treated as a list, and minimum/maximum list length is obeyed. Setting a value beyond the end of the list results in an exception. Empty values are added to maintain the correct minimum number of values.

.. code-block:: python

    >>> from fints.segments import HIRMG2
    >>> s = HIRMG2()
    >>> s
    fints.segments.HIRMG2(header=fints.formals.SegmentHeader('HIRMG', None, 2), responses=[fints.formals.Response(code=None, reference_element=None, text=None)])
    >>> s.responses[0].code = '0010'
    >>> s.responses[1].code = '0100'
    >>> s.print_nested()
    fints.segments.HIRMG2(
        header = fints.formals.SegmentHeader('HIRMG', None, 2),
        responses = [
                    fints.formals.Response(
                        code = '0010',
                        reference_element = None,
                        text = None,
                    ),
                    fints.formals.Response(
                        code = '0100',
                        reference_element = None,
                        text = None,
                    ),
            ],
    )
    >>> HIRMG2(responses=[fints.formals.Response('2342')]).print_nested()
    fints.segments.HIRMG2(
        header = fints.formals.SegmentHeader('HIRMG', None, 2),
        responses = [
                    fints.formals.Response(
                        code = '2342',
                        reference_element = None,
                        text = None,
                    ),
            ],
    )
