PyFinTS
=======

This is a pure-python implementation of FinTS (formerly known as HBCI), a
online-banking protocol commonly supported by German banks.

Limitations
-----------

* Only FinTS 3.0 is supported
* Only PIN/TAN authentication is supported, no signature cards
* Only a number of reading operations are currently supported
* Supports Python 3.4+

Banks tested:

* GLS Bank eG
* Triodos Bank
* BBBank eG
* Postbank
* [1822direkt](https://www.1822direkt.de/service/zugang-zum-konto/softwarebanking-mit-hbci/), including access to holding accounts
* Sparkasse
* Ing-Diba
* CortalConsors, including access to holding accounts
* DKB
* NIBC Direct
* Wüstenrot
* comdirect, including access to holding accounts

Usage
-----

```python
import logging
from datetime import date
from fints.client import FinTS3PinTanClient

logging.basicConfig(level=logging.DEBUG)
f = FinTS3PinTanClient(
    '123456789',  # Your bank's BLZ
    'myusername',
    'mypin',
    'https://mybank.com/…'  # endpoint, e.g.: https://hbci-pintan.gad.de/cgi-bin/hbciservlet
                            # for German banks, see http://www.hbci-zka.de/institute/institut_auswahl.htm
)

accounts = f.get_sepa_accounts()
print(accounts)
# [SEPAAccount(iban='DE12345678901234567890', bic='ABCDEFGH1DEF', accountnumber='123456790', subaccount='',
#              blz='123456789')]

statement = f.get_statement(accounts[0], date(2016, 12, 1), date.today())
print([t.data for t in statement])
# The statement is a list of transaction objects as parsed by the mt940 parser, see
# https://mt940.readthedocs.io/en/latest/mt940.html#mt940.models.Transaction
# for documentation. Most information is contained in a dict accessible via their
# ``data`` property

# for retrieving the holdings of an account:
holdings = f.get_holdings(accounts[0])
# holdings contains a list of namedtuple values containing ISIN, name,
# market_value, pieces, total_value and valuation_date as parsed from
# the MT535 message.
```

Credits and License
-------------------

Author: Raphael Michel <mail@raphaelmichel.de>

License: LGPL

This is a quite close port of the [fints-hbci-php](https://github.com/mschindler83/fints-hbci-php)
implementation that was released by Markus Schindler under the MIT license.
Thanks for your work!
