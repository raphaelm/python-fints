PyFinTS
=======

This is a pure-python implementation of FinTS (formerly known as HBCI), a
online-banking protocol commonly supported by German banks.


[Read our documentation for more info](https://python-fints.readthedocs.io)

Maintenance Status 
------------------

This project is maintained, but with limited capacity. Working on this is takes a lot of time and testing since all banks do things differently and once you move a part here, you break an unexpected one over there. Therefore: Bugs will only be fixed by me if they occur with a bank where I have an account. New features will only be developed if I need them. PRs will be merged if they either have a very low risk of breaking things elsewhere (e.g. purely adding new commands) or if I can test them. In any case, things might take a little time until I have the bandwidth to focus on them. Sorry about that :( 

Limitations
-----------

* Only FinTS 3.0 is supported
* Only PIN/TAN authentication is supported, no signature cards
* Only the following operations are supported:
  * Fetching bank statements
  * Fetching balances
  * Fetching holdings
  * SEPA transfers and debits (only with required TAN and with specific TAN methods)
* Supports Python 3.6+

Credits and License
-------------------

This library is maintained by Raphael Michel <mail@raphaelmichel.de>
and features major contributions by Henryk Plötz.

Further thanks for improving this library go out to:
Daniel Nowak, Patrick Braune, Mathias Dalheimer, Christopher Grebs, Markus Schindler, and many more.

License: LGPL
