"""
Tests for the wrapper's Kubernetes execution path.

When the runner executes inside Kubernetes there is no INPUT_LOCATION file; the
input context is read from a Secret, and the result is written back to a Secret
and/or pushed to a callback URL. These tests exercise that path with a fully
mocked Kubernetes client and callback transport, so no real cluster or network
is required.

Secret values in Kubernetes are base64-encoded strings, and the wrapper applies
its own (double) base64 encoding to the callback/fetch URLs. The helpers below
mirror that encoding so the fakes look exactly like a real Secret.
"""

import base64
import json
import unittest
from unittest import mock

import digitalai.release.integration.wrapper as wrapper
from digitalai.release.integration import k8s
from digitalai.release.integration.output_context import OutputContext

# Sample input context (Hello task) reused from the file-based wrapper test.
SAMPLE_INPUT_CONTEXT = {
    "release": {
        "id": "Applications/Folder1f65c7220b394afbb941154342fd9fc6/Release31de09e95c8e4ebb95aaed29a8082d0b",
        "automatedTaskAsUser": {"username": "admin", "password": "admin"},
    },
    "task": {
        "id": "Applications/Folder1f65c7220b394afbb941154342fd9fc6/Release31de09e95c8e4ebb95aaed29a8082d0b/Phase723a601c78804f7dbcaa8b05b83708f5/Task3a35b67b42b6428b854857fba470b39a",
        "type": "containerExamples.Hello",
        "properties": [
            {"name": "capabilities", "value": ["remote"], "kind": "SET_OF_STRING", "category": "input", "password": False},
            {"name": "yourName", "value": "World", "kind": "STRING", "category": "input", "password": False},
            {"name": "greeting", "value": None, "kind": "STRING", "category": "output", "password": False},
        ],
    },
}


def _b64(value) -> str:
    """base64-encode a str/bytes the way a Kubernetes Secret stores its values."""
    if isinstance(value, str):
        value = value.encode("UTF-8")
    return base64.b64encode(value).decode("UTF-8")


def _double_b64_url(url: str) -> str:
    """The wrapper expects callback/fetch URLs to be double base64-encoded."""
    return _b64(_b64(url))


class FakeSecret:
    """Minimal stand-in for a kubernetes V1Secret (only ``.data`` is used)."""

    def __init__(self, data):
        self.data = dict(data)


class FakeCoreV1Api:
    """Records secret reads/replacements so assertions can inspect them."""

    def __init__(self, secrets):
        self.secrets = secrets  # name -> FakeSecret
        self.replaced = []      # list of (name, namespace, body)

    def read_namespaced_secret(self, name, namespace):
        return self.secrets[name]

    def replace_namespaced_secret(self, name, namespace, body):
        self.replaced.append((name, namespace, body))
        self.secrets[name] = body


class _WrapperK8sTestBase(unittest.TestCase):
    """Shared setup: patch the wrapper's module globals and the k8s client."""

    INPUT_SECRET = "input-context-secret"
    NAMESPACE = "runner-ns"
    CALLBACK_URL = "http://release-server/callback"

    def _patch_global(self, name, value):
        patcher = mock.patch.object(wrapper, name, value)
        patcher.start()
        self.addCleanup(patcher.stop)

    def _install_fake_client(self, secrets):
        fake = FakeCoreV1Api(secrets)
        patcher = mock.patch.object(k8s, "get_client", return_value=fake)
        patcher.start()
        self.addCleanup(patcher.stop)
        return fake

    def setUp(self):
        # Force the Kubernetes branch: no input/output files.
        self._patch_global("input_context_file", "")
        self._patch_global("output_context_file", "")
        self._patch_global("input_context_secret", self.INPUT_SECRET)
        self._patch_global("runner_namespace", self.NAMESPACE)
        # A blank session-key decodes to b"" -> NoOp encryptor (plaintext I/O),
        # which keeps the test independent of AES key material.
        self._patch_global("base64_session_key", "")


