from fints.client import FinTS3PinTanClient
import pytest

@pytest.fixture
def fints_client(fints_server):
    return FinTS3PinTanClient(
        '12345678',
        'test1',
        '1234',
        fints_server
    )

def test_client_get_sepa_accounts(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()

    assert accounts

def test_client_resume(fints_client, fints_server):
    with fints_client:
        system_id = fints_client.system_id
        dialog_id = fints_client._standing_dialog.dialogue_id
        assert fints_client.bpd_version == 78

        d_data = fints_client.pause_dialog()

    c_data = fints_client.get_data(including_private=True)

    client2 = FinTS3PinTanClient(
        '12345678',
        'test1',
        '1234',
        fints_server,
        set_data=c_data
    )
    assert system_id == fints_client.system_id

    with fints_client.resume_dialog(d_data):
        assert dialog_id == fints_client._standing_dialog.dialogue_id
        assert fints_client.bpd_version == 78
