Upgrading from python-fints 1.x to 2.x
======================================

This library has seen a major rewrite in version 2.0 and the API has changed in a lot of places. These are the most
important changes to know:

* The ``get_statement`` method was renamed to ``get_transactions``. → :ref:`transactions`

* The ``start_simple_sepa_transfer`` method was renamed to ``simple_sepa_transfer`` and no longer takes a TAN method
  and TAN medium description as an argument. → :ref:`transfers`

* The ``start_sepa_transfer`` method was renamed to ``sepa_transfer`` and no longer takes a TAN method and TAN
  medium description as an argument. The new parameter ``pain_descriptor`` should be passed with the version of the
  PAIN format, e.g. ``urn:iso:std:iso:20022:tech:xsd:pain.001.001.03``. → :ref:`transfers`

* The ``start_sepa_debit`` method was renamed to ``sepa_debit`` and no longer takes a TAN method and TAN
  medium description as an argument. The new parameter ``pain_descriptor`` should be passed with the version of the
  PAIN format, e.g. ``urn:iso:std:iso:20022:tech:xsd:pain.008.003.01``. Also, a new parameter ``cor1`` is optionally
  available. → :ref:`debits`

* Working with TANs has changed a lot. ``get_tan_methos`` has been renamed to ``get_tan_mechanisms`` and has a new
  return data type. The chosen TAN method is now set on a client level with ``set_tan_mechanism`` and
  ``set_tan_medium``. You can find more information in the chapter :ref:`tans` and a full example in the chapter
  :ref:`transfers`.

* Debug logging output now contains parsed syntax structures instead of data blobs and is much easier to read.

* A new parser for FinTS has been added that is more robust and performs more validation.

In exchange, you get a couple of great new features:

* A new method :func:`fints.client.FinTS3Client.get_information` was added. → :ref:`information`

* It is now possible to serialize and store the state of the client to enable multi-step operations in a stateless
  environment. → :ref:`client-state`
