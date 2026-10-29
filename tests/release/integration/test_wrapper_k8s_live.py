"""
The wrapper's Kubernetes path against a real cluster.

Uses only the kubeconfig context named by RELEASE_LIVE_K8S_CONTEXT (default
``docker-desktop``), selected by name, so a different current context, such as
a shared cluster, is never touched. The module is skipped when that context
is missing or its API server does not answer.

Each run creates a namespace ``sdk-live-<random>`` for the runner's secrets and
deletes it afterwards. Callback and fetch URLs point at an HTTP server the test
runs on 127.0.0.1, which the wrapper reaches from this host.

Secrets are created with ``stringData`` holding what the runner stores; the
API returns them base64-encoded in ``data``, which is what the wrapper reads.
"""
import base64
import functools
import json
import os
import subprocess
import sys
import threading
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from types import SimpleNamespace

import pytest
import yaml
from kubernetes import client, config

from digitalai.release.integration import k8s, watcher
from digitalai.release.integration.job_data_encryptor import AESJobDataEncryptor
from digitalai.release.integration.output_context import OutputContext
from tests.support import input_context, task_property

pytestmark = pytest.mark.live

CONTEXT = os.getenv("RELEASE_LIVE_K8S_CONTEXT", "docker-desktop")
RESULT_KEY = "result"


def b64(text: str) -> str:
    return base64.b64encode(text.encode()).decode()


def unique(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:8]}"


def kubeconfig_path() -> str:
    return os.path.expanduser(os.getenv("KUBECONFIG", "~/.kube/config").split(os.pathsep)[0])


def write_single_context_kubeconfig(source: str, context: str, target) -> None:
    """
    Copies just ``context`` (with its cluster and user) into a kubeconfig of its own.

    Relative certificate, key and token file paths resolve against the
    kubeconfig's own directory, so they are made absolute for the copy.
    """
    with open(source) as f:
        full = yaml.safe_load(f)
    ctx = next(c for c in full["contexts"] if c["name"] == context)
    cluster = next(c for c in full["clusters"] if c["name"] == ctx["context"]["cluster"])
    user = next(u for u in full["users"] if u["name"] == ctx["context"]["user"])
    source_dir = os.path.dirname(os.path.abspath(source))
    for entry, keys in ((cluster["cluster"], ("certificate-authority",)),
                        (user["user"], ("client-certificate", "client-key", "tokenFile"))):
        for key in keys:
            if entry.get(key):
                entry[key] = os.path.join(source_dir, os.path.expanduser(entry[key]))
    target.write_text(yaml.safe_dump({"apiVersion": "v1", "kind": "Config", "current-context": context,
                                      "contexts": [ctx], "clusters": [cluster], "users": [user]}))


@pytest.fixture(scope="module")
def cluster(tmp_path_factory):
    source = kubeconfig_path()
    try:
        contexts, _ = config.list_kube_config_contexts(config_file=source)
    except Exception as exc:  # noqa: BLE001 - no usable kubeconfig means "skip"
        pytest.skip(f"no kubeconfig at {source}: {exc}")
    if CONTEXT not in [c["name"] for c in contexts]:
        pytest.skip(f"kubeconfig has no context named {CONTEXT!r}")

    api_client = config.new_client_from_config(config_file=source, context=CONTEXT)
    core = client.CoreV1Api(api_client)
    try:
        core.list_namespace(limit=1, _request_timeout=3)
    except Exception as exc:  # noqa: BLE001 - an unreachable cluster means "skip"
        api_client.close()
        pytest.skip(f"Kubernetes context {CONTEXT!r} is not reachable: {exc}")

    namespace = unique("sdk-live")
    core.create_namespace(client.V1Namespace(metadata=client.V1ObjectMeta(name=namespace)))
    kubeconfig = tmp_path_factory.mktemp("kube") / "config"
    write_single_context_kubeconfig(source, CONTEXT, kubeconfig)
    try:
        yield SimpleNamespace(core=core, namespace=namespace, kubeconfig=kubeconfig)
    finally:
        core.delete_namespace(namespace)
        api_client.close()


def create_secret(cluster, prefix, string_data) -> str:
    name = unique(prefix)
    cluster.core.create_namespaced_secret(cluster.namespace, client.V1Secret(
        metadata=client.V1ObjectMeta(name=name), string_data=string_data))
    return name


def read_secret(cluster, name):
    return cluster.core.read_namespaced_secret(name, cluster.namespace).data


