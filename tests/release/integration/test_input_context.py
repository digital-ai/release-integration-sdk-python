import pytest

from digitalai.release.integration.input_context import (
    AutomatedTaskAsUserContext,
    InputContext,
    PropertyDefinition,
    TaskContext,
)
from tests.support import RELEASE_ID, TASK_ID, input_context, task_property


def ci_property(name, properties, *, password=False):
    """A CI-kind property whose value is a nested CI definition."""
    return task_property(name, {"id": f"Configuration/{name}", "type": "test.Server", "properties": properties},
                         kind="CI", password=password)


def task_context(*properties):
    return TaskContext.from_dict({"id": TASK_ID, "type": "x.Task", "properties": list(properties)})


def test_from_dict_reads_release_task_and_run_as_user():
    context = InputContext.from_dict(input_context(username="deployer", password="pw"))

    assert context.release.id == RELEASE_ID
    assert context.release.automated_task_as_user == AutomatedTaskAsUserContext("deployer", "pw")
    assert context.task.id == TASK_ID
    assert context.task.type == "containerExamples.Hello"


def test_run_as_user_defaults_to_empty_when_absent():
    context = InputContext.from_dict({"release": {"id": RELEASE_ID}, "task": {"id": TASK_ID, "type": "x.Y"}})

    assert context.release.automated_task_as_user == AutomatedTaskAsUserContext(None, None)
    assert context.task.properties == []


def test_build_locals_maps_names_to_values():
    task = task_context(task_property("name", "World"), task_property("count", 3, kind="INTEGER"))

    assert task.build_locals() == {"name": "World", "count": 3}


def test_build_locals_unwraps_nested_ci_properties_into_dicts():
    task = task_context(ci_property("server", [
        task_property("url", "http://jenkins"),
        ci_property("proxy", [task_property("host", "proxy.local")]),
    ]))

    assert task.build_locals() == {"server": {"url": "http://jenkins", "proxy": {"host": "proxy.local"}}}


def test_build_locals_keeps_an_empty_ci_value_as_is():
    task = task_context(task_property("server", None, kind="CI"))

    assert task.build_locals() == {"server": None}


def test_output_properties_lists_only_output_category():
    task = task_context(task_property("in", "a"), task_property("out1", None, category="output"),
                        task_property("out2", None, category="output"))

    assert task.output_properties() == ["out1", "out2"]


def test_secrets_collects_password_values_from_task_and_ci_properties():
    task = task_context(
        task_property("token", "t0ken", password=True),
        task_property("user", "admin"),
        ci_property("server", [task_property("password", "srv-pw", password=True), task_property("url", "http://x")]),
    )

    assert task.secrets() == ["t0ken", "srv-pw"]


@pytest.mark.parametrize("value", ["", None])
def test_secrets_skips_empty_passwords(value):
    task = task_context(task_property("token", value, password=True),
                        ci_property("server", [task_property("password", value, password=True)]))

    assert task.secrets() == []


@pytest.mark.xfail(reason="secret_value() does not recurse into a CI nested in a CI property, "
                          "so that password is never masked")
def test_secrets_include_passwords_of_nested_ci_properties():
    prop = PropertyDefinition.from_dict(ci_property("server", [
        ci_property("proxy", [task_property("password", "proxy-pw", password=True)]),
    ]))

    assert prop.secret_value() == ["proxy-pw"]


def test_script_location_returns_the_property_value():
    task = task_context(task_property("scriptLocation", "sample/hello.py"))

    assert task.script_location() == "sample/hello.py"


def test_script_location_is_empty_when_not_set():
    assert task_context(task_property("name", "x")).script_location() == ""
