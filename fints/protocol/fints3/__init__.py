from .segments.crypto import FinTS3CryptoHeader, FinTS3CryptoBody
from .segments.message import FinTS3Footer, FinTS3Header
from .utils import segments_to_ascii


class FinTS3:
    version = 300

    def __init__(self):
        self.segments = []

        # global segment counter; used for "sub-segments" in the crypto body
        self.i = 1

        # these segments are special and have to be controlled by this class
        self.header = FinTS3Header(self.version)
        self.footer = FinTS3Footer()

    def append(self, segment):
        self.segments.append(segment)

    def to_ascii(self):
        self.i, ascii = segments_to_ascii(self.segments)
        size = len(ascii)

        # footer stuff for correct size calculation
        self.footer.set_counter(self.i + 1)
        footer = self.footer.to_ascii() + "'"
        size += len(footer)

        # prepend header with correct size
        self.header.set_counter(1)
        self.header.set_size(size + 1)
        ascii = self.header.to_ascii() + "'" + ascii

        # append footer
        ascii += footer

        return ascii


class FinTS3PinTan(FinTS3):
    def __init__(self, customer, blz, server=None):
        self.server = server

        super().__init__()

        self.crypto_header = FinTS3CryptoHeader(customer, blz)
        self.crypto_body = FinTS3CryptoBody()
        self.append(self.crypto_header)
        self.append(self.crypto_body)

    def append(self, segment):
        self.segments.append(segment)

    def to_ascii(self):
        # create the crypto body
        self.i, ascii = segments_to_ascii(self.segments, self.i)
        self.crypto_body.set_data(ascii)

        return super().to_ascii()
