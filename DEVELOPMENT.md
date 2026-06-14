# Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and packaging.

## Prerequisites

Install uv (see the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/)):

```sh
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Common tasks

```sh
# Install dependencies (creates a virtual environment and installs dev tools)
uv sync

# Run the tests
cd tests/release/integration
uv run python -m unittest test_wrapper.py

# Build the distribution
uv build
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
