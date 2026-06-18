[🏠 Docs Home](README.md) › **Examples**

# Examples

Task-oriented usage examples for the **Digital.ai Release Python SDK**. Each
snippet defines a task by subclassing [`BaseTask`](classes/base_task.md) or
[`ApiBaseTask`](classes/api_base_task.md) and implementing `execute`. The
Release runtime instantiates your task and calls `execute_task`, which runs
`execute` and handles errors and exit codes for you.

## Contents

- [Define a task with BaseTask](#define-a-task-with-basetask)
- [Read inputs and write outputs](#read-inputs-and-write-outputs)
- [Comments, status line, and reporting](#comments-status-line-and-reporting)
- [Fail or abort a task](#fail-or-abort-a-task)
- [Call the Release API with ApiBaseTask](#call-the-release-api-with-apibasetask)
- [Work with the current task, phase, release, and folder](#work-with-the-current-task-phase-release-and-folder)
- [Manage variables](#manage-variables)
- [Search by title](#search-by-title)
- [Build a client manually](#build-a-client-manually)

---

## Define a task with BaseTask

Subclass [`BaseTask`](classes/base_task.md) and implement the abstract
`execute` method. Input fields configured on the task are available through the
`input_properties` attribute (or [`get_input_properties`](classes/base_task.md#get_input_properties)).

**Classes:** [`BaseTask`](classes/base_task.md)

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

[↑ Contents](#contents)

## Read inputs and write outputs

Read configured input fields and publish results as output properties. Output
values must be one of `str`, `int`, `list`, `dict`, or `bool`. Output properties
are returned to Release and can be consumed by downstream tasks.

**Classes:** [`BaseTask`](classes/base_task.md)

```python
from digitalai.release.integration import BaseTask


class BuildSummary(BaseTask):

    def execute(self) -> None:
        inputs = self.get_input_properties()
        version = inputs["version"]
        artifacts = inputs.get("artifacts", [])

        self.set_output_property("version", version)
        self.set_output_property("artifactCount", len(artifacts))
        self.set_output_property("succeeded", True)
```

[↑ Contents](#contents)

## Comments, status line, and reporting

Surface progress to the Release UI: `add_comment` writes to the task's comment
section, `set_status_line` updates the one-line status, and
`add_reporting_record` attaches a reporting record to the output context.

**Classes:** [`BaseTask`](classes/base_task.md)

```python
from digitalai.release.integration import BaseTask


class Deploy(BaseTask):

    def execute(self) -> None:
        self.set_status_line("Deploying…")
        self.add_comment("Starting deployment to **prod**")

        # ... do the work ...

        self.set_status_line("Deployed")
        self.add_comment("Deployment finished successfully")
```

[↑ Contents](#contents)

## Fail or abort a task

Raising an exception from `execute` fails the task: `execute_task` records the
message and sets a non-zero exit code. To stop immediately, call `abort`, which
sets the exit code to `1` and exits the process.

**Classes:** [`BaseTask`](classes/base_task.md)

```python
from digitalai.release.integration import BaseTask


class GuardedTask(BaseTask):

    def execute(self) -> None:
        if not self.input_properties.get("confirmed"):
            # Fails the task with this message shown in Release
            raise ValueError("Task was not confirmed")

        if self.input_properties.get("cancel"):
            # Stop right away
            self.abort()

        self.add_comment("Proceeding")
```

[↑ Contents](#contents)

## Call the Release API with ApiBaseTask

Subclass [`ApiBaseTask`](classes/api_base_task.md) to call the Release v1 REST
API without building a client yourself. Every API is exposed as a lazily
created, cached property (`releaseApi`, `taskApi`, …), all sharing a single
client built from the task's "Run as user" context.

**Classes:** [`ApiBaseTask`](classes/api_base_task.md)

```python
from digitalai.release.integration.api_base_task import ApiBaseTask


class ShowVersion(ApiBaseTask):

    def execute(self) -> None:
        release = self.releaseApi.getRelease(self.get_release_id())
        self.add_comment(f"Working on {release.title}")

        version = self.getVersion()
        self.set_output_property("releaseVersion", version)
```

[↑ Contents](#contents)

## Work with the current task, phase, release, and folder

The current-context helpers resolve the objects the task is running in, so you
do not have to derive ids yourself.

**Classes:** [`ApiBaseTask`](classes/api_base_task.md)

```python
from digitalai.release.integration.api_base_task import ApiBaseTask


class Context(ApiBaseTask):

    def execute(self) -> None:
        task = self.getCurrentTask()
        phase = self.getCurrentPhase()
        release = self.getCurrentRelease()
        folder = self.getCurrentFolder()

        self.add_comment(
            f"Task '{task.title}' in phase '{phase.title}' "
            f"of release '{release.title}' (folder '{folder.title}')"
        )
```

[↑ Contents](#contents)

## Manage variables

Read and write release, folder, and global variables by name. Folder and global
names must include their `folder.` / `global.` prefix. When a variable does not
exist yet, the `set…` helpers create it, inferring the variable type from the
value.

**Classes:** [`ApiBaseTask`](classes/api_base_task.md)

```python
from digitalai.release.integration.api_base_task import ApiBaseTask


class Variables(ApiBaseTask):

    def execute(self) -> None:
        # Release variables (bare name)
        build = self.getReleaseVariable("JenkinsBuildNumber")
        self.setReleaseVariable("JenkinsBuildNumber", build + 1)

        # Folder variables (require the 'folder.' prefix)
        owner = self.getFolderVariable("folder.owner")
        self.setFolderVariable("folder.owner", owner)

        # Global variables (require the 'global.' prefix)
        self.setGlobalVariable("global.lastRunBy", "release-bot")
```

[↑ Contents](#contents)

## Search by title

Find tasks, phases, and releases by title.

**Classes:** [`ApiBaseTask`](classes/api_base_task.md)

```python
from digitalai.release.integration.api_base_task import ApiBaseTask


class Search(ApiBaseTask):

    def execute(self) -> None:
        # Tasks in the current release, optionally scoped to a phase
        deploys = self.getTasksByTitle("Deploy", phaseTitle="Production")

        # Phases in the current release
        phases = self.getPhasesByTitle("Production")

        # Releases by title across the instance
        releases = self.getReleasesByTitle("Nightly")

        self.add_comment(
            f"Found {len(deploys)} tasks, {len(phases)} phases, "
            f"{len(releases)} releases"
        )
```

[↑ Contents](#contents)

## Build a client manually

You can also build a `ReleaseAPIClient` directly from a `BaseTask` with
[`get_release_api_client`](classes/base_task.md#get_release_api_client). With no
arguments it uses the task context; pass arguments to override the server URL or
credentials (e.g. to authenticate with a personal access token, or to call a
different server).

**Classes:** [`BaseTask`](classes/base_task.md)

```python
from digitalai.release.integration import BaseTask


class CustomClient(BaseTask):

    def execute(self) -> None:
        # Default: server URL + 'Run as user' credentials from the task context
        client = self.get_release_api_client()

        # Override: a different server with a personal access token and a timeout
        other = self.get_release_api_client(
            server_address="https://release.example.com",
            personal_access_token="your-token-here",
            timeout=(5, 30),  # (connect, read) seconds
        )
        ...
```

[↑ Contents](#contents)

---

[🏠 Docs Home](README.md) · [Base Classes](README.md#base-classes)
