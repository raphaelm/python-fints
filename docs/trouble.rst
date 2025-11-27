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
    product_id = 'REPLACEME'

    f = FinTS3PinTanClient(*client_args, product_id=product_id)
    minimal_interactive_cli_bootstrap(f)


    def ask_for_tan(response):
        print("A TAN is required")
        print(response.challenge)
        if getattr(response, 'challenge_hhduc', None):
            try:
                terminal_flicker_unix(response.challenge_hhduc)
            except KeyboardInterrupt:
                pass
        if response.decoupled:
            tan = input('Please press enter after confirming the transaction in your app:')
        else:
            tan = input('Please enter TAN:')
        return f.send_tan(response, tan)


    def ask_for_vop(response: NeedVOPResponse):
        if response.vop_result.vop_single_result.result == "RVMC":
            print("Payee name is a close match")
            print("Name retrieved by bank:", response.vop_result.vop_single_result.close_match_name)
            if response.vop_result.vop_single_result.other_identification:
                print("Other info retrieved by bank:", response.vop_result.vop_single_result.other_identification)
        elif response.vop_result.vop_single_result.result == "RVNM":
            print("Payee name does not match match")
        elif response.vop_result.vop_single_result.result == "RVNA":
            print("Payee name could not be verified")
            print("Reason:", response.vop_result.vop_single_result.na_reason)
        elif response.vop_result.vop_single_result.result == "PDNG":
            print("Payee name could not be verified (pending state, can't be handled by this library)")
        print("Do you want to continue? Your bank will not be liable if the money ends up in the wrong place.")
        input('Please press enter to confirm or Ctrl+C to cancel')
        return f.approve_vop_response(response)


    # Open the actual dialog
    with f:
        # Since PSD2, a TAN might be needed for dialog initialization. Let's check if there is one required
        while isinstance(f.init_tan_response, NeedTANResponse):
            f.init_tan_response = ask_for_tan(f.init_tan_response)

        # Fetch accounts
        accounts = f.get_sepa_accounts()
        while isinstance(accounts, NeedTANResponse):
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

    f = FinTS3PinTanClient(*client_args, product_id=product_id, from_data=client_data)
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
                "Make a simple transfer",
                "Fetch statements as PDF",
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

                    while isinstance(res, NeedTANResponse | NeedVOPResponse):
                        if isinstance(res, NeedTANResponse):
                            res = ask_for_tan(res)
                        elif isinstance(res, NeedVOPResponse):
                            res = ask_for_vop(res)
                elif choice == 11:
                    print("Select statement")
                    statements = f.get_statements(account)
                    for i, statement in enumerate(statements):
                        print(i, f"Statement {statement.statement_number}/{statement.year}")
                    choice = int(input("Choice: ").strip())
                    statement = statements[choice]
                    output_pdf = 'statement.pdf'
                    res = f.get_statement(account, statement.statement_number, statement.year, StatementFormat.PDF)
                    while isinstance(res, NeedTANResponse):
                        res = ask_for_tan(res)
                    with open(output_pdf, 'wb') as file:
                        file.write(res.data)
                    print("Written to", output_pdf)
            except FinTSUnsupportedOperation as e:
                print("This operation is not supported by this bank:", e)