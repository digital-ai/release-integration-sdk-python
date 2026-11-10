import sys
from pathlib import Path

from digitalai.release.integration import BaseTask


class StderrFloodTask(BaseTask):
    """
    Writes to stderr without end and ignores the abort. With a stderr pipe that
    nobody reads, the write blocks once the pipe is full, holding the stream's
    lock. Creates the ``task_started`` file once execute() runs.
    """

    def execute(self) -> None:
        Path("task_started").touch()
        while True:
            sys.stderr.write("x" * 1024 + "\n")
