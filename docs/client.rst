.. _client:

The client object
=================

.. _client-state:

Storing and restoring client state
----------------------------------

The :class:`~fints.client.FinTS3Client` object keeps some internal state that's beneficial to keep
across invocations. This includes

 * A system identifier that uniquely identifies this particular FinTS endpoint
 * The Bank Parameter Data (BPD) with information about the bank and its advertised capabilities
 * The User Parameter Data (UPD) with information about the user account and allowed actions

.. autoclass:: fints.client.FinTS3Client
   :members: deconstruct, set_data
   :noindex:
   :undoc-members:

Using the :func:`~fints.client.FinTS3Client.deconstruct`/:func:`~fints.client.FinTS3Client.set_data`
facility is purely optional for reading operations, but may speed up the process because the BPD/UPD
can be cached and need not be transmitted again.

It may be required to use the facility for transaction operations if both parts of a two-step transaction
cannot be completed with the same :class:`~fints.client.FinTS3Client` object.

The :func:`~fints.client.FinTS3Client.deconstruct` parameter `include_private` (defaults to `False`) enables
including the User Parameter Data in the datablob. Set this to `True` if you can sufficiently ensure the
privacy of the returned datablob (mostly: user name and account numbers).

If your system manages multiple users/identity contexts, you SHOULD keep distinct datablobs per
user or context.

You SHOULD NOT call any other methods on the :class:`~fints.client.FinTS3Client` object
after calling :func:`~fints.client.FinTS3Client.deconstruct`.


Keeping the dialog open
-----------------------

All FinTS operations happen in the context of a so-called "dialog". The simple reading operations of this
library will automatically open and close the dialog when necessary, but each opening and each closing
takes one FinTS roundtrip.

For the case where multiple operations are to be performed one after the other you can indicate to the library
that you want to open a standing dialog and keep it open explicitly by entering the
:class:`~fints.client.FinTS3Client` as a context handler.

This can, and should be, complemented with the client state facility as follows:

.. code-block:: python

    datablob = ... # get from backend storage, or set to None
    client = FinTS3PinTanClient(..., from_data=datablob)

    with client:
        accounts = client.get_sepa_accounts()
        balance = client.get_balance(accounts[0])
        transactions = client.get_transactions(accounts[0])

    datablob = client.deconstruct()
    # Store datablob to backend storage

For transactions involving TANs it may be required by the bank to issue both steps for one transaction
within the same dialog. In this case it's mandatory to use a standing dialog, because otherwise each
step would be issued in its own, implicit, dialog.

.. _client-dialog-state:

Storing and restoring dialog state
----------------------------------

.. autoclass:: fints.client.FinTS3Client
   :members: pause_dialog, resume_dialog
   :noindex:
   :undoc-members:


