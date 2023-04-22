Upgrading from python-fints 3.x to 4.x
======================================

Release 4.0 of this library was made to introduce a breaking change:

* You now need to register your application with the Deutsche Kreditwirtschaft (German banking association) and supply
  your assigned product IT when initializing the library.

The library used to have a built-in product ID that was used as a default if you didn't. This was very useful, but
Deutsche Kreditwirtschaft asked us to stop doing this, since it undermindes the whole point of the product registration.
The ID included in prior versions of the library will be deactivated at some point and stop working.
