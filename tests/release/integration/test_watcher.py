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


def test_input_context_watcher_returns_when_the_watch_cannot_be_configured(monkeypatch):
    watch_once = mock.Mock(side_effect=ValueError("no secret"))
    monkeypatch.setattr(watcher, "_watch_input_secret", watch_once)
    thread = threading.Thread(target=watcher.start_input_context_watcher, args=(mock.Mock(),), daemon=True)

    thread.start()
    thread.join(timeout=5)

    assert not thread.is_alive()
    watch_once.assert_called_once()


# -- each session-key runs at most once -------------------------------------

def test_runs_new_input_already_in_the_secret_when_the_watch_opens(kube_client, monkeypatch):
    on_update = mock.Mock(return_value=None)

    watch_secret_after(monkeypatch, "k1", [secret_event("k2")], on_update)

    on_update.assert_called_once_with()


def test_does_not_run_the_executed_input_again(kube_client, monkeypatch):
    on_update = mock.Mock(return_value=None)

    watch_secret_after(monkeypatch, "k1", [secret_event("k1"), secret_event("k2"), secret_event("k2"),
                                           secret_event("k1")], on_update)

    on_update.assert_called_once_with()


def test_input_the_callback_ran_counts_as_handled(kube_client, monkeypatch):
    # The secret changed to k3 between the k2 event and the read, so the callback ran k3.
    on_update = mock.Mock(return_value="k3")

    watch_secret_after(monkeypatch, "k1", [secret_event("k2"), secret_event("k3")], on_update)

    on_update.assert_called_once_with()


def test_ignores_a_deleted_secret(kube_client, monkeypatch):
    on_update = mock.Mock(return_value=None)
    deleted = dict(secret_event("k2"), type="DELETED")

    watch_secret_after(monkeypatch, "k1", [deleted], on_update)

    on_update.assert_not_called()


def watch_secret_after(monkeypatch, executed_session_key, events, on_update):
    fake = FakeWatch(events)
    monkeypatch.setattr(watcher, "watch", SimpleNamespace(Watch=lambda: fake))
    watcher.start_input_secret_watcher(on_update, threading.Event(), executed_session_key)


# -- the daemon-mode loop: watching again after the watch fails or ends -------

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


def watch_loop(monkeypatch, *connections, executed_session_key="k1", on_update=None):
    stop = threading.Event()
    fake = FakeConnections(stop, *connections)
    monkeypatch.setattr(watcher, "watch", fake)
    monkeypatch.setattr(watcher, "RECONNECT_DELAY_SECONDS", 0)
    on_update = on_update or mock.Mock(return_value=None)
    watcher.start_input_context_watcher(on_update, executed_session_key, stop)
    return on_update, fake


def recorded_waits(monkeypatch, *connections, delay=1, max_delay=30, watch_seconds=None):
    """
    Runs the loop over ``connections`` and returns the delays it waited before
    re-opening the watch. ``watch_seconds`` gives how long each watch stays
    open (default 0: every watch ends at once).
    """
    stop = threading.Event()
    waits = []
    monkeypatch.setattr(stop, "wait", waits.append)
    monkeypatch.setattr(watcher, "watch", FakeConnections(stop, *connections))
    monkeypatch.setattr(watcher, "RECONNECT_DELAY_SECONDS", delay)
    monkeypatch.setattr(watcher, "MAX_RECONNECT_DELAY_SECONDS", max_delay)
    # The clock is read when each watch opens and when it ends.
    durations = list(watch_seconds or [0] * len(connections))
    now = [0.0]
    readings = []
    for seconds in durations:
        readings += [now[0], now[0] + seconds]
        now[0] += seconds
    monkeypatch.setattr(watcher, "_clock", iter(readings).__next__)

    watcher.start_input_context_watcher(mock.Mock(return_value=None), "k1", stop)
    return waits


def test_loop_does_not_rerun_the_input_already_run(kube_client, monkeypatch):
    on_update, _ = watch_loop(monkeypatch, [secret_event("k1")])

    on_update.assert_not_called()


def test_loop_runs_input_newer_than_the_one_already_run(kube_client, monkeypatch):
    on_update, _ = watch_loop(monkeypatch, [secret_event("k2")])

    on_update.assert_called_once_with()


