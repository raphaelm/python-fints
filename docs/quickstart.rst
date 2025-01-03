Getting started
===============

Register for a product ID
-------------------------

As of September 14th, 2019, all FinTS client programs need to be registered with the Deutsche Kreditwirtschaft.
You need to fill out a PDF form and will be assigned a product ID that you can pass to this library.
It can take up to two weeks for the product ID to be assigned.

The reason for this requirement is compliance with the European Unions 2nd Payment Services Directive (PSD2)
which mandates that end-users can transparently see which applications are accessing their bank account.

You can find more information as well as the registration form on the `DK Website`_ (only available in German).

Start coding
------------

First of all, you need to install the library::

    $ pip3 install fints

Then, you can initialize a FinTS client by providing your bank's BLZ, your username and PIN as well as the HBCI endpoint
of your bank. Logging in with a signature file or chip card is currently not supported. For example:

.. code-block:: python

    import logging
    from datetime import date
    import getpass
    from fints.client import FinTS3PinTanClient

    logging.basicConfig(level=logging.DEBUG)
    f = FinTS3PinTanClient(
        '123456789',  # Your bank's BLZ
        'myusername',  # Your login name
        getpass.getpass('PIN:'),  # Your banking PIN
        'https://hbci-pintan.gad.de/cgi-bin/hbciservlet',
        product_id='Your product ID'  # see above
    )

Since the implementation of PSD2, you will in almost all cases need to be ready to deal with TANs. For a quick start,
we included a minimal command-line utility to help choose a TAN method:

.. code-block:: python

    from fints.utils import minimal_interactive_cli_bootstrap
    minimal_interactive_cli_bootstrap(f)

You can then open up a real communication dialog to the bank with a ``with`` statement and issue commands:
commands using the client instance:

.. code-block:: python

    with f:
        # Since PSD2, a TAN might be needed for dialog initialization. Let's check if there is one required
        if f.init_tan_response:
            print("A TAN is required", f.init_tan_response.challenge)
            tan = input('Please enter TAN:')
            f.send_tan(f.init_tan_response, tan)

        # Fetch accounts
        accounts = f.get_sepa_accounts()

Go on to the next pages to find out what commands are supported! There is also a full example on how to get your bank transactions if a TAN is required (:ref:`tans-full-example`).

.. _DK Website: https://www.fints.org/de/hersteller/produktregistrierung
