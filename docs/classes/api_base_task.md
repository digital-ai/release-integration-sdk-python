[🏠 Docs Home](../README.md) › [Base Classes](../README.md#base-classes) › **ApiBaseTask**

# ApiBaseTask

> Base class for Release container tasks that need the v1 REST API.

| | |
|---|---|
| **Class** | `ApiBaseTask` |
| **Extends** | [`BaseTask`](base_task.md) |
| **Module** | `digitalai.release.integration.api_base_task` |
| **Source** | [`digitalai/release/integration/api_base_task.py`](../../digitalai/release/integration/api_base_task.py) |
| **Properties** | 31 |
| **Methods** | 16 |

Subclass `ApiBaseTask` instead of [`BaseTask`](base_task.md) to get a
ready-to-use, lazily created instance of every `com.xebialabs.xlrelease.api.v1`
wrapper as a property (`releaseApi`, `phaseApi`, `taskApi`, …). All wrappers
share a single, pre-configured `ReleaseAPIClient` built from the task's "Run as
user" context (credentials + server URL), so the client and each API object are
created only once, and only when first accessed.

Because it extends `BaseTask`, every method and attribute documented in
[BaseTask](base_task.md) is also available here.

```python
from digitalai.release.integration.api_base_task import ApiBaseTask


class MyTask(ApiBaseTask):
    def execute(self) -> None:
        release = self.releaseApi.getRelease(self.get_release_id())
        self.add_comment(f"Working on {release.title}")
```

> **Note:** The API wrappers and the domain models they return (`Task`, `Phase`,
> `Release`, `Folder`, `Variable`, …) are provided by the
> [`digitalai-release-api-client`](https://pypi.org/project/digitalai-release-api-client/)
> package, which the SDK depends on.

---

## API Properties

Each property returns a cached API wrapper, created on first access and bound to
the shared [`apiClient`](#apiclient). See the API client reference for the
methods each wrapper exposes.

| Property | Type | Description |
|----------|------|-------------|
| [`apiClient`](#apiclient) | `ReleaseAPIClient` | The shared client, created on first access from the task context. |
| `activityLogsApi` | `ActivityLogsApi` | Operations on activity logs. |
| `applicationApi` | `ApplicationApi` | Operations on applications. |
| `archiveApi` | `ArchiveApi` | Operations on archived releases. |
| `attachmentApi` | `AttachmentApi` | Operations on attachments. |
| `categoryApi` | `CategoryApi` | Operations on categories. |
| `configurationApi` | `ConfigurationApi` | Operations on shared configurations and global variables. |
| `deliveryApi` | `DeliveryApi` | Operations on deliveries. |
| `deliveryPatternApi` | `DeliveryPatternApi` | Operations on delivery patterns. |
| `dslApi` | `DslApi` | Operations with release DSL. |
| `environmentApi` | `EnvironmentApi` | Operations on environments. |
| `environmentLabelApi` | `EnvironmentLabelApi` | Operations on environment labels. |
| `environmentReservationApi` | `EnvironmentReservationApi` | Operations on environment reservations. |
| `environmentStageApi` | `EnvironmentStageApi` | Operations on environment stages. |
| `folderApi` | `FolderApi` | Operations on folders. |
| `folderVersioningApi` | `FolderVersioningApi` | Operations to store and synchronize folder contents. |
| `permissionsApi` | `PermissionsApi` | Operations on permissions. |
| `phaseApi` | `PhaseApi` | Operations on phases. |
| `releaseApi` | `ReleaseApi` | Operations on releases. |
| `reportApi` | `ReportApi` | Operations on reports. |
| `riskApi` | `RiskApi` | Operations on risk. |
| `rolesApi` | `RolesApi` | Operations on roles. |
| `searchApi` | `SearchApi` | Search operations across releases and templates. |
| `settingsApi` | `SettingsApi` | Operations on global settings. |
| `taskApi` | `TaskApi` | Operations on tasks. |
| `taskReportingApi` | `TaskReportingApi` | Operations on task reporting records. |
| `teamApi` | `TeamApi` | Operations on teams across releases, templates, and folders. |
| `templateApi` | `TemplateApi` | Operations on templates. |
| `triggersApi` | `TriggersApi` | Operations on triggers. |
| `userApi` | `UserApi` | Operations on users. |
| `variableApi` | `VariableApi` | Operations on variables across releases, templates, and folders. |

### `apiClient`

The shared `ReleaseAPIClient`, created on first access. Built from the task's
"Run as user" context (server URL + credentials) via
[`get_release_api_client`](base_task.md#get_release_api_client). Every API
wrapper property is bound to this same client.

**Type:** `ReleaseAPIClient`

[↑ API properties](#api-properties)

---

## Method Index

| Method | Returns | Description |
|--------|---------|-------------|
| [`getCurrentTask`](#getcurrenttask) | `Task` | Returns the task that is running this code. |
| [`getCurrentPhase`](#getcurrentphase) | `Phase` | Returns the phase that contains this task. |
| [`getCurrentRelease`](#getcurrentrelease) | `Release` | Returns the release this task belongs to. |
| [`getCurrentFolder`](#getcurrentfolder) | `Folder` | Returns the folder that contains the current release. |
| [`getReleaseVariable`](#getreleasevariable) | `Any` | Returns the value of a variable in the current release by name. |
| [`setReleaseVariable`](#setreleasevariable) | `Variable` | Sets the value of a variable in the current release by name. |
| [`getFolderVariable`](#getfoldervariable) | `Any` | Returns the value of a variable in the current folder by name. |
| [`setFolderVariable`](#setfoldervariable) | `Variable` | Sets the value of a variable owned by the current folder by name. |
| [`getGlobalVariable`](#getglobalvariable) | `Any` | Returns the value of a global variable by name. |
| [`setGlobalVariable`](#setglobalvariable) | `Variable` | Sets the value of a global variable by name. |
| [`getTasksByTitle`](#gettasksbytitle) | `list[Task]` | Finds tasks by title. |
| [`getPhasesByTitle`](#getphasesbytitle) | `list[Phase]` | Finds phases by title. |
| [`getReleasesByTitle`](#getreleasesbytitle) | `list[Release]` | Finds releases by title. |
| [`getVersion`](#getversion) | `str \| None` | Returns the version of this Digital.ai Release instance. |
| [`reset_api_clients`](#reset_api_clients) | `None` | Drops the cached client and API instances. |

---

## Methods

### `getCurrentTask`

Returns the task that is running this code. Fetches the task via `taskApi` using
the task's own id.

_No parameters._

**Returns:** `Task` — the current task.

[↑ Method index](#method-index)

### `getCurrentPhase`

Returns the phase that contains this task. The phase id is derived from the task
id, then fetched via `phaseApi`.

_No parameters._

**Returns:** `Phase` — the current phase.

[↑ Method index](#method-index)

### `getCurrentRelease`

Returns the release this task belongs to. Fetches the release via `releaseApi`
using the task's release id, so the caller does not need to know or substitute
the id itself.

_No parameters._

**Returns:** `Release` — the current release.

[↑ Method index](#method-index)

### `getCurrentFolder`

Returns the folder that contains the current release. The folder id is derived
from the release id, then fetched via `folderApi`.

_No parameters._

**Returns:** `Folder` — the current folder.

[↑ Method index](#method-index)

### `getReleaseVariable`

Returns the value of a variable in the current release by name. The Python3
equivalent of the Jython script global `releaseVariables[name]`. Pass the bare
variable name; the variable is looked up by its `key` and its stored value is
returned as-is.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | `str` | _required_ | the variable name (e.g. `"JenkinsBuildNumber"`). |

**Returns:** `Any` — the variable's value.

**Raises:** `KeyError` — if the release has no variable with that name.

[↑ Method index](#method-index)

### `setReleaseVariable`

Sets the value of a variable in the current release by name. The Python3
equivalent of the Jython script assignment `releaseVariables[name] = value`. If
the variable exists its value is updated; otherwise a new variable is created,
with its type inferred from `value`.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | `str` | _required_ | the variable name (e.g. `"JenkinsBuildNumber"`). |
| `value` | `Any` | _required_ | the new value to assign. |

**Returns:** `Variable` — the updated (or newly created) variable.

[↑ Method index](#method-index)

### `getFolderVariable`

Returns the value of a variable in the current folder by name. Like
[`getReleaseVariable`](#getreleasevariable), but scoped to the folder that
contains the current release. Inherited variables (from parent folders and
global variables) are included. The `folder.` prefix is required — pass the
fully qualified name (e.g. `"folder.foo"`).

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | `str` | _required_ | the variable name, including the `folder.` prefix. |

**Returns:** `Any` — the variable's value.

**Raises:** `ValueError` — if `name` does not start with `folder.`; `KeyError` — if no such variable is visible to the folder.

[↑ Method index](#method-index)

### `setFolderVariable`

Sets the value of a variable owned by the current folder by name. Only variables
the folder owns are matched: an inherited variable (defined on a parent folder
or as a global variable) is not. If the folder owns the variable its value is
updated; otherwise a new folder-owned variable is created (which shadows any
inherited value of the same name). The `folder.` prefix is required.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | `str` | _required_ | the variable name, including the `folder.` prefix. |
| `value` | `Any` | _required_ | the new value to assign. |

**Returns:** `Variable` — the updated (or newly created) variable.

**Raises:** `ValueError` — if `name` does not start with `folder.`.

[↑ Method index](#method-index)

### `getGlobalVariable`

Returns the value of a global variable by name. Global variables are stored with
a `global.` prefix, which is required here — pass the fully qualified name (e.g.
`"global.foo"`).

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | `str` | _required_ | the global variable name, including the `global.` prefix. |

**Returns:** `Any` — the variable's value.

**Raises:** `ValueError` — if `name` does not start with `global.`; `KeyError` — if no global variable with that name exists.

[↑ Method index](#method-index)

### `setGlobalVariable`

Sets the value of a global variable by name. The `global.` prefix is required.
If the variable exists its value is updated; otherwise a new global variable is
created, with its type inferred from `value`. The task's run-as user must hold
the permission to edit global variables.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `name` | `str` | _required_ | the global variable name, including the `global.` prefix. |
| `value` | `Any` | _required_ | the new value to assign. |

**Returns:** `Variable` — the updated (or newly created) variable.

**Raises:** `ValueError` — if `name` does not start with `global.`.

[↑ Method index](#method-index)

### `getTasksByTitle`

Finds tasks by title.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `taskTitle` | `str` | _required_ | the task title to search for. |
| `phaseTitle` | `str \| None` | `None` | optional phase title to scope the search; searches the whole release when omitted. |
| `releaseId` | `str \| None` | `None` | optional release to search; the current release when omitted. |

**Returns:** `list[Task]` — the matching tasks.

[↑ Method index](#method-index)

### `getPhasesByTitle`

Finds phases by title.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `phaseTitle` | `str` | _required_ | the phase title to search for. |
| `releaseId` | `str \| None` | `None` | optional release to search; the current release when omitted. |

**Returns:** `list[Phase]` — the matching phases.

[↑ Method index](#method-index)

### `getReleasesByTitle`

Finds releases by title.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `releaseTitle` | `str` | _required_ | the release title to search for. |

**Returns:** `list[Release]` — the matching releases.

[↑ Method index](#method-index)

### `getVersion`

Returns the version of this Digital.ai Release instance.

_No parameters._

**Returns:** `str \| None` — the instance version, or `None` if unavailable.

[↑ Method index](#method-index)

### `reset_api_clients`

Drops the cached client and API instances (e.g. to re-authenticate). The next
access to [`apiClient`](#apiclient) or any API wrapper property rebuilds them.

_No parameters._

**Returns:** _None._

[↑ Method index](#method-index)

---

[🏠 Docs Home](../README.md) · [Base Classes](../README.md#base-classes) · [Examples](../examples.md)
