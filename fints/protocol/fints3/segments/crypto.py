# See FinTS_3.0_Security_Sicherheitsverfahren_HBCI_Rel_20130718_final_version.pdf
import time
from collections import OrderedDict

from . import FinTS3Segment


# See B.5.3
# Currently PINTAN only
class FinTS3CryptoHeader(FinTS3Segment):
    def __init__(self, customer=None, blz=None):
        self.elements = OrderedDict([
            ('head', OrderedDict([
                ('identifier', 'HNVSK'),
                ('counter', 998),  # See B.8
                ('version', 3)
            ])),
            ('profile', OrderedDict([
                ('mode', 'PIN'),
                ('version', 1)
            ])),
            ('function', 998),  # kinda magic, but this is according to the example E.3.1
            ('role', '1'),
            ('identification', OrderedDict([
                ('identifier', 1),
                ('cid', ''),  # according to the documentation we can ignore this
                ('part', 0)  # according to the documentation we can ignore this
            ])),
            ('datetime', OrderedDict([
                ('identifier', 1),  # Sicherheitszeitstempel
                ('date', time.strftime('%Y%m%d')),  # YYYYMMDD
                ('time', time.strftime('%H%M%S'))  # HHMMSS
            ])),
            # p. 191
            ('encryption', OrderedDict([
                ('usage', 2),  # Owner Symmetric (OSY)
                ('mode', 2),  # Cipher Block Chaining (CBC)
                ('algorithm', 13),  # 2-Key-Triple-DES
                ('algparams', b'NOKEY'),  # Do we care?
                ('algkeyidentifier', 6),  # Must be right, according to aqBanking!
                ('algparamidentifier', 1)  # Only possible value --> Clear text (IVC)
            ])),
            # p. 184
            ('keyname', OrderedDict([
                ('foo', 280),
                ('bank', blz),  # so-called Bankleitzahl
                ('customer', customer),  # Username, in Germany often the account number
                ('keytype', 'V'),  # Chiffrierschlüssel
                ('keynumber', 1),
                ('keyversion', 1)
            ])),
            ('compression', 0)  # No compression
        ])


# See B.5.4
class FinTS3CryptoBody(FinTS3Segment):
    def __init__(self, data=None):
        self.elements = OrderedDict([
            ('head', OrderedDict([
                ('identifier', 'HNVSD'),
                ('counter', 999),  # See B.8
                ('version', 1)
            ])),
            ('data', b'')
        ])

    def set_data(self, data):
        self.elements['data'] = bytes(data, 'ISO-8859-2')

    def get_data(self, data):
        return self.elements['data']

# See B.5.1
# class FinTS3SignatureHeader(FinTS3Segment):
