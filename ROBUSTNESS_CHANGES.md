# Robustness Improvements — `digitalai/release/integration`

This document describes the robustness fixes applied across the integration SDK
package and the accompanying test updates. The behaviour exercised by the sample
input context (a `containerExamples.Hello` task) is preserved — the changes
harden failure paths, networking, and diagnostics without altering the happy
path.

## Sample input context used for verification

```json
{
  "release": {
    "id": "Applications/Folder1f65c7220b394afbb941154342fd9fc6/Release31de09e95c8e4ebb95aaed29a8082d0b",
    "automatedTaskAsUser": { "username": null, "password": null }
  },
  "task": {
    "id": "Applications/Folder1f65c7220b394afbb941154342fd9fc6/Release31de09e95c8e4ebb95aaed29a8082d0b/Phase723a601c78804f7dbcaa8b05b83708f5/Task3a35b67b42b6428b854857fba470b39a",
    "type": "containerExamples.Hello",
    "properties": [
      { "name": "capabilities", "value": ["remote"], "kind": "SET_OF_STRING", "category": "input", "password": false },
      { "name": "yourName", "value": "World", "kind": "STRING", "category": "input", "password": false },
      { "name": "greeting", "value": null, "kind": "STRING", "category": "output", "password": false }
    ]
  }
}
```

Expected output context: `{"exitCode": 0, "jobErrorMessage": "", "outputProperties": {"greeting": "Hello World"}, "reportingRecords": []}`.

---

## `wrapper.py`

| # | Change | Reason |
|---|--------|--------|
| 1 | **HTTP timeouts added** to the `requests.get` fetch and all callback POSTs (`HTTP_CONNECT_TIMEOUT` / `HTTP_READ_TIMEOUT`, env-overridable, default 10s/60s). | Without a timeout a hung or unreachable server stalls the runner **forever**, blocking the task slot. |
| 2 | **Single shared `urllib3.PoolManager`** (`_http_pool`) instead of constructing a new `PoolManager()` on every request. | Creating a fresh pool per call defeats connection pooling/keep-alive and leaks sockets. |
| 3 | **Callback HTTP status is now checked.** New `_post_callback()` helper raises on HTTP status `>= 400`. | Previously `urllib3` does not raise on 4xx/5xx, so a failed delivery was silently treated as success and never retried. |
| 4 | **`execute_task` `finally` guarded.** It no longer calls `dai_task_object.get_output_context()` blindly; if the task object is `None` or has no output context, it reports a failure context instead. | If construction or `execute_task` failed before producing an output context, the `finally` block raised a *second* exception that masked the original error. |
| 5 | **Removed dead status check** (`if response.status_code != 200`) after `raise_for_status()`. | `raise_for_status()` already raises on non-2xx; the follow-up check was dead code and would have wrongly rejected `201`/`204`. |
| 6 | **Task type format validated** before `task_type.split(".")[1]`. | A malformed `type` (no `.`) previously raised an opaque `IndexError`; now it raises a clear `ValueError`. |
| 7 | **`find_class_file` hardened** — skips files that can't be read/parsed (`SyntaxError`, `UnicodeDecodeError`, `OSError`) and reads them as UTF-8. | One unreadable or non-UTF-8 `.py` file anywhere under the CWD previously aborted the entire class search. |
| 8 | **`Optional[...]` type hints** for module globals (`input_context`, `dai_task_object`) and return-type hints added. | The previous `: InputContext = None` annotations lied to type checkers/IDEs. |
| 9 | Removed commented-out `#dai_logger.info(...)` dead lines; simplified redundant `not x or len(x) == 0` to `not x`; documented the intentional double-base64 decode of fetch/callback URLs. | Readability and maintainability. |

## `masked_io.py`

| # | Change | Reason |
|---|--------|--------|
| 1 | `write()` now **returns the number of characters written** (`len(s)`). | `TextIOBase.write` is contractually required to return an int; libraries (e.g. `print`, logging) may rely on it, and returning `None` can raise `TypeError`. |
| 2 | Secrets coerced with `str(secret)` before `replace`. | Defensive: a non-string secret value would otherwise raise inside `str.replace`. |

