"""
Concurrency-aware tests for the SIGABRT worker-thread abort model
(docs/SPEC-abort-worker-thread.md).

Most tests here exercise wrapper.py's internals directly, in-process, with
os._exit() and update_output_context() mocked out so a simulated abort does
not tear down the test runner itself or touch real files/secrets/callbacks.

One test (`test_real_sigabrt_interrupts_blocking_task`) sends a genuine
SIGABRT to a subprocess running the real wrapper end-to-end, mirroring how the
release-runner aborts a task, to prove the full integration works.
"""
import json
import os
import signal
import subprocess
import sys
import threading
import time
import unittest
from unittest import mock

import digitalai.release.integration.wrapper as wrapper
from digitalai.release.integration.base_task import BaseTask
from digitalai.release.integration.output_context import OutputContext

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class _RecordingAbortTask(BaseTask):
    """Stub task that counts abort() calls and lets tests set a canned output_context."""

    def __init__(self):
        super().__init__()
        self.abort_call_count = 0

    def execute(self) -> None:  # pragma: no cover - not used directly
        pass

    def abort(self) -> None:
        self.abort_call_count += 1
        super().abort()


class WrapperAbortHandlerTests(unittest.TestCase):
    """In-process tests for wrapper.abort_handler() and the single-writer flush guard."""

    def setUp(self):
        wrapper._reset_report_guard()
        wrapper.dai_task_object = None

    def tearDown(self):
        wrapper._reset_report_guard()
        wrapper.dai_task_object = None

    def test_abort_handler_calls_abort_flushes_once_and_exits(self):
        task = _RecordingAbortTask()
        task.output_context = OutputContext(0, "", {}, [])
        wrapper.dai_task_object = task

        with mock.patch.object(wrapper, "update_output_context") as mock_update, \
             mock.patch.object(wrapper.os, "_exit") as mock_exit:
            wrapper.abort_handler(signal.SIGABRT, None)

        self.assertEqual(task.abort_call_count, 1)
        mock_update.assert_called_once()
        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.exit_code, 1)
        self.assertEqual(reported_ctx.job_error_message, "Abort requested")
        mock_exit.assert_called_once_with(1)

    def test_abort_handler_does_not_double_flush(self):
        task = _RecordingAbortTask()
        task.output_context = OutputContext(0, "", {}, [])
        wrapper.dai_task_object = task

        with mock.patch.object(wrapper, "update_output_context") as mock_update, \
             mock.patch.object(wrapper.os, "_exit"):
            # Simulate the worker's own normal-completion path reporting first.
            self.assertTrue(wrapper._report_once())
            # Then the abort handler fires; abort() cleanup still runs, but the
            # flush must not happen a second time.
            wrapper.abort_handler(signal.SIGABRT, None)

        self.assertEqual(task.abort_call_count, 1)
        mock_update.assert_called_once()

    def test_abort_handler_with_no_task_object_exits_cleanly(self):
        wrapper.dai_task_object = None

        with mock.patch.object(wrapper, "update_output_context") as mock_update, \
             mock.patch.object(wrapper.os, "_exit") as mock_exit:
            wrapper.abort_handler(signal.SIGTERM, None)

        mock_update.assert_called_once()
        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.exit_code, 1)
        mock_exit.assert_called_once_with(1)

    def test_abort_handler_before_worker_starts_still_reports_abort_requested(self):
        # Simulates SIGABRT arriving right after dai_task_object is assigned,
        # before the worker thread has had a chance to run execute_task()'s
        # body -- i.e. before output_context was ever touched post-construction.
        task = _RecordingAbortTask()
        wrapper.dai_task_object = task

        with mock.patch.object(wrapper, "update_output_context") as mock_update, \
             mock.patch.object(wrapper.os, "_exit") as mock_exit:
            wrapper.abort_handler(signal.SIGABRT, None)

        self.assertEqual(task.abort_call_count, 1)
        mock_update.assert_called_once()
        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.exit_code, 1)
        self.assertEqual(reported_ctx.job_error_message, "Abort requested")
        mock_exit.assert_called_once_with(1)

    def test_abort_handler_logs_actual_signal_name(self):
        task = _RecordingAbortTask()
        task.output_context = OutputContext(0, "", {}, [])
        wrapper.dai_task_object = task

        with mock.patch.object(wrapper, "update_output_context"), \
             mock.patch.object(wrapper.os, "_exit"), \
             mock.patch.object(wrapper.dai_logger, "info") as mock_log_info:
            wrapper.abort_handler(signal.SIGABRT, None)

        logged_messages = [call.args[0] for call in mock_log_info.call_args_list]
        self.assertTrue(any("SIGABRT" in msg for msg in logged_messages))


