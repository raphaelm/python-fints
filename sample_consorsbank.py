#!/usr/bin/env python3
"""
Sample: Consorsbank (BLZ 76030080) with python-fints.

Demonstrates fetching accounts/transactions and making a SEPA transfer with
either of Consorsbank's two current TAN methods.

TAN methods
-----------
Consorsbank advertises two two-step TAN mechanisms:

* **901 "Consorsbank/myPrivateBank App"** (``zka_id = "Decoupled"``) — the new
  Consorsbank App. Login asks for a *typed* 9-digit TAN generated in the app;
  a SEPA transfer is *approved in the app* (decoupled), no TAN is typed.
* **900 "SecurePlus TAN Generator"** (``zka_id = "photoTAN"``) — login needs no
  TAN (the bank answers the dialog-init with ``3076``); a SEPA transfer returns
  an order-bound **photoTAN QR image** (``response.challenge_matrix``) that is
  scanned, after which the resulting TAN is typed.

Both were exercised end-to-end against Consorsbank. A real SEPA transfer with
mechanism ``901`` was accepted and booked.

.. note::
   The old **SecurePlus *App*** (the smartphone app, distinct from the
   SecurePlus *TAN-generator device*) was shut down for Consorsbank online
   banking on **2026-04-25**; since then it returns "TAN-Verfahren ungültig"
   and any TAN it produces — including ones scanned from the ``900`` photoTAN
   QR — is rejected with ``9941 TAN ungültig``. Use the new **Consorsbank App**
   (``901``) or the **physical SecurePlus TAN-generator device** (``900``).
   The ``900`` code path here is correct; only the decommissioned app's TAN is
   refused by the bank. (Source: kritische-anleger.de SecurePlus-App shutdown
   report, and the official Consorsbank HBCI FAQ.)

Protocol quirks handled by python-fints (see PR #209 and the login-SCA fix)
--------------------------------------------------------------------------
1. ``security_method_version=2`` for two-step TAN.
2. Full account details in ``KTI1.from_sepa_account``.
3. ``force_twostep_tan`` for segments the bank requires a TAN on despite
   reporting otherwise in HIPINS (otherwise: ``9075``).
4. The TAN-required response ``0030`` is attached to the **command segment**
   (``HKCCS``) instead of ``HKTAN``.
5. The **login** strong-customer-authentication response ``0030`` is attached
   to the **HKIDN** segment of the dialog-init, not ``HKTAN``. Without
   detecting it, the next command aborts the dialog with ``9800/9120``.
6. For decoupled app approval, Consorsbank returns ``0030`` **together with**
   ``3955`` ("Sicherheitsfreigabe erfolgt über anderen Kanal"). python-fints
   now flags the challenge as ``decoupled`` whenever ``3955`` is present.

What the user sees with the Consorsbank App (mechanism 901)
-----------------------------------------------------------
* **Login**: the bank asks for a *typed* TAN. Open the Consorsbank App,
  generate the (9-digit) TAN and type it in. ``response.decoupled`` is False.
* **SEPA transfer**: the bank pushes the order to the app for approval.
  ``response.decoupled`` is True; the user approves in the app and the client
  polls until the bank confirms — no TAN is typed.

Usage:
    pip install python-fints python-dotenv
    python sample_consorsbank.py

Environment variables (or .env file):
    FINTS_BLZ=76030080
    FINTS_USER=<your user id>
    FINTS_PIN=<your PIN>
    FINTS_SERVER=https://brokerage-hbci.consorsbank.de/hbci
    FINTS_PRODUCT_ID=<your registered product id>
    FINTS_TAN_MECHANISM=901          # 901 = Consorsbank App, 900 = SecurePlus generator
    MY_IBAN=<IBAN of the account to use>
    # To actually send money, set all of these:
    TRANSFER_TO_IBAN=<recipient IBAN>
    TRANSFER_TO_NAME=<recipient name>
    TRANSFER_AMOUNT=1.00
    TRANSFER_REASON=Test transfer
"""

import os
import time
import logging
from datetime import date, timedelta
from decimal import Decimal

from fints.client import FinTS3PinTanClient, NeedTANResponse, NeedVOPResponse

