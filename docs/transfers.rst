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

