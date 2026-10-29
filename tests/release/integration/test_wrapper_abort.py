"""
The SIGTERM/SIGABRT handler, called directly on the test's main thread.

update_output_context() and os._exit() are replaced (see the ``reported`` and
``exit_codes`` fixtures), so a simulated abort neither sends a result nor ends
the test run. Real signals are covered by test_wrapper_e2e.py.
"""
import signal
import threading
import time
from unittest import mock

import pytest

from digitalai.release.integration.base_task import BaseTask
from digitalai.release.integration.output_context import OutputContext
from tests.support import NoOpTask

ABORTED = OutputContext(1, "Abort requested", {}, [])


class CountingAbortTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.abort_calls = 0

    def execute(self) -> None:
        pass

    def abort(self) -> None:
        self.abort_calls += 1
        super().abort()


def start_worker(wrapper, task):
    """Runs task.execute_task() on a worker thread registered with the wrapper, as execute_task() does."""
    wrapper.dai_task_object = task
    worker = threading.Thread(target=task.execute_task, daemon=True)
    wrapper._worker = worker
    worker.start()
    return worker


@pytest.mark.parametrize("signum", [signal.SIGABRT, signal.SIGTERM], ids=["SIGABRT", "SIGTERM"])
def test_abort_calls_abort_reports_once_and_exits_1(isolated_wrapper, reported, exit_codes, signum):
    task = CountingAbortTask()
    isolated_wrapper.dai_task_object = task

    isolated_wrapper.abort_handler(signum, None)

    assert task.abort_calls == 1
    assert reported == [ABORTED]
    assert exit_codes == [1]


def test_abort_requests_a_cooperative_stop(isolated_wrapper, reported, exit_codes):
    task = NoOpTask()
    isolated_wrapper.dai_task_object = task

    isolated_wrapper.abort_handler(signal.SIGABRT, None)

    assert task.is_abort_requested()


def test_abort_logs_the_received_signal(isolated_wrapper, reported, exit_codes, dai_log):
    isolated_wrapper.dai_task_object = NoOpTask()

    isolated_wrapper.abort_handler(signal.SIGTERM, None)

    assert "Received SIGTERM to gracefully stop the process" in dai_log.messages


def test_abort_before_a_task_exists_reports_a_clear_message(isolated_wrapper, reported, exit_codes):
    isolated_wrapper.abort_handler(signal.SIGTERM, None)

    assert reported == [OutputContext(1, "Abort requested before the task started", {}, [])]
    assert exit_codes == [1]


def test_abort_after_the_result_was_reported_does_not_report_again(isolated_wrapper, reported, exit_codes):
    task = CountingAbortTask()
    isolated_wrapper.dai_task_object = task
    assert isolated_wrapper._report_once()

    isolated_wrapper.abort_handler(signal.SIGABRT, None)

    assert task.abort_calls == 1
    assert reported == [OutputContext(0, "", {}, [])]
    assert exit_codes == [1]


def test_cooperative_task_is_reported_with_what_it_recorded_while_stopping(isolated_wrapper, reported, exit_codes):
    class PollingTask(BaseTask):
        def execute(self) -> None:
            deadline = time.monotonic() + 5
            while not self.is_abort_requested() and time.monotonic() < deadline:
                time.sleep(0.01)
            self.set_output_property("processed", 3)
            self.add_reporting_record({"status": "ABORTED"})

    worker = start_worker(isolated_wrapper, PollingTask())

    isolated_wrapper.abort_handler(signal.SIGABRT, None)

    assert not worker.is_alive()
    assert reported == [OutputContext(1, "Abort requested", {"processed": 3}, [{"status": "ABORTED"}])]
    assert exit_codes == [1]


def test_task_that_ignores_the_abort_is_reported_after_the_grace_period(isolated_wrapper, reported, exit_codes,
                                                                         monkeypatch):
    monkeypatch.setattr(isolated_wrapper, "ABORT_GRACE_PERIOD_SECONDS", 0.2)
    unblock = threading.Event()

    class StuckTask(BaseTask):
        def execute(self) -> None:
            unblock.wait(10)

    worker = start_worker(isolated_wrapper, StuckTask())
    try:
        start = time.monotonic()
        isolated_wrapper.abort_handler(signal.SIGABRT, None)
        elapsed = time.monotonic() - start

        assert worker.is_alive()
    finally:
        unblock.set()

    assert 0.2 <= elapsed < 5
    assert reported == [ABORTED]
    assert exit_codes == [1]


def test_reported_result_is_a_snapshot_of_the_output_context(isolated_wrapper, reported, exit_codes):
    task = CountingAbortTask()
    task.set_output_property("a", 1)
    task.add_reporting_record({"r": 1})
    isolated_wrapper.dai_task_object = task

    isolated_wrapper.abort_handler(signal.SIGABRT, None)

    (snapshot,) = reported
    assert snapshot is not task.get_output_context()
    assert snapshot.output_properties is not task.get_output_properties()
    assert snapshot.reporting_records is not task.get_output_context().reporting_records
    assert snapshot == OutputContext(1, "Abort requested", {"a": 1}, [{"r": 1}])


def test_reported_result_shares_no_nested_object_with_the_task(isolated_wrapper, reported, exit_codes):
    task = CountingAbortTask()
    task.set_output_property("progress", {"done": 1})
    task.add_reporting_record({"items": [1]})
    isolated_wrapper.dai_task_object = task

    isolated_wrapper.abort_handler(signal.SIGABRT, None)

    (snapshot,) = reported
    assert snapshot.output_properties["progress"] is not task.get_output_properties()["progress"]
    assert snapshot.reporting_records[0] is not task.get_output_context().reporting_records[0]
    assert snapshot == OutputContext(1, "Abort requested", {"progress": {"done": 1}}, [{"items": [1]}])


