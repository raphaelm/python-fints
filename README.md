PyFinTS
=======

This is a pure-python implementation of FinTS (formerly known as HBCI), a
online-banking protocol commonly supported by German banks.


[Read our documentation for more info](https://python-fints.readthedocs.io)

Limitations
-----------

* Only FinTS 3.0 is supported
* Only PIN/TAN authentication is supported, no signature cards
* Only the following operations are supported:
  * Fetching bank statements
  * Fetching balances
  * Fetching holdings
  * SEPA transfers and debits (only with required TAN and with specific TAN methods)
* Supports Python 3.4+

Credits and License
-------------------

This library is maintained by Raphael Michel <mail@raphaelmichel.de>
and features major contributions by Henryk Plötz.

Further thanks for improving this library go out to:
Daniel Nowak, Patrick Braune, Mathias Dalheimer, Christopher Grebs, Markus Schindler, and many more.

License: LGPL
