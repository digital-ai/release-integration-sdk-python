# Development

This project uses [`uv`](https://docs.astral.sh/uv/) for dependency management and packaging.

## Prerequisites

Install uv (see the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/)):

```sh
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Set up a dev environment

```sh
# Installs runtime + dev dependencies into a managed virtual environment
uv sync --extra dev
```

## Build

The wheel packages the `digitalai` tree.

```sh
# Build both sdist and wheel into ./dist
uv build

# Or build a single artifact
uv build --wheel
uv build --sdist
```

## Run tests

```sh
# Run the whole suite
uv run python -m pytest

# Skip the slower subprocess tests, or the tests that need a Release server
uv run python -m pytest -m "not e2e"
uv run python -m pytest -m "not live"
```

Tests are grouped by module under `tests/release/integration/` (`test_<module>.py`), with the
wrapper split into `test_wrapper_io.py`, `test_wrapper_run.py`, `test_wrapper_execute_task.py`,
`test_wrapper_abort.py` and the subprocess runs in `test_wrapper_e2e.py`. Shared ids and input
contexts are in `tests/support.py`; fixtures are in `tests/release/integration/conftest.py`, and
the task classes the wrapper loads in tests are in `tests/release/integration/tasks/`.

Markers:

- `e2e`: runs the wrapper with `python -m` in a subprocess. The two real-`SIGABRT` tests are
  skipped on Windows, which cannot deliver `SIGABRT` to a child process.
- `live`: needs a real server, and is skipped when none is reachable.
  - `test_api_base_task_live.py` creates and deletes a folder, template, release and variables
    on a Release server, by default `http://localhost:5516` as `admin`/`admin`; set
    `RELEASE_LIVE_URL`, `RELEASE_LIVE_USER` and `RELEASE_LIVE_PASSWORD` to use another one.
  - `test_wrapper_k8s_live.py` runs the wrapper's Kubernetes path against a cluster: input and
    result secrets, the callback, the input-context watcher, and a full wrapper run. It uses only
    the kubeconfig context named by `RELEASE_LIVE_K8S_CONTEXT` (default `docker-desktop`, e.g.
    Docker Desktop with Kubernetes enabled), whatever the current context is, and works in a
    temporary `sdk-live-<random>` namespace that it deletes afterwards.

Known bugs are pinned by tests marked `xfail`. `xfail_strict` is on, so when a fix makes such a
test pass, the run fails until the marker is removed.

## Publish to PyPI

```sh
# Publish the distribution (uploads everything in dist/ to PyPI)
uv publish --token <pypi-token>
```

## Dependency management

```sh
# Add a runtime dependency
uv add <package>

# Add a development-only dependency
uv add --dev <package>

# Update the lockfile
uv lock
```
