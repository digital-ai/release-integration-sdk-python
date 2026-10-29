# Digital.ai Release Python SDK

The **Digital.ai Release Python SDK** (`digitalai-release-sdk`) provides a set of tools for developers to create container-based integration with Digital.ai Release. It simplifies integration creation by offering built-in functions to interact with the execution environment.

## Features
- Define custom tasks using the `BaseTask` abstract class.
- Subclass `ApiBaseTask` to access the Release APIs (`releaseApi`, `phaseApi`, `taskApi`, ...) through a ready-to-use client.
- Easily manage input and output properties.
- Interact with the Digital.ai Release environment seamlessly.


## Installation
Install the SDK using `pip`:

```sh
pip install digitalai-release-sdk
```

> **Note:** The SDK depends on [`digitalai-release-api-client`](https://pypi.org/project/digitalai-release-api-client/), which is installed automatically.

## Getting Started

### Example Task: `hello.py`

The following example demonstrates how to create a simple task using the SDK:

```python
from digitalai.release.integration import BaseTask

class Hello(BaseTask):
    
    def execute(self) -> None:
        # Get the name from the input
        name = self.input_properties.get('yourName')
        if not name:
            raise ValueError("The 'yourName' field cannot be empty")

        # Create greeting message
        greeting = f"Hello {name}"

        # Add greeting to the task's comment section in the UI
        self.add_comment(greeting)

        # Store greeting as an output property
        self.set_output_property('greeting', greeting)
```

### Example Task using the Release API: `ApiBaseTask`

Subclass `ApiBaseTask` to call the Release v1 REST API without building a client
yourself. Every API is exposed as a lazily created, cached property, all sharing
a single client built from the task's "Run as user" context:

```python
from digitalai.release.integration.api_base_task import ApiBaseTask


class ShowVersion(ApiBaseTask):

    def execute(self) -> None:
        release = self.releaseApi.getRelease(self.get_release_id())
        self.add_comment(f"Working on {release.title}")
```

## 🔗 Related Resources

- **[Digital.ai Python SDK Documentation](https://docs.digital.ai/release/docs/how-to/overview-python-sdk)**:   
  Comprehensive guide to using the Python SDK and building custom tasks.

- **[SDK Template Project for integration plugins](https://github.com/digital-ai/release-integration-template-python)**:   
  A starting point for building custom integrations using Digital.ai Release and Python.

- **[Digital.ai Release Python SDK](https://pypi.org/project/digitalai-release-sdk/)**:
  The official SDK package for integrating with Digital.ai Release on Pypi. 


## Changelog

### Unreleased

#### 🚀 Features

- Tasks can be aborted: the SDK runs `execute()` on a worker thread and handles `SIGABRT`/`SIGTERM` by calling the task's `abort()` hook. Long-running tasks can poll the new `is_abort_requested()` to stop cooperatively.
- After an abort is requested, the SDK waits up to `ABORT_GRACE_PERIOD_SECONDS` (default 3) for `execute()` to return, so the outputs and reporting records a task sets on its way out are reported.

#### 🐛 Fixes

- A signal received while the task result is being reported no longer cuts off the report; repeat signals during an abort are ignored.
- An aborted result is never reported with exit code 0, and a task calling `sys.exit(n)` is reported with exit code `n`.
- Tasks whose `__init__` does not call `super().__init__()` work again.
- `setReleaseVariable()`, `setFolderVariable()` and `setGlobalVariable()` accept a list for an existing list variable (`xlrelease.ListStringVariable`); it was rejected with a `TypeError` as if the variable held a string.

### Version 26.3.1

#### 🚀 Features

- Added the `ApiBaseTask` base class, exposing every Release v1 API as a lazily created, cached property.
- `get_release_api_client()` now supports optional credentials/server URL and `requests` library arguments.
- Added `get_phase_id()` and `get_folder_id()` helper methods to `BaseTask`.

#### 🛠️ Enhancements

- Improved stability and error handling for API requests and Kubernetes tasks.

