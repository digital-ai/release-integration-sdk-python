"""
End-to-end runs of ``python -m digitalai.release.integration.wrapper`` in a
subprocess, configured through environment variables as the runner does.
These cover what in-process tests cannot: settings read at import, the
masked standard streams, and real signal delivery.
"""
import base64
import json
import os
import signal
import subprocess
import sys
import time

import pytest

from digitalai.release.integration.job_data_encryptor import AESJobDataEncryptor
from tests.release.integration.conftest import make_task_workspace
from tests.support import input_context, task_property

pytestmark = pytest.mark.e2e

posix_only = pytest.mark.skipif(sys.platform == "win32", reason="Windows cannot deliver SIGABRT to a child process")


def wrapper_env(**extra):
    env = {k: v for k, v in os.environ.items() if k not in (
        "INPUT_LOCATION", "OUTPUT_LOCATION", "SESSION_KEY", "CALLBACK_URL", "RESULT_SECRET_NAME",
        "INPUT_CONTEXT_SECRET", "RUNNER_NAMESPACE", "EXECUTOR_EXECUTION_MODE", "ABORT_GRACE_PERIOD_SECONDS")}
    env.update(INPUT_LOCATION="input.json", OUTPUT_LOCATION="output.json", RELEASE_URL="http://localhost:5516",
               PYTHONUNBUFFERED="1", **extra)
    return env


def start_wrapper(workspace, context, *, encryptor=None, **env):
    payload = json.dumps(context)
    (workspace / "input.json").write_text(encryptor.encrypt(payload) if encryptor else payload)
    return subprocess.Popen([sys.executable, "-m", "digitalai.release.integration.wrapper"], cwd=workspace,
                            env=wrapper_env(**env), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True)


def finish(process, timeout=60):
    try:
        stdout, stderr = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        process.kill()
        stdout, stderr = process.communicate()
        pytest.fail(f"wrapper did not exit within {timeout}s\nstdout:\n{stdout}\nstderr:\n{stderr}")
    return process.returncode, stdout, stderr


def read_output(workspace, encryptor=None):
    path = workspace / "output.json"
    assert path.exists(), "wrapper did not write output.json"
    content = path.read_text()
    return json.loads(encryptor.decrypt(content) if encryptor else content)


def run_wrapper(workspace, context, **kwargs):
    returncode, stdout, stderr = finish(start_wrapper(workspace, context, **kwargs))
    assert returncode == 0, f"wrapper exited with {returncode}\nstdout:\n{stdout}\nstderr:\n{stderr}"
    return stdout


def test_successful_task_writes_its_result_to_the_output_file(task_workspace):
    run_wrapper(task_workspace, input_context("containerExamples.Hello", [task_property("yourName", "World")]))

    assert read_output(task_workspace) == {
        "exitCode": 0, "jobErrorMessage": "", "outputProperties": {"greeting": "Hello World"}, "reportingRecords": [],
    }


def test_session_key_encrypts_both_input_and_output(task_workspace):
    key = base64.b64encode(os.urandom(32)).decode()
    encryptor = AESJobDataEncryptor(key)

    run_wrapper(task_workspace, input_context("containerExamples.Hello", [task_property("yourName", "World")]),
                encryptor=encryptor, SESSION_KEY=key)

    assert read_output(task_workspace, encryptor)["outputProperties"] == {"greeting": "Hello World"}


@pytest.fixture(scope="module")
def secret_task_stdout(tmp_path_factory):
    """Stdout of SecretTask, which writes its secrets through print, the logger and a comment."""
    workspace = make_task_workspace(tmp_path_factory.mktemp("secret-task"))
    context = input_context("containerExamples.SecretTask", [task_property("token", "t0k3n-value", password=True)],
                            password="run-as-pw")
    return run_wrapper(workspace, context)


def test_printed_secrets_are_masked(secret_task_stdout):
    assert "print: ******** ********" in secret_task_stdout.splitlines()


@pytest.mark.xfail(reason="dai_logger's handler holds the original sys.stdout, so logged lines and "
                          "comments bypass MaskedIO and print secrets in clear text")
