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
# Run the tests
cd tests/release/integration
uv run python -m unittest test_wrapper.py
```

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