## `k8s.py`

| # | Change | Reason |
|---|--------|--------|
| 1 | `split_secret_resource_data` now **raises `ValueError`** on empty or malformed input instead of silently returning `("", "", "")`. | The blank tuple only surfaced later as a confusing Kubernetes API error (`read_namespaced_secret("", "")`); failing fast with a clear message is far easier to diagnose. |

## `watcher.py`

| # | Change | Reason |
|---|--------|--------|
| 1 | **Validates `INPUT_CONTEXT_SECRET` / `RUNNER_NAMESPACE`** before building the field selector. | If unset, the old code produced `metadata.name=None` and watched the wrong/empty namespace silently. |
| 2 | Watch stream is **always stopped** via `try/finally: w.stop()`; guards `secret.data` being `None`. | Prevents leaking the long-lived streaming connection and a `NoneType` crash on secrets without data. |

## `base_task.py`

| # | Change | Reason |
|---|--------|--------|
| 1 | `get_task_user()` returns `None` when there is no release context (instead of raising `AttributeError`); return type is now `Optional[...]`. | Tasks without a "Run as user" context could crash with an opaque attribute error. |
| 2 | `_validate_api_credentials()` handles a missing user safely and still raises the existing clear `ValueError`. | Same root cause — a clearer, intentional error message instead of `AttributeError`. |

---

## Tests

### `tests/release/integration/test_base_task.py` — rewritten
- **Fixed a broken import.** The file imported `_find_folder_id` / `_phase_id_from` from `base_task`, which no longer exist (id parsing was refactored into `ids.Ids`). The module failed to even collect (`ImportError`).
- Re-pointed id tests at the current `Ids` API and added coverage for `segment_name` / `parent_id` / `is_root`.
- Added `TestBaseTaskOutput`: success/error exit codes, output-property validation, input-property guard, and the new `get_task_user()` / credential-validation behaviour.

### `tests/release/integration/test_wrapper.py` — rewritten for robustness
- Now **self-contained**: writes the sample input context itself and removes any stale `output.json` in `setUp`.
- Runs the wrapper with an explicit `cwd` and `env` (no longer depends on ambient working directory / global `os.environ` mutation), and uses `sys.executable` instead of bare `python`.
- **Asserts the subprocess exit code** and that `output.json` was produced (the old test ignored the return code, so a crashing wrapper could pass), then compares against the expected output context.

### `tests/release/integration/input.json`
- Updated to the sample `containerExamples.Hello` input context (with `automatedTaskAsUser` set to `admin`/`admin`).

### `tests/release/integration/test_wrapper_k8s.py` — new
End-to-end coverage of the **Kubernetes execution path** (input read from a
Secret, result written to a Secret and pushed to a callback URL) using a fully
mocked Kubernetes client and callback transport — no cluster or network needed.
A blank `session-key` selects the NoOp encryptor so the test stays independent of
AES key material; helpers reproduce the real Secret base64 (and double-base64
URL) encoding.

Cases (11):
- **Input from Secret:** decodes the input context, sets `callback_url`, and registers the "Run as user" password for masking.
- **Fetch-URL fallback:** empty `input` triggers an HTTP fetch — and asserts a `timeout` is passed (regression guard for the robustness fix).
- **Missing fetch URL → `ValueError`.**
- **Secret read failure propagates** out of `get_task_details` (so `run()` reports failure).
- **Result written to Secret + callback pushed** to the correctly decoded URL.
- **Result > 1Mb** skips the Secret write but still pushes the callback.
- **Secret write failure is swallowed and logged** (`update_output_context` never raises) and no callback is attempted.
- **Callback retry:** first push fails → `retry_push_result_infinitely` re-reads the Secret and succeeds.
- **`should_retry_callback_request` matrix:** size × output-file presence (3 cases).

## Verification

```
$ python -m pytest tests/release/integration/
23 passed
```
