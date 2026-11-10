"""
wrapper.run() in daemon mode on a reused executor pod: the runner writes each
task's input to the input context secret, and the wrapper runs each one exactly
once, including when the secret watch fails while the runner removes the idle
executor (D-44246: the executor's last task ran a second time).

Runs in-process against a fake input context secret and Kubernetes watch.
"""
import base64
import json
import os
import signal
import sys
import threading
from types import SimpleNamespace
from unittest import mock

import pytest

from digitalai.release.integration import k8s, watcher
from digitalai.release.integration.job_data_encryptor import AESJobDataEncryptor
from digitalai.release.integration.output_context import OutputContext
from tests.support import input_context, task_property

SECRET = "executor-input"
NAMESPACE = "runner-ns"


def b64(text: str) -> str:
    return base64.b64encode(text.encode()).decode()


def input_secret_data(name):
    """
    The data of an input context secret for a Hello task greeting ``name``,
    with a new session-key, as Kubernetes returns it: base64-encoded values.
    """
    session_key = base64.b64encode(os.urandom(32)).decode()
    context = input_context("containerExamples.Hello", [task_property("yourName", name)])
    encrypted = AESJobDataEncryptor(session_key).encrypt(json.dumps(context))
    return {"session-key": b64(session_key), "url": b64(b64(f"http://127.0.0.1:9/callback/{name}")),
            "input": b64(encrypted), "fetchUrl": ""}


class FakeExecutorSecret:
    """
    The input context secret of one executor pod, written by the runner.

    Like a Kubernetes watch, each open watch receives every later change of the
    secret and keeps it until read. The runner assigns the next queued task when
    the executor is idle, i.e. when the newest watch has nothing left to read.
    Once the queue is empty, the runner removes the idle executor: every watch
    open at that point fails once it has delivered what it holds, and the RBAC
    resources are gone, so new watches fail too, until the pod is killed
    (SystemExit stands in for the SIGTERM that ends the process).
    """

    KILLED_AFTER_FAILED_WATCHES = 3

    def __init__(self, task_names):
        self.queue = list(task_names)
        self.watches = []
        self.removed = False
        self.failed_watches = 0
        self.data = None
        self._assign_next()

    def _assign_next(self):
        self.data = input_secret_data(self.queue.pop(0))
        self._publish("MODIFIED")

    def _publish(self, event_type):
        for buffered in self.watches:
            buffered.append({"type": event_type, "object": SimpleNamespace(data=dict(self.data))})

    def runner_acts(self):
        # The runner clears the previous result (same session-key), then assigns the next task.
        self._publish("MODIFIED")
        if self.queue:
            self._assign_next()
        else:
            self.removed = True

    # -- Kubernetes API used by the wrapper and watcher --

    def read_namespaced_secret(self, name, namespace):
        assert (name, namespace) == (SECRET, NAMESPACE)
        return SimpleNamespace(data=dict(self.data))

    list_namespaced_secret = object()

    def watch(self):
        fake = self

        class Watch:
            def stream(self, func, namespace, field_selector):
                assert (namespace, field_selector) == (NAMESPACE, f"metadata.name={SECRET}")
                if fake.removed:
                    fake.failed_watches += 1
                    if fake.failed_watches >= fake.KILLED_AFTER_FAILED_WATCHES:
                        raise SystemExit(143)
                    raise RuntimeError("(403) Forbidden")
                buffered = [{"type": "ADDED", "object": SimpleNamespace(data=dict(fake.data))}]
                fake.watches.append(buffered)
                while True:
                    while not buffered:
                        if fake.removed:
                            raise ConnectionError("watch connection broken")
                        fake.runner_acts()
                    yield buffered.pop(0)

            def stop(self):
                pass

        return Watch()


