import pytest
import requests

from fints.connection import FinTSHTTPSConnection
from fints.exceptions import FinTSConnectionError


class DummyMessage:
    segments = []

    def print_nested(self, stream=None, **kwargs):
        pass

    def render_bytes(self):
        return b"dummy"


def test_send_wraps_transport_errors():
    connection = FinTSHTTPSConnection("https://example.invalid/fints")

    def raise_timeout(*args, **kwargs):
        raise requests.exceptions.Timeout("request timed out")

    connection.session.post = raise_timeout

    with pytest.raises(FinTSConnectionError) as excinfo:
        connection.send(DummyMessage())

    assert "request timed out" in str(excinfo.value)
    assert isinstance(excinfo.value.__cause__, requests.exceptions.Timeout)
