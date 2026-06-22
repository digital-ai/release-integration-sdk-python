from __future__ import annotations

import ast
import base64
import importlib
import json
import os
import signal
import sys
import time
from typing import Any, Dict, Optional, Tuple

import requests

from digitalai.release.integration import k8s, watcher
from .base_task import BaseTask
from .input_context import InputContext
from .job_data_encryptor import AESJobDataEncryptor, NoOpJobDataEncryptor
from .logger import dai_logger
from .masked_io import MaskedIO
from .output_context import OutputContext

# Mask the standard output and error streams by replacing them with MaskedIO objects.
masked_std_out: MaskedIO = MaskedIO(sys.stdout)
masked_std_err: MaskedIO = MaskedIO(sys.stderr)
sys.stdout = masked_std_out
sys.stderr = masked_std_err

# input and output context file location
input_context_file: str = os.getenv('INPUT_LOCATION', '')
output_context_file: str = os.getenv('OUTPUT_LOCATION', '')
base64_session_key: str = os.getenv('SESSION_KEY', '')
release_server_url: str = os.getenv('RELEASE_URL', '')
callback_url: str = os.getenv('CALLBACK_URL', '')
input_context_secret: str = os.getenv('INPUT_CONTEXT_SECRET', '')
result_secret_key: str = os.getenv('RESULT_SECRET_NAME', '')
runner_namespace: str = os.getenv('RUNNER_NAMESPACE', '')
execution_mode: str = os.getenv('EXECUTOR_EXECUTION_MODE', '')

input_context: Optional[InputContext] = None

size_of_1Mb = 1024 * 1024

# HTTP timeouts (seconds). A missing timeout lets a hung server stall the runner forever.
HTTP_CONNECT_TIMEOUT = float(os.getenv('HTTP_CONNECT_TIMEOUT', '10'))
HTTP_READ_TIMEOUT = float(os.getenv('HTTP_READ_TIMEOUT', '60'))

# A single Session reused across all callback requests so the underlying urllib3
# connection pool is shared (instead of opening a fresh connection per call).
_http_session: requests.Session = requests.Session()
_HTTP_TIMEOUT = (HTTP_CONNECT_TIMEOUT, HTTP_READ_TIMEOUT)


# Create the encryptor
def get_encryptor():
    if base64_session_key:
        encryptor = AESJobDataEncryptor(base64_session_key)
    else:
        encryptor = NoOpJobDataEncryptor()
    return encryptor


# Initialize the global task object
dai_task_object: Optional[BaseTask] = None


def abort_handler(signum, frame):
    """
    This function handles the abort request by calling the abort method on the global task object, if it exists.
    If the task object does not exist, it logs a message and exits with a status code of 1.
    """
    dai_logger.info("Received SIGTERM to gracefully stop the process")
    global dai_task_object

    if dai_task_object:
        dai_task_object.abort()
    else:
        dai_logger.info("Abort requested")
        sys.exit(1)


# Register abort handler
signal.signal(signal.SIGTERM, abort_handler)


def _post_callback(url: str, encrypted_json) -> requests.Response:
    """
    POST the encrypted result to the callback URL using the shared Session.

    Raises an exception on transport errors *and* on HTTP error status codes
    (>= 400), so that the caller's retry logic is triggered in both cases.
    """
    response = _http_session.post(
        url,
        headers={'Content-Type': 'application/json'},
        data=encrypted_json,
        timeout=_HTTP_TIMEOUT,
    )
    response.raise_for_status()
    return response


