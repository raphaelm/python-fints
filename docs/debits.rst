.. _debits:

Creating SEPA debits
====================

You can submit a SEPA debit XML file to the bank with the ``sepa_debit`` method:

.. autoclass:: fints.client.FinTS3Client
   :members: sepa_debit
   :noindex:

You should then enter a TAN, read our chapter :ref:`tans` to find out more.

Full example
------------

You can easily generate XML using the ``sepaxml`` python library:

.. code-block:: python

    from sepaxml import SepaDD

    config = {
        "name": "Test Company",
        "IBAN": "DE12345",
        "BIC": "BIC12345",
        "batch": False,
        "creditor_id": "TESTCORPID",
        "currency": "EUR",
    }

    sepa = SepaDD(config, schema="pain.008.002.02")
    sepa.add_payment({
        "name": "Customer",
        "IBAN": "DE12345",
        "BIC": "BIC12345",
        "amount": 100,
        "type": "OOFF",  # FRST, RCUR, OOFF, FNAL
        "collection_date": datetime.date.today() + datetime.timedelta(days=3),
        "mandate_id": "FINTSTEST1",
        "mandate_date": datetime.date(2018, 7, 26),
        "description": "FinTS Test transaction",
    })
    pain_message = sepa.export().decode()

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

        res = client.sepa_debit(
            account=accounts[0],
            data=pain_message,
            multiple=False,
            control_sum=Decimal('1.00'),
            pain_descriptor='urn:iso:std:iso:20022:tech:xsd:pain.008.002.02'
        )

        if isinstance(res, NeedTANResponse):
            print("A TAN is required", res.challenge)

            if getattr(res, 'challenge_hhduc', None):
                try:
                    terminal_flicker_unix(res.challenge_hhduc)
                except KeyboardInterrupt:
                    pass

            tan = input('Please enter TAN:')
            res = client.send_tan(res, tan)

        print(res.status)
        print(res.responses)
