from unittest import mock

import pytest

from digitalai.release.integration import base_task
from digitalai.release.integration.base_task import BaseTask
from digitalai.release.integration.exceptions import AbortException
from digitalai.release.integration.input_context import AutomatedTaskAsUserContext, ReleaseContext
from digitalai.release.integration.output_context import OutputContext
from tests.support import FOLDER_ID, PHASE_ID, RELEASE_ID, SERVER_URL, TASK_ID, NoOpTask


def make_task(task_class=NoOpTask, *, username="admin", password="secret", server_url=SERVER_URL):
    task = task_class()
    task.task_id = TASK_ID
    task.release_server_url = server_url
    task.release_context = ReleaseContext(
        id=RELEASE_ID,
        automated_task_as_user=AutomatedTaskAsUserContext(username=username, password=password),
    )
    return task


class RaisingTask(BaseTask):
    error: BaseException = RuntimeError("boom")

    def execute(self) -> None:
        raise self.error


class NoSuperInitTask(BaseTask):
    """A task whose __init__ skips super().__init__(), as some existing plugins do."""

    def __init__(self):
        pass

    def execute(self) -> None:
        pass


# -- execute_task / abort --------------------------------------------------

def test_new_task_has_a_successful_empty_output_context():
    assert NoOpTask().get_output_context() == OutputContext(0, "", {}, [])


def test_execute_task_leaves_a_successful_result_unchanged():
    task = NoOpTask()

    task.execute_task()

    assert task.get_output_context() == OutputContext(0, "", {}, [])


def test_execute_task_reports_an_unexpected_error_as_a_failure():
    task = RaisingTask()

    task.execute_task()

    assert (task.output_context.exit_code, task.output_context.job_error_message) == (1, "boom")


def test_execute_task_turns_an_abort_into_exit_code_1():
    task = RaisingTask()
    task.error = AbortException()

    with pytest.raises(SystemExit) as exit_info:
        task.execute_task()

    assert exit_info.value.code == 1
    assert (task.output_context.exit_code, task.output_context.job_error_message) == (1, "Abort requested")


def test_abort_marks_the_result_aborted_and_raises():
    task = NoOpTask()

    with pytest.raises(AbortException):
        task.abort()

    assert (task.output_context.exit_code, task.output_context.job_error_message) == (1, "Abort requested")


def test_abort_is_not_requested_initially():
    assert NoOpTask().is_abort_requested() is False


def test_request_abort_makes_is_abort_requested_true():
    task = NoOpTask()

    task._request_abort()

    assert task.is_abort_requested() is True


def test_task_without_super_init_gets_an_output_context_on_first_use():
    task = NoSuperInitTask()

    task.set_output_property("ok", True)

    assert task.get_output_context() == OutputContext(0, "", {"ok": True}, [])


def test_task_without_super_init_supports_abort_requests():
    task = NoSuperInitTask()
    assert task.is_abort_requested() is False

    task._request_abort()

    assert task.is_abort_requested() is True


# -- output ----------------------------------------------------------------

@pytest.mark.parametrize("value", ["text", "", 7, 0, True, False, [1, "a"], {"k": "v"}, None],
                         ids=lambda v: repr(v))
def test_set_output_property_accepts_supported_types(value):
    task = NoOpTask()

    task.set_output_property("name", value)

    assert task.get_output_properties() == {"name": value}


@pytest.mark.parametrize("value", [1.5, (1, 2), {1, 2}, object()], ids=["float", "tuple", "set", "object"])
def test_set_output_property_rejects_unsupported_types(value):
    with pytest.raises(ValueError, match="Invalid data type"):
        NoOpTask().set_output_property("name", value)


@pytest.mark.parametrize("name", ["", None])
def test_set_output_property_rejects_an_empty_name(name):
    with pytest.raises(ValueError, match="name cannot be empty"):
        NoOpTask().set_output_property(name, "value")


def test_set_exit_code_and_error_message_update_the_output_context():
    task = NoOpTask()

    task.set_exit_code(3)
    task.set_error_message("partial failure")

    assert task.get_output_context() == OutputContext(3, "partial failure", {}, [])


def test_add_reporting_record_appends_in_order():
    task = NoOpTask()

    task.add_reporting_record({"n": 1})
    task.add_reporting_record({"n": 2})

    assert task.get_output_context().reporting_records == [{"n": 1}, {"n": 2}]


