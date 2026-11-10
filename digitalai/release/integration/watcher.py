"""
Daemon mode: waits for the runner to put the next task's input in the input
context secret of a reused executor pod, and runs it.

The runner starts each task on an idle executor by writing new input with a new
``session-key`` to the secret. The watcher calls back once for each new
``session-key``, one at a time:

- it remembers every ``session-key`` it has handled, and calls back only for a
  key it has not seen. The callback returns the key of the input it read, which
  then counts as handled too, as the secret can change between the event and
  the read. (The wrapper also refuses to run an input twice, so this only saves
  needless reads of the secret.)
- if the callback could not read the input (returns None), the key is not
  handled yet: the callback is repeated with a backoff until the input is read,
  so a brief API server outage cannot lose a task.
- a single watch is open at a time. When it fails or ends, it is opened again,
  with a backoff, and the handled keys are kept, so neither events delivered
  again nor the current state of the secret can run a handled task again.

Earlier versions started a new watcher from inside each task run, leaving one
open watch per finished task. When the newest watch failed (e.g. while the
runner was removing an idle executor), control returned to an older watcher,
which read the ``session-key`` changes it had buffered and ran the executor's
last task again (D-44246).
"""
import os
import threading
import time
from typing import Callable, Optional, Set

from kubernetes import watch
from .logger import dai_logger
from digitalai.release.integration import k8s

SESSION_KEY = "session-key"

# Delay before opening the watch again after it failed or ended. It doubles each
# time a watch fails or ends soon after it was opened, up to the maximum, and
# starts over after a watch that stayed open at least the maximum delay.
RECONNECT_DELAY_SECONDS = float(os.getenv("INPUT_WATCH_RECONNECT_DELAY", "1"))
MAX_RECONNECT_DELAY_SECONDS = float(os.getenv("INPUT_WATCH_MAX_RECONNECT_DELAY", "30"))

# Called for each new input; returns the session-key of the input it read
# (anything but None counts as read), or None if it could not read the input,
# in which case it is called again.
OnNewInput = Callable[[], Optional[str]]

# Replaced in tests.
_clock = time.monotonic


class _WatchState:
    """What the watcher keeps across watches."""

    def __init__(self, executed_session_key: Optional[str]):
        # Every session-key run so far (or found already present at start-up).
        # The runner uses a new key per task, so the set grows by one per task.
        self.handled_session_keys: Set[str] = {executed_session_key} if executed_session_key else set()


def start_input_context_watcher(on_input_context_update_func: OnNewInput,
                                executed_session_key: Optional[str] = None,
                                stop: Optional[threading.Event] = None) -> None:
    """
    Watches the input context secret and calls on_input_context_update_func, on
    this thread, once for each new session-key. The callback must not start
    another watcher.

    executed_session_key is the session-key of the input that has already been
    run; a secret holding any other key at start-up is new input and is run.
    If it is None, the key found when the watch opens counts as handled.

    The watch is opened again, with a backoff, whenever it fails or ends: a
    watch can drop at any time (API server restarts, idle connections closed
    by the network) and the executor must keep serving tasks. The process ends
    when the runner removes the pod. Returns only when stop is set, or at once
    if the secret to watch is not configured.
    """
    dai_logger.info("Input context watcher started")
    stop = stop or threading.Event()
    state = _WatchState(executed_session_key)
    delay = RECONNECT_DELAY_SECONDS

    while not stop.is_set():
        opened_at = _clock()
        try:
            _watch_input_secret(on_input_context_update_func, stop, state)
            reason = "ended"
        except ValueError:
            # Configuration error: opening the watch again cannot fix it.
            dai_logger.error("Cannot watch the input context secret.", exc_info=True)
            return
        except Exception as e:
            reason = f"failed ({type(e).__name__}: {e})"

        if stop.is_set():
            return
        if _clock() - opened_at >= MAX_RECONNECT_DELAY_SECONDS:
            # The watch was healthy; this is not part of a run of failures.
            delay = RECONNECT_DELAY_SECONDS
        dai_logger.warning(f"Input context watch {reason}; watching again in {delay:g}s")
        stop.wait(delay)
        delay = min(delay * 2, MAX_RECONNECT_DELAY_SECONDS)


def start_input_secret_watcher(on_input_context_update_func: OnNewInput, stop: threading.Event,
                               executed_session_key: Optional[str] = None) -> None:
    """
    Opens a single watch on the input context secret and calls
    on_input_context_update_func for each new session-key, until the watch
    ends or fails (raised) or stop is set. See start_input_context_watcher()
    for executed_session_key.
    """
    _watch_input_secret(on_input_context_update_func, stop, _WatchState(executed_session_key))


def _watch_input_secret(on_new_input: OnNewInput, stop: threading.Event, state: _WatchState) -> None:
    dai_logger.info("Input secret watcher started")

    secret_name = os.getenv("INPUT_CONTEXT_SECRET")
    namespace = os.getenv("RUNNER_NAMESPACE")
    if not secret_name or not namespace:
        raise ValueError(
            "INPUT_CONTEXT_SECRET and RUNNER_NAMESPACE must be set to watch the input context secret"
        )

    kubernetes_client = k8s.get_client()
    field_selector = "metadata.name=" + secret_name

    w = watch.Watch()
    try:
        for event in w.stream(kubernetes_client.list_namespaced_secret, namespace, field_selector=field_selector):
            _handle_event(event, on_new_input, state, stop)

            # Check if the watcher should be stopped
            if stop.is_set():
                break
    finally:
        # Always release the underlying streaming connection.
        w.stop()


def _handle_event(event, on_new_input: OnNewInput, state: _WatchState, stop: threading.Event) -> None:
    if event.get("type") == "DELETED":
        # The runner deletes the secret when it removes the executor; there is no input to run.
        return

    secret = event["object"]
    session_key = secret.data.get(SESSION_KEY) if secret.data else None
    if not session_key or session_key in state.handled_session_keys:
        return

    if not state.handled_session_keys:
        # Nothing was run yet: this is the input the executor started with.
        state.handled_session_keys.add(session_key)
        return

    dai_logger.info("Detected input context value change")
    executed_session_key = _run_new_input(on_new_input, stop)
    if executed_session_key is None:
        return  # stopped before the input could be read
    # Handled once read, whatever the outcome: the wrapper has run it or
    # reported its failure, and never runs an input twice.
    state.handled_session_keys.add(session_key)
    if isinstance(executed_session_key, str) and executed_session_key:
        state.handled_session_keys.add(executed_session_key)


def _run_new_input(on_new_input: OnNewInput, stop: threading.Event):
    """
    Calls on_new_input until it has read the new input, i.e. returns anything
    but None. A None result means the input context secret could not be read
    (e.g. the API server was briefly unavailable): nothing was run or reported,
    so the call is repeated with a backoff rather than waiting for another
    event, which may never come. Returns None only if stop is set first.
    """
    delay = RECONNECT_DELAY_SECONDS
    while True:
        result = on_new_input()
        if result is not None:
            return result
        if stop.is_set():
            return None
        dai_logger.warning(f"Could not read the new task input; trying again in {delay:g}s")
        if stop.wait(delay):
            return None
        delay = min(delay * 2, MAX_RECONNECT_DELAY_SECONDS)