def create_input_secret(cluster, session_key, callback_url, *, encrypted_input="", fetch_url=None) -> str:
    """The input-context secret as the runner creates it."""
    data = {"session-key": session_key, "url": b64(callback_url), "input": encrypted_input}
    if fetch_url:
        data["fetchUrl"] = b64(fetch_url)
    return create_secret(cluster, "input", data)


class LocalServer:
    """An HTTP server on 127.0.0.1 that records requests and replies with queued responses."""

    def __init__(self):
        self.requests = []
        self._responses = {}
        server = self

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                self._handle(b"")

            def do_POST(self):
                self._handle(self.rfile.read(int(self.headers.get("Content-Length", 0))))

            def _handle(self, body):
                server.requests.append((self.command, self.path, body))
                status, payload = server._next_response(self.path)
                self.send_response(status)
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, *args):
                pass

        self._httpd = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=self._httpd.serve_forever, daemon=True).start()

    def url(self, path: str) -> str:
        return f"http://127.0.0.1:{self._httpd.server_port}{path}"

    def respond(self, path, *responses):
        """Replies to ``path`` with each (status, body) in turn, then keeps repeating the last."""
        self._responses[path] = list(responses)

    def _next_response(self, path):
        queue = self._responses.get(path, [(200, b"")])
        return queue.pop(0) if len(queue) > 1 else queue[0]

    def close(self):
        self._httpd.shutdown()
        self._httpd.server_close()


@pytest.fixture
def server(monkeypatch):
    monkeypatch.setenv("NO_PROXY", "127.0.0.1,localhost")
    local = LocalServer()
    yield local
    local.close()


@pytest.fixture
def session_key():
    return base64.b64encode(os.urandom(32)).decode()


@pytest.fixture
def k8s_wrapper(isolated_wrapper, cluster, monkeypatch):
    """The wrapper set up as on a runner pod, using the live cluster's client."""
    monkeypatch.setattr(k8s, "kubernetes_client", cluster.core)
    monkeypatch.setattr(isolated_wrapper, "runner_namespace", cluster.namespace)
    return isolated_wrapper


def encrypted_input(session_key, context):
    return AESJobDataEncryptor(session_key).encrypt(json.dumps(context))


# -- input -----------------------------------------------------------------

def test_reads_and_decrypts_the_input_secret(k8s_wrapper, cluster, monkeypatch, session_key):
    context = input_context(properties=[task_property("token", "t0ken", password=True)], password="run-as-pw")
    name = create_input_secret(cluster, session_key, "http://127.0.0.1:9/callback",
                               encrypted_input=encrypted_input(session_key, context))
    monkeypatch.setattr(k8s_wrapper, "input_context_secret", name)

    properties, task_type, _ = k8s_wrapper.get_task_details()

    assert (properties, task_type) == ({"token": "t0ken"}, "containerExamples.Hello")
    assert base64.b64decode(k8s_wrapper.callback_url).decode() == "http://127.0.0.1:9/callback"
    assert k8s_wrapper.masked_std_out.secrets == ["t0ken", "run-as-pw"]


def test_fetches_the_input_when_the_secret_has_none(k8s_wrapper, cluster, server, monkeypatch, session_key):
    server.respond("/input", (200, encrypted_input(session_key, input_context()).encode()))
    name = create_input_secret(cluster, session_key, server.url("/callback"), fetch_url=server.url("/input"))
    monkeypatch.setattr(k8s_wrapper, "input_context_secret", name)

    properties, _, _ = k8s_wrapper.get_task_details()

    assert properties["yourName"] == "World"
    assert server.requests == [("GET", "/input", b"")]


# -- result ----------------------------------------------------------------

def test_stores_the_result_in_the_result_secret_and_posts_it(k8s_wrapper, cluster, server, monkeypatch,
                                                             session_key):
    result_secret = create_secret(cluster, "result", {RESULT_KEY: ""})
    monkeypatch.setattr(k8s_wrapper, "base64_session_key", session_key)
    monkeypatch.setattr(k8s_wrapper, "result_secret_key", f"{cluster.namespace}:{result_secret}:{RESULT_KEY}")
    monkeypatch.setattr(k8s_wrapper, "callback_url", b64(server.url("/callback")))

    k8s_wrapper.update_output_context(OutputContext(0, "", {"greeting": "Hello"}, []))

    stored = read_secret(cluster, result_secret)[RESULT_KEY]
    assert json.loads(AESJobDataEncryptor(session_key).decrypt(stored)) == {
        "exitCode": 0, "jobErrorMessage": "", "outputProperties": {"greeting": "Hello"}, "reportingRecords": [],
    }
    assert server.requests == [("POST", "/callback", stored.encode())]


