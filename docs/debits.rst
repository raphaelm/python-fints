Creating SEPA debits
====================

You can submit a SEPA debit XML file to the bank with the ``sepa_debit`` method:

.. autoclass:: fints.client.FinTS3Client
   :members: sepa_debit
   :noindex:

You should then enter a TAN, read our chapter :ref:`tans` to find out more.

Example
-------

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
