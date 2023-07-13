import threading

from kubernetes import client, config
from kubernetes.client import CoreV1Api

kubernetes_client: CoreV1Api = None
lock = threading.Lock()


def get_client():
    global kubernetes_client

    if not kubernetes_client:
        with lock:
            if not kubernetes_client:
                config.load_kube_config()
                kubernetes_client = client.CoreV1Api()

    return kubernetes_client
