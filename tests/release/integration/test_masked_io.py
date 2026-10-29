import io

import pytest

from digitalai.release.integration.masked_io import MaskedIO


@pytest.fixture
def sink():
    return io.StringIO()


@pytest.fixture
def stream(sink):
    stream = MaskedIO(sink)
    yield stream
    # A TextIOWrapper closes the stream it wraps when collected; detach so the sink stays readable.
    stream.detach()


def test_masks_every_occurrence_of_every_secret(stream, sink):
    stream.secrets = ["pw1", "tok"]

    stream.write("pw1 and tok and pw1 again")

    assert sink.getvalue() == "******** and ******** and ******** again"


def test_write_returns_the_length_of_the_unmasked_text(stream):
    stream.secrets = ["a-long-secret"]

    assert stream.write("x a-long-secret") == len("x a-long-secret")


def test_passes_text_through_without_secrets(stream, sink):
    stream.write("plain text")

    assert sink.getvalue() == "plain text"


def test_ignores_empty_secrets(stream, sink):
    stream.secrets = ["", None]

    stream.write("plain text")

    assert sink.getvalue() == "plain text"


def test_masks_non_string_secrets_by_their_text(stream, sink):
    stream.secrets = [12345]

    stream.write("pin 12345")

    assert sink.getvalue() == "pin ********"


def test_masks_with_the_secrets_set_most_recently(stream, sink):
    stream.secrets = ["old"]
    stream.secrets = ["new"]

    stream.write("old new")

    assert sink.getvalue() == "old ********"


@pytest.mark.xfail(reason="secrets are replaced in list order, so a secret that is a prefix of a "
                          "later one masks only part of it and leaks the rest")
def test_masks_a_secret_that_contains_another_secret(stream, sink):
    stream.secrets = ["admin", "admin123"]

    stream.write("admin123")

    assert sink.getvalue() == "********"
