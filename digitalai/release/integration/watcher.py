import logging
import os
import threading

from kubernetes import watch

from digitalai.release.integration import k8s

logger = logging.getLogger("Digitalai")


def start_input_context_watcher(on_input_context_update_func):
    logger.debug("input context watcher started")

    stop = threading.Event()

    try:
        start_input_secret_watcher(on_input_context_update_func, stop)
    except Exception:
        logger.error("Unexpected error occurred.", exc_info=True)
        return

    # Wait until the watcher is stopped
    stop.wait()


def start_input_secret_watcher(on_input_context_update_func, stop):
    logger.debug("input secret watcher started")
    kubernetes_client = k8s.get_client()

    field_selector = "metadata.name=" + os.getenv("INPUT_CONTEXT_SECRET")
    namespace = os.getenv("RUNNER_NAMESPACE")

    w = watch.Watch()
    for event in w.stream(kubernetes_client.list_namespaced_secret, namespace, field_selector=field_selector):
        logger.debug("event is %s", event)
        secret = event['object']
        old_input = event['raw_object']['data'].get("input")
        logger.debug("old input %s", old_input)
        new_input = secret.data.get("input")
        logger.debug("new input %s", new_input)

        # Checking if 'input' field has changed
        if old_input != new_input:
            logger.info("Detected input context value change")
            on_input_context_update_func()

        # Check if the watcher should be stopped
        if stop.is_set():
            break