def get_task_details() -> Tuple[Dict[str, Any], str, str]:
    """
    Get the task details by reading the input context file or fetching from secret, decrypting the contents using the encryptor,
    and parsing the JSON data into an InputContext object. Then, set the secrets for the masked standard output
    and error streams, build the task properties from the InputContext object.
    """
    dai_logger.info("Preparing for task properties")
    if input_context_file:
        dai_logger.info("Reading input context from file")
        with open(input_context_file) as data_input:
            input_content = data_input.read()
    else:
        k8s_client = k8s.get_client()
        dai_logger.info("Reading input context from secret")
        secret = k8s_client.read_namespaced_secret(input_context_secret, runner_namespace)
        global base64_session_key, callback_url
        base64_session_key = base64.b64decode(secret.data["session-key"])
        callback_url = base64.b64decode(secret.data["url"])

        input_content = secret.data["input"]
        if not input_content:
            fetch_url_base64 = secret.data["fetchUrl"]
            if not fetch_url_base64:
                raise ValueError("Cannot find fetch URL for task")

            # The fetch URL is double base64 encoded in the secret.
            fetch_url_bytes = base64.b64decode(fetch_url_base64)
            fetch_url = base64.b64decode(fetch_url_bytes).decode("UTF-8")
            try:
                response = _http_session.get(fetch_url, timeout=_HTTP_TIMEOUT)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                dai_logger.error("Failed to fetch data.", exc_info=True)
                raise e

            input_content = response.content
        else:
            input_content = base64.b64decode(input_content)

    decrypted_json = get_encryptor().decrypt(input_content)
    global input_context
    input_context = InputContext.from_dict(json.loads(decrypted_json))
    secrets = input_context.task.secrets()
    if input_context.release and input_context.release.automated_task_as_user and input_context.release.automated_task_as_user.password:
        secrets.append(input_context.release.automated_task_as_user.password)
    masked_std_out.secrets = secrets
    masked_std_err.secrets = secrets
    task_properties = input_context.task.build_locals()
    script_path = input_context.task.script_location()
    return task_properties, input_context.task.type, script_path


def update_output_context(output_context: OutputContext):
    """
    Update the output context file or secret by converting the output context object to a dictionary, serializing the
    dictionary to a JSON string, encrypting the string using the encryptor, and writing the encrypted string
    to the output context file or secret and pushing to callback URL.
    """
    output_content = json.dumps(output_context.to_dict())
    encrypted_json = get_encryptor().encrypt(output_content)
    try:
        if output_context_file:
            dai_logger.info("Writing output context to file")
            with open(output_context_file, "w") as data_output:
                data_output.write(encrypted_json)
        if result_secret_key:
            dai_logger.info("Writing output context to secret")
            if len(encrypted_json) >= size_of_1Mb:
                dai_logger.warning("Result size exceeds 1Mb and is too big to store in secret")
            else:
                namespace, name, key = k8s.split_secret_resource_data(result_secret_key)
                secret = k8s.get_client().read_namespaced_secret(name, namespace)
                secret.data[key] = encrypted_json
                k8s.get_client().replace_namespaced_secret(name, namespace, secret)
        if callback_url:
            dai_logger.info("Pushing result using HTTP")
            url = base64.b64decode(callback_url).decode("UTF-8")
            try:
                _post_callback(url, encrypted_json)
            except Exception:
                if should_retry_callback_request(encrypted_json):
                    dai_logger.error("Cannot finish Callback request.", exc_info=True)
                    dai_logger.info("Retry flag was set on Callback request, retrying until successful...")
                    retry_push_result_infinitely(encrypted_json)
                else:
                    raise

    except Exception:
        dai_logger.error("Unexpected error occurred.", exc_info=True)


