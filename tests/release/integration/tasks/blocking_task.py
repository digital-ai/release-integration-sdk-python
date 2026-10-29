import time
from pathlib import Path

from digitalai.release.integration import BaseTask


class BlockingTask(BaseTask):
    """
    Blocks without polling is_abort_requested(), so an abort can only end it by
    reporting after the grace period. Creates the ``task_started`` file once
    execute() runs, so a test knows when it is safe to signal.
    """

    def execute(self) -> None:
        Path("task_started").touch()
        time.sleep(30)
