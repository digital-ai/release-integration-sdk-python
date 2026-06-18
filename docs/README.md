# Digital.ai Release Python SDK — Documentation

Reference documentation for the **Digital.ai Release Python SDK**
(`digitalai-release-sdk`) — the toolkit for building container-based
integration tasks for Digital.ai Release. You define a task by subclassing a
base class and implementing `execute`; the SDK provides built-in helpers to read
inputs, write outputs, report progress, and call the Release REST API.

## Examples

New here? See **[Examples](examples.md)** for task-oriented, copy-pasteable
snippets covering defining tasks, handling inputs/outputs, and calling the
Release API.

## Base Classes

Subclass one of these to build a task. `ApiBaseTask` extends `BaseTask`, adding
ready-to-use Release API access.

| Name | Description | Documentation |
|------|-------------|---------------|
| `BaseTask` | Abstract base class for a task that can be executed. Implement `execute` and use the input/output and reporting helpers. | [classes/base_task.md](classes/base_task.md) |
| `ApiBaseTask` | Extends `BaseTask` with a ready-to-use, cached client and every `com.xebialabs.xlrelease.api.v1` wrapper exposed as a property. | [classes/api_base_task.md](classes/api_base_task.md) |

## Related

- **[Release API Python Client](https://pypi.org/project/digitalai-release-api-client/)** — the API wrappers (`releaseApi`, `taskApi`, …) and domain models (`Task`, `Release`, `Variable`, …) returned by [`ApiBaseTask`](classes/api_base_task.md) are provided by this dependency, installed automatically with the SDK.
- **[Python SDK Documentation](https://docs.digital.ai/release/docs/how-to/overview-python-sdk)** — guide to using the SDK and building custom tasks.
- **[Integration Template Project](https://github.com/digital-ai/release-integration-template-python)** — a starting point for building custom integrations.
