# Digital.ai Release Python SDK

The **Digital.ai Release Python SDK** (`digitalai-release-sdk`) provides a set of tools for developers to create container-based integration with Digital.ai Release. It simplifies integration creation by offering built-in functions to interact with the execution environment.

## Features
- Define custom tasks using the `BaseTask` abstract class.
- Subclass `ApiBaseTask` to get every Release v1 API as a cached property (`releaseApi`, `phaseApi`, `taskApi`, ...), all sharing one pre-configured client built from the task's "Run as user" context.
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

## Changelog

### Version 26.3.0 (Beta)

#### ⚠️ Breaking Changes

- **`ReleaseAPIClient` moved to the standalone [`digitalai-release-api-client`](https://pypi.org/project/digitalai-release-api-client/) package** so the API client can be used on its own. The SDK now depends on it and installs it automatically — only the import path changes (class names, method signatures, and behavior are unchanged):

  ```python
  # ❌ Old — bundled inside the SDK
  from digitalai.release.release_api_client import ReleaseAPIClient

  # ✅ New — provided by digitalai-release-api-client
  from com.xebialabs.xlrelease.release_api_client import ReleaseAPIClient
  ```

  `BaseTask.get_release_api_client()` still returns a `ReleaseAPIClient` exactly as before.

#### 🚀 Features

- Added the `ApiBaseTask` base class, exposing every Release v1 API as a lazily created, cached property.
- `get_release_api_client()` now supports optional credentials/server URL and `requests` library arguments.
- Added `get_phase_id()` and `get_folder_id()` helper methods to `BaseTask`.

#### 🛠️ Enhancements

- Improved stability and error handling for API requests and Kubernetes tasks.

---

## 🔗 Related Resources

- 🧪 **Python Template Project**: [release-integration-template-python](https://github.com/digital-ai/release-integration-template-python)  
  A starting point for building custom integrations using Digital.ai Release and Python.

- 📘 **Official Documentation**: [Digital.ai Release Python SDK Docs](https://docs.digital.ai/release/docs/category/python-sdk)  
  Comprehensive guide to using the Python SDK and building custom tasks.

- 📦 **Digital.ai Release Python SDK**: [digitalai-release-sdk on PyPI](https://pypi.org/project/digitalai-release-sdk/)  
  The official SDK package for integrating with Digital.ai Release.


