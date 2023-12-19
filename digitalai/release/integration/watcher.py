import logging
import os
import threading

from kubernetes import watch

from digitalai.release.integration import k8s

logger = logging.getLogger("Digitalai")


def start_input_context_watcher(on_input_context_update_func):
    logger.debug("Input context watcher started")

    stop = threading.Event()

    try:
        start_input_secret_watcher(on_input_context_update_func, stop)
    except Exception:
        logger.error("Unexpected error occurred.", exc_info=True)
        return

    # Wait until the watcher is stopped
    stop.wait()


def start_input_secret_watcher(on_input_context_update_func, stop):
    logger.debug("Input secret watcher started")

    kubernetes_client = k8s.get_client()
    field_selector = "metadata.name=" + os.getenv("INPUT_CONTEXT_SECRET")
    namespace = os.getenv("RUNNER_NAMESPACE")
    old_session_key = None

    w = watch.Watch()
    for event in w.stream(kubernetes_client.list_namespaced_secret, namespace, field_selector=field_selector):
        secret = event['object']
        logger.debug(f"secret {secret}")
        new_session_key = secret.data.get("session-key")

        # Checking if 'session-key' field has changed
        if old_session_key and old_session_key != new_session_key:
            logger.info("Detected input context value change")
            on_input_context_update_func()

        # Set old session-key value
        old_session_key = new_session_key

        # Check if the watcher should be stopped
        if stop.is_set():
            break
