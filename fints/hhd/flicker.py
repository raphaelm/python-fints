# Inspired by:
# https://github.com/willuhn/hbci4java/blob/master/src/org/kapott/hbci/manager/FlickerCode.java
# https://6xq.net/flickercodes/
# https://wiki.ccc-ffm.de/projekte:tangenerator:start#flickercode_uebertragung
import math
import re
import time

HHD_VERSION_13 = 13
HHD_VERSION_14 = 14
LC_LENGTH_HHD14 = 3
LC_LENGTH_HHD13 = 2
LDE_LENGTH_DEFAULT = 2
LDE_LENGTH_SPARDA = 3
BIT_ENCODING = 6  # Position of encoding bit
BIT_CONTROLBYTE = 7  # Position of bit that tells if there are a control byte
ENCODING_ASC = 1
ENCODING_BCD = 2


def parse(code):
    code = clean(code)
    try:
        return FlickerCode(code, HHD_VERSION_14)
    except:
        try:
            return FlickerCode(code, HHD_VERSION_14, LDE_LENGTH_SPARDA)
        except:
            return FlickerCode(code, HHD_VERSION_13)


def clean(code):
    if code.startswith('@'):
        code = code[res.challenge_hhd_uc.index('@', 2) + 1:]
    code = code.replace(" ", "").strip()
    if "CHLGUC" in code and "CHLGTEXT" in code:
        # Sometimes, HHD 1.3 codes are not transfered in the challenge field but in the free text,
        # contained in CHLGUCXXXX<code>CHLGTEXT
        code = "0" + code[code.index("CHLGUC") + 11:code.index("CHLGTEXT")]
    return code


def bit_sum(num, bits):
    s = 0
    for i in range(bits):
        s += num & (1 << i)
    return s


def digitsum(n):
    q = 0
    while n != 0:
        q += n % 10
        n = math.floor(n / 10)
    return q


def h(num, l):
    return hex(num).upper()[2:].zfill(l)


def asciicode(s):
    return ''.join(h(ord(c), 2) for c in s)


def swap_bytes(s):
    b = ""
    for i in range(0, len(s), 2):
        b += s[i + 1]
        b += s[i]
    return b


class FlickerCode:
    def __init__(self, code, version, lde_len=LDE_LENGTH_DEFAULT):
        self.version = version
        self.lc = None
        self.startcode = Startcode()
        self.de1 = DE(lde_len)
        self.de2 = DE(lde_len)
        self.de3 = DE(lde_len)
        self.rest = None
        self.parse(code)

    def parse(self, code):
        length = LC_LENGTH_HHD14 if self.version == HHD_VERSION_14 else LC_LENGTH_HHD13
        self.lc = int(code[0:length])
        if len(code) < length+self.lc:
            raise ValueError("lc too large: {} + {} > {}".format(self.lc, length, len(code)))
        code = code[length:]
        code = self.startcode.parse(code)
        self.version = self.startcode.version
        code = self.de1.parse(code, self.version)
        code = self.de2.parse(code, self.version)
        code = self.de3.parse(code, self.version)
        self.rest = code or None

    def render(self):
        s = self.create_payload()
        luhn = self.create_luhn_checksum()
        xor = self.create_xor_checksum(s)
        return s + luhn + xor

    def create_payload(self):
        s = str(self.startcode.render_length())
        for b in self.startcode.control_bytes:
            s += h(b, 2)
        s += self.startcode.render_data()
        for de in (self.de1, self.de2, self.de3):
            s += de.render_length()
            s += de.render_data()

        l = (len(s) + 2) // 2  # data + checksum / chars per byte
        lc = h(l, 2)
        return lc + s

    def create_xor_checksum(self, payload):
        xorsum = 0
        for c in payload:
            xorsum ^= int(c, 16)
        return h(xorsum, 1)

    def create_luhn_checksum(self):
        s = ""
        for b in self.startcode.control_bytes:
            s += h(b, 2)
        s += self.startcode.render_data()
        if self.de1.data is not None:
            s += self.de1.render_data()
        if self.de2.data is not None:
            s += self.de2.render_data()
        if self.de3.data is not None:
            s += self.de3.render_data()

        luhnsum = 0
        for i in range(0, len(s), 2):
            luhnsum += 1 * int(s[i], 16) + digitsum(2 * int(s[i + 1], 16))

        m = luhnsum % 10
        if m == 0:
            return "0"
        r = 10 - m
        ss = luhnsum + r
        luhn = ss - luhnsum
        return h(luhn, 1)


