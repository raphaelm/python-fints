import pytest
from fints.utils import decode_phototan_image


# HITAN3:
#  'challenge' contains a HHD 1.3 code embedded in the normal text payload
#  field.
#  Example: 'CHLGUC  00312908881344731012345678900515,00CHLGTEXT0292Sie haben eine ...'
#    The code in NeedTANResponse._parse_tan_challenge extracts
#     '2908881344731012345678900515,00'
#    from this, as a version 1.3 code. parse() should accept it
#    (start code: '88134473', IBAN: '1234567890', amount: '15,00')

# HITAN6:
# 'challenge' contains 4 fields:
#   2 bytes: mime type length
#   x bytes (see above): mime type
#   2 bytes: data length
#   y bytes: image data

CHALLENGE = b'\x00\timage/png\x0e\x82\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\xc8\x00\x00\x00\xc8\x08\x06\x00\x00\x00\xadX\xae\x9e\x00\x00\x00\x06bKGD\x00\xff\x00\xff\x00\xff\xa0\xbd\xa7\x93\x00\x00\x02MIDATx\x9c\xed\xdd\xb1\r\xc40\x0c\x04A\xea\xe1\xfe[\xf6w\xb0\x89\x023\x98\xa9@ \xb0Pxgf\xdeY\xec}W?o\xce9_?!\xb9\xdf\x9d\xdf\xd7\x0f\x80\xcd\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x1e;\xdaw\xdc\xef\xce\xf6\xfb\xf9A \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x9c\x99Y=T\xbd}G\xdb\x0e\xf9\x9d\xed\xf7\xf3\x83@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@x\xech\xdfq\xbf;\xdb\xef\xe7\x07\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81pff\xf5P\xf5\xf6\x1dm;\xe4w\xb6\xdf\xcf\x0f\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02\xe1\x0fp-(\x89A#\xd8\xc6\x00\x00\x00\x00IEND\xaeB`\x82'

