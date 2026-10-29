"""
Fixtures shared by the integration tests.

Importing ``wrapper`` has process-wide side effects: it replaces sys.stdout and
sys.stderr with MaskedIO streams, installs SIGTERM/SIGABRT handlers, and reads
its settings from environment variables once. Tests that use the wrapper
in-process therefore go through ``isolated_wrapper``, which pins those
settings so the developer's environment cannot change a test's outcome, and
resets the per-execution state the wrapper keeps in module globals.
"""
import shutil
import sys
from pathlib import Path

import pytest

import digitalai.release.integration.wrapper as wrapper
from digitalai.release.integration.logger import dai_logger

TASKS_DIR = Path(__file__).parent / "tasks"

# Module globals the wrapper initialises from environment variables at import.
_WRAPPER_SETTINGS = (
    "input_context_file",
    "output_context_file",
    "base64_session_key",
    "release_server_url",
    "callback_url",
    "input_context_secret",
    "result_secret_key",
    "runner_namespace",
    "execution_mode",
)


@pytest.fixture
def isolated_wrapper(monkeypatch):
    """The wrapper module with blank settings and fresh per-execution state."""
    for name in _WRAPPER_SETTINGS:
        monkeypatch.setattr(wrapper, name, "")
    monkeypatch.setattr(wrapper, "input_context", None)
    monkeypatch.setattr(wrapper, "dai_task_object", None)
    monkeypatch.setattr(wrapper.masked_std_out, "secrets", [])
    monkeypatch.setattr(wrapper.masked_std_err, "secrets", [])
    wrapper._reset_report_guard()
    yield wrapper
    wrapper._reset_report_guard()


@pytest.fixture
def reported(isolated_wrapper, monkeypatch):
    """Every OutputContext the wrapper reports, captured instead of sent."""
    contexts = []
    monkeypatch.setattr(wrapper, "update_output_context", contexts.append)
    return contexts


@pytest.fixture
def exit_codes(isolated_wrapper, monkeypatch):
    """Codes passed to os._exit(), which is replaced so the test runner survives."""
    codes = []
    monkeypatch.setattr(wrapper.os, "_exit", codes.append)
    return codes


@pytest.fixture
def dai_log(caplog):
    """caplog wired to dai_logger, which does not propagate to the root logger."""
    dai_logger.addHandler(caplog.handler)
    yield caplog
    dai_logger.removeHandler(caplog.handler)


def make_task_workspace(workspace: Path) -> Path:
    """
    Fills ``workspace`` as a runner working directory with the fixture tasks
    under ``src/``, laid out the way a task image is: ``scriptLocation`` paths
    resolve against ``src/``.
    """
    shutil.copytree(TASKS_DIR, workspace / "src", ignore=shutil.ignore_patterns("__pycache__"))
    return workspace


@pytest.fixture
def task_workspace(tmp_path):
    return make_task_workspace(tmp_path / "workspace")


@pytest.fixture
def importable_workspace(task_workspace, monkeypatch):
    """
    task_workspace as the current directory and on sys.path, so wrapper.run()
    can import fixture tasks in-process. The ``src`` modules it imports are
    dropped afterwards so the next test's workspace is imported afresh.
    """
    def drop_src_modules():
        for name in [m for m in sys.modules if m == "src" or m.startswith("src.")]:
            del sys.modules[name]

    drop_src_modules()
    monkeypatch.chdir(task_workspace)
    monkeypatch.syspath_prepend(str(task_workspace))
    yield task_workspace
    drop_src_modules()
