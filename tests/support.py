"""Shared test data: realistic Release ids, input contexts and a minimal task."""
from __future__ import annotations

from typing import Any, Dict, List, Optional

from digitalai.release.integration import BaseTask

FOLDER_ID = "Applications/Folder1f65c7220b394afbb941154342fd9fc6"
RELEASE_ID = f"{FOLDER_ID}/Release31de09e95c8e4ebb95aaed29a8082d0b"
PHASE_ID = f"{RELEASE_ID}/Phase723a601c78804f7dbcaa8b05b83708f5"
TASK_ID = f"{PHASE_ID}/Task3a35b67b42b6428b854857fba470b39a"

SERVER_URL = "http://localhost:5516"


class NoOpTask(BaseTask):
    """Smallest concrete BaseTask; execute() does nothing."""

    def execute(self) -> None:
        pass


def task_property(name: str, value: Any, *, kind: str = "STRING", category: str = "input",
                  password: bool = False) -> Dict[str, Any]:
    """One entry of the ``task.properties`` list in an input context."""
    return {"name": name, "value": value, "kind": kind, "category": category, "password": password}


def input_context(task_type: str = "containerExamples.Hello",
                  properties: Optional[List[Dict[str, Any]]] = None, *,
                  username: Optional[str] = "admin",
                  password: Optional[str] = "admin") -> Dict[str, Any]:
    """An input context as the Release server sends it to a container task."""
    if properties is None:
        properties = [
            task_property("yourName", "World"),
            task_property("greeting", None, category="output"),
        ]
    return {
        "release": {
            "id": RELEASE_ID,
            "automatedTaskAsUser": {"username": username, "password": password},
        },
        "task": {"id": TASK_ID, "type": task_type, "properties": properties},
    }
