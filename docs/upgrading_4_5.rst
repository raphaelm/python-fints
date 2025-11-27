Upgrading from python-fints 4.x to 5.x
======================================

Release 5.0 of this library was made to introduce breaking changes:

* When your bank no longer supports fetching MT940 bank statements, `get_transactions()` will transparently fall back
  to retrieve XML statements and convert them to dictionaries. While we tried to keep the most important fields in
  place, this will cause different output. Please verify that the new output does not cause issues in your application.

* When sending a credit transfer, you might now receive a `NeedVOPResponse` instead of a `NeedTANResponse` if there is
  no exact match of payer names. You can proceed with `approve_vop_response()` and will then receive your
  `NeedTANResponse` as usual.
