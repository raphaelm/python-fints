Troubleshooting and bug reporting
=================================

The FinTS specification is long and complicated and in many parts leaves things open to interpretation -- or sometimes
implementors interpret things differently even though they're not really open to interpretation. This is valid for us,
but also for the banks. Making the library work with many different banks is hard, and often impossible without access
to a test account. Therefore, we ask you for patience when reporting issues with different banks -- and you need to be
ready that we might not be able to help you because we do not have the time or bank account required to dig deeper.

Therefore, if you run into trouble with this library, you first need to ask yourself a very important question: **Is it
me or the library?** To answer this question for most cases, we have attached a script below, that we ask you to use
to try the affected feature of the library in a well-documented way. Apart from changing the arguments (i.e. your bank's
parameters and your credentials) at the top, we ask you **not to make any modifications**. Pasting this bit by bit into
a Jupyter notebook **is a modification**. If your issue does not include information as to whether the script below works
or does not work for your bank, **we will close your issue without further comment.**

**If the script below does not work for you**, there is probably a compatibility issue between this library and your
bank. Feel free to open an issue, but make sure the issue title includes the name of the bank and the text includes
what operations specifically fail.

**If the script below does work for you**, there is probably something wrong with your usage of the library or our
documentation. Feel free to open an issue, but **include full working example code** that is necessary to reproduce
the problem.

.. note:: Before posting anything on GitHub, make sure it does not contain your username, PIN, IBAN, or similarly sensitive data.

.. code-block:: python

    import datetime
    import getpass
    import logging
    import sys
    from decimal import Decimal

    from fints.client import FinTS3PinTanClient, NeedTANResponse, FinTSUnsupportedOperation
    from fints.hhd.flicker import terminal_flicker_unix
    from fints.utils import minimal_interactive_cli_bootstrap

    logging.basicConfig(level=logging.DEBUG)

    client_args = (
        'REPLACEME',  # BLZ
        'REPLACEME',  # USER
        getpass.getpass('PIN: '),
        'REPLACEME'  # ENDPOINT
    )

    f = FinTS3PinTanClient(*client_args)
    minimal_interactive_cli_bootstrap(f)


    def ask_for_tan(response):
        print("A TAN is required")
        print(response.challenge)
        if getattr(response, 'challenge_hhduc', None):
            try:
                terminal_flicker_unix(response.challenge_hhduc)
            except KeyboardInterrupt:
                pass
        tan = input('Please enter TAN:')
        return f.send_tan(response, tan)


    # Open the actual dialog
    with f:
        # Since PSD2, a TAN might be needed for dialog initialization. Let's check if there is one required
        if f.init_tan_response:
            ask_for_tan(f.init_tan_response)

        # Fetch accounts
        accounts = f.get_sepa_accounts()
        if isinstance(accounts, NeedTANResponse):
            accounts = ask_for_tan(accounts)
        if len(accounts) == 1:
            account = accounts[0]
        else:
            print("Multiple accounts available, choose one")
            for i, mm in enumerate(accounts):
                print(i, mm.iban)
            choice = input("Choice: ").strip()
            account = accounts[int(choice)]

        # Test pausing and resuming the dialog
        dialog_data = f.pause_dialog()

    client_data = f.deconstruct(including_private=True)

    f = FinTS3PinTanClient(*client_args, from_data=client_data)
    with f.resume_dialog(dialog_data):
        while True:
            operations = [
                "End dialog",
                "Fetch transactions of the last 30 days",
                "Fetch transactions of the last 120 days",
                "Fetch transactions XML of the last 30 days",
                "Fetch transactions XML of the last 120 days",
                "Fetch information",
                "Fetch balance",
                "Fetch holdings",
                "Fetch scheduled debits",
                "Fetch status protocol",
                "Make a simple transfer"
            ]

            print("Choose an operation")
            for i, o in enumerate(operations):
                print(i, o)
            choice = int(input("Choice: ").strip())
            try:
                if choice == 0:
                    break
                elif choice == 1:
                    res = f.get_transactions(account, datetime.date.today() - datetime.timedelta(days=30),
                                             datetime.date.today())
                    while isinstance(res, NeedTANResponse):
                        res = ask_for_tan(res)
                    print("Found", len(res), "transactions")
                elif choice == 2:
                    res = f.get_transactions(account, datetime.date.today() - datetime.timedelta(days=120),
                                             datetime.date.today())
                    while isinstance(res, NeedTANResponse):
                        res = ask_for_tan(res)
                    print("Found", len(res), "transactions")
                elif choice == 3:
                    res = f.get_transactions_xml(account, datetime.date.today() - datetime.timedelta(days=30),
                                                 datetime.date.today())
                    while isinstance(res, NeedTANResponse):
                        res = ask_for_tan(res)
                    print("Found", len(res[0]) + len(res[1]), "XML documents")
                elif choice == 4:
                    res = f.get_transactions_xml(account, datetime.date.today() - datetime.timedelta(days=120),
                                                 datetime.date.today())
                    while isinstance(res, NeedTANResponse):
                        res = ask_for_tan(res)
                    print("Found", len(res[0]) + len(res[1]), "XML documents")
                elif choice == 5:
                    print(f.get_information())
                elif choice == 6:
                    res = f.get_balance(account)
                    while isinstance(res, NeedTANResponse):
                        res = ask_for_tan(res)
                    print(res)
                elif choice == 7:
                    res = f.get_holdings(account)
                    while isinstance(res, NeedTANResponse):
                        res = ask_for_tan(res)
                    print(res)
                elif choice == 8:
                    res = f.get_scheduled_debits(account)
                    while isinstance(res, NeedTANResponse):
                        res = ask_for_tan(res)
                    print(res)
                elif choice == 9:
                    res = f.get_status_protocol()
                    while isinstance(res, NeedTANResponse):
                        res = ask_for_tan(res)
                    print(res)
                elif choice == 10:
                    res = f.simple_sepa_transfer(
                        account=accounts[0],
                        iban=input('Target IBAN:'),
                        bic=input('Target BIC:'),
                        amount=Decimal(input('Amount:')),
                        recipient_name=input('Recipient name:'),
                        account_name=input('Your name:'),
                        reason=input('Reason:'),
                        endtoend_id='NOTPROVIDED',
                    )

                    if isinstance(res, NeedTANResponse):
                        ask_for_tan(res)
            except FinTSUnsupportedOperation as e:
                print("This operation is not supported by this bank:", e)