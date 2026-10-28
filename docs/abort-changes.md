# Abort handling: issues on `main` and the fixes on `ReportRecords`

This document records the problems found in the abort support that was merged to `main` in
`75990ee` (D-43840, "Support abort signal in container python plugin"), and how the
`ReportRecords` branch fixes them. It covers every file the branch changes.

- **Baseline:** `main` at `75990ee`.
- **Branch:** `ReportRecords`, commit `abdf442` ("Report abort results reliably and let tasks
  stop cooperatively"), plus a wording fix for the default `abortTimeout` in `wrapper.py` and
  `docs/classes/base_task.md`.

## Contents

- [How an abort reaches the SDK](#how-an-abort-reaches-the-sdk)
- [Abort handling on `main`](#abort-handling-on-main)
- [Issues on `main`](#issues-on-main)
- [How the issues are resolved](#how-the-issues-are-resolved)
- [Changes by file](#changes-by-file)
- [Behaviour changes for task authors](#behaviour-changes-for-task-authors)
- [Verification](#verification)
- [Out of scope](#out-of-scope)

## How an abort reaches the SDK

When a user aborts a running container task in Release, the release-runner aborts it in two
phases:

1. **Phase 1 — signal.** The runner sends `SIGABRT` to process 1 of the task container:
   - Docker: `ContainerKill(…, Signal: "SIGABRT")` (`docker/container.go`).
   - Kubernetes: `exec /bin/kill -6 1` in the task container (`k8s/pod.go`).
2. **Phase 2 — force kill.** The runner waits for the task type's `abortTimeout`, a hidden
   property of `xlrelease.ContainerTask` that defaults to 30 seconds; the runner uses 10 seconds
   if it is `0`. If the task is still running after that, the runner kills the container
   (Docker) or deletes the pod (Kubernetes, which sends `SIGTERM` and then `SIGKILL`).

The result Release shows (exit code, error message, output properties, reporting records) is
whatever the SDK reports before the process exits. A result that is not reported before
Phase 2 is lost.

## Abort handling on `main`

`75990ee` introduced the threading model that the branch keeps:

- `wrapper.execute_task()` runs the task's `execute_task()` on a daemon worker thread. The main
  thread polls `worker.join(0.5)` so that it stays free to run signal handlers.
- `SIGABRT` and `SIGTERM` are handled by `wrapper.abort_handler()`. Python always runs signal
  handlers on the main thread.
- `BaseTask.abort()` sets exit code `1` and "Abort requested", then raises `AbortException`.
- `BaseTask.is_abort_requested()` lets a task poll for an abort.
- `_report_once()` makes sure the result is reported only once, whichever path reports first.

On `main`, `abort_handler()` does this, in order:

```python
dai_task_object._request_abort()   # is_abort_requested() now returns True
dai_task_object.abort()            # marks exit code 1, "Abort requested"
_report_once()                     # reports the result
os._exit(1)                        # ends the process, including the worker thread
```

## Issues on `main`

### 1. `is_abort_requested()` has no effect: no grace period

**Where:** `wrapper.py`, `abort_handler()` (lines 131–148 on `main`).

The handler sets the abort flag and then reports and calls `os._exit(1)` within microseconds,
without waiting for the worker thread. A task that polls `is_abort_requested()` never gets to
act on it: the process is gone before the next poll.

**Example:**

```python
class LongRunningTask(BaseTask):
    def execute(self) -> None:
        for item in items:
            if self.is_abort_requested():
                self.set_output_property("processed", count)   # never reported
                self.add_comment("Stopping early")             # never printed
                return
            process(item)
```

Anything the task sets while stopping is lost. The cooperative-stop API exists, but it cannot
change the reported result.

### 2. A signal during a report destroys the result

**Where:** `wrapper.py`, `_report_once()` (line 98) and `abort_handler()`.

Both the normal completion path (`execute_task()` → `_report_once()`) and the abort handler run
on the main thread. A signal handler runs between bytecodes of whatever the main thread is
doing, so it can interrupt a report that is in progress, for example while
`update_output_context()` is pushing to the callback URL or is in
`retry_push_result_infinitely()`.

`_report_lock` is an `RLock`, so the handler re-enters it on the same thread. It sees
`_result_reported = True`, returns without reporting, and calls `os._exit(1)` partway through
the push. **Release receives no result at all.**

A second signal while the handler's own report is being sent has the same effect, for example a
`SIGTERM` from a pod deletion after a `SIGABRT`.

### 3. The result is serialized while the worker thread may change it

**Where:** `wrapper.py`, `update_output_context()` (line 231) called from the handler.

The handler serializes `dai_task_object.get_output_context()` (the task's own object) with
`json.dumps(output_context.to_dict())` while `execute()` may still be adding output properties
or reporting records on the worker thread. This can fail with
`RuntimeError: dictionary changed size during iteration`.

`json.dumps` is outside the `try` in `update_output_context()`, so the exception escapes the
signal handler, `os._exit(1)` is never reached, and `run()`'s `except` reports a generic failure
with the exception message. The task's outputs and records are lost.

### 4. Regression: tasks whose `__init__` skips `super().__init__()` crash

**Where:** `base_task.py`, `__init__` (line 24) and `execute_task()`.

Before `75990ee`, `execute_task()` created the output context. `75990ee` moved that into
`BaseTask.__init__()`, and added `_abort_event` there too. A subclass that defines its own
`__init__` without calling `super().__init__()` now fails:

- `set_output_property()`, `set_exit_code()`, `add_reporting_record()` raise `AttributeError`
  (`output_context` does not exist). `execute_task()`'s `except` then calls `set_exit_code()`,
  which raises the same error again.
- `is_abort_requested()` raises `AttributeError` (`_abort_event` does not exist).

Such tasks worked on the previous SDK release.

### 5. An aborted or exited task can be reported as succeeded

**Where:** `wrapper.py`, `abort_handler()` and the `TODO` in `execute_task()` (line 347).

- If a task overrides `abort()` without calling `super().abort()` and without setting an exit
  code, the handler reports exit code `0`. Release then records an aborted task as successful.
- If a task calls `sys.exit(2)` (or `sys.exit("message")`) without calling `set_exit_code()`,
  the process exits with that status, but the reported result has exit code `0`. The `TODO` on
  `main` notes this and leaves it unresolved.

### 6. Smaller issues

| Issue | Where | Effect |
|-------|-------|--------|
| No flush before `os._exit()` | `abort_handler()` | `os._exit()` skips Python's stream flushing, so the last lines on stdout/stderr (including `##[start: comment]` markers Release reads) can be lost. |
| Misleading message when no task exists | `_report_once()` | A signal that arrives before the task object is created is reported as "Task produced no output context". |
| Thread safety of `abort()` overrides undocumented | `base_task.py`, docs | The SDK calls `abort()` on the main thread while `execute()` runs on the worker thread. Nothing told task authors that an override must be thread-safe. |
| Changelog | `README.md` | The abort feature was not in the changelog. |

## How the issues are resolved

### Grace period (issue 1)

`abort_handler()` now waits for the worker thread before reporting:

```python
task._request_abort()
task.abort()                                       # AbortException / SystemExit / errors caught
worker.join(timeout=ABORT_GRACE_PERIOD_SECONDS)    # new: let execute() stop
_report_once(aborted=True, …)
_exit_process(1)
```

- `ABORT_GRACE_PERIOD_SECONDS` is read from the environment and defaults to `3`. It must stay
  below `abortTimeout` (30 seconds by default).
- The worker thread is stored in a new module global `_worker` by `execute_task()`.
- The wait is skipped when there is no worker or it has already finished, so a task that is
  already done or never started is reported immediately.
- A task that never checks `is_abort_requested()` is reported after the grace period, as before
  apart from the wait.

### Report state instead of a flag (issue 2)

`_result_reported: bool` is replaced by `_report_state`, which is one of `pending`,
`in_progress` or `done`, plus two flags:

- `_abort_in_progress` — set while the handler handles a signal.
- `_exit_after_report` — set when a signal arrives during a report.

`abort_handler()` now starts with:

```python
with _report_lock:
    if _abort_in_progress:                     # repeat signal
        return                                 # ignored
    if _report_state == _REPORT_IN_PROGRESS:   # interrupted a report on the main thread
        _exit_after_report = True              # exit once the report finishes
        return                                 # let the push continue
    _abort_in_progress = True
```

`_report_once()` sets `in_progress` before reporting and `done` in a `finally`. If
`_exit_after_report` was set meanwhile, it exits after the report. The interrupted push
therefore always completes, and the process still exits.

### Report a copy of the output context (issue 3)

`_report_once()` now reports a copy made by `_snapshot_output_context()`: a new `OutputContext`
with `dict(output_properties)` and `list(reporting_records)`. Under CPython's GIL these copies
are taken in a single C call, so the worker thread cannot change the dictionary while it is
being serialized. With the grace period, the copy is normally taken after the worker has
already stopped.

### Create the output context and abort flag on first use (issue 4)

`BaseTask` gains `_ensure_output_context()`. `get_output_context()` calls it, and all setters
and getters go through `get_output_context()` instead of `self.output_context`:
`get_output_properties()`, `set_output_property()`, `set_exit_code()`, `set_error_message()`,
`add_reporting_record()`.

`is_abort_requested()` and `_request_abort()` read `_abort_event` with `getattr` and create it
if it is missing. Subclasses that skip `super().__init__()` work again.

### Never report an aborted or exited task as succeeded (issue 5)

- `_report_once(aborted=True)`: if the copy's exit code is `0`, it is set to `1`, and the error
  message to "Abort requested" if it is empty. The task's own message is kept when it set one.
- `execute_task()`: if the worker raised `SystemExit` with a non-zero status and the task did not
  set an exit code, that status is reported. The new helper `_exit_code_of()` maps
  `SystemExit.code` the way Python does: `None` → `0`, an `int` → itself, anything else → `1`.
  The error message is the string passed to `sys.exit()`, or "Task exited with code N".
  `sys.exit(0)` still reports success. The `SystemExit` is still re-raised after reporting, so
  the process exit status is unchanged.

### Smaller issues (issue 6)

- `_exit_process()` flushes `sys.stdout` and `sys.stderr` before `os._exit()`, both in the
  handler and in the exit-after-report path.
- A signal before the task object exists is reported as "Abort requested before the task
  started".
- The `abort()` docstring and `docs/classes/base_task.md` state that an override must be
  thread-safe, that outputs set in an override are reported, and that they must be set before
  `super().abort()` because it raises.
- `README.md` has an "Unreleased" changelog entry.

## Changes by file

### `digitalai/release/integration/wrapper.py`

| Change | Details |
|--------|---------|
| `ABORT_GRACE_PERIOD_SECONDS` | New setting, from the environment, default `3`. The comment explains the relation to `abortTimeout`. |
| Report state | `_result_reported` replaced by `_report_state` (`_REPORT_PENDING`, `_REPORT_IN_PROGRESS`, `_REPORT_DONE`), plus `_abort_in_progress`, `_exit_after_report` and `_worker`. The comment above them explains why a signal can arrive during a report. |
| `_reset_report_guard()` | Resets all four values, so each daemon-mode execution starts clean. |
| `_snapshot_output_context()` | New. Returns a copy of the task's output context, or a failure context with the given message when there is no task. |
| `_flush_std_streams()`, `_exit_process()` | New. Flush stdout/stderr, then `os._exit()`. |
| `_report_once()` | New parameters `aborted` and `no_task_message`. Moves `pending` → `in_progress` → `done`, reports the copy, forces a non-zero exit code when `aborted`, and exits afterwards if `_exit_after_report` is set. |
| `abort_handler()` | Ignores repeat signals, defers to an in-progress report, waits up to the grace period for the worker, reports with `aborted=True`, exits through `_exit_process()`. The docstring describes the three steps. The `global dai_task_object` statement is removed; the handler reads it into a local. |
| `_exit_code_of()` | New. Maps `SystemExit.code` to the process exit status. |
| `execute_task()` | Stores the worker in `_worker`; copies a non-zero `sys.exit()` status into the output context when the task set none. The `TODO` is removed because it is resolved. The docstring is updated. |

### `digitalai/release/integration/base_task.py`

| Change | Details |
|--------|---------|
| `abort()` docstring | Adds the thread-safety note and when to set outputs in an override. |
| `is_abort_requested()` | Reads `_abort_event` with `getattr`; returns `False` if it does not exist. |
| `_request_abort()` | Creates `_abort_event` if it does not exist. |
| `_ensure_output_context()` | New. Creates `OutputContext(0, "", {}, [])` if `output_context` is missing or `None`. |
| `get_output_context()` | Calls `_ensure_output_context()` first. |
| Getters and setters | `get_output_properties()`, `set_output_property()`, `set_exit_code()`, `set_error_message()` and `add_reporting_record()` use `get_output_context()`. |

`BaseTask.__init__()` still creates the output context and the abort event; the new code only
covers subclasses that skip it.

### `tests/release/integration/test_wrapper_abort.py`

Existing tests on `main` are kept, except one that asserted the old behaviour:

- `test_direct_sys_exit_propagates_status_and_reports_context_as_is` (expected exit code `0`
  reported for `sys.exit(2)`) becomes `test_direct_sys_exit_propagates_status_and_reports_its_code`
  (expects `2` and "Task exited with code 2").

New tests:

| Test class | Test | What it checks |
|------------|------|----------------|
| `WrapperExecuteTaskThreadingTests` | `test_sys_exit_with_message_reports_exit_code_1_and_the_message` | `sys.exit("Configuration missing")` reports exit code `1` and the message. |
| | `test_sys_exit_zero_reports_success` | `sys.exit(0)` still reports exit code `0`. |
| `WrapperAbortGracePeriodTests` | `test_cooperative_stop_within_grace_period_is_reported` | A task polling `is_abort_requested()` stops; its output property and reporting record are in the reported result, with exit code `1`. |
| | `test_task_that_does_not_stop_is_reported_after_grace_period` | A blocked task is reported after the (patched, 0.2 s) grace period, not before and not much later. |
| | `test_reported_result_is_a_copy_of_the_output_context` | The reported context and its properties dictionary are copies, not the task's own objects. |
| | `test_signal_during_report_lets_the_report_finish_then_exits` | A signal raised inside `update_output_context()` lets the push complete with the task's own result, then exits once. |
| | `test_second_signal_during_abort_is_ignored` | A signal arriving inside `abort()` is ignored; one report, one exit. |
| | `test_aborted_result_never_reports_exit_code_0` | An `abort()` override that sets no exit code is still reported with `1` and "Abort requested", keeping its outputs. |
| | `test_signal_before_task_exists_reports_a_clear_message` | Reports "Abort requested before the task started". |
| `WrapperTaskWithoutSuperInitTests` | `test_runs_and_reports_outputs` | A task without `super().__init__()` runs and reports its outputs. |
| | `test_can_be_aborted` | Such a task can be aborted, and `is_abort_requested()` works. |

`WrapperRealSigabrtEndToEndTest` runs the real wrapper in a subprocess and sends a real
`SIGABRT`:

- The shared logic moves into `_run_and_abort(task_type)`; input and output files are renamed
  to `abort_input.json` / `abort_output.json`.
- `test_real_sigabrt_interrupts_blocking_task` now also asserts that the wrapper waits at least
  the grace period before exiting.
- New `test_real_sigabrt_reports_outputs_of_cooperative_task` checks that a cooperative task
  exits within the grace period and that its output property and reporting record are reported.
- The class is skipped on Windows, which cannot deliver `SIGABRT` to a child process.

### `tests/release/integration/cooperative_task.py`

New fixture task for the end-to-end test. `CooperativeTask` loops until `is_abort_requested()`,
then sets `stoppedCooperatively` and adds a reporting record with the number of loop passes.

### `docs/classes/base_task.md`

- `abort`: adds the thread-safety note, how outputs set in an override are reported, and that
  an aborted result is always reported with a non-zero exit code.
- `is_abort_requested`: describes `ABORT_GRACE_PERIOD_SECONDS`, what is included in the result,
  and the relation to `abortTimeout` (30 seconds by default; 10 seconds if set to `0`).

### `docs/examples.md`

The `LongRunningTask` example now mentions the grace period and that what the task records while
stopping is reported.

### `README.md`

New "Unreleased" changelog section: the abort feature and grace period under Features; the
report-during-signal, exit-code and `super().__init__()` fixes under Fixes.

## Behaviour changes for task authors

| Situation | `main` | `ReportRecords` |
|-----------|--------|-----------------|
| Task polls `is_abort_requested()` and returns | Process killed immediately; outputs set while stopping are lost | Outputs and records set within the grace period are reported |
| Task ignores the abort | Reported immediately | Reported after up to `ABORT_GRACE_PERIOD_SECONDS` (default 3 s) |
| Signal while the result is being sent | Send cut off; no result | Send completes, then the process exits |
| Second signal during an abort | Can cut off the first report | Ignored |
| `abort()` override sets no exit code | Reported as success (exit code `0`) | Reported with exit code `1`, "Abort requested" |
| `sys.exit(2)` in `execute()` | Reported exit code `0` | Reported exit code `2` |
| Subclass without `super().__init__()` | `AttributeError` | Works |

The only timing change is the wait for a task that does not stop: it exits up to 3 seconds
later. Set `ABORT_GRACE_PERIOD_SECONDS=0` to disable the wait.

## Verification

| Level | Result |
|-------|--------|
| Unit tests, Windows | 126 passed, 2 skipped (the real-`SIGABRT` tests). |
| Unit and end-to-end tests, Linux (`python:3.12-slim` container) | All pass, including both real-`SIGABRT` tests. The other skipped tests need a live Release server. |
| Real wrapper, real `SIGABRT`, Linux container | Template example tasks: cooperative stop, checkpoint `abort()`, `abort()` override cleanup, and a task that ignores the abort all report exit code `1` with their outputs. The ignoring task exits 3.0 s after the signal. |
| Live Release, Docker runner | All six template abort examples behave as above. Release records the outputs and the task's comments; results arrive 0.1–3.1 s after the abort. |
| Live Release, Kubernetes runner (Docker Desktop) | Same results. The runner log shows `SIGABRT` delivered via `exec /bin/kill -6 1` for every aborted pod, with no fallback to pod deletion. Results arrive 0.3–3.2 s after the abort. |

Release marks an aborted container task as FAILED, with the comments "Script aborted by user"
and "Execution failed. Cause: Abort requested". That is Release's own behaviour.

## Out of scope

These are outside the SDK or unchanged by the branch:

- **Images without `/bin/kill`.** On Kubernetes the runner runs `/bin/kill -6 1` in the task
  container. Images such as `python:3.12-slim` have no `kill` binary, so the exec fails and the
  runner deletes the pod immediately. The SDK still handles the resulting `SIGTERM`, but this has
  not been tested end to end. Alpine-based images have `kill` (busybox).
- **Shell-form entrypoints.** If the image starts the wrapper through a shell (`CMD python -m …`
  without brackets, or a script without `exec`), process 1 is the shell, which does not pass the
  signal on.
- **Daemon mode.** An abort still ends the whole executor process with `os._exit()`, as on
  `main`. The runner starts a new executor for the next task.
- **Slow Kubernetes API calls.** Writing the result secret uses the HTTP timeouts (10 s connect,
  60 s read). A slow enough API server can still let Phase 2 delete the pod first.
- **Executor reuse in the runner.** With `evictionTime > 0`, sequential tasks with the same image
  do not always share a pod: the runner marks an executor idle only after draining its logs, so
  the next task can arrive first and get a new pod. This is runner behaviour.