class _CooperativeTask(BaseTask):
    """Task whose execute() polls is_abort_requested() and stops promptly, reporting
    a distinct, custom result so tests can tell it stopped cooperatively rather
    than being torn down by the abort handler."""

    def execute(self) -> None:
        while not self.is_abort_requested():
            time.sleep(0.02)
        self.set_output_property("stopped_cooperatively", True)
        self.set_error_message("Stopped cooperatively")


class WrapperExecuteTaskThreadingTests(unittest.TestCase):
    """In-process tests for wrapper.execute_task()'s worker-thread + guard behavior."""

    def setUp(self):
        wrapper._reset_report_guard()
        wrapper.dai_task_object = None

    def tearDown(self):
        wrapper._reset_report_guard()
        wrapper.dai_task_object = None

    def test_execute_task_normal_completion_reports_once(self):
        class _FastTask(BaseTask):
            def execute(self) -> None:
                self.set_output_property("greeting", "Hello World")

        task = _FastTask()

        with mock.patch.object(wrapper, "update_output_context") as mock_update:
            wrapper.execute_task(task)

        mock_update.assert_called_once()
        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.exit_code, 0)
        self.assertEqual(reported_ctx.output_properties, {"greeting": "Hello World"})

    def test_cooperative_task_stops_promptly_when_abort_requested(self):
        task = _CooperativeTask()

        def _request_abort_shortly():
            time.sleep(0.1)
            task._request_abort()

        threading.Thread(target=_request_abort_shortly, daemon=True).start()

        with mock.patch.object(wrapper, "update_output_context") as mock_update:
            start = time.monotonic()
            wrapper.execute_task(task)
            elapsed = time.monotonic() - start

        # The worker should notice is_abort_requested() and return well within
        # a couple of poll intervals, without needing a real signal.
        self.assertLess(elapsed, 2.0)
        mock_update.assert_called_once()
        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.job_error_message, "Stopped cooperatively")
        self.assertTrue(reported_ctx.output_properties.get("stopped_cooperatively"))

    def test_execute_task_resets_guard_across_daemon_iterations(self):
        class _FastTask(BaseTask):
            def execute(self) -> None:
                pass

        task1 = _FastTask()
        task2 = _FastTask()

        with mock.patch.object(wrapper, "update_output_context") as mock_update:
            wrapper.execute_task(task1)
            wrapper.execute_task(task2)

        # Each iteration must flush its own task's result; the guard from the
        # first iteration must not suppress the second.
        self.assertEqual(mock_update.call_count, 2)
        self.assertIs(wrapper.dai_task_object, task2)

    def test_abort_exception_propagates_exit_status_after_reporting(self):
        from digitalai.release.integration.exceptions import AbortException

        class _AbortingTask(BaseTask):
            def execute(self) -> None:
                raise AbortException()

        task = _AbortingTask()

        with mock.patch.object(wrapper, "update_output_context") as mock_update:
            with self.assertRaises(SystemExit) as ctx:
                wrapper.execute_task(task)

        # BaseTask.execute_task() sets exit_code=1/"Abort requested" then
        # sys.exit(1); the status must be propagated on the main thread.
        self.assertEqual(ctx.exception.code, 1)
        mock_update.assert_called_once()
        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.exit_code, 1)
        self.assertEqual(reported_ctx.job_error_message, "Abort requested")

    def test_direct_sys_exit_propagates_status_and_reports_its_code(self):
        class _ExitingTask(BaseTask):
            def execute(self) -> None:
                sys.exit(2)

        task = _ExitingTask()

        with mock.patch.object(wrapper, "update_output_context") as mock_update:
            with self.assertRaises(SystemExit) as ctx:
                wrapper.execute_task(task)

        # The exact SystemExit code must be preserved.
        self.assertEqual(ctx.exception.code, 2)
        # ...and reported, so Release does not see a success.
        mock_update.assert_called_once()
        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.exit_code, 2)
        self.assertEqual(reported_ctx.job_error_message, "Task exited with code 2")

    def test_sys_exit_with_message_reports_exit_code_1_and_the_message(self):
        class _ExitingTask(BaseTask):
            def execute(self) -> None:
                sys.exit("Configuration missing")

        with mock.patch.object(wrapper, "update_output_context") as mock_update:
            with self.assertRaises(SystemExit):
                wrapper.execute_task(_ExitingTask())

        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.exit_code, 1)
        self.assertEqual(reported_ctx.job_error_message, "Configuration missing")

    def test_sys_exit_zero_reports_success(self):
        class _ExitingTask(BaseTask):
            def execute(self) -> None:
                sys.exit(0)

        with mock.patch.object(wrapper, "update_output_context") as mock_update:
            with self.assertRaises(SystemExit):
                wrapper.execute_task(_ExitingTask())

        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.exit_code, 0)

    def test_normal_completion_does_not_raise_system_exit(self):
        class _FastTask(BaseTask):
            def execute(self) -> None:
                self.set_output_property("ok", True)

        task = _FastTask()

        with mock.patch.object(wrapper, "update_output_context") as mock_update:
            # Must return normally, not raise SystemExit.
            wrapper.execute_task(task)

        mock_update.assert_called_once()