@pytest.fixture
def daemon_wrapper(isolated_wrapper, importable_workspace, monkeypatch):
    monkeypatch.setattr(isolated_wrapper, "execution_mode", "daemon")
    monkeypatch.setattr(isolated_wrapper, "input_context_secret", SECRET)
    monkeypatch.setattr(isolated_wrapper, "runner_namespace", NAMESPACE)
    monkeypatch.setenv("INPUT_CONTEXT_SECRET", SECRET)
    monkeypatch.setenv("RUNNER_NAMESPACE", NAMESPACE)
    monkeypatch.setattr(watcher, "RECONNECT_DELAY_SECONDS", 0)
    return isolated_wrapper


def run_daemon(wrapper, monkeypatch, secret):
    monkeypatch.setattr(k8s, "get_client", lambda: secret)
    monkeypatch.setattr(watcher.watch, "Watch", secret.watch)
    try:
        wrapper.run()
    except SystemExit as exited:
        return exited.code
    return None


def greetings(reported):
    return [result.output_properties.get("greeting") for result in reported]


def test_each_queued_task_runs_once_when_the_idle_executor_is_removed(daemon_wrapper, reported, monkeypatch):
    secret = FakeExecutorSecret(["job-1", "job-2", "job-3", "job-4"])

    exit_code = run_daemon(daemon_wrapper, monkeypatch, secret)

    assert greetings(reported) == ["Hello job-1", "Hello job-2", "Hello job-3", "Hello job-4"]
    # Still watching (and running nothing) until the pod was killed.
    assert exit_code == 143


def test_single_task_runs_once_when_the_idle_executor_is_removed(daemon_wrapper, reported, monkeypatch):
    secret = FakeExecutorSecret(["job-1"])

    run_daemon(daemon_wrapper, monkeypatch, secret)

    assert greetings(reported) == ["Hello job-1"]


def test_failed_input_is_not_run_again(daemon_wrapper, reported, monkeypatch):
    secret = FakeExecutorSecret(["job-1", "job-2"])
    real_read = secret.read_namespaced_secret
    reads = []

    def read_failing_first(name, namespace):
        result = real_read(name, namespace)
        reads.append(result)
        if len(reads) == 1:
            # Recorded, then unusable: the task cannot be loaded.
            result.data["input"] = b64("not encrypted with this key")
        return result

    monkeypatch.setattr(secret, "read_namespaced_secret", read_failing_first)

    run_daemon(daemon_wrapper, monkeypatch, secret)

    assert [r.exit_code for r in reported] == [1, 0]
    assert greetings(reported)[1:] == ["Hello job-2"]


# -- an input runs at most once, whatever the watcher calls back for ----------

class StaticSecret:
    """An input context secret that changes only when the test says so."""

    list_namespaced_secret = object()

    def __init__(self, name):
        self.data = input_secret_data(name)

    def read_namespaced_secret(self, name, namespace):
        return SimpleNamespace(data=dict(self.data))


class OneWatch:
    """Replaces watch.Watch(): one watch that replays fixed events, then stops the loop."""

    def __init__(self, events, stop):
        self.events = events
        self.stop_loop = stop

    def stream(self, func, *args, **kwargs):
        try:
            yield from self.events
        finally:
            self.stop_loop.set()

    def stop(self):
        pass


def modified(session_key):
    return {"type": "MODIFIED", "object": SimpleNamespace(data={"session-key": session_key})}


@pytest.mark.parametrize("announced", [["k2", "k3", "k4"], ["k2", "k2", "k3"]], ids=["k2-k3-k4", "k2-k2-k3"])
def test_input_announced_by_late_events_runs_once(daemon_wrapper, reported, monkeypatch, announced):
    # By the time the first event is handled, the secret already holds the newest input, so that
    # input runs then. The events still buffered after it announce other keys, but the secret
    # still holds the input already run, so it must not run a second time.
    secret = StaticSecret("First")
    monkeypatch.setattr(k8s, "get_client", lambda: secret)
    first_key = daemon_wrapper.run_task_from_input()
    secret.data = input_secret_data("Newest")

    stop = threading.Event()
    monkeypatch.setattr(watcher.watch, "Watch", lambda: OneWatch([modified(k) for k in announced], stop))
    watcher.start_input_context_watcher(daemon_wrapper.run_task_from_input, first_key, stop)

    assert greetings(reported) == ["Hello First", "Hello Newest"]


