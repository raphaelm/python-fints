import base64
import io
import logging

import requests
from fints.utils import Password

from .exceptions import *
from .message import FinTSInstituteMessage, FinTSMessage

logger = logging.getLogger(__name__)


class FinTSHTTPSConnection:
    def __init__(self, url):
        self.url = url

    def send(self, msg: FinTSMessage):
        log_out = io.StringIO()
        with Password.protect():
            msg.print_nested(stream=log_out, prefix="\t")
            logger.debug("Sending >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n{}\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n".format(log_out.getvalue()))
            log_out.truncate(0)

        r = requests.post(
            self.url, data=base64.b64encode(msg.render_bytes()),
            headers={
                'Content-Type': 'text/plain',
            },
        )

        if r.status_code < 200 or r.status_code > 299:
            raise FinTSConnectionError('Bad status code {}'.format(r.status_code))

        response = base64.b64decode(r.content.decode('iso-8859-1'))
        retval = FinTSInstituteMessage(segments=response)

        with Password.protect():
            retval.print_nested(stream=log_out, prefix="\t")
            logger.debug("Received <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n{}\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n".format(log_out.getvalue()))
        return retval
