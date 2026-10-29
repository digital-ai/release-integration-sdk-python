import time
from pathlib import Path

from digitalai.release.integration import BaseTask


class CooperativeTask(BaseTask):
    """
    Polls is_abort_requested() and records outputs on the way out, which the
    wrapper must report. Creates the ``task_started`` file after its first loop
    pass, so once a test sees the file, at least one pass has been counted.
    """

    def execute(self) -> None:
        processed = 0
        while not self.is_abort_requested():
            processed += 1
            if processed == 1:
                Path("task_started").touch()
            time.sleep(0.05)
        self.set_output_property("stoppedCooperatively", True)
        self.add_reporting_record({"processed": processed})