def test_input_already_run_is_not_run_or_reported_again(daemon_wrapper, reported, monkeypatch):
    secret = StaticSecret("Once")
    monkeypatch.setattr(k8s, "get_client", lambda: secret)

    keys = [daemon_wrapper.run_task_from_input() for _ in range(2)]

    assert greetings(reported) == ["Hello Once"]
    assert keys == [secret.data["session-key"]] * 2


def test_failure_already_reported_for_an_input_is_not_reported_again(daemon_wrapper, reported, monkeypatch):
    secret = StaticSecret("Broken")
    secret.data["input"] = b64("not encrypted with this key")
    monkeypatch.setattr(k8s, "get_client", lambda: secret)

    for _ in range(2):
        daemon_wrapper.run_task_from_input()

    assert [r.exit_code for r in reported] == [1]


def test_input_that_fails_after_it_was_checked_is_reported_as_failed(daemon_wrapper, reported, monkeypatch):
    secret = StaticSecret("Missing")
    context = input_context("containerExamples.Missing", [])
    session_key = base64.b64decode(secret.data["session-key"]).decode()
    secret.data["input"] = b64(AESJobDataEncryptor(session_key).encrypt(json.dumps(context)))
    monkeypatch.setattr(k8s, "get_client", lambda: secret)

    daemon_wrapper.run_task_from_input()

    assert [(r.exit_code, r.job_error_message) for r in reported] == [(1, "Could not find the 'Missing' class")]


# -- signals between tasks: the executor is idle or loading the next input --

@pytest.fixture
def reported_to(isolated_wrapper, monkeypatch):
    """Each reported result with the callback URL it was sent to."""
    results = []

    def capture(context):
        results.append((base64.b64decode(isolated_wrapper.callback_url).decode(), context))

    monkeypatch.setattr(isolated_wrapper, "update_output_context", capture)
    return results


def callback_of(secret):
    return base64.b64decode(base64.b64decode(secret.data["url"])).decode()


def test_removing_an_idle_executor_does_not_abort_its_last_task(daemon_wrapper, reported, exit_codes, monkeypatch):
    secret = StaticSecret("Last")
    monkeypatch.setattr(k8s, "get_client", lambda: secret)
    daemon_wrapper.run_task_from_input()
    last_task = daemon_wrapper.dai_task_object
    monkeypatch.setattr(last_task, "abort", mock.Mock())

    daemon_wrapper.abort_handler(signal.SIGTERM, None)

    last_task.abort.assert_not_called()
    assert not last_task.is_abort_requested()
    assert greetings(reported) == ["Hello Last"]
    assert exit_codes == [0]


def test_skipping_an_input_already_run_leaves_the_executor_idle(daemon_wrapper, reported, exit_codes, monkeypatch):
    secret = StaticSecret("Once")
    monkeypatch.setattr(k8s, "get_client", lambda: secret)
    daemon_wrapper.run_task_from_input()
    daemon_wrapper.run_task_from_input()  # a late watch event: the secret still holds the same input

    daemon_wrapper.abort_handler(signal.SIGTERM, None)

    assert greetings(reported) == ["Hello Once"]
    assert exit_codes == [0]


class Exited(BaseException):
    """Raised in place of os._exit(), so the process 'ends' where the real one would."""


