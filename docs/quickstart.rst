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
        'https://hbci-pintan.gad.de/cgi-bin/hbciservlet',
        product_id='Your product ID'
    )


You can then execute commands using the client instance:

.. code-block:: python

    accounts = f.get_sepa_accounts()

Go on to the next pages to find out what commands are supported!

.. note::

    As of September 14th, 2019, all FinTS programs should be registered with the ZKA or
    banks will block access. You need to fill out a PDF form and will be assigned a
    product ID that you can pass above.

    If you set the ``product_id`` to ``None``, the library will fill in the default
    product ID for python-fints. This works fine for evaluation, but should never be used
    if you bundle python-fints within a larger project. This might also not be acceptable
    by some banks.

    Click here to read more about the `registration process`_.


.. _registration process: https://www.hbci-zka.de/register/prod_register.htm
