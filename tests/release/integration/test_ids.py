import pytest

from digitalai.release.integration.ids import Ids
from tests.support import FOLDER_ID, PHASE_ID, RELEASE_ID, TASK_ID


@pytest.mark.parametrize("object_id, expected", [
    (TASK_ID, "Task3a35b67b42b6428b854857fba470b39a"),
    ("Applications", "Applications"),
])
def test_segment_name_is_the_last_path_segment(object_id, expected):
    assert Ids.segment_name(object_id) == expected


def test_parent_id_drops_the_last_segment():
    assert Ids.parent_id(TASK_ID) == PHASE_ID


@pytest.mark.parametrize("object_id, expected", [
    ("Applications", True),
    (RELEASE_ID, False),
])
def test_is_root_is_true_only_without_a_separator(object_id, expected):
    assert Ids.is_root(object_id) is expected


@pytest.mark.parametrize("object_id", [
    TASK_ID,
    f"{PHASE_ID}/TaskGroup1/Task2",
    PHASE_ID,
], ids=["task", "task-in-group", "phase-itself"])
def test_phase_id_from_finds_the_enclosing_phase(object_id):
    assert Ids.phase_id_from(object_id) == PHASE_ID


@pytest.mark.parametrize("object_id", [RELEASE_ID, "Task1"])
def test_phase_id_from_raises_when_no_phase_in_path(object_id):
    with pytest.raises(ValueError, match="No phase found"):
        Ids.phase_id_from(object_id)


@pytest.mark.parametrize("object_id, expected", [
    (RELEASE_ID, FOLDER_ID),
    (f"{FOLDER_ID}/Folder2/Release1", f"{FOLDER_ID}/Folder2"),
    ("Applications/Release1", "Applications"),
], ids=["release-in-folder", "nested-folder", "release-at-root"])
def test_find_folder_id_finds_the_nearest_folder(object_id, expected):
    assert Ids.find_folder_id(object_id) == expected