def test_loop_runs_each_new_input_once(kube_client, monkeypatch):
    events = [secret_event(k) for k in ("k1", "k2", "k2", "k3", "k3", "k4")]

    on_update, _ = watch_loop(monkeypatch, events)

    assert on_update.call_count == 3


def test_loop_does_not_rerun_the_last_input_after_an_idle_disconnect(kube_client, monkeypatch):
    # D-44246: after the watch drops, the secret still holds the last task's input. Seeing it
    # again on the new watch must not run that task a second time.
    on_update, fake = watch_loop(monkeypatch,
                                 [secret_event("k1"), secret_event("k2"), secret_event("k3"), ConnectionLost],
                                 [secret_event("k3")])

    assert fake.opened == 2
    assert on_update.call_count == 2


def test_loop_runs_new_input_seen_after_reconnecting(kube_client, monkeypatch):
    on_update, fake = watch_loop(monkeypatch, [secret_event("k1"), ConnectionLost], [secret_event("k2")])

    assert fake.opened == 2
    on_update.assert_called_once_with()


def test_loop_reconnects_after_a_clean_end_of_stream(kube_client, monkeypatch):
    on_update, fake = watch_loop(monkeypatch, [secret_event("k1")], [secret_event("k2")])

    assert fake.opened == 2
    on_update.assert_called_once_with()


def test_loop_keeps_reconnecting_through_a_long_outage(kube_client, monkeypatch):
    # An executor must survive an API server outage; it ends only when the runner removes the pod.
    outage = [[ConnectionLost]] * 20

    on_update, fake = watch_loop(monkeypatch, *outage, [secret_event("k2")])

    assert fake.opened == 21
    on_update.assert_called_once_with()


def test_loop_remembers_the_input_the_callback_actually_ran(kube_client, monkeypatch):
    # The event for k2 arrives, but by the time the input is read the secret already holds k3.
    on_update, _ = watch_loop(monkeypatch, [secret_event("k2"), secret_event("k3")],
                              on_update=mock.Mock(return_value="k3"))

    on_update.assert_called_once_with()


def test_loop_returns_at_once_when_the_secret_is_not_configured(kube_client, monkeypatch):
    monkeypatch.delenv("INPUT_CONTEXT_SECRET")
    fake = FakeConnections(threading.Event(), [secret_event("k2")])
    monkeypatch.setattr(watcher, "watch", fake)

    watcher.start_input_context_watcher(mock.Mock())

    assert fake.opened == 0


def test_a_task_exit_ends_the_loop(kube_client, monkeypatch):
    with pytest.raises(SystemExit):
        watch_loop(monkeypatch, [secret_event("k2")], on_update=mock.Mock(side_effect=SystemExit(3)))


def test_loop_backs_off_between_failed_watches(kube_client, monkeypatch):
    waits = recorded_waits(monkeypatch, [ConnectionLost], [ConnectionLost], [ConnectionLost], [], max_delay=3)

    assert waits == [1, 2, 3]


def test_loop_backs_off_when_watches_keep_ending_soon_after_opening(kube_client, monkeypatch):
    # Each watch delivers the secret's current state, then ends or fails at once: the API server
    # must not be flooded with new watches.
    waits = recorded_waits(monkeypatch, [secret_event("k1")], [secret_event("k1"), ConnectionLost],
                           [secret_event("k1")], [secret_event("k1")], [], max_delay=4)

    assert waits == [1, 2, 4, 4]


def test_loop_starts_the_backoff_over_after_a_watch_that_stayed_open(kube_client, monkeypatch):
    # Two quick failures, then a watch that was healthy for an hour before it failed.
    waits = recorded_waits(monkeypatch, [ConnectionLost], [ConnectionLost], [secret_event("k1"), ConnectionLost],
                           [], max_delay=30, watch_seconds=[0, 0, 3600, 0])

    assert waits == [1, 2, 1]


def test_loop_waits_before_reopening_a_watch_that_ended_cleanly(kube_client, monkeypatch):
    waits = recorded_waits(monkeypatch, [secret_event("k1")], [], watch_seconds=[3600, 0])

    assert waits == [1]