class TestGetTaskDetailsFromSecret(_WrapperK8sTestBase):

    def test_reads_input_context_from_secret(self):
        input_json = json.dumps(SAMPLE_INPUT_CONTEXT)
        secret = FakeSecret({
            "session-key": _b64(""),            # -> NoOp encryptor
            "url": _double_b64_url(self.CALLBACK_URL),
            "input": _b64(input_json),
        })
        self._install_fake_client({self.INPUT_SECRET: secret})

        task_properties, task_type, script_path = wrapper.get_task_details()

        self.assertEqual(task_type, "containerExamples.Hello")
        self.assertEqual(task_properties["yourName"], "World")
        self.assertEqual(script_path, "")
        # callback_url global is set to the (single-decoded) callback bytes.
        self.assertEqual(base64.b64decode(wrapper.callback_url).decode("UTF-8"), self.CALLBACK_URL)
        # The "Run as user" password is registered as a secret to be masked.
        self.assertIn("admin", wrapper.masked_std_out.secrets)

    def test_reads_input_context_via_fetch_url_when_input_empty(self):
        input_json = json.dumps(SAMPLE_INPUT_CONTEXT)
        fetch_url = "http://blob-store/large-input"
        secret = FakeSecret({
            "session-key": _b64(""),
            "url": _double_b64_url(self.CALLBACK_URL),
            "input": "",                         # empty -> use fetchUrl
            "fetchUrl": _double_b64_url(fetch_url),
        })
        self._install_fake_client({self.INPUT_SECRET: secret})

        fake_response = mock.Mock()
        fake_response.content = input_json.encode("UTF-8")
        fake_response.status_code = 200
        fake_response.raise_for_status = mock.Mock()

        with mock.patch.object(wrapper._http_session, "get", return_value=fake_response) as fake_get:
            task_properties, task_type, _ = wrapper.get_task_details()

        fake_get.assert_called_once()
        self.assertEqual(fake_get.call_args.args[0], fetch_url)
        # A timeout must be supplied so a hung blob store cannot stall the runner.
        self.assertIn("timeout", fake_get.call_args.kwargs)
        fake_response.raise_for_status.assert_called_once()
        self.assertEqual(task_type, "containerExamples.Hello")
        self.assertEqual(task_properties["yourName"], "World")

    def test_missing_fetch_url_raises(self):
        secret = FakeSecret({
            "session-key": _b64(""),
            "url": _double_b64_url(self.CALLBACK_URL),
            "input": "",
            "fetchUrl": "",
        })
        self._install_fake_client({self.INPUT_SECRET: secret})

        with self.assertRaises(ValueError):
            wrapper.get_task_details()

    def test_secret_read_failure_propagates(self):
        # get_task_details does not swallow k8s errors: a failure to read the
        # input secret must surface so run() can report the task as failed.
        fake = mock.Mock()
        fake.read_namespaced_secret.side_effect = RuntimeError("k8s unavailable")
        patcher = mock.patch.object(k8s, "get_client", return_value=fake)
        patcher.start()
        self.addCleanup(patcher.stop)

        with self.assertRaises(RuntimeError):
            wrapper.get_task_details()


