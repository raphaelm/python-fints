from fints.utils import fints_escape
from . import FinTS3Segment


class HKIDN(FinTS3Segment):
    """
    HKIDN (Identifikation)
    Section C.3.1.2
    """
    type = 'HKIDN'
    version = 2

    def __init__(self, segmentno, blz, username, systemid=0, customerid=1):
        data = [
            '{}:{}'.format(self.country_code, blz),
            fints_escape(username),
            systemid,
            customerid
        ]
        super().__init__(segmentno, data)


class HKVVB(FinTS3Segment):
    """
    HKVVB (Verarbeitungsvorbereitung)
    Section C.3.1.3
    """
    type = 'HKVVB'
    version = 3

    LANG_DE = 1
    LANG_EN = 2
    LANG_FR = 3

    PRODUCT_NAME = 'pyfints'
    PRODUCT_VERSION = '0.1'

    def __init__(self, segmentno, lang=LANG_DE):
        data = [
            0, 0, lang, fints_escape(self.PRODUCT_NAME), fints_escape(self.PRODUCT_VERSION)
        ]
        super().__init__(segmentno, data)


class HKSYN(FinTS3Segment):
    """
    HKSYN (Synchronisation)
    Section C.8.1.2
    """
    type = 'HKSYN'
    version = 3

    SYNC_MODE_NEW_CUSTOMER_ID = 0
    SYNC_MODE_LAST_MSG_NUMBER = 1
    SYNC_MODE_SIGNATURE_ID = 2

    def __init__(self, segmentno, mode=SYNC_MODE_NEW_CUSTOMER_ID):
        data = [
            mode
        ]
        super().__init__(segmentno, data)


class HKTAN(FinTS3Segment):
    """
    HKTAN (TAN-Verfahren festlegen)
    Section C.2.1.2
    """
    type = 'HKTAN'

    def __init__(self, segno, process, aref, medium):
        self.version = 3
        if process == 4:
            if medium == '':
                data = [
                    process
                ]
            else:
                data = [
                    process, '', '', '', '', '', '', '', medium
                ]
        else:
            data = [
                process, '', aref, '', 'N'
            ]
        super().__init__(segno, data)


class HKTAB(FinTS3Segment):
    """
    HKTAB (Verfügbarre TAN-Medien ermitteln)
    Section C.2.1.2
    """
    type = 'HKTAB'

    def __init__(self, segno):
        self.version = 4
        data = [
            '0', 'A'
        ]
        super().__init__(segno, data)
