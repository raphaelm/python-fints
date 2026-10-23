.. _transfers:

Sending SEPA transfers
======================

Simple mode
-----------

You can create a simple SEPA transfer using this convenient client method:

.. autoclass:: fints.client.FinTS3Client
   :members: simple_sepa_transfer
   :noindex:

The return value may be a `NeedVOPResponse` in which case you need to call `approve_vop_response` to proceed.

At any point, you might receive a `NeedTANResponse`.
You should then enter a TAN, read our chapter :ref:`tans` to find out more.

.. autoclass:: fints.client.FinTS3PinTanClient
   :members: approve_vop_response
   :noindex:


Advanced mode
-------------

If you want to use advanced methods, you can supply your own SEPA XML:

.. autoclass:: fints.client.FinTS3Client
   :members: sepa_transfer
   :noindex:

Full example
------------

.. code-block:: python

    client = FinTS3PinTanClient(...)
    minimal_interactive_cli_bootstrap(client)

    with client:
        if client.init_tan_response:
            print("A TAN is required", client.init_tan_response.challenge)

            if getattr(client.init_tan_response, 'challenge_hhduc', None):
                try:
                    terminal_flicker_unix(client.init_tan_response.challenge_hhduc)
                except KeyboardInterrupt:
                    pass

            tan = input('Please enter TAN:')
            client.send_tan(client.init_tan_response, tan)

        res = client.simple_sepa_transfer(
            account=accounts[0],
            iban='DE12345',
            bic='BIC12345',
            amount=Decimal('7.00'),
            recipient_name='Foo',
            account_name='Test',
            reason='Birthday gift',
            endtoend_id='NOTPROVIDED',
        )

        while isinstance(res, NeedTANResponse | NeedVOPResponse):
            if isinstance(res, NeedTANResponse):
                print("A TAN is required", res.challenge)

                if getattr(res, 'challenge_hhduc', None):
                    try:
                        terminal_flicker_unix(res.challenge_hhduc)
                    except KeyboardInterrupt:
                        pass

                if result.decoupled:
                    tan = input('Please press enter after confirming the transaction in your app:')
                else:
                    tan = input('Please enter TAN:')
                res = client.send_tan(res, tan)
            elif isinstance(res, NeedVOPResponse):
                if res.vop_result.vop_single_result.result == "RCVC":
                    print("Payee name is an exact match")
                    if res.vop_result.vop_single_result.other_identification:
                        print("Other info retrieved by bank:", res.vop_result.vop_single_result.other_identification)
                elif res.vop_result.vop_single_result.result == "RVMC":
                    print("Payee name is a close match")
                    print("Name retrieved by bank:", res.vop_result.vop_single_result.close_match_name)
                    if res.vop_result.vop_single_result.other_identification:
                        print("Other info retrieved by bank:", res.vop_result.vop_single_result.other_identification)
                elif res.vop_result.vop_single_result.result == "RVNM":
                    print("Payee name does not match match")
                elif res.vop_result.vop_single_result.result == "RVNA":
                    print("Payee name could not be verified")
                    print("Reason:", res.vop_result.vop_single_result.na_reason)
                elif res.vop_result.vop_single_result.result == "PDNG":
                    print("Payee name could not be verified (pending state, can't be handled by this library)")
                print("Do you want to continue? Your bank will not be liable if the money ends up in the wrong place.")
                input('Please press enter to confirm or Ctrl+C to cancel')
                res = client.approve_vop_response(res)

        print(res.status)
        print(res.responses)



Creating standing orders
------------------------

You can create a SEPA standing order ("Dauerauftrag") with the same convenience as a simple transfer. The schedule
is given by the date of the first execution, the time unit (monthly or weekly), the interval (every n months or weeks)
and the execution day (day of the month or of the week):

.. autoclass:: fints.client.FinTS3Client
   :members: simple_create_standing_order
   :noindex:

.. autoclass:: fints.formals.StandingOrderTimeUnit1
   :noindex:

The first and last execution dates can be given as ``datetime.date`` or as ``VirtualDate`` (see
:ref:`standing-orders`). A virtual date also allows days beyond the end of the month, e.g.
``VirtualDate(2030, 4, 31)`` as first execution of a standing order executed on the 31st of each month.

Which intervals, execution days and advance notices the bank allows, e.g. to only offer allowed values to the user,
can be found out with ``get_standing_order_parameters``:

.. autoclass:: fints.client.FinTS3Client
   :members: get_standing_order_parameters
   :noindex:

If you want to supply your own SEPA XML, use ``create_standing_order``. The requested execution date
(``ReqdExctnDt``) in the pain message must be ``1999-01-01``, as for a simple transfer:

