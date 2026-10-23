Reading operations
==================

.. note::

   Starting from version 3, **all of the methods on this page** can return a ``NeedTANResponse`` instead of actual
   data if your bank requires a TAN. You should then enter a TAN, read our chapter :ref:`tans` to find out more.

Fetching your bank accounts
---------------------------

The most simple method allows you to get all bank accounts that your user has access to:

.. autoclass:: fints.client.FinTS3Client
   :noindex:
   :members: get_sepa_accounts

This method will return a list of named tuples of the following type:

.. autoclass:: fints.models.SEPAAccount

You will need this account object for many further operations to show which account you want to operate on.

.. _information:

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

.. _transactions:

Reading account transactions
----------------------------

You can fetch the banking statement of an account within a certain timeframe with the ``get_transactions``
operation.

.. autoclass:: fints.client.FinTS3Client
   :members: get_transactions, get_transactions_xml
   :noindex:

This method will return a list of ``Transaction`` objects from the ``mt-940`` library. You can find more information
in `their documentation <https://mt940.readthedocs.io/en/latest/mt940.html#mt940.models.Transaction>`_.


Fetching holdings
-----------------

You can fetch the holdings of an account with the ``get_holdings`` method:

.. autoclass:: fints.client.FinTS3Client
   :members: get_holdings
   :noindex:

This method will return a list of ``Holding`` objects:

.. autoclass:: fints.models.Holding


.. _standing-orders:

Fetching standing orders
------------------------

You can fetch the SEPA standing orders ("Daueraufträge") of an account with the ``get_standing_orders`` method:

.. autoclass:: fints.client.FinTS3Client
   :members: get_standing_orders
   :noindex:

This method will return a list of ``HICDB1`` segments, one per standing order. The schedule is available in
``standing_order_details`` (see :class:`~fints.formals.StandingOrderDetails3`), a suspension, if any, in
``suspension`` (see :class:`~fints.formals.StandingOrderSuspension3`). Recipient, amount and purpose are contained in
the SEPA pain.001 message in ``sepa_pain_message``, which you can read with ``parse_sepa_transfer_pain``:

.. autofunction:: fints.utils.parse_sepa_transfer_pain

.. autoclass:: fints.models.SEPATransferPayment

The first and last execution dates are *virtual dates*, which allow 31 days in every month (e.g. 2025-04-31 for a
standing order executed on the last day of each month). They are returned as ``VirtualDate`` objects:

.. autoclass:: fints.models.VirtualDate
   :members: to_date

Example:

.. code-block:: python

    from fints.utils import parse_sepa_transfer_pain

    standing_orders = client.get_standing_orders(account)
    while isinstance(standing_orders, NeedTANResponse):
        standing_orders = ask_for_tan(standing_orders)

    for order in standing_orders:
        details = order.standing_order_details
        payment = parse_sepa_transfer_pain(order.sepa_pain_message)
        print("Task ID:", order.task_id)
        print("First/last execution:", details.first_execution_date, details.last_execution_date)
        print("Interval:", details.interval, details.time_unit, "on day", details.execution_day)
        print("Recipient:", payment.recipient_name, payment.iban, payment.bic)
        print("Amount:", payment.amount.amount, payment.amount.currency)
        print("Purpose:", payment.reason)
