import pytest
import requests

from fints.connection import DEFAULT_TIMEOUT, FinTSHTTPSConnection
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


def test_send_passes_the_timeout_to_requests():
    connection = FinTSHTTPSConnection("https://example.invalid/fints", timeout=30)
    captured = {}

    def capture(*args, **kwargs):
        captured.update(kwargs)
        raise requests.exceptions.Timeout("request timed out")

    connection.session.post = capture

    with pytest.raises(FinTSConnectionError):
        connection.send(DummyMessage())

    assert captured["timeout"] == 30


def test_send_uses_the_default_timeout_when_none_is_given():
    connection = FinTSHTTPSConnection("https://example.invalid/fints")
    captured = {}

    def capture(*args, **kwargs):
        captured.update(kwargs)
        raise requests.exceptions.Timeout("request timed out")

    connection.session.post = capture

    with pytest.raises(FinTSConnectionError):
        connection.send(DummyMessage())

    assert captured["timeout"] == DEFAULT_TIMEOUT