class ChangingDict(dict):
    """A nested output the worker changes while it is read: reading it fails ``failures`` times."""

    def __init__(self, failures, **items):
        super().__init__(**items)
        self.failures = failures

    def items(self):
        if self.failures:
            self.failures -= 1
            raise RuntimeError("dictionary changed size during iteration")
        return super().items()


def test_output_changed_while_read_is_read_again(isolated_wrapper, reported, exit_codes):
    task = CountingAbortTask()
    task.set_output_property("progress", ChangingDict(failures=2, done=1))
    isolated_wrapper.dai_task_object = task

    isolated_wrapper.abort_handler(signal.SIGABRT, None)

    assert reported == [OutputContext(1, "Abort requested", {"progress": {"done": 1}}, [])]
    assert exit_codes == [1]


def test_output_that_keeps_changing_is_left_out_of_the_aborted_result(isolated_wrapper, reported, exit_codes,
                                                                     dai_log):
    task = CountingAbortTask()
    task.set_output_property("progress", ChangingDict(failures=1000, done=1))
    task.add_reporting_record({"r": 1})
    isolated_wrapper.dai_task_object = task

    isolated_wrapper.abort_handler(signal.SIGABRT, None)

    assert reported == [ABORTED]
    assert exit_codes == [1]
    assert any("without the task's outputs" in message for message in dai_log.messages)


def test_abort_exits_even_when_reporting_fails(isolated_wrapper, exit_codes, monkeypatch):
    monkeypatch.setattr(isolated_wrapper, "update_output_context", mock.Mock(side_effect=RuntimeError("push failed")))
    isolated_wrapper.dai_task_object = NoOpTask()

    with pytest.raises(RuntimeError, match="push failed"):
        isolated_wrapper.abort_handler(signal.SIGABRT, None)

    assert exit_codes == [1]


def test_abort_override_that_sets_no_exit_code_is_still_reported_as_failed(isolated_wrapper, reported, exit_codes):
    class QuietAbortTask(BaseTask):
        def execute(self) -> None:
            pass

        def abort(self) -> None:
            self.set_output_property("cleanedUp", True)

    isolated_wrapper.dai_task_object = QuietAbortTask()

    isolated_wrapper.abort_handler(signal.SIGABRT, None)

    assert reported == [OutputContext(1, "Abort requested", {"cleanedUp": True}, [])]


def test_abort_override_keeps_its_own_error_message(isolated_wrapper, reported, exit_codes):
    class CustomAbortTask(BaseTask):
        def execute(self) -> None:
            pass

        def abort(self) -> None:
            self.set_error_message("Cancelled by operator")

    isolated_wrapper.dai_task_object = CustomAbortTask()

    isolated_wrapper.abort_handler(signal.SIGABRT, None)

    assert reported == [OutputContext(1, "Cancelled by operator", {}, [])]


@pytest.mark.parametrize("error", [SystemExit(3), RuntimeError("cleanup failed")], ids=["sys-exit", "exception"])
def test_abort_override_that_raises_still_reports_and_exits_1(isolated_wrapper, reported, exit_codes, error):
    class RaisingAbortTask(BaseTask):
        def execute(self) -> None:
            pass

        def abort(self) -> None:
            raise error

    isolated_wrapper.dai_task_object = RaisingAbortTask()

    isolated_wrapper.abort_handler(signal.SIGABRT, None)

    assert reported == [ABORTED]
    assert exit_codes == [1]


def test_signal_during_a_report_lets_the_report_finish_then_exits(isolated_wrapper, exit_codes, monkeypatch):
    pushed = []

    def push_interrupted_by_a_signal(context):
        # Python runs signal handlers on the main thread, possibly mid-push.
        isolated_wrapper.abort_handler(signal.SIGABRT, None)
        pushed.append(context)

    monkeypatch.setattr(isolated_wrapper, "update_output_context", push_interrupted_by_a_signal)

    isolated_wrapper.execute_task(NoOpTask())

    assert pushed == [OutputContext(0, "", {}, [])]
    assert exit_codes == [1]


def test_second_signal_during_an_abort_is_ignored(isolated_wrapper, reported, exit_codes):
    class ReentrantAbortTask(BaseTask):
        def execute(self) -> None:
            pass

        def abort(self) -> None:
            isolated_wrapper.abort_handler(signal.SIGTERM, None)
            super().abort()

    isolated_wrapper.dai_task_object = ReentrantAbortTask()

    isolated_wrapper.abort_handler(signal.SIGABRT, None)

    assert reported == [ABORTED]
    assert exit_codes == [1]


def test_task_without_super_init_can_be_aborted(isolated_wrapper, reported, exit_codes):
    class NoSuperInitTask(BaseTask):
        def __init__(self):
            pass

        def execute(self) -> None:
            pass

    task = NoSuperInitTask()
    isolated_wrapper.dai_task_object = task

    isolated_wrapper.abort_handler(signal.SIGABRT, None)

    assert task.is_abort_requested()
    assert reported == [ABORTED]


def test_handlers_are_installed_for_sigterm_and_sigabrt(isolated_wrapper):
    assert signal.getsignal(signal.SIGTERM) is isolated_wrapper.abort_handler
    assert signal.getsignal(signal.SIGABRT) is isolated_wrapper.abort_handler
