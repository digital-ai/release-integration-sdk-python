import time

from digitalai.release.integration import BaseTask


class BlockingTask(BaseTask):
    """
    Fixture task used by test_wrapper_abort.py to verify that SIGABRT interrupts
    a task promptly even while it is blocked in an uninterruptible call (i.e.
    without polling is_abort_requested()).
    """

    def execute(self) -> None:
        time.sleep(30)
