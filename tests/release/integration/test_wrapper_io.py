"""
How the wrapper reads the input context and delivers the result.

With INPUT_LOCATION set, the input comes from a file and the result goes to
OUTPUT_LOCATION. On Kubernetes there is no file: the input comes from a
Secret, and the result goes to a result Secret and/or a callback URL.

Kubernetes stores Secret values base64-encoded, and the wrapper decodes the
URLs and session key once more, so the helpers below encode values exactly as
the runner does. The Kubernetes client and HTTP session are faked.
"""
import base64
import json
import os
from datetime import datetime, timezone
from types import SimpleNamespace
from unittest import mock

import pytest
import requests

from digitalai.release.integration import BuildRecord, k8s
from digitalai.release.integration.job_data_encryptor import AESJobDataEncryptor, NoOpJobDataEncryptor
from digitalai.release.integration.output_context import OutputContext
from tests.support import RELEASE_ID, input_context, task_property

pytestmark = pytest.mark.usefixtures("isolated_wrapper")

INPUT_SECRET = "input-context-secret"
NAMESPACE = "runner-ns"
RESULT_SECRET = "result-secret"
RESULT_KEY = "result"
CALLBACK_URL = "http://release-server/callback"
LARGE = "x" * (1024 * 1024 + 1024)  # over the 1 MiB a Secret can hold


def b64(value) -> str:
    """base64 of a str/bytes, as text."""
    if isinstance(value, str):
        value = value.encode("UTF-8")
    return base64.b64encode(value).decode("UTF-8")


def secret_url(url: str) -> str:
    """How a URL is stored in the input-context Secret: base64 of its base64."""
    return b64(b64(url))


class FakeCoreV1Api:
    """Serves secrets by name and records replacements."""

    def __init__(self, secrets):
        self.secrets = secrets
        self.replaced = []

    def read_namespaced_secret(self, name, namespace):
        return self.secrets[name]

    def replace_namespaced_secret(self, name, namespace, body):
        self.replaced.append((name, namespace, json.loads(json.dumps(body.data))))


def install_kube(monkeypatch, secrets):
    """Serves ``{secret name: data}`` through a fake Kubernetes client."""
    fake = FakeCoreV1Api({name: SimpleNamespace(data=data) for name, data in secrets.items()})
    monkeypatch.setattr(k8s, "get_client", lambda: fake)
    return fake


@pytest.fixture
def on_kubernetes(isolated_wrapper, monkeypatch):
    """Wrapper settings of a Kubernetes runner: input from a Secret, no files."""
    monkeypatch.setattr(isolated_wrapper, "input_context_secret", INPUT_SECRET)
    monkeypatch.setattr(isolated_wrapper, "runner_namespace", NAMESPACE)
    return isolated_wrapper


@pytest.fixture
def post(isolated_wrapper, monkeypatch):
    """The callback POST, recorded instead of sent."""
    fake = mock.Mock(name="_post_callback")
    monkeypatch.setattr(isolated_wrapper, "_post_callback", fake)
    return fake


@pytest.fixture
def session_key():
    return b64(os.urandom(32))


# -- encryptor -------------------------------------------------------------

def test_encryptor_is_aes_when_a_session_key_is_set(isolated_wrapper, monkeypatch, session_key):
    monkeypatch.setattr(isolated_wrapper, "base64_session_key", session_key)

    assert isinstance(isolated_wrapper.get_encryptor(), AESJobDataEncryptor)


def test_encryptor_is_noop_without_a_session_key(isolated_wrapper):
    assert isinstance(isolated_wrapper.get_encryptor(), NoOpJobDataEncryptor)


# -- input from a file -----------------------------------------------------

@pytest.fixture
def input_file(isolated_wrapper, monkeypatch, tmp_path):
    """Writes an input context to INPUT_LOCATION; call with the context dict."""
    path = tmp_path / "input.json"
    monkeypatch.setattr(isolated_wrapper, "input_context_file", str(path))

    def write(context, encryptor=NoOpJobDataEncryptor()):
        path.write_text(encryptor.encrypt(json.dumps(context)))

    return write


