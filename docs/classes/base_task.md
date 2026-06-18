[🏠 Docs Home](../README.md) › [Base Classes](../README.md#base-classes) › **BaseTask**

# BaseTask

> An abstract base class representing a task that can be executed.

| | |
|---|---|
| **Class** | `BaseTask` |
| **Module** | `digitalai.release.integration.base_task` |
| **Source** | [`digitalai/release/integration/base_task.py`](../../digitalai/release/integration/base_task.py) |
| **Methods** | 18 |

Subclass `BaseTask` to build a container-based integration task. Implement the
abstract [`execute`](#execute) method with your task logic; the Release runtime
calls [`execute_task`](#execute_task), which wraps `execute` with error handling
and exit-code management. Inside `execute` you read the task's input through
[`get_input_properties`](#get_input_properties) (or the `input_properties`
attribute) and report results through `set_output_property`, `add_comment`,
`set_status_line`, and `add_reporting_record`.

For tasks that need to call the Release v1 REST API, subclass
[`ApiBaseTask`](api_base_task.md) instead — it extends `BaseTask` and exposes a
ready-to-use API client.

```python
from digitalai.release.integration import BaseTask


class Hello(BaseTask):

    def execute(self) -> None:
        name = self.input_properties.get("yourName")
        if not name:
            raise ValueError("The 'yourName' field cannot be empty")
        greeting = f"Hello {name}"
        self.add_comment(greeting)
        self.set_output_property("greeting", greeting)
```

---

## Method Index

| Method | Returns | Description |
|--------|---------|-------------|
| [`execute`](#execute) | `None` | Abstract method holding the task's main logic; implemented by subclasses. |
| [`execute_task`](#execute_task) | `None` | Runs `execute` with error handling and exit-code management; called by the runtime. |
| [`abort`](#abort) | `None` | Sets the exit code to 1 and exits the program. |
| [`get_input_properties`](#get_input_properties) | `dict[str, Any]` | Returns the task's input properties. |
| [`set_output_property`](#set_output_property) | `None` | Sets a named output property of the task. |
| [`get_output_properties`](#get_output_properties) | `dict[str, Any]` | Returns the output properties of the task. |
| [`get_output_context`](#get_output_context) | `OutputContext` | Returns the task's `OutputContext`. |
| [`set_exit_code`](#set_exit_code) | `None` | Sets the task's exit code. |
| [`set_error_message`](#set_error_message) | `None` | Sets the task's error message. |
| [`add_comment`](#add_comment) | `None` | Logs a comment shown in the task's comment section in the UI. |
| [`set_status_line`](#set_status_line) | `None` | Sets the status line of the task. |
| [`add_reporting_record`](#add_reporting_record) | `None` | Adds a reporting record to the output context. |
| [`get_release_server_url`](#get_release_server_url) | `str` | Returns the Release server URL of the task. |
| [`get_task_user`](#get_task_user) | `AutomatedTaskAsUserContext \| None` | Returns the "Run as user" details, or `None`. |
| [`get_release_id`](#get_release_id) | `str` | Returns the release id of the task. |
| [`get_task_id`](#get_task_id) | `str` | Returns the task id. |
| [`get_phase_id`](#get_phase_id) | `str` | Returns the phase id, derived from the task id. |
| [`get_folder_id`](#get_folder_id) | `str` | Returns the id of the folder that contains the release. |
| [`get_release_api_client`](#get_release_api_client) | `ReleaseAPIClient` | Builds a `ReleaseAPIClient`, by default from the task context. |

---

## Methods

### `execute`

**Abstract** — must be implemented by subclasses. Holds the main logic of the
task. The Release runtime invokes it through [`execute_task`](#execute_task), so
you normally do not call it yourself.

_No parameters._

**Returns:** _None._

```python
class MyTask(BaseTask):
    def execute(self) -> None:
        ...  # your task logic
```

[↑ Method index](#method-index)

### `execute_task`

Executes the task by calling [`execute`](#execute). If an `AbortException` is
raised during execution, the task's exit code is set to `1` and the program
exits with status `1`. If any other exception is raised, the exit code is set to
`1` and its message is stored as the error message. This is the entry point the
runtime calls.

_No parameters._

**Returns:** _None._

[↑ Method index](#method-index)

### `abort`

Sets the task's exit code to `1` and exits the program with a status code of `1`.

_No parameters._

**Returns:** _None._

[↑ Method index](#method-index)

### `get_input_properties`

Returns the input properties dictionary of the task.

_No parameters._

**Returns:** `dict[str, Any]` — the task's input properties.

**Raises:** `ValueError` — if the input properties have not been set.

[↑ Method index](#method-index)

### `set_output_property`

Sets the name and value of an output property of the task.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | `str` | _required_ | the output property name. Cannot be empty. |
| `value` | `Any` | _required_ | the value to store. Accepted types are `str`, `int`, `list`, `dict`, `bool`. |

**Returns:** _None._

**Raises:** `ValueError` — if `name` is empty, or `value` is not one of the accepted data types.

[↑ Method index](#method-index)

### `get_output_properties`

Returns the output properties dictionary of the task's `OutputContext`.

_No parameters._

**Returns:** `dict[str, Any]` — the output properties set so far.

[↑ Method index](#method-index)

### `get_output_context`

Returns the `OutputContext` object associated with the task.

_No parameters._

**Returns:** `OutputContext` — the task's output context.

[↑ Method index](#method-index)

### `set_exit_code`

Sets the exit code of the task's `OutputContext`.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | `int` | _required_ | the exit code (`0` for success, non-zero for failure). |

**Returns:** _None._

[↑ Method index](#method-index)

### `set_error_message`

Sets the error message of the task's `OutputContext`.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | `str` | _required_ | the error message to record. |

**Returns:** _None._

[↑ Method index](#method-index)

### `add_comment`

Logs a comment for the task. The comment is shown in the task's comment section
in the Release UI.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `comment` | `str` | _required_ | the comment text. |

**Returns:** _None._

[↑ Method index](#method-index)

### `set_status_line`

Sets the status line of the task.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `status_line` | `str` | _required_ | the status text to display. |

**Returns:** _None._

[↑ Method index](#method-index)

### `add_reporting_record`

Adds a reporting record to the task's `OutputContext`.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `reporting_record` | `Any` | _required_ | the reporting record to append. |

**Returns:** _None._

[↑ Method index](#method-index)

### `get_release_server_url`

Returns the Release server URL of the associated task.

_No parameters._

**Returns:** `str` — the Release server URL.

[↑ Method index](#method-index)

### `get_task_user`

Returns the user details that are executing the task (the "Run as user"
context), or `None` when no release context is available.

_No parameters._

**Returns:** `AutomatedTaskAsUserContext \| None` — the task user context, or `None`.

[↑ Method index](#method-index)

### `get_release_id`

Returns the release id of the task.

_No parameters._

**Returns:** `str` — the release identifier.

[↑ Method index](#method-index)

### `get_task_id`

Returns the task id.

_No parameters._

**Returns:** `str` — the task identifier.

[↑ Method index](#method-index)

### `get_phase_id`

Returns the phase id of the task, derived from the task id.

_No parameters._

**Returns:** `str` — the phase identifier.

[↑ Method index](#method-index)

### `get_folder_id`

Returns the id of the folder that contains the release, derived from the release
id.

_No parameters._

**Returns:** `str` — the folder identifier.

[↑ Method index](#method-index)

### `get_release_api_client`

Returns a `ReleaseAPIClient`. All arguments are optional: when omitted, the
client is configured from the task context (server URL and the "Run as user"
credentials). Any argument that is provided overrides the corresponding task
default.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `server_address` | `str` | `None` | Release server URL. Defaults to the task's server URL. |
| `username` | `str` | `None` | username. Defaults to the task user's username. |
| `password` | `str` | `None` | password. Defaults to the task user's password. |
| `personal_access_token` | `str` | `None` | personal access token for authentication. When set, it is used instead of username/password. |
| `timeout` | `float \| tuple[float, float] \| None` | `None` | default timeout (in seconds) applied to every request. Accepts a single float or a `(connect, read)` tuple. Can be overridden per call. |
| `**kwargs` | `Any` | — | additional session parameters (e.g. `headers`, `verify`, `proxies`). |

**Returns:** `ReleaseAPIClient` — a configured client.

**Raises:** `ValueError` — if the server URL, username, or password cannot be resolved (e.g. the "Run as user" property is not set on the release).

> **Tip:** if your task needs the API, subclass [`ApiBaseTask`](api_base_task.md)
> instead of calling this method directly — it builds and caches the client and
> every API wrapper for you.

[↑ Method index](#method-index)

---

[🏠 Docs Home](../README.md) · [Base Classes](../README.md#base-classes) · [Examples](../examples.md)
