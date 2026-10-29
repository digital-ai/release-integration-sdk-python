"""
wrapper.execute_task() runs the task on a worker thread, reports its result
exactly once, and turns a sys.exit() inside the task into the process exit
status and the reported exit code.
"""
import sys
import threading
import time

import pytest

from digitalai.release.integration.base_task import BaseTask
from digitalai.release.integration.exceptions import AbortException
from digitalai.release.integration.output_context import OutputContext
from tests.support import NoOpTask


class GreetingTask(BaseTask):
    def execute(self) -> None:
        self.set_output_property("greeting", "Hello World")


class ExitingTask(BaseTask):
    def __init__(self, code):
        super().__init__()
        self.code = code

    def execute(self) -> None:
        sys.exit(self.code)


def test_reports_the_task_result_once(isolated_wrapper, reported):
    isolated_wrapper.execute_task(GreetingTask())

    assert reported == [OutputContext(0, "", {"greeting": "Hello World"}, [])]


def test_runs_the_task_on_a_worker_thread(isolated_wrapper, reported):
    threads = []

    class RecordingTask(BaseTask):
        def execute(self) -> None:
            threads.append(threading.current_thread())

    isolated_wrapper.execute_task(RecordingTask())

    assert threads[0] is not threading.main_thread()
    assert threads[0].daemon


def test_reports_a_failing_task_as_failed(isolated_wrapper, reported):
    class FailingTask(BaseTask):
        def execute(self) -> None:
            raise ValueError("Deployment target unreachable")

    isolated_wrapper.execute_task(FailingTask())

    assert reported == [OutputContext(1, "Deployment target unreachable", {}, [])]


def test_outputs_that_cannot_be_serialized_are_reported_as_a_failure(isolated_wrapper, reported):
    class SetOutputTask(BaseTask):
        def execute(self) -> None:
            self.set_output_property("deployment", {"handle": object()})

    isolated_wrapper.execute_task(SetOutputTask())

    (result,) = reported
    assert (result.exit_code, result.output_properties, result.reporting_records) == (1, {}, [])
    assert "The task's outputs could not be reported" in result.job_error_message
    assert "not JSON serializable" in result.job_error_message


def test_each_execution_reports_its_own_result(isolated_wrapper, reported):
    first, second = NoOpTask(), GreetingTask()

    isolated_wrapper.execute_task(first)
    isolated_wrapper.execute_task(second)

    assert reported == [OutputContext(0, "", {}, []), OutputContext(0, "", {"greeting": "Hello World"}, [])]
    assert isolated_wrapper.dai_task_object is second


def test_abort_exception_is_reported_and_exits_with_1(isolated_wrapper, reported):
    class AbortingTask(BaseTask):
        def execute(self) -> None:
            raise AbortException()

    with pytest.raises(SystemExit) as exit_info:
        isolated_wrapper.execute_task(AbortingTask())

    assert exit_info.value.code == 1
    assert reported == [OutputContext(1, "Abort requested", {}, [])]


@pytest.mark.parametrize("code, reported_code, message", [
    (2, 2, "Task exited with code 2"),
    ("Configuration missing", 1, "Configuration missing"),
    (0, 0, ""),
    (None, 0, ""),
], ids=["int", "message", "zero", "none"])
def test_sys_exit_is_reported_and_propagated(isolated_wrapper, reported, code, reported_code, message):
    with pytest.raises(SystemExit) as exit_info:
        isolated_wrapper.execute_task(ExitingTask(code))

    assert exit_info.value.code == code
    assert reported == [OutputContext(reported_code, message, {}, [])]


def test_sys_exit_keeps_an_exit_code_the_task_set_itself(isolated_wrapper, reported):
    class FailingThenExitingTask(BaseTask):
        def execute(self) -> None:
            self.set_exit_code(5)
            self.set_error_message("Quota exceeded")
            sys.exit(2)

    with pytest.raises(SystemExit):
        isolated_wrapper.execute_task(FailingThenExitingTask())

    assert reported == [OutputContext(5, "Quota exceeded", {}, [])]


def test_sys_exit_keeps_an_error_message_the_task_set_itself(isolated_wrapper, reported):
    class ExplainedExitTask(BaseTask):
        def execute(self) -> None:
            self.set_error_message("Quota exceeded")
            sys.exit(2)

    with pytest.raises(SystemExit):
        isolated_wrapper.execute_task(ExplainedExitTask())

    assert reported == [OutputContext(2, "Quota exceeded", {}, [])]


def test_task_without_super_init_runs_and_reports(isolated_wrapper, reported):
    class NoSuperInitTask(BaseTask):
        def __init__(self):
            pass

        def execute(self) -> None:
            self.set_output_property("ok", True)

    isolated_wrapper.execute_task(NoSuperInitTask())

    assert reported == [OutputContext(0, "", {"ok": True}, [])]


def test_task_without_super_init_has_its_output_context_before_it_runs(isolated_wrapper, reported):
    # Created on the main thread, so the worker and an abort() run by the signal
    # handler share one output context instead of each creating their own.
    contexts = []

    class NoSuperInitTask(BaseTask):
        def __init__(self):
            pass

        def execute(self) -> None:
            contexts.append(self.__dict__.get("output_context"))

    isolated_wrapper.execute_task(NoSuperInitTask())

    assert contexts[0] is not None


def test_cooperative_task_sees_an_abort_requested_from_another_thread(isolated_wrapper, reported):
    started = threading.Event()

    class CooperativeTask(BaseTask):
        def execute(self) -> None:
            started.set()
            deadline = time.monotonic() + 5
            while not self.is_abort_requested() and time.monotonic() < deadline:
                time.sleep(0.01)
            self.set_output_property("stoppedOnRequest", self.is_abort_requested())

    task = CooperativeTask()
    threading.Thread(target=lambda: started.wait(5) and task._request_abort(), daemon=True).start()

    isolated_wrapper.execute_task(task)

    assert reported == [OutputContext(0, "", {"stoppedOnRequest": True}, [])]


@pytest.mark.parametrize("code, expected", [(None, 0), (0, 0), (3, 3), ("message", 1)])
def test_exit_code_of_matches_the_process_exit_status(isolated_wrapper, code, expected):
    assert isolated_wrapper._exit_code_of(SystemExit(code)) == expected
