from fints.client import FinTS3PinTanClient, TransactionResponse, NeedTANResponse, ResponseStatus, NeedRetryResponse
from fints.exceptions import FinTSClientPINError, FinTSClientTemporaryAuthError, FinTSUnsupportedOperation
from fints.formals import StandingOrderTimeUnit1
from fints.models import VirtualDate
from decimal import Decimal
import datetime
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


def test_get_standing_orders(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()

        standing_orders = fints_client.get_standing_orders(accounts[0])

        assert len(standing_orders) == 2
        assert standing_orders[0].task_id == 'ORDER1'
        assert standing_orders[0].standing_order_details.interval == 1
        assert b'Max Vermieter' in standing_orders[0].sepa_pain_message
        assert str(standing_orders[1].standing_order_details.last_execution_date) == '2027-04-31'
        assert standing_orders[1].suspension.annually_recurring is False
        assert standing_orders[1].suspension.suspension_end.isoformat() == '2025-11-30'
        assert standing_orders[1].task_cancelable is True


def test_get_standing_order_parameters(fints_client):
    with fints_client:
        fints_client.get_sepa_accounts()

    hicdes = fints_client.bpd.find_segment_first('HICDES').parameter
    hicdes.months = '0102030612'
    hicdes.weeks = '0102'
    hicdes.execution_days_month = '01159899'
    hicdes.execution_days_week = '12345'

    parameters = fints_client.get_standing_order_parameters()

    assert parameters['create'] == {
        'months': [1, 2, 3, 6, 12],
        'weeks': [1, 2],
        'execution_days_month': [1, 15, 98, 99],
        'execution_days_week': [1, 2, 3, 4, 5],
        'min_advance_notice': 1,
        'max_advance_notice': 3650,
    }
    # The test bank allows all intervals and days for changes, but no weekly standing orders
    assert parameters['change']['months'] == list(range(1, 13))
    assert parameters['change']['execution_days_month'] == list(range(1, 31)) + [97, 98, 99]
    assert parameters['change']['weeks'] == []
    assert parameters['change']['execution_days_week'] == []


def test_get_standing_order_parameters_unsupported(fints_client):
    with fints_client:
        fints_client.get_sepa_accounts()

    # Bank does not support changing standing orders
    fints_client.bpd.segments = [s for s in fints_client.bpd.segments if s.header.type != 'HICDNS']

    parameters = fints_client.get_standing_order_parameters()

    assert parameters['create'] is not None
    assert parameters['change'] is None


def test_delete_standing_order(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        standing_orders = fints_client.get_standing_orders(accounts[0])

        res = fints_client.delete_standing_order(accounts[0], standing_orders[0])

        assert isinstance(res, TransactionResponse)
        assert res.status == ResponseStatus.SUCCESS
        assert res.responses[0].code == '0020'
        assert res.responses[0].text == 'SEPA-Dauerauftrag ORDER1 gelöscht'


def test_delete_standing_order_scheduled_not_allowed(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        standing_orders = fints_client.get_standing_orders(accounts[0])

        with pytest.raises(FinTSUnsupportedOperation):
            fints_client.delete_standing_order(accounts[0], standing_orders[0], datetime.date(2030, 1, 1))


def test_create_standing_order(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()

        res = fints_client.simple_create_standing_order(
            accounts[0],
            'DE111234567800000002',
            'GENODE23X42',
            'Test Receiver',
            Decimal('1.23'),
            'Test Sender',
            'Test standing order',
            datetime.date(2030, 1, 31),
            StandingOrderTimeUnit1.MONTHLY,
            1,
            31,
            last_execution_date=VirtualDate(2030, 4, 31),
        )

        assert isinstance(res, TransactionResponse)
        assert res.status == ResponseStatus.SUCCESS
        assert res.responses[0].code == '0020'
        assert res.responses[0].text == 'SEPA-Dauerauftrag eingerichtet 20300131:M:1:31:20300431'
        assert res.data['task_id'] == 'ORDER3'


def test_create_standing_order_custom_pain(fints_client):
    from sepaxml import SepaTransfer

    with fints_client:
        accounts = fints_client.get_sepa_accounts()

        sepa = SepaTransfer({'name': 'Test Sender', 'IBAN': accounts[0].iban, 'BIC': accounts[0].bic,
                             'batch': False, 'currency': 'EUR'}, 'pain.001.001.03')
        sepa.add_payment({'name': 'Test Receiver', 'IBAN': 'DE111234567800000002', 'amount': 123,
                          'execution_date': datetime.date(1999, 1, 1), 'description': 'Test standing order'})

        # sepaxml exports bytes, which are accepted as well as str
        res = fints_client.create_standing_order(
            accounts[0], sepa.export(), datetime.date(2030, 1, 15), StandingOrderTimeUnit1.MONTHLY, 1, 15,
        )

        assert res.status == ResponseStatus.SUCCESS
        assert res.responses[0].text == 'SEPA-Dauerauftrag eingerichtet 20300115:M:1:15'


def test_create_standing_order_weekly_not_supported(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()

        with pytest.raises(FinTSUnsupportedOperation):
            fints_client.simple_create_standing_order(
                accounts[0],
                'DE111234567800000002',
                'GENODE23X42',
                'Test Receiver',
                Decimal('1.23'),
                'Test Sender',
                'Test standing order',
                datetime.date(2030, 1, 7),
                StandingOrderTimeUnit1.WEEKLY,
                1,
                1,
            )


def test_change_standing_order(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        standing_orders = fints_client.get_standing_orders(accounts[0])

        res = fints_client.simple_change_standing_order(
            accounts[0], standing_orders[0], amount=Decimal('900'), execution_day=15,
        )

        assert isinstance(res, TransactionResponse)
        assert res.status == ResponseStatus.SUCCESS
        assert res.responses[0].text == 'SEPA-Dauerauftrag ORDER1 geändert 900.00 20250101:M:1:15'
        assert res.data['task_id'] == 'ORDER1B'
        assert res.data['task_id_old'] == 'ORDER1'


def test_change_standing_order_custom_pain(fints_client):
    from fints.utils import modify_sepa_transfer_pain

    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        standing_orders = fints_client.get_standing_orders(accounts[0])
        order = standing_orders[1]
        details = order.standing_order_details

        pain = modify_sepa_transfer_pain(order.sepa_pain_message, amount=Decimal('30')).decode()
        res = fints_client.change_standing_order(
            accounts[0], order, pain,
            details.first_execution_date, details.time_unit, details.interval, details.execution_day,
            last_execution_date=details.last_execution_date,
        )

        assert res.status == ResponseStatus.SUCCESS
        assert res.responses[0].text == 'SEPA-Dauerauftrag ORDER2 geändert 30.00 20250215:M:3:15:20270431'


def test_change_standing_order_remove_last_execution_date(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        standing_orders = fints_client.get_standing_orders(accounts[0])

        res = fints_client.simple_change_standing_order(accounts[0], standing_orders[1], remove_last_execution_date=True)

        assert res.status == ResponseStatus.SUCCESS
        assert res.responses[0].text == 'SEPA-Dauerauftrag ORDER2 geändert 25.50 20250215:M:3:15'

        with pytest.raises(ValueError):
            fints_client.simple_change_standing_order(
                accounts[0], standing_orders[1], last_execution_date=datetime.date(2030, 1, 15),
                remove_last_execution_date=True,
            )


def test_change_standing_order_unchanged_details_omitted(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        standing_orders = fints_client.get_standing_orders(accounts[0])
        # Banks allowing several scheduled changes must not receive unchanged, changeable details
        fints_client.bpd.find_segment_first('HICDNS').parameter.max_scheduled_changes = 2

        res = fints_client.simple_change_standing_order(accounts[0], standing_orders[0], amount=Decimal('900'))

        assert res.responses[0].text == 'SEPA-Dauerauftrag ORDER1 geändert 900.00 '


def test_change_standing_order_weekly_not_supported(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        standing_orders = fints_client.get_standing_orders(accounts[0])

        with pytest.raises(FinTSUnsupportedOperation):
            fints_client.simple_change_standing_order(
                accounts[0], standing_orders[0], time_unit=StandingOrderTimeUnit1.WEEKLY, execution_day=1,
            )


def test_change_standing_order_scheduled_not_allowed(fints_client):
    with fints_client:
        accounts = fints_client.get_sepa_accounts()
        standing_orders = fints_client.get_standing_orders(accounts[0])

        with pytest.raises(FinTSUnsupportedOperation):
            fints_client.simple_change_standing_order(
                accounts[0], standing_orders[0], amount=Decimal('900'), execution_date=datetime.date(2030, 1, 1),
            )
