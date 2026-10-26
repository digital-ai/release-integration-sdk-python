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

    def test_direct_sys_exit_propagates_status_and_reports_context_as_is(self):
        class _ExitingTask(BaseTask):
            def execute(self) -> None:
                sys.exit(2)

        task = _ExitingTask()

        with mock.patch.object(wrapper, "update_output_context") as mock_update:
            with self.assertRaises(SystemExit) as ctx:
                wrapper.execute_task(task)

        # The exact SystemExit code must be preserved.
        self.assertEqual(ctx.exception.code, 2)
        # Strict master parity: the output context is reported as-is (default
        # success), not reconciled to the SystemExit code.
        mock_update.assert_called_once()
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


class WrapperRealSigabrtEndToEndTest(unittest.TestCase):
    """
    Full end-to-end test: runs the real wrapper module as a subprocess against a
    task that blocks in execute() without polling is_abort_requested(), sends it
    a genuine SIGABRT partway through, and asserts it reports an aborted result
    promptly instead of waiting for the 30s sleep to finish.
    """

    def setUp(self):
        self.input_path = os.path.join(THIS_DIR, "blocking_input.json")
        self.output_path = os.path.join(THIS_DIR, "blocking_output.json")
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def tearDown(self):
        for path in (self.input_path, self.output_path):
            if os.path.exists(path):
                os.remove(path)

    def test_real_sigabrt_interrupts_blocking_task(self):
        input_context = {
            "release": {
                "id": "Applications/Folder1f65c7220b394afbb941154342fd9fc6/Release31de09e95c8e4ebb95aaed29a8082d0b",
                "automatedTaskAsUser": {"username": "admin", "password": "admin"},
            },
            "task": {
                "id": "Applications/Folder1f65c7220b394afbb941154342fd9fc6/Release31de09e95c8e4ebb95aaed29a8082d0b/Phase723a601c78804f7dbcaa8b05b83708f5/Task3a35b67b42b6428b854857fba470b39a",
                "type": "containerExamples.BlockingTask",
                "properties": [
                    {"name": "capabilities", "value": ["remote"], "kind": "SET_OF_STRING", "category": "input", "password": False},
                ],
            },
        }
        with open(self.input_path, "w") as f:
            json.dump(input_context, f)

        env = dict(os.environ)
        env["INPUT_LOCATION"] = "blocking_input.json"
        env["OUTPUT_LOCATION"] = "blocking_output.json"
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
            # Give the task time to enter its blocking sleep(30) call.
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
        # Must be well under the task's 30s sleep -- proves the abort was
        # timely rather than relying on the runner's Phase-2 force-kill.
        self.assertLess(elapsed, 10.0)

        self.assertTrue(os.path.exists(self.output_path), "wrapper did not produce blocking_output.json")
        with open(self.output_path) as f:
            actual_output = json.load(f)

        self.assertEqual(actual_output["exitCode"], 1)
        self.assertEqual(actual_output["jobErrorMessage"], "Abort requested")


if __name__ == '__main__':
    unittest.main()
