.. _tans:

Working with TANs
=================

Many operations in FinTS will require a form of two-step authentication, called TANs. TANs are
mostly required for operations that move money or change details of a bank account. TANs can be
generated with a multitude of methods, including paper lists, smartcard readers, SMS messages, and
smartphone apps.

TAN methods
-----------

Before doing any operations involving TANs, you should get a list of supported TAN mechanisms:

.. code-block:: python

    mechanisms = client.get_tan_mechanisms()

The returned dictionary maps identifiers (generally: three-digit numerals) to instances of a
:func:`~fints.formals.TwoStepParametersCommon` subclass with varying fields, depending on the
version of the two-step process and the bank.

The `name` field of these objects provides a user-friendly name of the TAN mechanism that you
can display to the user to choose from. To select a TAN mechanism, you can use
:func:`~fints.client.FinTS3PinTanClient.set_tan_mechanism`, which takes the identifier used as
key in the :func:`~fints.client.FinTS3PinTanClient.get_tan_mechanisms` return value.

If the ``description_required`` attribute for the TAN mechanism is :attr:`~fints.formals.DescriptionRequired.MUST`,
you will need to get a list of TAN media with :func:`~fints.client.FinTS3PinTanClient.get_tan_media` and select the
appropriate one with :func:`~fints.client.FinTS3PinTanClient.set_tan_medium`.

Have a look at the source code of :func:`~fints.utils.minimal_interactive_cli_bootstrap` for an example on how to
ask the user for these properties.

You may not change the active TAN mechanism or TAN medium within a standing dialog (see :ref:`client-dialog-state`).

The selection of the active TAN mechanism/medium is stored with the persistent client data (see :ref:`client-state`).

.. autoclass:: fints.client.FinTS3PinTanClient
   :members: get_tan_mechanisms, set_tan_mechanism, get_current_tan_mechanism, get_tan_media, set_tan_medium
   :noindex:
   :undoc-members:

TAN challenges
--------------

When you try to perform an operation that requires a TAN to proceed, you will receive an object containing
the bank's challenge (and some internal data to continue the operation once the TAN has been processed):

.. autoclass:: fints.client.NeedTANResponse
   :undoc-members:
   :members:

The ``challenge`` attribute will contain human-readable instructions on how to proceed.

The ``challenge_html`` attribute will possibly contain a nicer, formatted, HTML version of the challenge text
that you should prefer if your primary interface can render HTML. The contents are guaranteed to be proper and
clean (by using the `bleach` library): They can be used with `mark_safe` in Django.

The ``challenge_hhduc`` attribute will contain the challenge to be used with a TAN generator device using the
Hand Held Device Unidirectional Coupling specification (such as a Flicker-Code).

Flicker-Code / optiTAN
----------------------

If you want to use chipTAN with an optical TAN device, we provide utilities to print the flicker code on
a unix terminal. Just pass the ``challenge_hhd_uc`` value to this method:

.. autofunction:: fints.hhd.flicker.terminal_flicker_unix

You should probably catch for ``KeyboardInterrupts`` to allow the user to abort the displaying and to continue
with the TAN:

.. code-block:: python

    try:
        terminal_flicker_unix(result.challenge_hhduc)
    except KeyboardInterrupt:
        pass

photoTAN
--------

If you want to use photoTAN, use the ``challenge_matrix`` attribute to access the image file, e.g. by writing it to
a file:

.. code-block:: python

    with open("tan.png", "wb") as writer:
       writer.write(result.challenge_matrix[1])
       writer.close()

Sending the TAN
---------------

Once obtained the TAN, you can send it with the ``send_tan`` client method:

.. autoclass:: fints.client.FinTS3PinTanClient
   :members: send_tan
   :noindex:

For example:

.. code-block:: python

    tan = input('Please enter the TAN code: ')
    result = client.send_tan(result, tan)


Storing and restoring TAN state
-------------------------------

The :func:`~fints.client.NeedTANResponse.get_data` method and
:func:`~fints.client.NeedRetryResponse.from_data` factory method can be used to store and restore
a TAN state object between steps.

.. autoclass:: fints.client.NeedRetryResponse
   :undoc-members:
   :members: from_data

You SHOULD use this facility together with the client and dialog state restoration facilities:


.. code-block:: python
   :caption: First step

    client = FinTS3PinTanClient(...)
    # Optionally: choose a tan mechanism with
    # client.set_tan_mechanism(…)

    with client:
        response = client.sepa_transfer(...)
    
        dialog_data = client.pause_dialog()
    client_data = client.deconstruct()
    tan_data = response.get_data()

.. code-block:: python
   :caption: Second step

    tan_request = NeedRetryResponse.from_data(tan_data)
    print("TAN request: {}".format(tan_request.challenge))
    tan = input('Enter TAN: ')

.. code-block:: python
   :caption: Third step

    tan_request = NeedRetryResponse.from_data(tan_data)
    client = FinTS3PinTanClient(..., from_data=client_data)
    with client.resume_dialog(dialog_data):
        response = client.send_tan(tan_request, tan)

    print(response.status)
    print(response.responses)


Reference
---------

.. autoclass:: fints.formals.TwoStepParameters2
   :noindex:
   :undoc-members:
   :members:
   :inherited-members:
   :member-order: bysource
   :exclude-members: is_unset, naive_parse, print_nested

.. autoclass:: fints.formals.TwoStepParameters3
   :noindex:
   :undoc-members:
   :members:
   :inherited-members:
   :member-order: bysource
   :exclude-members: is_unset, naive_parse, print_nested

.. autoclass:: fints.formals.TwoStepParameters5
   :noindex:
   :undoc-members:
   :members:
   :inherited-members:
   :member-order: bysource
   :exclude-members: is_unset, naive_parse, print_nested
