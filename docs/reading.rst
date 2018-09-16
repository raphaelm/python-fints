Reading operations
==================

Fetching your bank accounts
---------------------------

The most simple method allows you to get all bank accounts that your user has access to:

.. autoclass:: fints.client.FinTS3Client
   :noindex:
   :members: get_sepa_accounts
   :noindex:

This method will return a list of named tuples of the following type:

.. autoclass:: fints.models.SEPAAccount

You will need this account object for many further operations to show which account you want to operate on.

Fetching bank information
-------------------------

During the first interaction with the bank some meta information about the bank and your user is transmitted
from the bank.

.. autoclass:: fints.client.FinTS3Client
   :members: get_information
   :noindex:


Fetching account balances
-------------------------

You can fetch the current balance of an account with the ``get_balance`` operation.

.. autoclass:: fints.client.FinTS3Client
  :members: get_balance
  :noindex:

This method will return a list of ``Balance`` objects from the ``mt-940`` library. You can find more information
in `their documentation <https://mt940.readthedocs.io/en/latest/mt940.html#mt940.models.Balance>`_.


Reading account transactions
----------------------------

You can fetch the banking statement of an account within a certain timeframe with the ``get_transactions``
operation.

.. autoclass:: fints.client.FinTS3Client
   :members: get_transactions
   :noindex:

This method will return a list of ``Transaction`` objects from the ``mt-940`` library. You can find more information
in `their documentation <https://mt940.readthedocs.io/en/latest/mt940.html#mt940.models.Transaction>`_.


Fetching holdings
-----------------

You can fetch the holdings of an account with the ``get_holdings`` method:

.. autoclass:: fints.client.FinTS3Client
   :noindex:
   :members: get_holdings
   :noindex:

This method will return a list of ``Holding`` objects:

.. autoclass:: fints.models.Holding
