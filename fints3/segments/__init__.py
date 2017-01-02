class FinTS3Segment:
    type = '???'
    country_code = 280
    version = 2

    def __init__(self, segmentno, data):
        self.segmentno = segmentno
        self.data = data

    def __str__(self):
        res = '{}:{}:{}'.format(self.type, self.segmentno, self.version)
        for d in self.data:
            res += '+' + str(d)
        return res + "'"