logging.basicConfig(level=logging.WARNING)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def handle_tan(response, client):
    """Resolve TAN / VoP / decoupled challenges.

    * Decoupled (e.g. Consorsbank App): the user approves the order inside the
      banking app; we poll with ``send_tan`` until the bank confirms.
    * photoTAN / QR: an image is shown to scan, then the TAN is typed.
    * Plain: the user types the TAN shown by the app/generator.
    """
    while isinstance(response, (NeedTANResponse, NeedVOPResponse)):
        if isinstance(response, NeedVOPResponse):
            # Verification of Payee result; approve and continue.
            response = client.approve_vop_response(response)
            continue

        print(f"\nTAN required: {response.challenge}")

        # Decoupled app approval (Consorsbank App): no TAN is typed.
        if response.decoupled:
            input("Approve the request in your Consorsbank App, then press ENTER... ")
            # Poll the bank until the decoupled approval is registered.
            response = client.send_tan(response, "")
            while isinstance(response, NeedTANResponse) and response.decoupled:
                time.sleep(4)
                response = client.send_tan(response, "")
            continue

        # photoTAN / QR code image (e.g. SecurePlus generator).
        if response.challenge_matrix:
            mime_type, image_data = response.challenge_matrix
            ext = ".png" if "png" in mime_type else ".jpg"
            img_path = f"tan_challenge{ext}"
            with open(img_path, "wb") as f:
                f.write(image_data)
            print(f"  Challenge image saved to {img_path} ({len(image_data)} bytes)")
            tan = input("Scan the image and enter the TAN: ")
        else:
            # Plain typed TAN (e.g. Consorsbank App login TAN, 9 digits).
            tan = input("Enter the TAN from your app/generator: ")

        response = client.send_tan(response, tan)

    return response


def main():
    blz = os.environ.get("FINTS_BLZ", "76030080")
    user = os.environ["FINTS_USER"]
    pin = os.environ["FINTS_PIN"]
    server = os.environ.get("FINTS_SERVER", "https://brokerage-hbci.consorsbank.de/hbci")
    product_id = os.environ.get("FINTS_PRODUCT_ID")
    mechanism = os.environ.get("FINTS_TAN_MECHANISM", "901")
    my_iban = os.environ.get("MY_IBAN")

    client = FinTS3PinTanClient(
        bank_identifier=blz,
        user_id=user,
        pin=pin,
        server=server,
        product_id=product_id,
        # Consorsbank reports HKKAZ:N / HKSAL:N in HIPINS but actually requires
        # a TAN for them; HKCCS always requires a TAN.
        force_twostep_tan={"HKKAZ", "HKSAL"},
    )

    # 901 = Consorsbank App (current), 900 = physical SecurePlus TAN generator.
    if not client.get_current_tan_mechanism():
        client.fetch_tan_mechanisms()
    client.set_tan_mechanism(mechanism)

    with client:
        # Login strong-customer-authentication (typed TAN with the app).
        if client.init_tan_response:
            handle_tan(client.init_tan_response, client)

        # --- Fetch accounts ---
        accounts = client.get_sepa_accounts()
        if isinstance(accounts, NeedTANResponse):
            accounts = handle_tan(accounts, client)

        print("Accounts:")
        for a in accounts:
            print(f"  {a.iban}  (BIC: {a.bic})")

        if my_iban:
            account = next((a for a in accounts if a.iban == my_iban), None)
            if not account:
                print(f"Account {my_iban} not found")
                return
        else:
            account = accounts[0]
        print(f"\nUsing account: {account.iban}")

        # --- Fetch transactions ---
        print("\nFetching transactions (last 30 days)...")
        start_date = date.today() - timedelta(days=30)
        res = client.get_transactions(account, start_date=start_date)
        if isinstance(res, (NeedTANResponse, NeedVOPResponse)):
            res = handle_tan(res, client)
        if res:
            print(f"Found {len(res)} transactions; showing last 5:")
            for t in res[-5:]:
                d = t.data
                amt = d.get("amount")
                amount_str = f"{amt.amount:>10.2f} {amt.currency}" if amt else ""
                print(f"  {d.get('date')}  {amount_str}  {d.get('applicant_name', '')}")
        else:
            print("No transactions found.")

        # --- SEPA transfer (approved in the Consorsbank App) ---
        to_iban = os.environ.get("TRANSFER_TO_IBAN")
        if to_iban:
            print(f"\nSubmitting SEPA transfer to {to_iban} ...")
            res = client.simple_sepa_transfer(
                account=account,
                iban=to_iban,
                bic=os.environ.get("TRANSFER_TO_BIC", ""),
                recipient_name=os.environ["TRANSFER_TO_NAME"],
                amount=Decimal(os.environ.get("TRANSFER_AMOUNT", "1.00")),
                account_name=os.environ.get("TRANSFER_FROM_NAME", user),
                reason=os.environ.get("TRANSFER_REASON", "Test transfer"),
            )
            # The bank pushes the order to the Consorsbank App for approval.
            res = handle_tan(res, client)
            print(f"Transfer result: {getattr(res, 'status', None)} {getattr(res, 'responses', None)}")
        else:
            print("\n(Set TRANSFER_TO_IBAN/TRANSFER_TO_NAME to perform a transfer.)")

    print("\nDone!")


if __name__ == "__main__":
    main()
