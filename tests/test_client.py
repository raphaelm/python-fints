from fints.client import FinTS3PinTanClient, TransactionResponse, NeedTANResponse, ResponseStatus, NeedRetryResponse
from fints.exceptions import FinTSClientPINError, FinTSClientTemporaryAuthError
from decimal import Decimal
import pytest


@pytest.fixture
def fints_client(fints_server):
    return FinTS3PinTanClient(
        '12345678',
        'test1',
        '1234',
        fints_server,
        product_id="TEST-123", product_version="1.2.3",
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
        product_id="TEST-123", product_version="1.2.3",
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


def test_pin_locked(fints_server):
    client = FinTS3PinTanClient(
        '12345678',
        'test1',
        '3938',
        fints_server,
        product_id="TEST-123", product_version="1.2.3",
    )
    with pytest.raises(FinTSClientTemporaryAuthError):
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
        dialog_id = fints_client._standing_dialog.dialog_id
        assert fints_client.bpd_version == 78

        d_data = fints_client.pause_dialog()

    c_data = fints_client.deconstruct(including_private=True)

    FinTS3PinTanClient(
        '12345678',
        'test1',
        '1234',
        fints_server,
        from_data=c_data,
        product_id="TEST-123", product_version="1.2.3",
    )
    assert system_id == fints_client.system_id

    with fints_client.resume_dialog(d_data):
        assert dialog_id == fints_client._standing_dialog.dialog_id
        assert fints_client.bpd_version == 78


def test_transfer_1step(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        a = fints_client.simple_sepa_transfer(
            accounts[0],
            'DE111234567800000002',
            'GENODE23X42',
            'Test Receiver',
            Decimal('1.23'),
            'Test Sender',
            'Test transfer 1step',
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
            'GENODE23X42',
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
            'GENODE23X42',
            'Test Receiver',
            Decimal('2.34'),
            'Test Sender',
            'Test transfer 2step'
        )

        assert isinstance(a, NeedTANResponse)

        b = fints_client.send_tan(a, '123456')
        assert b.status == ResponseStatus.SUCCESS
        assert b.responses[0].text == "Transfer 2.34 to DE111234567800000002 re 'Test transfer 2step'"


def test_transfer_2step_continue(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        a = fints_client.simple_sepa_transfer(
            accounts[0],
            'DE111234567800000002',
            'GENODE23X42',
            'Test Receiver',
            Decimal('3.42'),
            'Test Sender',
            'Test transfer 2step'
        )

        a_data = a.get_data()

        a_prime = NeedRetryResponse.from_data(a_data)

        b = fints_client.send_tan(a_prime, '123456')
        assert b.status == ResponseStatus.SUCCESS
        assert b.responses[0].text == "Transfer 3.42 to DE111234567800000002 re 'Test transfer 2step'"


def test_tan_wrong(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        a = fints_client.simple_sepa_transfer(
            accounts[0],
            'DE111234567800000002',
            'GENODE23X42',
            'Test Receiver',
            Decimal('3.33'),
            'Test Sender',
            'Test transfer 2step'
        )

        b = fints_client.send_tan(a, '99881')
        assert b.status == ResponseStatus.ERROR


def test_tan_hhduc(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        a = fints_client.simple_sepa_transfer(
            accounts[0],
            'DE111234567800000002',
            'GENODE23X42',
            'Test Receiver',
            Decimal('5.23'),
            'Test Sender',
            'Test transfer hhduc 2step'
        )

        from fints.hhd.flicker import parse
        assert a.challenge == 'Geben Sie den Startcode als TAN an'
        flicker = parse(a.challenge_hhduc)

        b = fints_client.send_tan(a, flicker.startcode.data)
        assert b.status == ResponseStatus.SUCCESS


def test_get_transactions(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()

        transactions = fints_client.get_transactions(accounts[0])

        assert len(transactions) == 3
        assert transactions[0].data['amount'].amount == Decimal('182.34')
