import logging
import sys
from abc import ABC, abstractmethod
from typing import Any, Dict

from digitalai.release.v1.configuration import Configuration

from digitalai.release.v1.api_client import ApiClient

from .input_context import AutomatedTaskAsUserContext, ReleaseContext
from .output_context import OutputContext
from .exceptions import AbortException

logger = logging.getLogger("Digitalai")


class BaseTask(ABC):
    """
    An abstract base class representing a task that can be executed.
    """
    def execute_task(self) -> None:
        """
        Executes the task by calling the execute method. If an AbortException is raised during execution,
        the task's exit code is set to 1 and the program exits with a status code of 1. If any other exception
        is raised, the task's exit code is also set to 1.
        """
        try:
            self.output_context = OutputContext(0, "", {}, [])
            self.execute()
        except AbortException:
            logger.debug("Abort requested")
            self.set_exit_code(1)
            sys.exit(1)
            self.set_error_message("Abort requested")
        except Exception as e:
            logger.error("Unexpected error occurred.", exc_info=True)
            self.set_exit_code(1)
            self.set_error_message(str(e))

    @abstractmethod
    def execute(self) -> None:
        """
        This is an abstract method that must be implemented by subclasses of BaseTask. It represents the main
        logic of the task.
        """
        pass

    def abort(self) -> None:
        """
        Sets the task's exit code to 1 and exits the program with a status code of 1.
        """
        self.set_exit_code(1)
        sys.exit(1)

    def get_output_context(self) -> OutputContext:
        """
        Returns the OutputContext object associated with the task.
        """
        return self.output_context

    def get_output_properties(self) -> Dict[str, Any]:
        """
        Returns the output properties dictionary of the task's OutputContext object.
        """
        return self.output_context.output_properties

    def get_input_properties(self) -> Dict[str, Any]:
        """
        Returns the input properties dictionary of the task
        """
        if not self.input_properties:
            raise ValueError(f"Input properties have not been set")
        return self.input_properties

    def set_output_property(self, name: str, value: Any) -> None:
        """
        Sets the name and value of an output property of the task
        """
        if not name:
            raise ValueError("Output property name cannot be empty")
        self.output_context.output_properties[name] = value

    def set_exit_code(self, value) -> None:
        """
        Sets the exit code of the task's OutputContext object.
        """
        self.output_context.exit_code = value

    def set_error_message(self, value) -> None:
        """
        Sets the error message of the task's OutputContext object.
        """
        self.output_context.job_error_message = value

    def add_comment(self, comment: str) -> None:
        """
        Logs a comment of the task.
        """
        logger.debug(f"##[start: comment]{comment}##[end: comment]")

    def set_status_line(self, status_line: str) -> None:
        """
        Set the status of the task.
        """
        logger.debug(f"##[start: status]{status_line}##[end: status]")

    def add_reporting_record(self, reporting_record: Any) -> None:
        """
        Adds a reporting record to the OutputContext
        """
        self.output_context.reporting_records.append(reporting_record)

    def get_release_server_url(self) -> str:
        """
        Returns the Release server URL of the associated task
        """
        return self.release_server_url

    def get_task_user(self) -> AutomatedTaskAsUserContext:
        """
        Returns the user details that are executing the task.
        """
        return self.release_context.automated_task_as_user

    def get_default_api_client(self) -> ApiClient:
        """
        Returns an ApiClient object with default configuration based on the task.
        """
        if not all([self.get_release_server_url(), self.get_task_user().username, self.get_task_user().password]):
            raise ValueError("Cannot connect to Release API without server URL, username, or password. "
                             "Make sure that the 'Run as user' property is set on the release.")

        configuration = Configuration(
            host=self.get_release_server_url(),
            username=self.get_task_user().username,
            password=self.get_task_user().password)

        return ApiClient(configuration)

    def get_release_id(self) -> str:
        """
        Returns the Release ID of the task
        """
        return self.release_context.id

    def get_task_id(self) -> str:
        """
        Returns the Task ID of the task
        """
        return self.task_id