def test_task_details_from_file_return_properties_type_and_script(isolated_wrapper, input_file):
    input_file(input_context("containerExamples.Hello", [
        task_property("yourName", "World"),
        task_property("scriptLocation", "sample/hello.py"),
    ]))

    properties, task_type, script_path = isolated_wrapper.get_task_details()

    assert properties == {"yourName": "World", "scriptLocation": "sample/hello.py"}
    assert task_type == "containerExamples.Hello"
    assert script_path == "sample/hello.py"
    assert isolated_wrapper.input_context.release.id == RELEASE_ID


def test_task_details_from_file_are_decrypted_with_the_session_key(isolated_wrapper, monkeypatch, input_file,
                                                                    session_key):
    monkeypatch.setattr(isolated_wrapper, "base64_session_key", session_key)
    input_file(input_context(), AESJobDataEncryptor(session_key))

    properties, _, _ = isolated_wrapper.get_task_details()

    assert properties["yourName"] == "World"


def test_task_details_register_password_inputs_and_run_as_password_for_masking(isolated_wrapper, input_file):
    input_file(input_context(properties=[task_property("token", "t0ken", password=True)], password="run-as-pw"))

    isolated_wrapper.get_task_details()

    assert isolated_wrapper.masked_std_out.secrets == ["t0ken", "run-as-pw"]
    assert isolated_wrapper.masked_std_err.secrets == ["t0ken", "run-as-pw"]


def test_task_details_without_run_as_password_mask_only_password_inputs(isolated_wrapper, input_file):
    input_file(input_context(properties=[task_property("token", "t0ken", password=True)],
                             username=None, password=None))

    isolated_wrapper.get_task_details()

    assert isolated_wrapper.masked_std_out.secrets == ["t0ken"]


# -- input from a Kubernetes secret ----------------------------------------

def test_task_details_from_secret_set_the_callback_url(on_kubernetes, monkeypatch):
    install_kube(monkeypatch, {INPUT_SECRET: {
        "session-key": b64(""), "url": secret_url(CALLBACK_URL), "input": b64(json.dumps(input_context())),
    }})

    properties, task_type, _ = on_kubernetes.get_task_details()

    assert (properties["yourName"], task_type) == ("World", "containerExamples.Hello")
    assert base64.b64decode(on_kubernetes.callback_url).decode() == CALLBACK_URL


def test_task_details_from_secret_are_decrypted_with_its_session_key(on_kubernetes, monkeypatch, session_key):
    encrypted = AESJobDataEncryptor(session_key).encrypt(json.dumps(input_context()))
    install_kube(monkeypatch, {INPUT_SECRET: {
        "session-key": b64(session_key), "url": secret_url(CALLBACK_URL), "input": b64(encrypted),
    }})

    properties, _, _ = on_kubernetes.get_task_details()

    assert properties["yourName"] == "World"


def test_task_details_are_fetched_from_the_fetch_url_when_the_secret_has_no_input(on_kubernetes, monkeypatch):
    install_kube(monkeypatch, {INPUT_SECRET: {
        "session-key": b64(""), "url": secret_url(CALLBACK_URL), "input": "",
        "fetchUrl": secret_url("http://release-server/input"),
    }})
    response = mock.Mock(content=json.dumps(input_context()).encode())
    get = mock.Mock(return_value=response)
    monkeypatch.setattr(on_kubernetes._http_session, "get", get)

    properties, _, _ = on_kubernetes.get_task_details()

    get.assert_called_once_with("http://release-server/input", timeout=on_kubernetes._HTTP_TIMEOUT)
    response.raise_for_status.assert_called_once_with()
    assert properties["yourName"] == "World"


def test_task_details_fetch_failure_propagates(on_kubernetes, monkeypatch):
    install_kube(monkeypatch, {INPUT_SECRET: {
        "session-key": b64(""), "url": secret_url(CALLBACK_URL), "input": "",
        "fetchUrl": secret_url("http://release-server/input"),
    }})
    response = mock.Mock()
    response.raise_for_status.side_effect = requests.HTTPError("503 Service Unavailable")
    monkeypatch.setattr(on_kubernetes._http_session, "get", mock.Mock(return_value=response))

    with pytest.raises(requests.HTTPError):
        on_kubernetes.get_task_details()


