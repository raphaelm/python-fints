Upgrading from python-fints 2.x to 3.x
======================================

Release 3.0 of this library was made to adjust to changes made by the banks as part of their PSD2 implementation
in 2019. Here's what you should know when porting your code:

* A TAN can now be required for dialog initialization. In this case, ``client.init_tan_response`` will contain a
  ``NeedTANResponse``.

* Basically every method of the client class can now return a ``NeedTANResponse``, so you should always expect this
  case and handle it gracefully.

* Since everything can require a TAN, everything requires a standing dialog. Issuing interactive commands outside of a
  ``with client:`` statement is now deprecated. It still might work in very few cases, so we didn't disable it, but we
  do not support it any longer. This affects you mostly when you work with this on a Python REPL or e.g. in a Notebook.