def test_abort_while_the_next_input_loads_is_reported_for_that_input(daemon_wrapper, reported_to, monkeypatch):
    def exit_process(code):
        raise Exited(code)

    monkeypatch.setattr(daemon_wrapper.os, "_exit", exit_process)
    secret = StaticSecret("First")
    first_callback = callback_of(secret)
    monkeypatch.setattr(k8s, "get_client", lambda: secret)
    daemon_wrapper.run_task_from_input()
    first_task = daemon_wrapper.dai_task_object
    monkeypatch.setattr(first_task, "abort", mock.Mock())

    # The runner assigns the next task, then aborts it while the wrapper is still finding its task class.
    secret.data = input_secret_data("Next")

    def abort_while_loading(root_dir, class_name):
        daemon_wrapper.abort_handler(signal.SIGABRT, None)

    monkeypatch.setattr(daemon_wrapper, "find_class_file", abort_while_loading)
    with pytest.raises(Exited) as exited:
        daemon_wrapper.run_task_from_input()

    first_task.abort.assert_not_called()
    assert exited.value.args == (1,)
    assert reported_to == [
        (first_callback, OutputContext(0, "", {"greeting": "Hello First"}, [])),
        (callback_of(secret), OutputContext(1, "Abort requested before the task started", {}, [])),
    ]


def test_unreadable_next_input_is_not_reported_to_the_previous_task(daemon_wrapper, reported_to, monkeypatch):
    secret = StaticSecret("First")
    monkeypatch.setattr(k8s, "get_client", lambda: secret)
    daemon_wrapper.run_task_from_input()

    # The executor is being removed: its secret can no longer be read.
    monkeypatch.setattr(secret, "read_namespaced_secret", mock.Mock(side_effect=RuntimeError("(403) Forbidden")))
    assert daemon_wrapper.run_task_from_input() is None

    assert len(reported_to) == 1


# -- the input context secret cannot be read for a while ---------------------

def test_next_task_runs_after_its_input_could_not_be_read_for_a_while(daemon_wrapper, reported_to, monkeypatch):
    secret = StaticSecret("First")
    monkeypatch.setattr(k8s, "get_client", lambda: secret)
    first_key = daemon_wrapper.run_task_from_input()

    # The runner assigns the next task; the first two reads of its input fail (API server unavailable).
    secret.data = input_secret_data("Next")
    real_read = secret.read_namespaced_secret
    reads = mock.Mock(side_effect=[RuntimeError("connection refused"), RuntimeError("connection refused"),
                                   real_read(SECRET, NAMESPACE)])
    monkeypatch.setattr(secret, "read_namespaced_secret", reads)

    stop = threading.Event()
    events = [modified(first_key), modified(secret.data["session-key"])]
    monkeypatch.setattr(watcher.watch, "Watch", lambda: OneWatch(events, stop))
    watcher.start_input_context_watcher(daemon_wrapper.run_task_from_input, first_key, stop)

    assert reads.call_count == 3
    assert [(url, r.output_properties.get("greeting")) for url, r in reported_to] == [
        ("http://127.0.0.1:9/callback/First", "Hello First"),
        ("http://127.0.0.1:9/callback/Next", "Hello Next"),
    ]


def test_executor_exits_when_its_first_input_cannot_be_read(daemon_wrapper, reported, monkeypatch):
    # The first task's result may never reach the runner; exiting makes the runner fail that task,
    # instead of the watcher treating its input as handled and the task hanging.
    unreadable = mock.Mock(read_namespaced_secret=mock.Mock(side_effect=RuntimeError("connection refused")))
    monkeypatch.setattr(k8s, "get_client", lambda: unreadable)
    start_watcher = mock.Mock()
    monkeypatch.setattr(watcher, "start_input_context_watcher", start_watcher)

    with pytest.raises(SystemExit) as exited:
        daemon_wrapper.run()

    assert exited.value.code == 1
    start_watcher.assert_not_called()


def test_input_with_unusable_routing_data_stays_unread_until_corrected(daemon_wrapper, reported_to, monkeypatch):
    secret = StaticSecret("First")
    monkeypatch.setattr(k8s, "get_client", lambda: secret)
    daemon_wrapper.run_task_from_input()

    # The next input has no callback URL yet: nothing can be routed, so it is not claimed.
    secret.data = input_secret_data("Next")
    url = secret.data.pop("url")
    assert daemon_wrapper.run_task_from_input() is None

    secret.data["url"] = url
    assert daemon_wrapper.run_task_from_input() == secret.data["session-key"]

    assert [r.output_properties.get("greeting") for _, r in reported_to] == ["Hello First", "Hello Next"]


