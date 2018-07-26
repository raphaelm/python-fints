Getting started
===============

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
        'https://hbci-pintan.gad.de/cgi-bin/hbciservlet'
    )


You can then execute commands using the client instance:

.. code-block:: python

    accounts = f.get_sepa_accounts()

Go on to the next pages to find out what commands are supported!