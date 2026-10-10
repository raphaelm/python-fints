#!/usr/bin/env python3
"""
Sample: Consorsbank (BLZ 76030080) with python-fints.

Demonstrates fetching transactions and making SEPA transfers with
photoTAN (QR code) authentication.

Consorsbank requires three compatibility fixes (see PR #209):
  1. security_method_version=2 for two-step TAN
  2. Full account details in KTI1.from_sepa_account
  3. force_twostep_tan for segments the bank requires TAN on
     despite HIPINS reporting otherwise

Additionally, Consorsbank attaches the TAN-required response (0030)
to the command segment (HKCCS) rather than the HKTAN segment, which
is handled by Fix 4 in this branch.

Usage:
    pip install python-fints python-dotenv
    python sample_consorsbank.py

Environment variables (or .env file):
    FINTS_BLZ=76030080
    FINTS_USER=<your user id>
    FINTS_PIN=<your PIN>
    FINTS_SERVER=https://brokerage-hbci.consorsbank.de/hbci
    FINTS_PRODUCT_ID=<your registered product id>
    MY_IBAN=<IBAN of the account to use>
"""

import os
import sys
import logging
import subprocess
from datetime import date, timedelta
from decimal import Decimal

from fints.client import FinTS3PinTanClient, NeedTANResponse

logging.basicConfig(level=logging.WARNING)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


def handle_tan(response, client):
    """Handle TAN challenges including photoTAN with QR code image."""
    while isinstance(response, NeedTANResponse):
        print(f"\nTAN required: {response.challenge}")

        # photoTAN / QR code image
        if response.challenge_matrix:
            mime_type, image_data = response.challenge_matrix
            ext = ".png" if "png" in mime_type else ".jpg"
            img_path = f"tan_challenge{ext}"
            with open(img_path, "wb") as f:
                f.write(image_data)
            print(f"  QR code saved to {img_path} ({len(image_data)} bytes)")
            # On macOS: subprocess.Popen(["open", img_path])
            # On Linux: subprocess.Popen(["xdg-open", img_path])
            tan = input("Scan the QR code and enter TAN: ")

        # Flicker / HHD UC challenge
        elif response.challenge_hhduc:
            print(f"  HHD UC data available")
            tan = input("Enter TAN: ")

        # Decoupled (app confirmation)
        elif response.decoupled:
            input("Confirm in your banking app, then press ENTER: ")
            tan = ""

        # Manual TAN entry
        else:
            tan = input("Enter TAN: ")

        response = client.send_tan(response, tan)
    return response


def main():
    blz = os.environ.get("FINTS_BLZ", "76030080")
    user = os.environ["FINTS_USER"]
    pin = os.environ["FINTS_PIN"]
    server = os.environ.get("FINTS_SERVER", "https://brokerage-hbci.consorsbank.de/hbci")
    product_id = os.environ.get("FINTS_PRODUCT_ID")
    my_iban = os.environ.get("MY_IBAN")

    client = FinTS3PinTanClient(
        bank_identifier=blz,
        user_id=user,
        pin=pin,
        server=server,
        product_id=product_id,
        # Consorsbank reports HKKAZ:N and HKSAL:N in HIPINS but actually
        # requires TAN for these operations.  HKCCS always requires TAN.
        force_twostep_tan={"HKKAZ", "HKSAL"},
    )

    # Select photoTAN mechanism (Consorsbank uses 900)
    if not client.get_current_tan_mechanism():
        client.fetch_tan_mechanisms()
    client.set_tan_mechanism("900")

    with client:
        if client.init_tan_response:
            handle_tan(client.init_tan_response, client)

        # --- Fetch accounts ---
        accounts = client.get_sepa_accounts()
        if isinstance(accounts, NeedTANResponse):
            accounts = handle_tan(accounts, client)

        print("Accounts:")
        for a in accounts:
            print(f"  {a.iban}  (BIC: {a.bic})")

        # Select account
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
        if isinstance(res, NeedTANResponse):
            res = handle_tan(res, client)

        if res:
            print(f"Found {len(res)} transactions:")
            for t in res[-5:]:  # show last 5
                d = t.data
                amt = d.get("amount")
                amount_str = f"{amt.amount:>10.2f} {amt.currency}" if amt else ""
                print(f"  {d.get('date')}  {amount_str}  {d.get('applicant_name', '')}")
        else:
            print("No transactions found.")

        # --- SEPA Transfer (uncomment to use) ---
        # res = client.simple_sepa_transfer(
        #     account=account,
        #     iban="DE89370400440532013000",
        #     bic="COBADEFFXXX",
        #     recipient_name="Max Mustermann",
        #     amount=Decimal("1.00"),
        #     account_name="Your Name",
        #     reason="Test transfer",
        # )
        # if isinstance(res, NeedTANResponse):
        #     res = handle_tan(res, client)
        # print(f"Transfer result: {res.status} {res.responses}")

    print("\nDone!")


if __name__ == "__main__":
    main()