class WrapperAbortGracePeriodTests(unittest.TestCase):
    """
    abort_handler() waits for the worker for up to ABORT_GRACE_PERIOD_SECONDS
    before reporting, guards an in-progress report, and ignores repeat signals.
    """

    def setUp(self):
        wrapper._reset_report_guard()
        wrapper.dai_task_object = None

    def tearDown(self):
        wrapper._reset_report_guard()
        wrapper.dai_task_object = None

    def _start_worker(self, task):
        """Starts task.execute_task() on a worker thread, as execute_task() does."""
        wrapper.dai_task_object = task
        worker = threading.Thread(target=task.execute_task, daemon=True)
        wrapper._worker = worker
        worker.start()
        return worker

    def test_cooperative_stop_within_grace_period_is_reported(self):
        class _PollingTask(BaseTask):
            def execute(self) -> None:
                while not self.is_abort_requested():
                    time.sleep(0.01)
                self.set_output_property("processed", 3)
                self.add_reporting_record({"status": "ABORTED"})

        task = _PollingTask()
        worker = self._start_worker(task)

        with mock.patch.object(wrapper, "update_output_context") as mock_update, \
             mock.patch.object(wrapper.os, "_exit") as mock_exit:
            wrapper.abort_handler(signal.SIGABRT, None)

        self.assertFalse(worker.is_alive())
        mock_update.assert_called_once()
        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.exit_code, 1)
        self.assertEqual(reported_ctx.job_error_message, "Abort requested")
        self.assertEqual(reported_ctx.output_properties, {"processed": 3})
        self.assertEqual(reported_ctx.reporting_records, [{"status": "ABORTED"}])
        mock_exit.assert_called_once_with(1)

    def test_task_that_does_not_stop_is_reported_after_grace_period(self):
        release = threading.Event()

        class _StuckTask(BaseTask):
            def execute(self) -> None:
                release.wait(10)

        task = _StuckTask()
        self._start_worker(task)

        try:
            with mock.patch.object(wrapper, "ABORT_GRACE_PERIOD_SECONDS", 0.2), \
                 mock.patch.object(wrapper, "update_output_context") as mock_update, \
                 mock.patch.object(wrapper.os, "_exit") as mock_exit:
                start = time.monotonic()
                wrapper.abort_handler(signal.SIGABRT, None)
                elapsed = time.monotonic() - start
        finally:
            release.set()

        self.assertGreaterEqual(elapsed, 0.2)
        self.assertLess(elapsed, 2.0)
        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.exit_code, 1)
        mock_exit.assert_called_once_with(1)

    def test_reported_result_is_a_copy_of_the_output_context(self):
        task = _RecordingAbortTask()
        task.set_output_property("a", 1)
        wrapper.dai_task_object = task

        with mock.patch.object(wrapper, "update_output_context") as mock_update, \
             mock.patch.object(wrapper.os, "_exit"):
            wrapper.abort_handler(signal.SIGABRT, None)

        (reported_ctx,), _ = mock_update.call_args
        self.assertIsNot(reported_ctx, task.get_output_context())
        self.assertIsNot(reported_ctx.output_properties, task.get_output_properties())
        self.assertEqual(reported_ctx.output_properties, {"a": 1})

    def test_signal_during_report_lets_the_report_finish_then_exits(self):
        class _FastTask(BaseTask):
            def execute(self) -> None:
                self.set_output_property("greeting", "Hello")

        pushed = []

        def _push_interrupted_by_signal(context):
            # The signal handler runs on the main thread in the middle of the push.
            wrapper.abort_handler(signal.SIGABRT, None)
            pushed.append(context)

        with mock.patch.object(wrapper, "update_output_context", side_effect=_push_interrupted_by_signal), \
             mock.patch.object(wrapper.os, "_exit") as mock_exit:
            wrapper.execute_task(_FastTask())

        # The push completed with the task's own result, and only then did the process exit.
        self.assertEqual(len(pushed), 1)
        self.assertEqual(pushed[0].exit_code, 0)
        self.assertEqual(pushed[0].output_properties, {"greeting": "Hello"})
        mock_exit.assert_called_once_with(1)

    def test_second_signal_during_abort_is_ignored(self):
        class _ReentrantAbortTask(BaseTask):
            def execute(self) -> None:  # pragma: no cover - not used directly
                pass

            def abort(self) -> None:
                # A second signal arrives while the first is being handled.
                wrapper.abort_handler(signal.SIGTERM, None)
                super().abort()

        wrapper.dai_task_object = _ReentrantAbortTask()

        with mock.patch.object(wrapper, "update_output_context") as mock_update, \
             mock.patch.object(wrapper.os, "_exit") as mock_exit:
            wrapper.abort_handler(signal.SIGABRT, None)

        mock_update.assert_called_once()
        mock_exit.assert_called_once_with(1)

    def test_aborted_result_never_reports_exit_code_0(self):
        class _QuietAbortTask(BaseTask):
            def execute(self) -> None:  # pragma: no cover - not used directly
                pass

            def abort(self) -> None:
                # Overrides abort() without calling super() or setting an exit code.
                self.set_output_property("cleaned_up", True)

        wrapper.dai_task_object = _QuietAbortTask()

        with mock.patch.object(wrapper, "update_output_context") as mock_update, \
             mock.patch.object(wrapper.os, "_exit"):
            wrapper.abort_handler(signal.SIGABRT, None)

        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.exit_code, 1)
        self.assertEqual(reported_ctx.job_error_message, "Abort requested")
        self.assertEqual(reported_ctx.output_properties, {"cleaned_up": True})

    def test_signal_before_task_exists_reports_a_clear_message(self):
        with mock.patch.object(wrapper, "update_output_context") as mock_update, \
             mock.patch.object(wrapper.os, "_exit"):
            wrapper.abort_handler(signal.SIGTERM, None)

        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.exit_code, 1)
        self.assertEqual(reported_ctx.job_error_message, "Abort requested before the task started")


