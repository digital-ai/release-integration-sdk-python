# Abort handling: issues on `main` and the fixes on `ReportRecords`

This document records the problems found in the abort support that was merged to `main` in
`75990ee` (D-43840, "Support abort signal in container python plugin"), and how the
`ReportRecords` branch fixes them. It covers every file the branch changes.

- **Baseline:** `main` at `75990ee`.
- **Branch:** `ReportRecords`, commit `abdf442` ("Report abort results reliably and let tasks
  stop cooperatively"), plus a wording fix for the default `abortTimeout` in `wrapper.py` and
  `docs/classes/base_task.md`.
- **Status:** all issues below are fixed on `ReportRecords` and verified on the Docker and
  Kubernetes runners. `main` still has them, and no SDK release contains the fixes yet.

## Contents

- [Summary of issues and fixes](#summary-of-issues-and-fixes)
- [How an abort reaches the SDK](#how-an-abort-reaches-the-sdk)
- [Abort handling on `main`](#abort-handling-on-main)
- [Issues on `main`](#issues-on-main)
- [How the issues are resolved](#how-the-issues-are-resolved)
- [Changes by file](#changes-by-file)
- [Behaviour changes for task authors](#behaviour-changes-for-task-authors)
- [Verification](#verification)
- [Out of scope](#out-of-scope)

## Summary of issues and fixes

Line numbers refer to `main` at `75990ee` (column "On `main`") and to `ReportRecords`
(column "Fixed on `ReportRecords`"). Each issue is described in detail under
[Issues on `main`](#issues-on-main), and each fix under
[How the issues are resolved](#how-the-issues-are-resolved).

| # | Issue | On `main`: where and effect | Fixed on `ReportRecords`: where | How it is fixed | Tests |
|---|-------|-----------------------------|---------------------------------|-----------------|-------|
| 1 | `is_abort_requested()` has no effect: no grace period | `wrapper.py` `abort_handler()`, lines 131–148: sets the abort flag, reports and calls `os._exit(1)` immediately, without waiting for `execute()`.<br>**Effect:** outputs, reporting records and comments a task sets while stopping are lost. | `wrapper.py`:<br>• [`ABORT_GRACE_PERIOD_SECONDS`, line 58](../digitalai/release/integration/wrapper.py#L58)<br>• [`_worker`, line 101](../digitalai/release/integration/wrapper.py#L101), set in [`execute_task()`, line 486](../digitalai/release/integration/wrapper.py#L486)<br>• [`abort_handler()` wait, line 276](../digitalai/release/integration/wrapper.py#L276) | After calling `abort()`, the handler waits up to `ABORT_GRACE_PERIOD_SECONDS` (environment variable, default `3`) for the worker thread with `worker.join(timeout=…)`, then reports. The wait is skipped if there is no worker or it has finished. A task that never stops is reported when the wait ends. | `test_cooperative_task_is_reported_with_what_it_recorded_while_stopping`<br>`test_task_that_ignores_the_abort_is_reported_after_the_grace_period`<br>`test_sigabrt_reports_what_a_cooperative_task_recorded_while_stopping` (real `SIGABRT`)<br>`test_sigabrt_reports_a_blocked_task_as_aborted_after_the_grace_period` (real `SIGABRT`) |
| 2 | A signal during a report destroys the result | `wrapper.py` `_report_once()`, line 98 (`_result_reported` flag) and `abort_handler()`: the handler runs on the main thread, can interrupt the main thread's own report, re-enters the `RLock`, sees the flag set and calls `os._exit(1)` mid-send. A second signal during an abort does the same.<br>**Effect:** Release receives no result. | `wrapper.py`:<br>• [report state, lines 85–97](../digitalai/release/integration/wrapper.py#L85-L97)<br>• [`_report_once()` state changes, lines 207 and 217–219](../digitalai/release/integration/wrapper.py#L207-L219)<br>• [`abort_handler()` guards, lines 246–253](../digitalai/release/integration/wrapper.py#L246-L253)<br>• [`_reset_report_guard()`, line 108](../digitalai/release/integration/wrapper.py#L108) | The boolean flag is replaced by `_report_state` (`pending` → `in_progress` → `done`) plus `_abort_in_progress` and `_exit_after_report`. If a signal arrives while a report is `in_progress`, the handler sets `_exit_after_report` and returns, so the send completes; `_report_once()` then exits. A signal while an abort is already being handled is ignored. `_reset_report_guard()` resets all of this for each daemon-mode execution. | `test_signal_during_a_report_lets_the_report_finish_then_exits`<br>`test_second_signal_during_an_abort_is_ignored`<br>`test_each_execution_reports_its_own_result` |
| 3 | The result is serialized while the task may still change it | `wrapper.py` `update_output_context()`, line 231: `json.dumps()` of the task's own output context, called from the handler while `execute()` may still add outputs on the worker thread. `json.dumps` is outside the `try`.<br>**Effect:** possible `RuntimeError: dictionary changed size during iteration`; the handler never reaches `os._exit`, and the task is reported as a generic failure without its outputs. | `wrapper.py`:<br>• [`_snapshot_output_context()`, lines 118–157](../digitalai/release/integration/wrapper.py#L118-L157), called from [`_report_once()`, line 190](../digitalai/release/integration/wrapper.py#L190)<br>• [`abort_handler()` exit, lines 282–286](../digitalai/release/integration/wrapper.py#L282-L286) | `_report_once()` reports a fully detached copy: `_snapshot_output_context()` serializes the context and builds a new `OutputContext` from the JSON, so the result shares no object, nested or not, with the task. If a nested output changes while it is read (`RuntimeError`), it is read again, up to 5 times; if that keeps failing, or an output cannot be serialized, the result is reported as failed without outputs and records. `abort_handler()` exits in a `finally`, so a failed report cannot keep the process running. With the grace period, the copy is normally taken after the worker has stopped. | `test_reported_result_is_a_snapshot_of_the_output_context`<br>`test_reported_result_shares_no_nested_object_with_the_task`<br>`test_output_changed_while_read_is_read_again`<br>`test_output_that_keeps_changing_is_left_out_of_the_aborted_result`<br>`test_abort_exits_even_when_reporting_fails`<br>`test_outputs_that_cannot_be_serialized_are_reported_as_a_failure` |
| 4 | Regression: tasks whose `__init__` skips `super().__init__()` crash | `base_task.py` `__init__()`, line 24: the output context and `_abort_event` are created only here; `execute_task()` no longer creates the output context.<br>**Effect:** `AttributeError` in `set_output_property()`, `set_exit_code()`, `add_reporting_record()` (raised again from `execute_task()`'s error handler) and in `is_abort_requested()`. | `base_task.py`:<br>• [`_ensure_output_context()`, line 90](../digitalai/release/integration/base_task.py#L90), called by [`get_output_context()`, line 98](../digitalai/release/integration/base_task.py#L98)<br>• getters/setters use `get_output_context()`: [lines 109](../digitalai/release/integration/base_task.py#L109), [133](../digitalai/release/integration/base_task.py#L133), [139](../digitalai/release/integration/base_task.py#L139), [145](../digitalai/release/integration/base_task.py#L145), [163](../digitalai/release/integration/base_task.py#L163)<br>• [`is_abort_requested()`, line 78](../digitalai/release/integration/base_task.py#L78) and [`_request_abort()`, line 86](../digitalai/release/integration/base_task.py#L86) | The output context is created on first use if it is missing. `get_output_properties()`, `set_output_property()`, `set_exit_code()`, `set_error_message()` and `add_reporting_record()` go through `get_output_context()`. `is_abort_requested()` returns `False` and `_request_abort()` creates the event when `_abort_event` is missing. `__init__()` is unchanged. `execute_task()` creates the output context on the main thread before it starts the worker ([line 490](../digitalai/release/integration/wrapper.py#L490)); otherwise the worker's first setter and an `abort()` override run by the signal handler can each create one, and the worker's replaces the handler's, losing its cleanup outputs and message. | `test_task_without_super_init_runs_and_reports`<br>`test_task_without_super_init_can_be_aborted`<br>`test_task_without_super_init_has_its_output_context_before_it_runs` |
| 5a | An `abort()` override that sets no exit code is reported as succeeded | `wrapper.py` `abort_handler()`: reports the task's context as it is.<br>**Effect:** an override that does not call `super().abort()` reports exit code `0`, and Release records the aborted task as successful. | `wrapper.py`:<br>• [`_report_once(aborted=True)`, lines 211–213](../digitalai/release/integration/wrapper.py#L211-L213), called from [`abort_handler()`, line 283](../digitalai/release/integration/wrapper.py#L283) | On the abort path, an exit code of `0` in the reported copy becomes `1`, and an empty error message becomes "Abort requested". A message the task set itself is kept. | `test_abort_override_that_sets_no_exit_code_is_still_reported_as_failed` |
| 5b | `sys.exit(n)` is reported as exit code `0` | `wrapper.py` `execute_task()`, `TODO` at line 347: the `SystemExit` is re-raised so the process exits with `n`, but the reported context keeps exit code `0`.<br>**Effect:** Release records the task as successful. | `wrapper.py`:<br>• [`_exit_code_of()`, line 433](../digitalai/release/integration/wrapper.py#L433)<br>• [`execute_task()`, lines 496–502](../digitalai/release/integration/wrapper.py#L496-L502) | If the worker raised `SystemExit` with a non-zero status and the task set no exit code, that status is reported. `_exit_code_of()` maps `SystemExit.code` like Python does: `None` → `0`, an `int` → itself (a `bool` → `0` or `1`, so the result holds a number, not `true`), anything else → `1`. The error message is the string passed to `sys.exit()`, or "Task exited with code N". The `SystemExit` is still re-raised. The `TODO` is removed. | `test_sys_exit_is_reported_and_propagated` (`int`, `message`, `zero`, `none`, `true` and `false` cases) |
| 6a | Output not flushed before exit | `wrapper.py` `abort_handler()`: `os._exit(1)` skips Python's stream flushing.<br>**Effect:** the last stdout/stderr lines, including the `##[start: comment]` markers Release reads, can be lost. | `wrapper.py`:<br>• [`_flush_std_streams()`, lines 160–182](../digitalai/release/integration/wrapper.py#L160-L182) and [`_exit_process()`, line 185](../digitalai/release/integration/wrapper.py#L185), used by `abort_handler()` and `_report_once()` | `sys.stdout` and `sys.stderr` are flushed before every `os._exit()`. The flush runs on a separate thread and is waited for at most `FLUSH_TIMEOUT_SECONDS` (1 s): with buffered streams (no `PYTHONUNBUFFERED`), a task blocked writing to a full stderr pipe that nobody reads holds the stream's lock, and an unbounded flush kept the process running, after reporting, until the runner force-killed it. | `test_exit_flushes_stdout_and_stderr_first`<br>`test_exit_does_not_wait_for_a_blocked_stream`<br>`test_sigabrt_exits_while_the_task_is_blocked_writing_to_stderr` (real `SIGABRT`)<br>Live runs show the task's comments in Release. |
| 6b | Misleading message when a signal arrives before the task exists | `wrapper.py` `_report_once()`: reports "Task produced no output context". | `wrapper.py`:<br>• [`_snapshot_output_context()`, line 118](../digitalai/release/integration/wrapper.py#L118) with the message passed from [`abort_handler()`, line 283](../digitalai/release/integration/wrapper.py#L283) | The handler reports "Abort requested before the task started". The normal path keeps the old message. | `test_abort_before_a_task_exists_reports_a_clear_message` |
| 6c | Thread safety of `abort()` overrides undocumented | `base_task.py` `abort()` docstring and `docs/classes/base_task.md`: no mention that `abort()` runs on the main thread while `execute()` runs on the worker thread. | • [`base_task.py` `abort()` docstring, lines 62–67](../digitalai/release/integration/base_task.py#L62-L67)<br>• [`docs/classes/base_task.md`, `abort`](classes/base_task.md#abort) and [`is_abort_requested`](classes/base_task.md#is_abort_requested)<br>• [`docs/examples.md`](examples.md) | The docs state that an override must be thread-safe, that outputs set in it are reported, and that they must be set before `super().abort()` because it raises. They also describe the grace period and its relation to `abortTimeout`. | Documentation only. |
| 6d | Abort feature missing from the changelog | `README.md`. | [`README.md`, "Unreleased"](../README.md#unreleased) | New "Unreleased" section listing the abort feature, the grace period and the fixes. | Documentation only. |

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

`_report_once()` now reports a copy made by `_snapshot_output_context()`, and that copy shares
no object with the task. Copying only the outer `output_properties` dictionary and
`reporting_records` list is not enough: a nested value, such as a dictionary output, would still
be the task's own object, and a task that ignores the abort can change it while it is serialized.

The copy is therefore made by serializing the context and building a new `OutputContext` from the
JSON. That read can still meet a nested value being changed, which raises `RuntimeError`; the
copy is then retried, up to 5 times. A deep copy would not help, as `copy.deepcopy` iterates the
same dictionary and fails the same way, and the SDK cannot lock changes a task makes directly on
its own objects. If the copy keeps failing, or an output cannot be serialized at all, the result
is reported as failed, without outputs and reporting records, and the reason is logged.

`abort_handler()` calls `_exit_process(1)` in a `finally`, so even a report that fails cannot
leave the aborted process running. With the grace period, the copy is normally taken after the
worker has already stopped.

### Create the output context and abort flag on first use (issue 4)

`BaseTask` gains `_ensure_output_context()`. `get_output_context()` calls it, and all setters
and getters go through `get_output_context()` instead of `self.output_context`:
`get_output_properties()`, `set_output_property()`, `set_exit_code()`, `set_error_message()`,
`add_reporting_record()`.

`is_abort_requested()` and `_request_abort()` read `_abort_event` with `getattr` and create it
if it is missing. Subclasses that skip `super().__init__()` work again.

Creating the output context on first use is a check followed by an assignment, so two threads
using it for the first time at once can each create one. That happens when a cooperative task
sets its first output as it stops, while the signal handler runs the task's `abort()` override:
the worker's context replaces the handler's, and the override's outputs and message are lost.
`execute_task()` therefore calls `get_output_context()` on the main thread before it starts the
worker, so both threads use the same object.

### Never report an aborted or exited task as succeeded (issue 5)

- `_report_once(aborted=True)`: if the copy's exit code is `0`, it is set to `1`, and the error
  message to "Abort requested" if it is empty. The task's own message is kept when it set one.
- `execute_task()`: if the worker raised `SystemExit` with a non-zero status and the task did not
  set an exit code, that status is reported. The new helper `_exit_code_of()` maps
  `SystemExit.code` the way Python does: `None` → `0`, an `int` → itself, anything else → `1`.
  A `bool`, as in `sys.exit(not ok)`, becomes `0` or `1`, so the result holds a number, not `true`.
  The error message is the string passed to `sys.exit()`, or "Task exited with code N".
  `sys.exit(0)` still reports success. The `SystemExit` is still re-raised after reporting, so
  the process exit status is unchanged.

### Smaller issues (issue 6)

- `_exit_process()` flushes `sys.stdout` and `sys.stderr` before `os._exit()`, both in the
  handler and in the exit-after-report path. It waits for the flush at most
  `FLUSH_TIMEOUT_SECONDS` (1 s), so a task blocked writing to a full, unread stderr pipe, which
  holds the stream's lock when stdio is buffered, cannot keep the process from exiting. Nothing
  is logged on a timeout, since the logger writes to stdout, which may be the blocked stream.
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
| `_snapshot_output_context()` | New. Returns a fully detached copy of the task's output context (serialized and rebuilt, retried up to `_SNAPSHOT_ATTEMPTS` times), a copy without outputs if that fails, or a failure context with the given message when there is no task. |
| `_flush_std_streams()`, `_exit_process()` | New. Flush stdout/stderr, waiting at most `FLUSH_TIMEOUT_SECONDS`, then `os._exit()`. |
| `_report_once()` | New parameters `aborted` and `no_task_message`. Moves `pending` → `in_progress` → `done`, reports the copy, forces a non-zero exit code when `aborted`, and exits afterwards if `_exit_after_report` is set. |
| `abort_handler()` | Ignores repeat signals, defers to an in-progress report, waits up to the grace period for the worker, reports with `aborted=True`, exits through `_exit_process()`, also when reporting fails. The docstring describes the three steps. The `global dai_task_object` statement is removed; the handler reads it into a local. |
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

### Tests

The test suite was reorganized into pytest modules (see `DEVELOPMENT.md`); the summary table
names the tests for each issue. The abort behaviour is covered by:

| File | What it covers |
|------|----------------|
| `tests/release/integration/test_wrapper_abort.py` | `abort_handler()` called in-process with `update_output_context()` and `os._exit()` replaced: the grace period, a cooperative stop, a task that ignores the abort, a signal during a report, a repeat signal, `abort()` overrides (no exit code, own message, raising), tasks without `super().__init__()`, and the detached snapshot, including a nested output that changes while it is read and a report that fails. |
| `tests/release/integration/test_wrapper_execute_task.py` | The worker thread, one report per execution, `AbortException`, `sys.exit()` codes and messages, and outputs that cannot be serialized. |
| `tests/release/integration/test_wrapper_e2e.py` | The real wrapper in a subprocess with a real `SIGABRT` (skipped on Windows, which cannot deliver it to a child process). It waits for the task to start before signalling, and uses a 2 s grace period. One test aborts a task blocked writing to a full stderr pipe that is never read, with buffered stdio, and checks that the process still exits. |
| `tests/release/integration/tasks/` | The tasks those subprocess runs load: `BlockingTask` ignores the abort; `CooperativeTask` loops until `is_abort_requested()`, then sets `stoppedCooperatively` and adds a reporting record with the number of loop passes. |

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
| Test suite, Windows, with a live Release server and Docker Desktop Kubernetes | 362 passed, 3 skipped (the real-`SIGABRT` tests), 4 xfailed (known secret-masking bugs, unrelated to abort). |
| Test suite, Linux (Python 3.10 container, as in CI) | 326 passed, 7 skipped (the live Release and Kubernetes tests, with no servers in the container), 4 xfailed; all three real-`SIGABRT` tests pass. Three consecutive runs. |
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
