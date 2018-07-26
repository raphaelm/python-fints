Sending SEPA transfers
======================

Simple mode
-----------

You can create a simple SEPA transfer using this convenient client method:

.. autoclass:: fints.client.FinTS3Client
   :members: start_simple_sepa_transfer

You should then enter a TAN, read our chapter :ref:`tans` to find out more.

Advanced mode
-------------

If you want to use advanced methods, you can supply your own SEPA XML:

.. autoclass:: fints.client.FinTS3Client
   :members: start_sepa_transfer

Example
-------

.. code-block:: python

    client = FinTS3PinTanClient(…)

    accounts = f.get_sepa_accounts()
    account = accounts[0]

    methods = f.get_tan_methods()
    method = methods[0]
    assert method.description_required != '2'

    tan_desc = ''
    res = f.start_simple_sepa_transfer(
        account=accounts[0],
        iban='DE12345',
        bic='BIC12345',
        amount=Decimal('7.00'),
        recipient_name='Foo',
        account_name='Test',
        reason='Birthday gift',
        endtoend_id='NOTPROVIDED',
        tan_method=method
    )
    print(res.challenge)

    if getattr(res, challenge_hhd_uc, None):
        try:
            terminal_flicker_unix(res.challenge_hhd_uc)
        except KeyboardInterrupt:
            pass

    tan = input('Please enter TAN:')
    res = f.send_tan(res, tan)
