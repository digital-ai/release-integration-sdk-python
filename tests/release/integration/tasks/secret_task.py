from digitalai.release.integration import BaseTask, dai_logger


class SecretTask(BaseTask):
    """Writes its password input and the run-as-user password through every output channel."""

    def execute(self) -> None:
        token = self.input_properties["token"]
        run_as_password = self.get_task_user().password
        print(f"print: {token} {run_as_password}")
        dai_logger.info(f"logger: {token} {run_as_password}")
        self.add_comment(f"comment: {token} {run_as_password}")