class _NoSuperInitTask(BaseTask):
    """Task whose __init__ does not call super().__init__()."""

    def __init__(self):
        self.calls = 0

    def execute(self) -> None:
        self.set_output_property("ok", True)


class WrapperTaskWithoutSuperInitTests(unittest.TestCase):

    def setUp(self):
        wrapper._reset_report_guard()
        wrapper.dai_task_object = None

    def tearDown(self):
        wrapper._reset_report_guard()
        wrapper.dai_task_object = None

    def test_runs_and_reports_outputs(self):
        with mock.patch.object(wrapper, "update_output_context") as mock_update:
            wrapper.execute_task(_NoSuperInitTask())

        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.exit_code, 0)
        self.assertEqual(reported_ctx.output_properties, {"ok": True})

    def test_can_be_aborted(self):
        task = _NoSuperInitTask()
        self.assertFalse(task.is_abort_requested())
        wrapper.dai_task_object = task

        with mock.patch.object(wrapper, "update_output_context") as mock_update, \
             mock.patch.object(wrapper.os, "_exit"):
            wrapper.abort_handler(signal.SIGABRT, None)

        self.assertTrue(task.is_abort_requested())
        (reported_ctx,), _ = mock_update.call_args
        self.assertEqual(reported_ctx.exit_code, 1)


