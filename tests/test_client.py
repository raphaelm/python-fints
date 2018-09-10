from fints.client import FinTS3PinTanClient, TransactionResponse, NeedTANResponse, ResponseStatus
from fints.exceptions import FinTSClientPINError
from decimal import Decimal
import pytest

@pytest.fixture
def fints_client(fints_server):
    return FinTS3PinTanClient(
        '12345678',
        'test1',
        '1234',
        fints_server
    )

def test_get_sepa_accounts(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()

    assert accounts

def test_get_information(fints_client):
    with fints_client:
        information = fints_client.get_information()

    assert information["bank"]["name"] == 'Test Bank'

def test_pin_wrong(fints_server):
    client = FinTS3PinTanClient(
        '12345678',
        'test1',
        '99999',
        fints_server,
    )
    with pytest.raises(FinTSClientPINError):
        with client:
            pass

    assert client.pin.blocked

    with pytest.raises(Exception):
        with client:
            pass

    with pytest.raises(Exception, match="Refusing"):
        str(client.pin)

def test_resume(fints_client, fints_server):
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

def test_transfer_1step(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        a = fints_client.simple_sepa_transfer(
            accounts[0],
            'DE111234567800000002',
            'GENODE00TES',
            'Test Receiver',
            Decimal('1.23'),
            'Test Sender',
            'Test transfer 1step'
        )

        assert isinstance(a, TransactionResponse)
        assert a.status == ResponseStatus.SUCCESS

        assert a.responses[0].code == '0010'
        assert a.responses[0].text == "Transfer 1.23 to DE111234567800000002 re 'Test transfer 1step'"

def test_transfer_1step_regression(fints_client):
    # Passing a float is not officially supported, but should not fail with wrong values
    # Decimal(1.23) is Decimal('1.229999999999999982236431605997495353221893310546875')
    # which emphatically should not be cut to 122 cents.

    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        a = fints_client.simple_sepa_transfer(
            accounts[0],
            'DE111234567800000002',
            'GENODE00TES',
            'Test Receiver',
            1.23,
            'Test Sender',
            'Test transfer 1step'
        )

        assert isinstance(a, TransactionResponse)
        assert a.responses[0].text == "Transfer 1.23 to DE111234567800000002 re 'Test transfer 1step'"

def test_transfer_2step(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        a = fints_client.simple_sepa_transfer(
            accounts[0],
            'DE111234567800000002',
            'GENODE00TES',
            'Test Receiver',
            Decimal('2.34'),
            'Test Sender',
            'Test transfer 2step'
        )

        assert isinstance(a, NeedTANResponse)

        b = fints_client.send_tan(a, '123456')
        assert b.status == ResponseStatus.SUCCESS
        assert b.responses[0].text == "Transfer 2.34 to DE111234567800000002 re 'Test transfer 2step'"

def test_tan_wrong(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        a = fints_client.simple_sepa_transfer(
            accounts[0],
            'DE111234567800000002',
            'GENODE00TES',
            'Test Receiver',
            Decimal('2.34'),
            'Test Sender',
            'Test transfer 2step'
        )

        b = fints_client.send_tan(a, '99881')
        assert b.status == ResponseStatus.ERROR
