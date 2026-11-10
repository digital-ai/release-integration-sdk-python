"""
wrapper.run(): locating and importing the task class, wiring the task context,
and reporting setup failures. Runs in-process against the fixture tasks in
tasks/, copied to a temporary runner directory (see ``importable_workspace``).
"""
import json
import os
from unittest import mock

import pytest

from digitalai.release.integration.output_context import OutputContext
from tests.support import RELEASE_ID, TASK_ID, input_context, task_property


@pytest.fixture
def run_task(isolated_wrapper, importable_workspace, reported, monkeypatch, tmp_path):
    """Runs the wrapper on an input context and returns the single reported result."""
    input_path = tmp_path / "input.json"
    monkeypatch.setattr(isolated_wrapper, "input_context_file", str(input_path))

    def run(context, *, release_url="http://localhost:5516"):
        monkeypatch.setattr(isolated_wrapper, "release_server_url", release_url)
        input_path.write_text(json.dumps(context))
        isolated_wrapper.run()
        (result,) = reported
        return result

    return run


def hello_context(script_location=None, task_type="containerExamples.Hello"):
    properties = [task_property("yourName", "World")]
    if script_location is not None:
        properties.append(task_property("scriptLocation", script_location))
    return input_context(task_type, properties)


def test_finds_the_task_class_by_name_without_a_script_location(run_task):
    assert run_task(hello_context()) == OutputContext(0, "", {"greeting": "Hello World"}, [])


@pytest.mark.parametrize("script_location", ["sample/hello.py", "/sample/hello.py", "sample\\hello.py"],
                         ids=["relative", "leading-slash", "backslash"])
def test_loads_the_task_class_from_the_script_location(run_task, script_location):
    result = run_task(hello_context(script_location))

    assert result.output_properties == {"greeting": "Hello World from sample"}


def test_wires_the_task_context_into_the_task(run_task):
    context = input_context("containerExamples.ContextEcho", [task_property("yourName", "World")],
                            username="deployer", password="pw")

    result = run_task(context, release_url="http://release:5516/")

    assert result == OutputContext(0, "", {
        "serverUrl": "http://release:5516",
        "releaseId": RELEASE_ID,
        "taskId": TASK_ID,
        "username": "deployer",
        "inputs": {"yourName": "World"},
    }, [])


def test_reports_a_failing_task_as_failed(run_task):
    result = run_task(input_context("containerExamples.FailingTask", []))

    assert result == OutputContext(1, "Deployment target unreachable", {}, [])


@pytest.mark.parametrize("context, message", [
    (hello_context(task_type="Hello"),
     "Invalid task type 'Hello', expected format '<prefix>.<ClassName>'"),
    (hello_context(task_type="containerExamples.Missing"),
     "Could not find the 'Missing' class"),
    (hello_context("sample/missing.py"),
     f"Script file not found at: {os.path.join('src', 'sample', 'missing.py')}"),
    (hello_context("sample/hello.py", task_type="containerExamples.ContextEcho"),
     f"Class 'ContextEcho' not found in script file: {os.path.join('src', 'sample', 'hello.py')}"),
], ids=["type-without-prefix", "class-not-found", "script-not-found", "class-not-in-script"])
def test_setup_failure_is_reported_as_failed(run_task, context, message):
    result = run_task(context)

    assert result == OutputContext(1, message, {}, [])


def test_unreadable_input_is_reported_as_failed(isolated_wrapper, reported, monkeypatch, tmp_path):
    monkeypatch.setattr(isolated_wrapper, "input_context_file", str(tmp_path / "missing.json"))

    isolated_wrapper.run()

    (result,) = reported
    assert result.exit_code == 1
    assert "missing.json" in result.job_error_message


@pytest.mark.parametrize("mode, watches", [("daemon", True), ("", False)], ids=["daemon", "single-run"])
def test_daemon_mode_watches_for_the_next_input_after_running(isolated_wrapper, run_task, monkeypatch, mode,
                                                              watches):
    monkeypatch.setattr(isolated_wrapper, "execution_mode", mode)
    start_watcher = mock.Mock()
    monkeypatch.setattr(isolated_wrapper.watcher, "start_input_context_watcher", start_watcher)

    run_task(hello_context())

    if watches:
        start_watcher.assert_called_once_with(isolated_wrapper.run)
    else:
        start_watcher.assert_not_called()


# -- find_class_file -------------------------------------------------------

def test_find_class_file_finds_a_top_level_class_in_a_nested_module(isolated_wrapper, tmp_path):
    module = tmp_path / "pkg" / "deep" / "tasks.py"
    module.parent.mkdir(parents=True)
    module.write_text("class Helper:\n    pass\n\nclass Deploy:\n    pass\n")

    assert isolated_wrapper.find_class_file(str(tmp_path), "Deploy") == str(module)


def test_find_class_file_ignores_nested_classes_and_non_python_files(isolated_wrapper, tmp_path):
    (tmp_path / "outer.py").write_text("class Outer:\n    class Deploy:\n        pass\n")
    (tmp_path / "notes.txt").write_text("class Deploy:\n    pass\n")

    assert isolated_wrapper.find_class_file(str(tmp_path), "Deploy") is None


def test_find_class_file_skips_files_it_cannot_parse(isolated_wrapper, tmp_path):
    (tmp_path / "a_broken.py").write_text("class Broken(:\n")
    (tmp_path / "b_binary.py").write_bytes(b"\xff\xfe\x00 not utf-8")
    (tmp_path / "c_task.py").write_text("class Deploy:\n    pass\n")

    assert isolated_wrapper.find_class_file(str(tmp_path), "Deploy") == str(tmp_path / "c_task.py")