class DE:
    def __init__(self, lde_len):
        self.length = 0
        self.lde = 0
        self.lde_length = lde_len
        self.encoding = None
        self.data = None

    def parse(self, data, version):
        self.version = version
        if not data:
            return data
        self.lde = int(data[0:self.lde_length])
        data = data[self.lde_length:]

        self.length = bit_sum(self.lde, 5)
        self.data = data[0:self.length]
        return data[self.length:]

    def set_encoding(self):
        if self.data is None:
            self.encoding = ENCODING_BCD
        elif self.encoding is not None:
            pass
        elif re.match("^[0-9]{1,}$", self.data):
            # BCD only if the value is fully numeric, no IBAN etc.
            self.encoding = ENCODING_BCD
        else:
            self.encoding = ENCODING_ASC

    def render_length(self):
        self.set_encoding()
        if self.data is None:
            return ""
        l = len(self.render_data()) // 2
        if self.encoding == ENCODING_BCD:
            return h(l, 2)

        if self.version == HHD_VERSION_14:
            l = l + (1 << BIT_ENCODING)
            return h(l, 2)

        return "1" + h(l, 1)

    def render_data(self):
        self.set_encoding()
        if self.data is None:
            return ""

        if self.encoding == ENCODING_ASC:
            return asciicode(self.data)

        if len(self.data) % 2 == 1:
            return self.data + "F"

        return self.data


class Startcode(DE):
    def __init__(self):
        super().__init__(LDE_LENGTH_DEFAULT)
        self.control_bytes = []

    def parse(self, data):
        self.lde = int(data[:2], 16)
        data = data[2:]

        self.length = bit_sum(self.lde, 5)

        self.version = HHD_VERSION_13
        if self.lde & (1 << BIT_CONTROLBYTE) != 0:
            self.version = HHD_VERSION_14
            for i in range(10):
                cbyte = int(data[:2], 16)
                self.control_bytes.append(cbyte)
                data = data[2:]
                if cbyte & (1 << BIT_CONTROLBYTE) == 0:
                    break

        self.data = data[:self.length]
        return data[self.length:]

    def render_length(self):
        s = super().render_length()
        if self.version == HHD_VERSION_13 or not self.control_bytes:
            return s
        l = int(s, 16) + (1 << BIT_CONTROLBYTE)
        return h(l, 2)


def terminal_flicker_unix(code, field_width=3, space_width=3, height=1, clear=False, wait=0.05):
    """
    Re-encodes a flicker code and prints it on a unix terminal.

    :param code: Challenge value
    :param field_width: Width of fields in characters (default: 3).
    :param space_width: Width of spaces in characters (default: 3).
    :param height: Height of fields in characters (default: 1).
    :param clear: Clear terminal after every line (default: ``False``).
    :param wait: Waiting interval between lines (default: 0.05).
    """
    # Inspired by Andreas Schiermeier
    # https://git.ccc-ffm.de/?p=smartkram.git;a=blob_plain;f=chiptan/flicker/flicker.sh;h
    # =7066293b4e790c2c4c1f6cbdab703ed9976ffe1f;hb=refs/heads/master
    code = parse(code).render()
    data = swap_bytes(code)
    high = '\033[48;05;15m'
    low = '\033[48;05;0m'
    std = '\033[0m'
    stream = ['10000', '00000', '11111', '01111', '11111', '01111', '11111']
    for c in data:
        v = int(c, 16)
        stream.append('1' + str(v & 1) + str((v & 2) >> 1) + str((v & 4) >> 2) + str((v & 8) >> 3))
        stream.append('0' + str(v & 1) + str((v & 2) >> 1) + str((v & 4) >> 2) + str((v & 8) >> 3))

    while True:
        for frame in stream:
            if clear:
                print('\033c', end='')

            for i in range(height):
                for c in frame:
                    print(low + ' ' * space_width, end='')
                    if c == '1':
                        print(high + ' ' * field_width, end='')
                    else:
                        print(low+ ' ' * field_width, end='')
                print(low + ' ' * space_width + std)

            time.sleep(wait)
