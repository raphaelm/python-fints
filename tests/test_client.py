from fints.client import FinTS3PinTanClient


def test_client_get_sepa_accounts(fints_server):
    f = FinTS3PinTanClient(
        '12345678',
        'test1',
        '1234',
        fints_server
    )

    with f:
        accounts = f.get_sepa_accounts()

    assert accounts