def test_decode_phototan_image():
    data = decode_phototan_image(CHALLENGE)

    assert data["mime_type"] == "image/png"
    assert data["image"] == b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\xc8\x00\x00\x00\xc8\x08\x06\x00\x00\x00\xadX\xae\x9e\x00\x00\x00\x06bKGD\x00\xff\x00\xff\x00\xff\xa0\xbd\xa7\x93\x00\x00\x02MIDATx\x9c\xed\xdd\xb1\r\xc40\x0c\x04A\xea\xe1\xfe[\xf6w\xb0\x89\x023\x98\xa9@ \xb0Pxgf\xdeY\xec}W?o\xce9_?!\xb9\xdf\x9d\xdf\xd7\x0f\x80\xcd\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x1e;\xdaw\xdc\xef\xce\xf6\xfb\xf9A \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x08\x04\x82@ \x9c\x99Y=T\xbd}G\xdb\x0e\xf9\x9d\xed\xf7\xf3\x83@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@\x10\x08\x04\x81@x\xech\xdfq\xbf;\xdb\xef\xe7\x07\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81 \x10\x08\x02\x81pff\xf5P\xf5\xf6\x1dm;\xe4w\xb6\xdf\xcf\x0f\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02A \x10\x04\x02\xe1\x0fp-(\x89A#\xd8\xc6\x00\x00\x00\x00IEND\xaeB`\x82'


def _make_pain(version, bic='GENODE23X42', payments=1):
    import datetime
    from sepaxml import SepaTransfer

    sepa = SepaTransfer({'name': 'Test Sender', 'IBAN': 'DE111234567800000001', 'BIC': 'GENODE23X42',
                         'batch': False, 'currency': 'EUR'}, version)
    for i in range(payments):
        payment = {'name': 'Test Receiver', 'IBAN': 'DE111234567800000002', 'amount': 123,
                   'execution_date': datetime.date(1999, 1, 1), 'description': 'Old reason'}
        if bic:
            payment['BIC'] = bic
        sepa.add_payment(payment)
    return sepa.export()


def _remove_from_pain(pain, name):
    from lxml import etree

    root = etree.fromstring(pain)
    for element in root.xpath('//*[local-name()="{}"]'.format(name)):
        element.getparent().remove(element)
    return etree.tostring(root, xml_declaration=True, encoding='UTF-8')


@pytest.mark.parametrize("version, bic_tag", [('pain.001.001.03', 'BIC'), ('pain.001.001.09', 'BICFI')])
def test_modify_sepa_transfer_pain(version, bic_tag):
    from decimal import Decimal
    from lxml import etree
    from sepaxml.validation import try_valid_xml
    from fints.utils import modify_sepa_transfer_pain

    def values(xml, name):
        return [e.text for e in etree.fromstring(xml).xpath('//*[local-name()="{}"]'.format(name))]

    original = _make_pain(version)

    # Change amount and reason: control sums follow, message id is renewed, everything else stays
    changed = modify_sepa_transfer_pain(original, amount=Decimal('30'), reason='New reason')
    try_valid_xml(changed, version)
    assert values(changed, 'InstdAmt') == ['30.00']
    assert set(values(changed, 'CtrlSum')) == {'30.00'}
    assert values(changed, 'Ustrd') == ['New reason']
    assert values(changed, 'MsgId') != values(original, 'MsgId')
    assert values(changed, 'ReqdExctnDt') == values(original, 'ReqdExctnDt') or \
        values(changed, 'Dt') == values(original, 'Dt')

    # New IBAN without BIC removes the old recipient BIC (the debtor BIC stays)
    changed = modify_sepa_transfer_pain(original.decode(), iban='DE02120300000000202051')
    try_valid_xml(changed, version)
    assert 'DE02120300000000202051' in values(changed, 'IBAN')
    assert not etree.fromstring(changed).xpath('//*[local-name()="CdtrAgt"]')
    assert len(values(changed, bic_tag)) == 1

    # BIC for a message without recipient BIC: CdtrAgt is created with the tag of the schema version
    changed = modify_sepa_transfer_pain(_make_pain(version, bic=None), bic='COBADEFFXXX')
    try_valid_xml(changed, version)
    assert 'COBADEFFXXX' in values(changed, bic_tag)

    changed = modify_sepa_transfer_pain(original, endtoend_id='NEW-E2E-ID')
    try_valid_xml(changed, version)
    assert values(changed, 'EndToEndId') == ['NEW-E2E-ID']

    # Recipient name: only the creditor name changes, the debtor name stays
    changed = modify_sepa_transfer_pain(original, recipient_name='New Receiver')
    try_valid_xml(changed, version)
    assert 'New Receiver' in values(changed, 'Nm')
    assert 'Test Receiver' not in values(changed, 'Nm')
    assert 'Test Sender' in values(changed, 'Nm')

    # Reason for a message without remittance information: RmtInf/Ustrd is created
    changed = modify_sepa_transfer_pain(_remove_from_pain(original, 'RmtInf'), reason='New reason')
    try_valid_xml(changed, version)
    assert values(changed, 'Ustrd') == ['New reason']

    with pytest.raises(ValueError):
        modify_sepa_transfer_pain(_make_pain(version, payments=2), amount=Decimal('1'))


@pytest.mark.parametrize("version", ['pain.001.001.03', 'pain.001.001.09'])
def test_parse_sepa_transfer_pain(version):
    from decimal import Decimal
    from fints.models import Amount
    from fints.utils import modify_sepa_transfer_pain, parse_sepa_transfer_pain

    payment = parse_sepa_transfer_pain(_make_pain(version))
    assert payment.recipient_name == 'Test Receiver'
    assert payment.iban == 'DE111234567800000002'
    assert payment.bic == 'GENODE23X42'
    assert payment.amount == Amount(Decimal('1.23'), 'EUR')
    assert payment.reason == 'Old reason'
    assert payment.endtoend_id == 'NOTPROVIDED'

    # Reads back what modify_sepa_transfer_pain changed, also from a str
    changed = modify_sepa_transfer_pain(_make_pain(version), amount=Decimal('30'), reason='New reason', bic='COBADEFFXXX',
                                        endtoend_id='NEW-E2E-ID')
    payment = parse_sepa_transfer_pain(changed.decode())
    assert payment.amount == Amount(Decimal('30.00'), 'EUR')
    assert payment.reason == 'New reason'
    assert payment.bic == 'COBADEFFXXX'
    assert payment.endtoend_id == 'NEW-E2E-ID'

    assert parse_sepa_transfer_pain(_make_pain(version, bic=None)).bic is None

    # Missing values are None
    payment = parse_sepa_transfer_pain(_remove_from_pain(_make_pain(version), 'Amt'))
    assert payment.amount is None
    assert payment.recipient_name == 'Test Receiver'

    with pytest.raises(ValueError):
        parse_sepa_transfer_pain(_make_pain(version, payments=2))