def test_retry_rereads_the_callback_url_from_the_input_secret(k8s_wrapper, cluster, server, monkeypatch,
                                                              session_key):
    server.respond("/first", (503, b""))
    name = create_input_secret(cluster, session_key, server.url("/second"))
    monkeypatch.setattr(k8s_wrapper, "input_context_secret", name)
    monkeypatch.setattr(k8s_wrapper, "base64_session_key", session_key)
    monkeypatch.setattr(k8s_wrapper, "callback_url", b64(server.url("/first")))

    # Too large for a secret, so a failed callback is retried.
    k8s_wrapper.update_output_context(OutputContext(0, "", {"big": "x" * (1024 * 1024)}, []))

    assert [(method, path) for method, path, _ in server.requests] == [("POST", "/first"), ("POST", "/second")]


# -- watcher ---------------------------------------------------------------

def test_watcher_calls_back_on_each_session_key_change_until_stopped(cluster, monkeypatch):
    name = create_secret(cluster, "input", {"session-key": "k1"})
    monkeypatch.setenv("INPUT_CONTEXT_SECRET", name)
    monkeypatch.setenv("RUNNER_NAMESPACE", cluster.namespace)

    # Watch.stream() calls the list function to open each watch; once it returns, changes are seen.
    watching = threading.Event()
    list_secrets = cluster.core.list_namespaced_secret

    @functools.wraps(list_secrets)
    def list_and_signal(*args, **kwargs):
        response = list_secrets(*args, **kwargs)
        watching.set()
        return response

    monkeypatch.setattr(k8s, "kubernetes_client", SimpleNamespace(list_namespaced_secret=list_and_signal))

    def set_session_key(value):
        cluster.core.patch_namespaced_secret(name, cluster.namespace, {"stringData": {"session-key": value}})

    updates = []
    updated = threading.Event()
    stop = threading.Event()

    def on_update():
        updates.append(read_secret(cluster, name)["session-key"])
        if len(updates) == 2:
            # The watcher checks the stop flag after each callback, so this ends the watch after k3.
            # Setting it from the test thread instead could stop the watch before k3 is seen.
            stop.set()
        updated.set()

    thread = threading.Thread(target=watcher.start_input_secret_watcher, args=(on_update, stop), daemon=True)
    thread.start()
    assert watching.wait(10), "the watch did not start"

    set_session_key("k2")
    assert updated.wait(10), "no callback after the session key changed"
    set_session_key("k3")
    thread.join(10)

    assert not thread.is_alive()
    assert updates == [b64("k2"), b64("k3")]


# -- end to end ------------------------------------------------------------

@pytest.mark.e2e
def test_wrapper_runs_a_task_from_kubernetes_secrets(cluster, server, task_workspace, session_key):
    context = input_context("containerExamples.Hello", [task_property("yourName", "World")])
    input_secret = create_input_secret(cluster, session_key, server.url("/callback"),
                                       encrypted_input=encrypted_input(session_key, context))
    result_secret = create_secret(cluster, "result", {RESULT_KEY: ""})
    env = {k: v for k, v in os.environ.items() if k not in (
        "INPUT_LOCATION", "OUTPUT_LOCATION", "SESSION_KEY", "CALLBACK_URL", "EXECUTOR_EXECUTION_MODE",
        "KUBERNETES_SERVICE_HOST", "SKIP_TLS_LEGACY_K8S")}
    env.update(INPUT_CONTEXT_SECRET=input_secret, RUNNER_NAMESPACE=cluster.namespace,
               RESULT_SECRET_NAME=f"{cluster.namespace}:{result_secret}:{RESULT_KEY}",
               RELEASE_URL="http://localhost:5516", KUBECONFIG=str(cluster.kubeconfig))

    process = subprocess.run([sys.executable, "-m", "digitalai.release.integration.wrapper"], cwd=task_workspace,
                             env=env, capture_output=True, text=True, timeout=60)

    assert process.returncode == 0, f"stdout:\n{process.stdout}\nstderr:\n{process.stderr}"
    stored = read_secret(cluster, result_secret)[RESULT_KEY]
    assert json.loads(AESJobDataEncryptor(session_key).decrypt(stored)) == {
        "exitCode": 0, "jobErrorMessage": "", "outputProperties": {"greeting": "Hello World"},
        "reportingRecords": [],
    }
    assert server.requests == [("POST", "/callback", stored.encode())]
