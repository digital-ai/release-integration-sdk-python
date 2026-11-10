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

### Version 27.1.0b1

#### 🚀 Features

- Tasks can be aborted. On abort, the SDK calls the task's `abort()` method; long-running tasks can check `is_abort_requested()` and stop early.
- After an abort, the SDK waits briefly (`ABORT_GRACE_PERIOD_SECONDS`, default 3) so the task's outputs and reporting records are still sent.
- Added the `AiUsageRecord` reporting record for AI agent runs (model, tokens, cost and more). Requires a Release version that supports `udm.AiUsageRecord`.

#### 🐛 Fixes

- The task result is no longer cut off if an abort signal arrives while it is being reported.
- Aborted tasks no longer report exit code 0; `sys.exit(n)` now reports exit code `n`.
- Tasks that don't call `super().__init__()` work again.
- `setReleaseVariable()`, `setFolderVariable()` and `setGlobalVariable()` now accept a list for list variables.