.. autoclass:: fints.client.FinTS3Client
   :members: create_standing_order
   :noindex:

As with transfers, the return value may be a `NeedVOPResponse` (call `approve_vop_response` to proceed) or a
`NeedTANResponse`. If the bank assigns a task id to the new standing order, it is returned in ``data['task_id']``
of the final ``TransactionResponse``.

.. note::

   Returning the task id (Auftragsidentifikation) on creation is optional for banks, and many banks do not do it:
   ``data['task_id']`` is then not set, even though the standing order was created successfully (e.g. response code
   ``0010 Auftrag entgegengenommen``). In this case, call ``get_standing_orders`` afterwards to obtain the task id
   of the new standing order. You need it for example to delete the standing order later on. As with changes (see
   below), it may take a while until the new standing order shows up there.

.. code-block:: python

    from fints.formals import StandingOrderTimeUnit1

    res = client.simple_create_standing_order(
        account=account,
        iban='DE89370400440532013000',
        bic='COBADEFFXXX',
        recipient_name='Max Mustermann',
        amount=Decimal('25.00'),
        account_name='Your name',
        reason='Monthly rent',
        first_execution_date=datetime.date(2030, 1, 1),
        time_unit=StandingOrderTimeUnit1.MONTHLY,
        interval=1,
        execution_day=1,
    )
    while isinstance(res, NeedTANResponse | NeedVOPResponse):
        if isinstance(res, NeedTANResponse):
            res = ask_for_tan(res)
        elif isinstance(res, NeedVOPResponse):
            res = client.approve_vop_response(res)

    print(res.status, res.data.get('task_id'))


Changing standing orders
------------------------

To change a SEPA standing order, pass one of the objects returned by ``get_standing_orders`` (see
:ref:`standing-orders`) together with the values to change. All values that are not given are kept. To make a
standing order unlimited, pass ``remove_last_execution_date=True``:

.. autoclass:: fints.client.FinTS3Client
   :members: simple_change_standing_order
   :noindex:

Which values may be changed is decided by the bank. The bank may assign a new task id to the changed standing order,
it is returned in ``data['task_id']`` (and the previous one in ``data['task_id_old']``) of the final
``TransactionResponse`` if the bank reports it. Otherwise, call ``get_standing_orders`` again to obtain it.

.. note::

   Banks may process changes asynchronously, especially if they answer with response code
   ``0010 Auftrag entgegengenommen`` (order accepted) instead of ``0020`` (order executed). It can then take a while
   until the change is visible in online banking and in ``get_standing_orders``. In the meantime, the standing order
   may even be missing completely from ``get_standing_orders`` for a minute or so. Wait a bit before fetching the
   standing orders again, and do not submit the change a second time.

.. code-block:: python

    standing_orders = client.get_standing_orders(account)
    while isinstance(standing_orders, NeedTANResponse):
        standing_orders = ask_for_tan(standing_orders)

    order = standing_orders[0]
    res = client.simple_change_standing_order(account, order, amount=Decimal('30.00'), execution_day=15)
    while isinstance(res, NeedTANResponse | NeedVOPResponse):
        if isinstance(res, NeedTANResponse):
            res = ask_for_tan(res)
        elif isinstance(res, NeedVOPResponse):
            res = client.approve_vop_response(res)

    print(res.status, res.data.get('task_id'))

If you want to supply your own SEPA XML, use ``change_standing_order``. The bank requires the complete new pain
message in the same schema as the pain message of the existing standing order (``order.sepa_descriptor``). To change
single values of the existing pain message while keeping its schema, you can use ``modify_sepa_transfer_pain``:

.. autoclass:: fints.client.FinTS3Client
   :members: change_standing_order
   :noindex:

.. autofunction:: fints.utils.modify_sepa_transfer_pain


Deleting standing orders
------------------------

You can delete a SEPA standing order ("Dauerauftrag") by passing one of the objects returned by
``get_standing_orders`` (see :ref:`standing-orders`) to ``delete_standing_order``:

.. autoclass:: fints.client.FinTS3Client
   :members: delete_standing_order
   :noindex:

At any point, you might receive a `NeedTANResponse`.
You should then enter a TAN, read our chapter :ref:`tans` to find out more.

.. code-block:: python

    standing_orders = client.get_standing_orders(account)
    while isinstance(standing_orders, NeedTANResponse):
        standing_orders = ask_for_tan(standing_orders)

    order = standing_orders[0]
    res = client.delete_standing_order(account, order)
    while isinstance(res, NeedTANResponse):
        res = ask_for_tan(res)

    print(res.status)
    print(res.responses)