def test_task_details_require_a_fetch_url_when_the_secret_has_no_input(on_kubernetes, monkeypatch):
    install_kube(monkeypatch, {INPUT_SECRET: {
        "session-key": b64(""), "url": secret_url(CALLBACK_URL), "input": "", "fetchUrl": "",
    }})

    with pytest.raises(ValueError, match="Cannot find fetch URL"):
        on_kubernetes.get_task_details()


def test_task_details_secret_read_failure_propagates(on_kubernetes, monkeypatch):
    client = mock.Mock()
    client.read_namespaced_secret.side_effect = RuntimeError("k8s unavailable")
    monkeypatch.setattr(k8s, "get_client", lambda: client)

    with pytest.raises(RuntimeError, match="k8s unavailable"):
        on_kubernetes.get_task_details()


# -- result to a file ------------------------------------------------------

@pytest.fixture
def output_file(isolated_wrapper, monkeypatch, tmp_path):
    path = tmp_path / "output.json"
    monkeypatch.setattr(isolated_wrapper, "output_context_file", str(path))
    return path


def test_result_is_written_to_the_output_file_as_json(isolated_wrapper, output_file):
    isolated_wrapper.update_output_context(OutputContext(0, "", {"greeting": "Hello World"}, []))

    assert json.loads(output_file.read_text()) == {
        "exitCode": 0, "jobErrorMessage": "", "outputProperties": {"greeting": "Hello World"}, "reportingRecords": [],
    }


def test_result_is_encrypted_with_the_session_key(isolated_wrapper, monkeypatch, output_file, session_key):
    monkeypatch.setattr(isolated_wrapper, "base64_session_key", session_key)

    isolated_wrapper.update_output_context(OutputContext(1, "failed", {}, []))

    assert json.loads(AESJobDataEncryptor(session_key).decrypt(output_file.read_text()))["exitCode"] == 1


def test_result_serializes_reporting_record_objects(isolated_wrapper, output_file):
    when = datetime(2026, 3, 4, 5, 6, 7, tzinfo=timezone.utc)
    record = BuildRecord(target_id="T1", build="#42", build_url="http://ci/42", project="app", outcome="SUCCESS",
                         start_date=when, end_date=when, duration="PT1M")

    isolated_wrapper.update_output_context(OutputContext(0, "", {}, [record]))

    (written,) = json.loads(output_file.read_text())["reportingRecords"]
    assert written == record.to_dict()


# -- result to a Kubernetes secret and callback ----------------------------

@pytest.fixture
def result_to_secret(on_kubernetes, monkeypatch, session_key):
    """
    Result delivery of a Kubernetes runner: a result Secret plus the callback URL.
    The runner always provides a session key there, and the wrapper relies on it:
    the encrypted result is base64 text, which a real API server accepts as a
    Secret ``data`` value, while plain JSON is rejected (see test_wrapper_k8s_live.py).
    """
    monkeypatch.setattr(on_kubernetes, "base64_session_key", session_key)
    monkeypatch.setattr(on_kubernetes, "result_secret_key", f"{NAMESPACE}:{RESULT_SECRET}:{RESULT_KEY}")
    monkeypatch.setattr(on_kubernetes, "callback_url", b64(CALLBACK_URL).encode())
    return on_kubernetes


def test_result_is_stored_in_the_result_secret_and_posted_to_the_callback(result_to_secret, monkeypatch, post,
                                                                           session_key):
    kube = install_kube(monkeypatch, {RESULT_SECRET: {RESULT_KEY: "", "other": "kept"}})

    result_to_secret.update_output_context(OutputContext(0, "", {"greeting": "Hello"}, []))

    ((name, namespace, data),) = kube.replaced
    assert (name, namespace) == (RESULT_SECRET, NAMESPACE)
    assert data["other"] == "kept"
    assert json.loads(AESJobDataEncryptor(session_key).decrypt(data[RESULT_KEY]))["outputProperties"] == {
        "greeting": "Hello"}
    post.assert_called_once_with(CALLBACK_URL, data[RESULT_KEY])


def test_result_too_large_for_a_secret_is_only_posted(result_to_secret, monkeypatch, post):
    kube = install_kube(monkeypatch, {RESULT_SECRET: {RESULT_KEY: ""}})

    result_to_secret.update_output_context(OutputContext(0, "", {"big": LARGE}, []))

    assert kube.replaced == []
    post.assert_called_once()


