import os
import threading
from typing import Callable, Optional

from kubernetes import watch
from .logger import dai_logger
from digitalai.release.integration import k8s

# Delay before re-opening the input-context watch after its connection fails,
# doubled after each consecutive failure up to the maximum.
RECONNECT_DELAY_SECONDS = float(os.getenv("INPUT_WATCH_RECONNECT_DELAY", "1"))
MAX_RECONNECT_DELAY_SECONDS = float(os.getenv("INPUT_WATCH_MAX_RECONNECT_DELAY", "30"))


class SessionKeyTracker:
    """
    Remembers the session key of the input that was last run.

    The runner writes every new job to the input-context secret with a new
    session key, so a key that differs from the last one run means a new job.
    One tracker is shared by every watch connection the process opens, so an
    event replayed after a reconnect, or read late from a connection buffer,
    cannot run the same input twice.
    """

    def __init__(self, last_run: Optional[str] = None):
        self.last_run = last_run

    def is_new(self, session_key: Optional[str]) -> bool:
        return bool(session_key) and session_key != self.last_run


def _input_secret_location():
    secret_name = os.getenv("INPUT_CONTEXT_SECRET")
    namespace = os.getenv("RUNNER_NAMESPACE")
    if not secret_name or not namespace:
        raise ValueError(
            "INPUT_CONTEXT_SECRET and RUNNER_NAMESPACE must be set to watch the input context secret"
        )
    return secret_name, namespace


def start_input_context_watcher(on_input_context_update_func: Callable[[], Optional[str]],
                                current_session_key: Optional[str] = None,
                                stop: Optional[threading.Event] = None) -> None:
    """
    Runs the daemon-mode loop: waits for new input in the input-context secret
    and calls on_input_context_update_func once per new session key, until stop
    is set or the process exits.

    current_session_key is the session key of the input already run before the
    loop started, so the secret's current state is not run a second time.

    The callback runs on this loop and must not start another watcher. If it
    returns the session key of the input it actually ran, that key is the one
    remembered, so a later event for that key is ignored.

    A failed watch connection (for example one closed by the network after a
    long idle period) is re-opened with a backoff instead of ending the loop.
    """
    dai_logger.info("Input context watcher started")

    try:
        _input_secret_location()
    except ValueError:
        dai_logger.error("Unexpected error occurred.", exc_info=True)
        return

    stop = stop or threading.Event()
    tracker = SessionKeyTracker(current_session_key)
    delay = RECONNECT_DELAY_SECONDS

    while not stop.is_set():
        try:
            events = start_input_secret_watcher(on_input_context_update_func, stop, tracker)
            if stop.is_set():
                break
            # The stream ended cleanly (e.g. the server timed out the watch): re-open it. A stream
            # that delivered events was healthy, so start the backoff over; one that delivered
            # none keeps backing off, so repeated empty responses cannot flood the API server.
            if events:
                delay = RECONNECT_DELAY_SECONDS
            stop.wait(delay)
            if not events:
                delay = min(delay * 2, MAX_RECONNECT_DELAY_SECONDS)
        except Exception as e:
            if stop.is_set():
                break
            dai_logger.warning(f"Input context watch failed ({type(e).__name__}: {e}); "
                               f"reconnecting in {delay:g}s")
            stop.wait(delay)
            delay = min(delay * 2, MAX_RECONNECT_DELAY_SECONDS)


def start_input_secret_watcher(on_input_context_update_func: Callable[[], Optional[str]],
                               stop: threading.Event,
                               tracker: Optional[SessionKeyTracker] = None) -> int:
    """
    Opens one watch connection on the input-context secret and calls
    on_input_context_update_func for each new session key it sees, until the
    connection ends or stop is set. Returns the number of events received.

    Without a tracker, the first session key seen is only recorded, since the
    input it belongs to is assumed to have been run already.
    """
    dai_logger.info("Input secret watcher started")

    secret_name, namespace = _input_secret_location()
    kubernetes_client = k8s.get_client()
    field_selector = "metadata.name=" + secret_name
    record_first_key = tracker is None
    tracker = tracker or SessionKeyTracker()

    events = 0
    w = watch.Watch()
    try:
        for event in w.stream(kubernetes_client.list_namespaced_secret, namespace, field_selector=field_selector):
            events += 1
            # The runner deletes the secret when it evicts the executor; that is not new input.
            if event.get("type") != "DELETED":
                secret = event['object']
                session_key = secret.data.get("session-key") if secret.data else None

                if record_first_key and session_key:
                    record_first_key = False
                    tracker.last_run = session_key
                elif tracker.is_new(session_key):
                    dai_logger.info("Detected input context value change")
                    # Record the key before running, so a failed run is not retried by a later event.
                    tracker.last_run = session_key
                    ran = on_input_context_update_func()
                    if isinstance(ran, str) and ran:
                        tracker.last_run = ran

            # Check if the watcher should be stopped
            if stop.is_set():
                break
    finally:
        # Always release the underlying streaming connection.
        w.stop()
    return events
