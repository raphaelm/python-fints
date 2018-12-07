FinTS Segments
--------------
A segment is the core communication workhorse in FinTS. Each segment has a header of fixed format, which includes the segment type ("Segmentkennung"), number within the message, version, and, optionally, the number of the segment of another message it is in response or relation to ("Bezugssegment").

The header is followed by a nested structure of fields and groups of fields, the exact specification of which depends on the segment type and version.

All segment classes derive from  :class:`~fints.segments.base.FinTS3Segment`, which specifies the ``header`` attribute of :class:`~fints.formals.SegmentHeader` type.

.. autoclass:: fints.segments.base.FinTS3Segment
   :members:
   :inherited-members: print_nested
   :member-order: bysource

   .. attribute:: TYPE

      Segment type. Will be determined from the class name in subclasses, if the class name consists only of uppercase characters followed by decimal digits. Subclasses may explicitly set a class attribute instead.

   .. attribute:: VERSION

      Segment version. Will be determined from the class name in subclasses, if the class name consists only of uppercase characters followed by decimal digits. Subclasses may explicitly set a class attribute instead.

   .. classmethod:: find_subclass(segment: list)

      Parse the given ``segment`` parameter as a :class:`~fints.formals.SegmentHeader` and return a subclass with matching type and version class attributes.

The :class:`~fints.segments.base.FinTS3Segment` class and its base classes employ a number of dynamic programming techniques so that derived classes need only specify the name, order and type of fields. All type conversion, construction etc. will take place automatically. All derived classes basically should behave "as expected", returning only native Python datatypes.

Consider this example segment class:

.. code-block:: python

    class HNHBS1(FinTS3Segment):
        message_number = DataElementField(type='num', max_length=4)

Calling ``print_nested`` on an instance of this class might output:

.. code-block:: python

    fints.segments.HNHBS1(
        header = fints.formals.SegmentHeader('HNHBS', 4, 1),
        message_number = 1,
    )

.. toctree::
   :maxdepth: 2

   all