def retry_push_result_infinitely(encrypted_json):
    """
    Keeps retrying to push encrypted data to the callback URL with exponential backoff, capping at 3 minutes.
    Callback URL is re-fetched from input context secret since it will change when remote-runner restarts.
    """
    retry_delay = 1
    max_backoff = 180
    backoff_factor = 2.0

    while True:
        # If we can't read the secret we should fail fast (let the exception propagate).
        secret = k8s.get_client().read_namespaced_secret(input_context_secret, runner_namespace)

        try:
            current_callback_url = base64.b64decode(secret.data["url"])
            url = base64.b64decode(current_callback_url).decode("UTF-8")
            return _post_callback(url, encrypted_json)
        except Exception as e:
            dai_logger.warning(f"Cannot finish retried Callback request: {e}. Retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
            retry_delay = min(retry_delay * backoff_factor, max_backoff)


def should_retry_callback_request(encrypted_data) -> bool:
    """
    Checks if callback request should be retried on failure.
    It should be retried when result is too big for Secret and Output File handler is not used.
    """
    return len(encrypted_data) >= size_of_1Mb and not input_context_file


def execute_task(task_object: BaseTask):
    """
    Execute the given task object by setting it as the global task object and starting its execution.
    If an exception is raised during execution, log the error. Finally, update the output context file
    using the output context of the task object.
    """
    global dai_task_object
    try:
        dai_task_object = task_object
        dai_logger.info("Starting task execution")
        dai_task_object.execute_task()
    except Exception:
        dai_logger.error("Unexpected error occurred.", exc_info=True)
    finally:
        # Guard against a task object that was never constructed or that failed
        # before producing an output context, so the finally block does not raise
        # a second exception that masks the original one.
        if dai_task_object is not None and dai_task_object.get_output_context() is not None:
            update_output_context(dai_task_object.get_output_context())
        else:
            dai_logger.error("No output context available to report task result")
            update_output_context(OutputContext(1, "Task produced no output context", {}, []))


def find_class_file(root_dir, class_name):
    for root, _, files in os.walk(root_dir):
        for filename in files:
            if filename.endswith('.py'):
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, encoding="utf-8") as file:
                        node = ast.parse(file.read())
                except (SyntaxError, UnicodeDecodeError, OSError):
                    # Skip files that cannot be read or parsed instead of aborting the whole search.
                    continue
                classes = [n.name for n in node.body if isinstance(n, ast.ClassDef)]
                if class_name in classes:
                    return filepath
    return None


def run():
    try:
        # Get task details, parse the script file to get the task class, import the module,
        # create an instance of the task class, and execute the task
        task_props, task_type, script_path = get_task_details()
        if "." not in task_type:
            raise ValueError(f"Invalid task type '{task_type}', expected format '<prefix>.<ClassName>'")
        task_class_name = task_type.split(".")[1]

        if script_path:
            script_path = script_path.lstrip("/\\")
            script_path = script_path.replace("/", os.sep).replace("\\", os.sep)

            full_path = os.path.join(os.getcwd(), "src", script_path)
            relative_path = os.path.join("src", script_path)

            if not os.path.isfile(full_path):
                raise ValueError(f"Script file not found at: {relative_path}")

            module_name = full_path.replace(os.getcwd() + os.sep, "")
            module_name = module_name.replace(".py", "").replace(os.sep, ".")
            module = importlib.import_module(module_name)

            if not hasattr(module, task_class_name):
                raise ValueError(
                    f"Class '{task_class_name}' not found in script file: {relative_path}"
                )

        else:
            class_file_path = find_class_file(os.getcwd(), task_class_name)
            if not class_file_path:
                raise ValueError(f"Could not find the '{task_class_name}' class")
            module_name = class_file_path.replace(os.getcwd() + os.sep, "")
            module_name = module_name.replace(".py", "").replace(os.sep, ".")
            module = importlib.import_module(module_name)

        task_class = getattr(module, task_class_name)
        task_obj = task_class()
        task_obj.input_properties = task_props
        task_obj.release_server_url = release_server_url.strip('/')
        task_obj.release_context = input_context.release
        task_obj.task_id = input_context.task.id
        execute_task(task_obj)
    except Exception as e:
        # Log the error and update the output context file with exit code 1 if an exception is raised
        dai_logger.error("Unexpected error occurred.", exc_info=True)
        update_output_context(OutputContext(1, str(e), {}, []))
    finally:
        if execution_mode == "daemon":
            watcher.start_input_context_watcher(run)


if __name__ == "__main__":
    run()
