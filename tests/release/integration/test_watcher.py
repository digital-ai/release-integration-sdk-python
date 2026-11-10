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


def test_input_context_watcher_returns_when_the_secret_is_not_configured(monkeypatch):
    monkeypatch.delenv("INPUT_CONTEXT_SECRET", raising=False)
    thread = threading.Thread(target=watcher.start_input_context_watcher, args=(mock.Mock(),), daemon=True)

    thread.start()
    thread.join(timeout=5)

    assert not thread.is_alive()


def test_ignores_the_deletion_of_the_secret(kube_client, monkeypatch):
    on_update = mock.Mock()
    deleted = {"type": "DELETED", "object": SimpleNamespace(data={"session-key": "k2"})}

    watch_secret(monkeypatch, [secret_event("k1"), deleted], on_update)

    on_update.assert_not_called()


# -- the daemon-mode loop --------------------------------------------------

class ConnectionLost(Exception):
    pass


class FakeConnections:
    """
    Each Watch() is one watch connection. It replays its list of events, then
    fails with ConnectionLost (when the list ends with it) or ends cleanly.
    The loop is stopped once the last connection ends.
    """

    def __init__(self, stop, *connections):
        self.stop = stop
        self.connections = list(connections)
        self.opened = 0

    def Watch(self):
        connections = self

        class _Watch:
            def stream(self, func, *args, **kwargs):
                events = connections.connections[connections.opened]
                connections.opened += 1
                try:
                    for event in events:
                        if event is ConnectionLost:
                            raise ConnectionLost("connection reset by peer")
                        yield event
                finally:
                    if connections.opened == len(connections.connections):
                        connections.stop.set()

            def stop(self):
                pass

        return _Watch()


def watch_loop(monkeypatch, *connections, current_session_key=None, on_update=None):
    stop = threading.Event()
    fake = FakeConnections(stop, *connections)
    monkeypatch.setattr(watcher, "watch", fake)
    monkeypatch.setattr(watcher, "RECONNECT_DELAY_SECONDS", 0)
    on_update = on_update or mock.Mock(return_value=None)
    watcher.start_input_context_watcher(on_update, current_session_key, stop)
    return on_update, fake


def test_loop_does_not_rerun_the_input_already_run(kube_client, monkeypatch):
    on_update, _ = watch_loop(monkeypatch, [secret_event("k1")], current_session_key="k1")

    on_update.assert_not_called()


def test_loop_runs_input_newer_than_the_one_already_run(kube_client, monkeypatch):
    on_update, _ = watch_loop(monkeypatch, [secret_event("k2")], current_session_key="k1")

    on_update.assert_called_once_with()


def test_loop_runs_each_new_input_once(kube_client, monkeypatch):
    events = [secret_event(k) for k in ("k1", "k2", "k2", "k3", "k3", "k4")]

    on_update, _ = watch_loop(monkeypatch, events, current_session_key="k1")

    assert on_update.call_count == 3


def test_loop_reconnects_after_the_connection_is_lost(kube_client, monkeypatch):
    on_update, fake = watch_loop(monkeypatch,
                                 [secret_event("k1"), ConnectionLost],
                                 [secret_event("k1"), secret_event("k2")],
                                 current_session_key="k1")

    assert fake.opened == 2
    on_update.assert_called_once_with()


def test_loop_does_not_rerun_the_last_input_after_an_idle_disconnect(kube_client, monkeypatch):
    # D-44246: after an idle disconnect the secret still holds the last job's input. Seeing it
    # again, on the new connection, must not run that job a second time.
    on_update, fake = watch_loop(monkeypatch,
                                 [secret_event("k1"), secret_event("k2"), secret_event("k3"), ConnectionLost],
                                 [secret_event("k3")],
                                 current_session_key="k1")

    assert fake.opened == 2
    assert on_update.call_count == 2


def test_loop_remembers_the_input_the_callback_actually_ran(kube_client, monkeypatch):
    # The event for k2 arrives, but by the time the input is read the secret already holds k3.
    on_update, _ = watch_loop(monkeypatch, [secret_event("k2"), secret_event("k3")],
                              current_session_key="k1", on_update=mock.Mock(return_value="k3"))

    on_update.assert_called_once_with()


def test_loop_reconnects_after_a_clean_end_of_stream(kube_client, monkeypatch):
    on_update, fake = watch_loop(monkeypatch, [secret_event("k1")], [secret_event("k2")],
                                 current_session_key="k1")

    assert fake.opened == 2
    on_update.assert_called_once_with()


def test_loop_backs_off_between_failed_connections(kube_client, monkeypatch):
    stop = threading.Event()
    waits = []
    monkeypatch.setattr(stop, "wait", waits.append)
    monkeypatch.setattr(watcher, "watch", FakeConnections(stop, [ConnectionLost], [ConnectionLost],
                                                          [ConnectionLost], []))
    monkeypatch.setattr(watcher, "RECONNECT_DELAY_SECONDS", 1)
    monkeypatch.setattr(watcher, "MAX_RECONNECT_DELAY_SECONDS", 3)

    watcher.start_input_context_watcher(mock.Mock(), "k1", stop)

    assert waits == [1, 2, 3]


def test_loop_backs_off_when_the_watch_keeps_ending_without_events(kube_client, monkeypatch):
    stop = threading.Event()
    waits = []
    monkeypatch.setattr(stop, "wait", waits.append)
    monkeypatch.setattr(watcher, "watch", FakeConnections(stop, [], [], [], [], []))
    monkeypatch.setattr(watcher, "RECONNECT_DELAY_SECONDS", 1)
    monkeypatch.setattr(watcher, "MAX_RECONNECT_DELAY_SECONDS", 4)

    watcher.start_input_context_watcher(mock.Mock(), "k1", stop)

    assert waits == [1, 2, 4, 4]


def test_loop_waits_before_reopening_a_watch_that_ended_cleanly(kube_client, monkeypatch):
    stop = threading.Event()
    waits = []
    monkeypatch.setattr(stop, "wait", waits.append)
    monkeypatch.setattr(watcher, "watch", FakeConnections(stop, [ConnectionLost], [ConnectionLost],
                                                          [secret_event("k1")], [secret_event("k1")]))
    monkeypatch.setattr(watcher, "RECONNECT_DELAY_SECONDS", 1)
    monkeypatch.setattr(watcher, "MAX_RECONNECT_DELAY_SECONDS", 30)

    watcher.start_input_context_watcher(mock.Mock(), "k1", stop)

    # A stream that delivered events starts the backoff over.
    assert waits == [1, 2, 1]
