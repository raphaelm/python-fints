import random

from fints.protocol.fints3.segments.message import HNHBK, HNSHK, HNVSK, HNVSD, HNSHA, HNHBS


class FinTSMessage:
    def __init__(self, blz, username, pin, systemid, dialogid, msgno, encrypted_segments):
        self.blz = blz
        self.username = username
        self.pin = pin
        self.systemid = systemid
        self.dialogid = dialogid
        self.msgno = msgno
        self.segments = []
        self.encrypted_segments = []

        sig_head = self.build_signature_head()
        enc_head = self.build_encryption_head()
        self.segments.append(enc_head)

        self.enc_envelop = HNVSD(999, '')
        self.segments.append(self.enc_envelop)

        self.append_enc_segment(sig_head)
        for s in encrypted_segments:
            self.append_enc_segment(s)

        cur_count = len(encrypted_segments) + 3

        sig_end = HNSHA(cur_count, self.secref, self.pin)
        self.append_enc_segment(sig_end)
        self.segments.append(HNHBS(cur_count + 1, msgno))

    def append_enc_segment(self, seg):
        self.encrypted_segments.append(seg)
        self.enc_envelop.set_data(self.enc_envelop.encoded_data + str(seg))

    def build_signature_head(self):
        rand = random.SystemRandom()
        self.secref = rand.randint(1000000, 9999999)
        return HNSHK(2, self.secref, self.blz, self.username, self.systemid)

    def build_encryption_head(self):
        return HNVSK(998, self.blz, self.username, self.systemid)

    def build_header(self):
        l = sum([len(str(s)) for s in self.segments])
        return HNHBK(l, self.dialogid, self.msgno)

    def __str__(self):
        return str(self.build_header()) + ''.join([str(s) for s in self.segments])