def test_result_secret_failure_is_logged_not_raised(result_to_secret, monkeypatch, post, dai_log):
    client = mock.Mock()
    client.read_namespaced_secret.side_effect = RuntimeError("k8s unavailable")
    monkeypatch.setattr(k8s, "get_client", lambda: client)

    result_to_secret.update_output_context(OutputContext(0, "", {}, []))

    assert "Unexpected error occurred." in dai_log.messages
    post.assert_not_called()


def test_failed_callback_of_a_small_result_is_logged_not_retried(result_to_secret, monkeypatch, post, dai_log):
    install_kube(monkeypatch, {RESULT_SECRET: {RESULT_KEY: ""}})
    post.side_effect = requests.ConnectionError("refused")
    retry = mock.Mock()
    monkeypatch.setattr(result_to_secret, "retry_push_result_infinitely", retry)

    result_to_secret.update_output_context(OutputContext(0, "", {}, []))

    retry.assert_not_called()
    assert "Unexpected error occurred." in dai_log.messages


def test_failed_callback_of_a_large_result_is_retried(result_to_secret, monkeypatch, post, session_key):
    install_kube(monkeypatch, {RESULT_SECRET: {RESULT_KEY: ""}})
    post.side_effect = requests.ConnectionError("refused")
    retry = mock.Mock()
    monkeypatch.setattr(result_to_secret, "retry_push_result_infinitely", retry)

    result_to_secret.update_output_context(OutputContext(0, "", {"big": LARGE}, []))

    (pushed,), _ = retry.call_args
    assert json.loads(AESJobDataEncryptor(session_key).decrypt(pushed))["outputProperties"]["big"] == LARGE


def test_retry_rereads_the_callback_url_and_backs_off_up_to_three_minutes(on_kubernetes, monkeypatch, post):
    urls = iter([f"{CALLBACK_URL}/{attempt}" for attempt in range(11)])
    client = mock.Mock()
    client.read_namespaced_secret.side_effect = lambda name, ns: SimpleNamespace(data={"url": secret_url(next(urls))})
    monkeypatch.setattr(k8s, "get_client", lambda: client)
    delivered = mock.Mock(name="response")
    post.side_effect = [requests.ConnectionError("refused")] * 10 + [delivered]
    sleeps = []
    monkeypatch.setattr(on_kubernetes.time, "sleep", sleeps.append)

    response = on_kubernetes.retry_push_result_infinitely("payload")

    assert sleeps == [1, 2, 4, 8, 16, 32, 64, 128, 180, 180]
    assert [c.args for c in post.call_args_list] == [(f"{CALLBACK_URL}/{n}", "payload") for n in range(11)]
    assert response is delivered
    client.read_namespaced_secret.assert_called_with(INPUT_SECRET, NAMESPACE)


@pytest.mark.parametrize("payload, input_file, expected", [
    (LARGE, "", True),
    ("small", "", False),
    (LARGE, "input.json", False),
], ids=["large-without-input-file", "small", "large-with-input-file"])
def test_should_retry_only_a_large_result_without_an_input_file(isolated_wrapper, monkeypatch, payload, input_file,
                                                                expected):
    monkeypatch.setattr(isolated_wrapper, "input_context_file", input_file)

    assert isolated_wrapper.should_retry_callback_request(payload) is expected


def test_post_callback_returns_the_response_on_success(isolated_wrapper, monkeypatch):
    response = mock.Mock()
    monkeypatch.setattr(isolated_wrapper._http_session, "post", mock.Mock(return_value=response))

    assert isolated_wrapper._post_callback(CALLBACK_URL, "payload") is response
    response.raise_for_status.assert_called_once_with()


def test_post_callback_sends_json_with_a_timeout_and_raises_on_http_errors(isolated_wrapper, monkeypatch):
    response = mock.Mock()
    response.raise_for_status.side_effect = requests.HTTPError("500")
    session_post = mock.Mock(return_value=response)
    monkeypatch.setattr(isolated_wrapper._http_session, "post", session_post)

    with pytest.raises(requests.HTTPError):
        isolated_wrapper._post_callback(CALLBACK_URL, "payload")

    session_post.assert_called_once_with(CALLBACK_URL, headers={"Content-Type": "application/json"},
                                         data="payload", timeout=isolated_wrapper._HTTP_TIMEOUT)
