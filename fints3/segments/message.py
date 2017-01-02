import time

from . import FinTS3Segment


class HNHBK(FinTS3Segment):
    """
    HNHBK (Nachrichtenkopf)
    Section B.5.2
    """
    type = 'HNHBK'
    version = 3

    HEADER_LENGTH = 29

    def __init__(self, msglen, dialogid, msgno):

        if len(str(msglen)) != 12:
            msglen = str(int(msglen) + self.HEADER_LENGTH + len(str(dialogid)) + len(str(msgno))).zfill(12)

        data = [
            msglen,
            300,
            dialogid,
            msgno
        ]
        super().__init__(1, data)


class HNSHK(FinTS3Segment):
    """
    HNSHK (Signaturkopf)
    Section B.5.1
    """
    type = 'HNSHK'
    version = 4

    SECURITY_FUNC = 999
    SECURITY_BOUNDARY = 1  # SHM
    SECURITY_SUPPLIER_ROLE = 1  # ISS

    def __init__(self, segno, secref, blz, username, systemid, profile_version, security_function=SECURITY_FUNC):
        data = [
            ':'.join(['PIN', str(profile_version)]),
            security_function,
            secref,
            self.SECURITY_BOUNDARY,
            self.SECURITY_SUPPLIER_ROLE,
            ':'.join(['1', '', str(systemid)]),
            1,
            ':'.join(['1', time.strftime('%Y%m%d'), time.strftime('%H%M%S')]),
            ':'.join(['1', '999', '1']),  # Negotiate hash algorithm
            ':'.join(['6', '10', '16']),  # RSA mode
            ':'.join([str(self.country_code), blz, username, 'S', '0', '0']),
        ]
        super().__init__(segno, data)


class HNVSK(FinTS3Segment):
    """
    HNVSK (Verschlüsslungskopf)
    Section B.5.3
    """
    type = 'HNVSK'
    version = 3

    COMPRESSION_NONE = 0
    SECURITY_SUPPLIER_ROLE = 1  # ISS

    def __init__(self, segno, blz, username, systemid, profile_version):
        data = [
            ':'.join(['PIN', str(profile_version)]),
            998,
            self.SECURITY_SUPPLIER_ROLE,
            ':'.join(['1', '', str(systemid)]),
            ':'.join(['1', time.strftime('%Y%m%d'), time.strftime('%H%M%S')]),
            ':'.join(['2', '2', '13', '@8@00000000', '5', '1']),  # Crypto algorithm
            ':'.join([str(self.country_code), blz, username, 'S', '0', '0']),
            self.COMPRESSION_NONE
        ]
        super().__init__(segno, data)


class HNVSD(FinTS3Segment):
    """
    HNVSD (Verschlüsselte Daten)
    Section B.5.4
    """
    type = 'HNVSD'
    version = 1

    def __init__(self, segno, encoded_data):
        self.encoded_data = encoded_data
        data = [
            '@{}@{}'.format(len(encoded_data), encoded_data)
        ]
        super().__init__(segno, data)

    def set_data(self, encoded_data):
        self.encoded_data = encoded_data
        self.data = [
            '@{}@{}'.format(len(encoded_data), encoded_data)
        ]


class HNSHA(FinTS3Segment):
    """
    HNSHA (Signaturabschluss)
    Section B.5.2
    """
    type = 'HNSHA'
    version = 2

    SECURITY_FUNC = 999
    SECURITY_BOUNDARY = 1  # SHM
    SECURITY_SUPPLIER_ROLE = 1  # ISS
    PINTAN_VERSION = 1  # 1-step

    def __init__(self, segno, secref, pin):
        data = [
            secref,
            '',
            pin
        ]
        super().__init__(segno, data)


class HNHBS(FinTS3Segment):
    """
    HNHBS (Nachrichtenabschluss)
    Section B.5.3
    """
    type = 'HNHBS'
    version = 1

    def __init__(self, segno, msgno):
        data = [
            str(msgno)
        ]
        super().__init__(segno, data)
