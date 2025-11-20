from digitalai.release.integration import BaseTask
from digitalai.release.integration import dai_logger

class Hello1(BaseTask):
    """
       The purpose of this task is to greet by the given name.
    """
    def execute(self) -> None:

        print("Inside Sample Folder - Hello Task")

        name = self.input_properties['yourName']
        if not name:
            raise ValueError("The 'name' field cannot be empty")

        greeting = f"Hello {name}"

        dai_logger.info(f"get_release_server_url() : {self.get_release_server_url()}")
        dai_logger.info(f"get_task_user() : {self.get_task_user()}")
        dai_logger.info(f"get_release_id() : {self.get_release_id()}")
        dai_logger.info(f"get_task_id() : {self.get_task_id()}")

        # Add to the comment section of the task in the UI
        self.add_comment(greeting)

        self.set_output_property('greeting', greeting)

