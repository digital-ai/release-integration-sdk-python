from digitalai.release.integration import BaseTask


class Hello(BaseTask):
    """
    Same class name as ../hello.py with a different greeting, so a test can
    tell that the wrapper loaded the class from the scriptLocation path.
    """

    def execute(self) -> None:
        self.set_output_property("greeting", f"Hello {self.input_properties['yourName']} from sample")
