PyFinTS
=======

This is a pure-python implementation of FinTS (formerly known as HBCI), a
online-banking protocol commonly supported by German banks.

Limitations
-----------

* Only FinTS 3.0 is supported
* Only PIN/TAN authentication is supported, no signature cards
* Only a number of reading operations are currently supported

Usage
-----

    import logging
    from fints3.client import FinTS3PinTanClient

    logging.basicConfig(level=logging.DEBUG)
    f = FinTS3PinTanClient(
        '123456789',  # Your bank's BLZ
        'myusername',
        'mypin',
        'https://mybank.com/…'  # endpoint, e.g.: https://hbci-pintan.gad.de/cgi-bin/hbciservlet
    )

    print(f.get_sepa_accounts())


Credits and License
-------------------

Author: Raphael Michel <mail@raphaelmichel.de>

License: LGPL

This is a quite close port of the [fints-hbci-php](https://github.com/mschindler83/fints-hbci-php)
implementation that was released by Markus Schindler under the MIT license.
Thanks for your work!