class TestUpdateOutputContextToSecret(_WrapperK8sTestBase):

    RESULT_SECRET_NAME = "result-secret"
    RESULT_KEY = "result"

    def setUp(self):
        super().setUp()
        self._patch_global("result_secret_key", f"{self.NAMESPACE}:{self.RESULT_SECRET_NAME}:{self.RESULT_KEY}")
        # callback_url global as set by get_task_details: single base64 of the URL.
        self._patch_global("callback_url", _b64(self.CALLBACK_URL).encode("UTF-8"))

    def test_writes_result_to_secret_and_pushes_callback(self):
        result_secret = FakeSecret({self.RESULT_KEY: ""})
        fake = self._install_fake_client({self.RESULT_SECRET_NAME: result_secret})

        output = OutputContext(0, "", {"greeting": "Hello World"}, [])

        with mock.patch.object(wrapper, "_post_callback") as fake_post:
            wrapper.update_output_context(output)

        # Result written back to the secret (NoOp encryptor -> plaintext JSON).
        self.assertEqual(len(fake.replaced), 1)
        name, namespace, body = fake.replaced[0]
        self.assertEqual(name, self.RESULT_SECRET_NAME)
        self.assertEqual(namespace, self.NAMESPACE)
        stored = json.loads(body.data[self.RESULT_KEY])
        self.assertEqual(stored["outputProperties"], {"greeting": "Hello World"})

        # Callback pushed to the decoded URL with the encrypted body.
        fake_post.assert_called_once()
        pushed_url, pushed_body = fake_post.call_args.args
        self.assertEqual(pushed_url, self.CALLBACK_URL)
        self.assertEqual(json.loads(pushed_body)["exitCode"], 0)

    def test_result_too_large_skips_secret_but_still_pushes_callback(self):
        result_secret = FakeSecret({self.RESULT_KEY: ""})
        fake = self._install_fake_client({self.RESULT_SECRET_NAME: result_secret})

        # > 1Mb of output so it cannot be stored in a Secret.
        big_value = "x" * (wrapper.size_of_1Mb + 1024)
        output = OutputContext(0, "", {"big": big_value}, [])

        with mock.patch.object(wrapper, "_post_callback") as fake_post:
            wrapper.update_output_context(output)

        # Secret write skipped because the payload is too big.
        self.assertEqual(fake.replaced, [])
        # Callback is still attempted.
        fake_post.assert_called_once()

    def test_secret_write_failure_is_swallowed_and_logged(self):
        # update_output_context must never raise: a failure to write the result
        # secret is logged and swallowed so the runner exits cleanly. Because the
        # failure happens before the callback step, no callback is attempted.
        fake = mock.Mock()
        fake.read_namespaced_secret.side_effect = RuntimeError("k8s write unavailable")
        patcher = mock.patch.object(k8s, "get_client", return_value=fake)
        patcher.start()
        self.addCleanup(patcher.stop)

        output = OutputContext(0, "", {"greeting": "Hello World"}, [])

        with mock.patch.object(wrapper, "_post_callback") as fake_post:
            # Must not raise.
            wrapper.update_output_context(output)

        fake_post.assert_not_called()

    def test_callback_retries_when_too_big_and_no_output_file(self):
        result_secret = FakeSecret({self.RESULT_KEY: ""})
        # The retry path re-reads the input-context secret for a fresh URL.
        input_secret = FakeSecret({"url": _double_b64_url(self.CALLBACK_URL)})
        self._install_fake_client({
            self.RESULT_SECRET_NAME: result_secret,
            self.INPUT_SECRET: input_secret,
        })

        big_value = "x" * (wrapper.size_of_1Mb + 1024)
        output = OutputContext(0, "", {"big": big_value}, [])

        # First push fails; should_retry_callback_request() is True (too big, no
        # output file) so retry_push_result_infinitely is invoked and succeeds.
        with mock.patch.object(wrapper, "_post_callback", side_effect=[RuntimeError("boom"), mock.Mock()]) as fake_post:
            wrapper.update_output_context(output)

        self.assertEqual(fake_post.call_count, 2)


class TestShouldRetryCallbackRequest(unittest.TestCase):

    def test_retries_when_too_big_and_no_output_file(self):
        with mock.patch.object(wrapper, "input_context_file", ""):
            self.assertTrue(wrapper.should_retry_callback_request("x" * (wrapper.size_of_1Mb + 1)))

    def test_no_retry_when_small(self):
        with mock.patch.object(wrapper, "input_context_file", ""):
            self.assertFalse(wrapper.should_retry_callback_request("small"))

    def test_no_retry_when_output_file_present(self):
        with mock.patch.object(wrapper, "input_context_file", "output.json"):
            self.assertFalse(wrapper.should_retry_callback_request("x" * (wrapper.size_of_1Mb + 1)))


if __name__ == "__main__":
    unittest.main()
