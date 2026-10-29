from digitalai.release.integration import BaseTask


class ContextEcho(BaseTask):
    """Reports the task context the wrapper wired into the task as output properties."""

    def execute(self) -> None:
        self.set_output_property("serverUrl", self.get_release_server_url())
        self.set_output_property("releaseId", self.get_release_id())
        self.set_output_property("taskId", self.get_task_id())
        self.set_output_property("username", self.get_task_user().username)
        self.set_output_property("inputs", self.get_input_properties())
