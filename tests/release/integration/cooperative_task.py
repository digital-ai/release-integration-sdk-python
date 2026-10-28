import time

from digitalai.release.integration import BaseTask


class CooperativeTask(BaseTask):
    """
    Fixture task used by test_wrapper_abort.py to verify that a task polling
    is_abort_requested() can stop within the abort grace period and have the
    outputs it sets on the way out reported.
    """

    def execute(self) -> None:
        processed = 0
        while not self.is_abort_requested():
            processed += 1
            time.sleep(0.05)
        self.set_output_property("stoppedCooperatively", True)
        self.add_reporting_record({"processed": processed})
