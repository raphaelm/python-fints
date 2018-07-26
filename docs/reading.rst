Reading operations
==================

Fetching your bank accounts
---------------------------

The most simple method allows you to get all bank accounts that your user has access to:

.. autoclass:: fints.client.FinTS3Client
   :members: get_sepa_accounts

This method will return a list of named tuples of the following type:

.. autoclass:: fints.models.SEPAAccount

You will need this account object for many further operations to show which account you want to operate on.


Fetching account balances
-------------------------

You can fetch the current balance of an account with the ``get_balance`` operation.

.. autoclass:: fints.client.FinTS3Client
  :members: get_balance

This method will return a list of ``Balance`` objects from the ``mt-940`` library. You can find more information
in `balance <their documentation>`_.


Reading account statements
--------------------------

You can fetch the banking statement of an account within a certain timeframe with the ``get_statement``
operation.

.. autoclass:: fints.client.FinTS3Client
   :members: get_statement

This method will return a list of ``Transaction`` objects from the ``mt-940`` library. You can find more information
in `their documentation`_.


Fetching holdings
-----------------

You can fetch the holdings of an account with the ``get_holdings`` method:

.. autoclass:: fints.client.FinTS3Client
   :members: get_holdings

This method will return a list of ``Holding`` objects:

.. autoclass:: fints.models.Holding


.. _their documentation: https://mt940.readthedocs.io/en/latest/mt940.html#mt940.models.Transaction
.. _balance: https://mt940.readthedocs.io/en/latest/mt940.html#mt940.models.Balance
