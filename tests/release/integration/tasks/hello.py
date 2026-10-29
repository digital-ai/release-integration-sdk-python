from digitalai.release.integration import BaseTask


class Hello(BaseTask):
    """Greets the given name. Found by class name when no scriptLocation is set."""

    def execute(self) -> None:
        self.set_output_property("greeting", f"Hello {self.input_properties['yourName']}")
