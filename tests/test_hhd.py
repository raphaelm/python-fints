import pytest
from fints.hhd.flicker import parse, HHD_VERSION_13


# HITAN3:
#  'challenge' contains a HHD 1.3 code embedded in the normal text payload
#  field.
#  Example: 'CHLGUC  00312908881344731012345678900515,00CHLGTEXT0292Sie haben eine ...'
#    The code in NeedTANResponse._parse_tan_challenge extracts 
#     '2908881344731012345678900515,00'
#    from this, as a version 1.3 code. parse() should accept it
#    (start code: '88134473', IBAN: '1234567890', amount: '15,00')

def test_flicker_hhd13():
    flicker = parse('2908881344731012345678900515,00')

    assert flicker.version == HHD_VERSION_13
    assert flicker.lc == 29
    assert flicker.startcode.data == '88134473'
    assert flicker.de1.data == '1234567890'
    assert flicker.de2.data == '15,00'
    assert flicker.de3.data is None

    assert flicker.render() == '1204881344730512345678901531352C30303B'


# The old code in fints.hhd.flicker.clean would add a 0
def test_flicker_hhd13_old():
    flicker = parse('02908881344731012345678900515,00')

    assert flicker.version == HHD_VERSION_13
    assert flicker.lc == 29
    assert flicker.startcode.data == '88134473'

    assert flicker.render() == '1204881344730512345678901531352C30303B'


# From https://github.com/willuhn/hbci4java/blob/master/test/hbci4java/secmech/FlickerTest.java
#  Maybe we should be able to handle this and others?
@pytest.mark.xfail
def test_flicker_hhd13_hbci4java_1():
    flicker = parse('CHLGUC 002624088715131306389726041,00CHLGTEXT0244 Sie h')

    assert flicker.lc == 24
    assert flicker.startcode.data == '87151313'

    assert flicker.render() == '0F04871513130338972614312C30303B'
