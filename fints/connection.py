import base64

import requests

from .message import FinTSMessage


class FinTSConnectionError(Exception):
    pass


class FinTSHTTPSConnection:
    def __init__(self, url):
        self.url = url

    def send(self, msg: FinTSMessage):
        r = requests.post(
            self.url, data=base64.b64encode(str(msg).encode('iso-8859-1')),
        )
        if r.status_code < 200 or r.status_code > 299:
            raise FinTSConnectionError('Bad status code {}'.format(r.status_code))
        return base64.b64decode(r.content.decode('iso-8859-1')).decode('iso-8859-1')
