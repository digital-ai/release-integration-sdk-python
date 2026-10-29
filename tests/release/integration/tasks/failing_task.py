from digitalai.release.integration import BaseTask


class FailingTask(BaseTask):
    def execute(self) -> None:
        raise ValueError("Deployment target unreachable")
