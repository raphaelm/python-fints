Sending SEPA transfers
======================

Simple mode
-----------

You can create a simple SEPA transfer using this convenient client method:

.. autoclass:: fints.client.FinTS3Client
   :members: simple_sepa_transfer
   :noindex:

You should then enter a TAN, read our chapter :ref:`tans` to find out more.

Advanced mode
-------------

If you want to use advanced methods, you can supply your own SEPA XML:

.. autoclass:: fints.client.FinTS3Client
   :members: sepa_transfer
   :noindex:

Example
-------

.. code-block:: python

    client = FinTS3PinTanClient(...)

    accounts = client.get_sepa_accounts()
    account = accounts[0]

    mechanisms = client.get_tan_mechanisms()
    mechanism = mechanisms[client.get_current_tan_mechanism()]
    if mechanism.description_required == fints.formals.DescriptionRequired.MUST:
        usage_option, media = client.get_tan_media()

        client.set_tan_medium(media[0])

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

    if isinstance(res, NeedTANResponse):
        print(res.challenge)

        if getattr(res, 'challenge_hhduc', None):
            try:
                terminal_flicker_unix(res.challenge_hhduc)
            except KeyboardInterrupt:
                pass

        tan = input('Please enter TAN:')
        res = client.send_tan(res, tan)

    print(res.status)
    print(res.responses)