@pytest.mark.parametrize("channel", ["logger:", "##[start: comment]comment:"], ids=["logger", "comment"])
def test_logged_secrets_are_masked(secret_task_stdout, channel):
    (line,) = [line for line in secret_task_stdout.splitlines() if channel in line]

    assert "t0k3n-value" not in line and "run-as-pw" not in line


# -- real SIGABRT ----------------------------------------------------------

GRACE_PERIOD = 2.0


def wait_until_started(workspace, process):
    """Waits for the fixture task's ``task_started`` file, failing if the wrapper exits or 30s pass."""
    marker = workspace / "task_started"
    deadline = time.monotonic() + 30
    while not marker.exists():
        if process.poll() is not None or time.monotonic() > deadline:
            _, stdout, stderr = finish(process)
            pytest.fail(f"task did not start\nstdout:\n{stdout}\nstderr:\n{stderr}")
        time.sleep(0.05)


def run_and_abort(workspace, task_type):
    """Runs task_type, sends SIGABRT once execute() has started; returns (seconds to exit, output)."""
    process = start_wrapper(workspace, input_context(task_type, []),
                            ABORT_GRACE_PERIOD_SECONDS=str(GRACE_PERIOD))
    wait_until_started(workspace, process)

    start = time.monotonic()
    process.send_signal(signal.SIGABRT)
    returncode, stdout, stderr = finish(process, timeout=15)
    elapsed = time.monotonic() - start

    assert returncode == 1, f"wrapper exited with {returncode}\nstdout:\n{stdout}\nstderr:\n{stderr}"
    return elapsed, read_output(workspace)


@posix_only
def test_sigabrt_reports_a_blocked_task_as_aborted_after_the_grace_period(task_workspace):
    elapsed, output = run_and_abort(task_workspace, "containerExamples.BlockingTask")

    assert GRACE_PERIOD <= elapsed < 10
    assert output == {"exitCode": 1, "jobErrorMessage": "Abort requested", "outputProperties": {},
                      "reportingRecords": []}


@posix_only
def test_sigabrt_reports_what_a_cooperative_task_recorded_while_stopping(task_workspace):
    elapsed, output = run_and_abort(task_workspace, "containerExamples.CooperativeTask")

    assert elapsed < GRACE_PERIOD
    assert (output["exitCode"], output["jobErrorMessage"]) == (1, "Abort requested")
    assert output["outputProperties"] == {"stoppedCooperatively": True}
    (record,) = output["reportingRecords"]
    assert record["processed"] > 0


@posix_only
def test_sigabrt_exits_while_the_task_is_blocked_writing_to_stderr(task_workspace):
    (task_workspace / "input.json").write_text(json.dumps(input_context("containerExamples.StderrFloodTask", [])))
    env = wrapper_env(ABORT_GRACE_PERIOD_SECONDS=str(GRACE_PERIOD))
    del env["PYTHONUNBUFFERED"]  # buffered streams have the lock a blocked write holds
    read_end, write_end = os.pipe()  # stderr goes here and is never read, so it fills up
    try:
        with open(task_workspace / "stdout.log", "w") as stdout:
            process = subprocess.Popen([sys.executable, "-m", "digitalai.release.integration.wrapper"],
                                       cwd=task_workspace, env=env, stdout=stdout, stderr=write_end)
        os.close(write_end)
        wait_until_started(task_workspace, process)
        time.sleep(1)  # the pipe fills within milliseconds; then the task's write blocks

        start = time.monotonic()
        process.send_signal(signal.SIGABRT)
        try:
            process.wait(timeout=15)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
            pytest.fail("wrapper did not exit after SIGABRT while the task was blocked writing to stderr")
        elapsed = time.monotonic() - start
    finally:
        os.close(read_end)

    assert process.returncode == 1
    assert elapsed < GRACE_PERIOD + 5
    assert read_output(task_workspace) == {"exitCode": 1, "jobErrorMessage": "Abort requested",
                                           "outputProperties": {}, "reportingRecords": []}