def test_abort_while_switching_to_the_next_task_is_reported_for_that_task(daemon_wrapper, reported_to, monkeypatch):
    # A signal can interrupt the main thread between installing the new task's callback and
    # resetting the report state; it must not look like an idle executor (exit 0, nothing reported).
    def exit_process(code):
        raise Exited(code)

    monkeypatch.setattr(daemon_wrapper.os, "_exit", exit_process)
    secret = StaticSecret("First")
    first_callback = callback_of(secret)
    monkeypatch.setattr(k8s, "get_client", lambda: secret)
    daemon_wrapper.run_task_from_input()
    secret.data = input_secret_data("Next")

    real_start = daemon_wrapper._start_task_input

    def abort_mid_handoff():
        daemon_wrapper.abort_handler(signal.SIGABRT, None)  # the callback is switched, the report state not yet
        real_start()

    monkeypatch.setattr(daemon_wrapper, "_start_task_input", abort_mid_handoff)
    with pytest.raises(Exited) as exited:
        daemon_wrapper.run_task_from_input()

    assert exited.value.args == (1,)
    assert reported_to == [
        (first_callback, OutputContext(0, "", {"greeting": "Hello First"}, [])),
        (callback_of(secret), OutputContext(1, "Abort requested before the task started", {}, [])),
    ]


def test_abort_right_after_the_handoff_begins_is_not_lost(daemon_wrapper, reported_to, monkeypatch):
    # A real signal handler can run between any two statements. Fire it at the first line that runs
    # once _task_handoff() has set its flag: the deferred signal must survive the rest of the set-up.
    def exit_process(code):
        raise Exited(code)

    monkeypatch.setattr(daemon_wrapper.os, "_exit", exit_process)
    secret = StaticSecret("First")
    monkeypatch.setattr(k8s, "get_client", lambda: secret)
    daemon_wrapper.run_task_from_input()
    secret.data = input_secret_data("Next")

    handoff_code = daemon_wrapper._task_handoff.__wrapped__.__code__
    fired = []

    def trace_calls(frame, event, arg):
        if frame.f_code is not handoff_code:
            return None

        def trace_lines(frame, event, arg):
            if event == "line" and daemon_wrapper._handoff_in_progress and not fired:
                fired.append(frame.f_lineno)
                daemon_wrapper.abort_handler(signal.SIGABRT, None)
            return trace_lines

        return trace_lines

    previous = sys.gettrace()
    sys.settrace(trace_calls)
    try:
        with pytest.raises(Exited) as exited:
            daemon_wrapper.run_task_from_input()
    finally:
        sys.settrace(previous)

    assert fired, "the signal was never injected"
    assert exited.value.args == (1,)
    assert reported_to[1:] == [
        (callback_of(secret), OutputContext(1, "Abort requested before the task started", {}, []))]


def test_file_input_announced_by_a_watch_event_runs_once(daemon_wrapper, reported, monkeypatch, tmp_path):
    # Not a runner set-up (daemon mode uses a secret), but a file input must never look unread,
    # or the watcher would run it again and again.
    input_path = tmp_path / "input.json"
    input_path.write_text(json.dumps(input_context("containerExamples.Hello", [task_property("yourName", "File")])))
    monkeypatch.setattr(daemon_wrapper, "input_context_file", str(input_path))
    # The watch is faked below; without a client the watcher would retry forever where no kubeconfig exists (CI).
    monkeypatch.setattr(k8s, "get_client", lambda: SimpleNamespace(list_namespaced_secret=object()))
    stop = threading.Event()
    calls = []

    def run_once_then_stop():
        calls.append(1)
        if len(calls) > 1:
            stop.set()  # a retry: stop instead of looping forever
        return daemon_wrapper.run_task_from_input()

    monkeypatch.setattr(watcher.watch, "Watch", lambda: OneWatch([modified("k1"), modified("k2")], stop))
    watcher.start_input_context_watcher(run_once_then_stop, None, stop)

    assert len(calls) == 1
    assert greetings(reported) == ["Hello File"]