@unittest.skipIf(sys.platform == "win32", "Windows cannot deliver SIGABRT to a child process")
class WrapperRealSigabrtEndToEndTest(unittest.TestCase):
    """
    Full end-to-end tests: run the real wrapper module as a subprocess, send it
    a genuine SIGABRT partway through (as the release-runner does), and check
    the reported result.
    """

    def setUp(self):
        self.input_path = os.path.join(THIS_DIR, "abort_input.json")
        self.output_path = os.path.join(THIS_DIR, "abort_output.json")
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def tearDown(self):
        for path in (self.input_path, self.output_path):
            if os.path.exists(path):
                os.remove(path)

    def _run_and_abort(self, task_type: str):
        """Runs the wrapper on task_type, sends SIGABRT after 1s, and returns (seconds to exit, output)."""
        input_context = {
            "release": {
                "id": "Applications/Folder1f65c7220b394afbb941154342fd9fc6/Release31de09e95c8e4ebb95aaed29a8082d0b",
                "automatedTaskAsUser": {"username": "admin", "password": "admin"},
            },
            "task": {
                "id": "Applications/Folder1f65c7220b394afbb941154342fd9fc6/Release31de09e95c8e4ebb95aaed29a8082d0b/Phase723a601c78804f7dbcaa8b05b83708f5/Task3a35b67b42b6428b854857fba470b39a",
                "type": task_type,
                "properties": [
                    {"name": "capabilities", "value": ["remote"], "kind": "SET_OF_STRING", "category": "input", "password": False},
                ],
            },
        }
        with open(self.input_path, "w") as f:
            json.dump(input_context, f)

        env = dict(os.environ)
        env["INPUT_LOCATION"] = os.path.basename(self.input_path)
        env["OUTPUT_LOCATION"] = os.path.basename(self.output_path)
        env["RELEASE_URL"] = "http://localhost:5516"

        proc = subprocess.Popen(
            [sys.executable, "-m", "digitalai.release.integration.wrapper"],
            cwd=THIS_DIR,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        try:
            # Give the task time to start running execute().
            time.sleep(1.0)
            start = time.monotonic()
            proc.send_signal(signal.SIGABRT)
            stdout, stderr = proc.communicate(timeout=10)
            elapsed = time.monotonic() - start
        except subprocess.TimeoutExpired:
            proc.kill()
            stdout, stderr = proc.communicate()
            self.fail(
                f"wrapper did not exit promptly after SIGABRT\nstdout:\n{stdout}\nstderr:\n{stderr}"
            )

        self.assertEqual(
            proc.returncode, 1,
            msg=f"wrapper exited with {proc.returncode}\nstdout:\n{stdout}\nstderr:\n{stderr}",
        )
        self.assertTrue(os.path.exists(self.output_path), "wrapper did not produce an output file")
        with open(self.output_path) as f:
            return elapsed, json.load(f)

    def test_real_sigabrt_interrupts_blocking_task(self):
        elapsed, actual_output = self._run_and_abort("containerExamples.BlockingTask")

        # The task ignores the abort, so the wrapper reports after the grace
        # period -- well under the task's 30s sleep and the runner's force-kill.
        self.assertGreaterEqual(elapsed, wrapper.ABORT_GRACE_PERIOD_SECONDS)
        self.assertLess(elapsed, 10.0)
        self.assertEqual(actual_output["exitCode"], 1)
        self.assertEqual(actual_output["jobErrorMessage"], "Abort requested")

    def test_real_sigabrt_reports_outputs_of_cooperative_task(self):
        elapsed, actual_output = self._run_and_abort("containerExamples.CooperativeTask")

        # The task stops as soon as it sees the abort, well within the grace period.
        self.assertLess(elapsed, wrapper.ABORT_GRACE_PERIOD_SECONDS)
        self.assertEqual(actual_output["exitCode"], 1)
        self.assertEqual(actual_output["jobErrorMessage"], "Abort requested")
        self.assertEqual(actual_output["outputProperties"], {"stoppedCooperatively": True})
        self.assertEqual(len(actual_output["reportingRecords"]), 1)
        self.assertGreater(actual_output["reportingRecords"][0]["processed"], 0)


if __name__ == '__main__':
    unittest.main()
