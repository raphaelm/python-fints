.. _tans:

Working with TANs
=================

TAN methods
-----------

Before doing any operations involving TANs, you should get a list of supported TAN methods and select the TAN method
you want to use:

.. code-block:: python

    methods = client.get_tan_methods()
    method = methods[0]

The returned values have a subtype ``fints.models.TANMethod``, with varying parameters depending on the version
used by the bank:

.. autoclass:: fints.client.FinTS3Client
   :members: get_tan_methods

.. autoclass:: fints.models.TANMethod1

.. autoclass:: fints.models.TANMethod2

.. autoclass:: fints.models.TANMethod3

.. autoclass:: fints.models.TANMethod4

.. autoclass:: fints.models.TANMethod5

.. autoclass:: fints.models.TANMethod6

.. warning:: If the ``description_required`` attribute is ``2``, you will need to get the description of the TAN medium
             you want to use and pass it as ``tan_description`` to some operations. You can send a request for this
             information with the ``client.get_tan_description()`` method call. Currently, this returns an unparsed
             response from the bank. In the future, we will probably return a structured result here.

TAN challenges
--------------

You should then pass the chosen ``TANMethod`` object to your operation, e.g. ``start_simple_sepa_transfer``.
If a TAN is required, this operation will return a ``TANChallenge``, again depending on the version used by the bank.

.. autoclass:: fints.models.TANChallenge3

.. autoclass:: fints.models.TANChallenge4

.. autoclass:: fints.models.TANChallenge5

.. autoclass:: fints.models.TANChallenge6

The ``challenge`` attribute will contain human-readable instructions on how to proceed.

Flicker-Code / optiTAN
----------------------

If you want to use chipTAN with an optical TAN device, we provide utilities to print the flicker code on
a unix terminal. Just pass the ``result.challenge_hhd_uc`` value to this method:

.. autofunction:: fints.hhd.flicker.terminal_flicker_unix

You should probably catch for ``KeyboardInterrupts`` to allow the user to abort the displaying and to continue
with the TAN:

.. code-block:: python

    try:
        terminal_flicker_unix(result.challenge_hhd_uc)
    except KeyboardInterrupt:
        pass

Sending the TAN
---------------

Once obtained the TAN, you can send it with the ``send_tan`` client method:

.. autoclass:: fints.client.FinTS3Client
   :members: send_tan

For example:

.. code-block:: python

    tan = input('Bitte die TAN eingeben.')
    result = client.send_tan(result, tan)
