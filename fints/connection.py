import base64

import requests

from .message import FinTSMessage

from fints.parser import FinTS3Parser
from fints.utils import Password

class FinTSConnectionError(Exception):
    pass


class FinTSHTTPSConnection:
    def __init__(self, url):
        self.url = url

    def send(self, msg: FinTSMessage):
        print("Sending >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        with Password.protect():
            FinTS3Parser().parse_message(str(msg).encode('iso-8859-1')).print_nested()
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        r = requests.post(
            self.url, data=base64.b64encode(str(msg).encode('iso-8859-1')),
        )
        if r.status_code < 200 or r.status_code > 299:
            raise FinTSConnectionError('Bad status code {}'.format(r.status_code))
        retval = base64.b64decode(r.content.decode('iso-8859-1'))
        print("Received <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        with Password.protect():
            FinTS3Parser().parse_message(retval).print_nested()
        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        return retval