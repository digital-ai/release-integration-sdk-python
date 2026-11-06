import threading
from types import SimpleNamespace
from unittest import mock

import pytest

from digitalai.release.integration import k8s, watcher

SECRET = "input-context-secret"
NAMESPACE = "runner-ns"


def secret_event(session_key):
    data = None if session_key is None else {"session-key": session_key}
    return {"object": SimpleNamespace(data=data)}


class FakeWatch:
    """Replays a fixed list of watch events."""

    def __init__(self, events):
        self.events = events
        self.consumed = 0
        self.stream_call = None
        self.stopped = False

    def stream(self, func, *args, **kwargs):
        self.stream_call = (func, args, kwargs)
        for event in self.events:
            self.consumed += 1
            yield event

    def stop(self):
        self.stopped = True


@pytest.fixture
def kube_client(monkeypatch):
    client = mock.Mock()
    monkeypatch.setattr(k8s, "get_client", lambda: client)
    monkeypatch.setenv("INPUT_CONTEXT_SECRET", SECRET)
    monkeypatch.setenv("RUNNER_NAMESPACE", NAMESPACE)
    return client


def watch_secret(monkeypatch, events, on_update=None, stop=None):
    fake = FakeWatch(events)
    monkeypatch.setattr(watcher, "watch", SimpleNamespace(Watch=lambda: fake))
    watcher.start_input_secret_watcher(on_update or mock.Mock(), stop or threading.Event())
    return fake


def test_watches_only_the_input_context_secret(kube_client, monkeypatch):
    fake = watch_secret(monkeypatch, [])

    assert fake.stream_call == (kube_client.list_namespaced_secret, (NAMESPACE,),
                                {"field_selector": f"metadata.name={SECRET}"})


def test_calls_back_each_time_the_session_key_changes(kube_client, monkeypatch):
    on_update = mock.Mock()

    watch_secret(monkeypatch, [secret_event(k) for k in ("k1", "k1", "k2", "k2", "k3")], on_update)

    assert on_update.call_count == 2


def test_first_event_only_records_the_session_key(kube_client, monkeypatch):
    on_update = mock.Mock()

    watch_secret(monkeypatch, [secret_event("k1")], on_update)

    on_update.assert_not_called()


def test_tolerates_a_secret_without_data(kube_client, monkeypatch):
    on_update = mock.Mock()

    watch_secret(monkeypatch, [secret_event(None), secret_event("k1"), secret_event("k2")], on_update)

    on_update.assert_called_once_with()


def test_stops_after_the_current_event_once_stop_is_set(kube_client, monkeypatch):
    stop = threading.Event()
    stop.set()

    fake = watch_secret(monkeypatch, [secret_event("k1"), secret_event("k2")], stop=stop)

    assert fake.consumed == 1
    assert fake.stopped


def test_releases_the_watch_when_the_callback_fails(kube_client, monkeypatch):
    fake = FakeWatch([secret_event("k1"), secret_event("k2")])
    monkeypatch.setattr(watcher, "watch", SimpleNamespace(Watch=lambda: fake))

    with pytest.raises(RuntimeError):
        watcher.start_input_secret_watcher(mock.Mock(side_effect=RuntimeError("boom")), threading.Event())

    assert fake.stopped


@pytest.mark.parametrize("missing", ["INPUT_CONTEXT_SECRET", "RUNNER_NAMESPACE"])
def test_requires_secret_name_and_namespace(kube_client, monkeypatch, missing):
    monkeypatch.delenv(missing)

    with pytest.raises(ValueError, match="INPUT_CONTEXT_SECRET and RUNNER_NAMESPACE"):
        watcher.start_input_secret_watcher(mock.Mock(), threading.Event())


def test_input_context_watcher_returns_when_the_secret_watcher_fails(monkeypatch):
    monkeypatch.setattr(watcher, "start_input_secret_watcher", mock.Mock(side_effect=ValueError("no secret")))
    thread = threading.Thread(target=watcher.start_input_context_watcher, args=(mock.Mock(),), daemon=True)

    thread.start()
    thread.join(timeout=5)

    assert not thread.is_alive()