def test_add_comment_logs_the_comment_marker(dai_log):
    NoOpTask().add_comment("Deployed v1.2")

    assert dai_log.messages == ["##[start: comment]Deployed v1.2##[end: comment]"]


def test_set_status_line_logs_the_status_marker(dai_log):
    NoOpTask().set_status_line("Waiting for approval")

    assert dai_log.messages == ["##[start: status]Waiting for approval##[end: status]"]


# -- input and context -----------------------------------------------------

def test_get_input_properties_returns_the_properties_set_by_the_wrapper():
    task = NoOpTask()
    task.input_properties = {"yourName": "World"}

    assert task.get_input_properties() == {"yourName": "World"}


def test_get_input_properties_raises_until_set():
    with pytest.raises(ValueError, match="have not been set"):
        NoOpTask().get_input_properties()


def test_context_getters_return_the_wired_ids():
    task = make_task()

    assert task.get_task_id() == TASK_ID
    assert task.get_release_id() == RELEASE_ID
    assert task.get_release_server_url() == SERVER_URL


def test_get_phase_id_is_derived_from_the_task_id():
    assert make_task().get_phase_id() == PHASE_ID


def test_get_folder_id_is_derived_from_the_release_id():
    assert make_task().get_folder_id() == FOLDER_ID


def test_get_task_user_returns_the_run_as_user():
    assert make_task(username="admin", password="secret").get_task_user() == AutomatedTaskAsUserContext(
        "admin", "secret")


def test_get_task_user_is_none_without_a_release_context():
    assert NoOpTask().get_task_user() is None


# -- get_release_api_client ------------------------------------------------

@pytest.fixture
def client_class(monkeypatch):
    """Replaces ReleaseAPIClient so no client is built; returns the stand-in class."""
    fake = mock.Mock(name="ReleaseAPIClient")
    monkeypatch.setattr(base_task, "ReleaseAPIClient", fake)
    return fake


def test_api_client_uses_the_run_as_user_credentials(client_class):
    client = make_task(username="admin", password="secret").get_release_api_client()

    client_class.assert_called_once_with(SERVER_URL, "admin", "secret", timeout=None)
    assert client is client_class.return_value


def test_api_client_treats_a_password_without_username_as_a_token(client_class):
    make_task(username=None, password="pat-123").get_release_api_client()

    client_class.assert_called_once_with(SERVER_URL, personal_access_token="pat-123", timeout=None)


def test_api_client_prefers_an_explicit_token_over_credentials(client_class):
    make_task().get_release_api_client(personal_access_token="pat-123")

    client_class.assert_called_once_with(SERVER_URL, personal_access_token="pat-123", timeout=None)


def test_api_client_arguments_override_the_task_context(client_class):
    make_task().get_release_api_client("http://other:5516", "deployer", "pw", timeout=(1, 5),
                                       headers={"X-Test": "1"})

    client_class.assert_called_once_with("http://other:5516", "deployer", "pw", timeout=(1, 5),
                                         headers={"X-Test": "1"})


def test_api_client_works_without_a_task_context_when_given_arguments(client_class):
    NoOpTask().get_release_api_client(SERVER_URL, "admin", "secret")

    client_class.assert_called_once_with(SERVER_URL, "admin", "secret", timeout=None)


@pytest.mark.parametrize("username, password, server_url", [
    ("admin", None, SERVER_URL),
    ("", "", SERVER_URL),
    (None, None, SERVER_URL),
    ("admin", "secret", None),
    (None, "pat-123", None),
], ids=["no-password", "blank-credentials", "no-credentials", "no-server-url", "token-without-server-url"])
def test_api_client_requires_server_url_and_credentials(client_class, username, password, server_url):
    task = make_task(username=username, password=password, server_url=server_url)

    with pytest.raises(ValueError, match="Cannot connect to Release API"):
        task.get_release_api_client()

    client_class.assert_not_called()


def test_api_client_requires_a_release_context_or_arguments(client_class):
    task = NoOpTask()
    task.release_server_url = SERVER_URL

    with pytest.raises(ValueError, match="Cannot connect to Release API"):
        task.get_release_api_client()
