import json
import os
import subprocess
import sys
import unittest

# Directory that holds the test fixtures (input.json, hello.py, src/...).
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

# Sample input context for a "Hello" container task (matches input.json).
SAMPLE_INPUT_CONTEXT = {
    "release": {
        "id": "Applications/Folder1f65c7220b394afbb941154342fd9fc6/Release31de09e95c8e4ebb95aaed29a8082d0b",
        "automatedTaskAsUser": {"username": "admin", "password": "admin"},
    },
    "task": {
        "id": "Applications/Folder1f65c7220b394afbb941154342fd9fc6/Release31de09e95c8e4ebb95aaed29a8082d0b/Phase723a601c78804f7dbcaa8b05b83708f5/Task3a35b67b42b6428b854857fba470b39a",
        "type": "containerExamples.Hello",
        "properties": [
            {"name": "capabilities", "value": ["remote"], "kind": "SET_OF_STRING", "category": "input", "password": False},
            {"name": "yourName", "value": "World", "kind": "STRING", "category": "input", "password": False},
            {"name": "greeting", "value": None, "kind": "STRING", "category": "output", "password": False},
        ],
    },
}

EXPECTED_OUTPUT = {
    "exitCode": 0,
    "jobErrorMessage": "",
    "outputProperties": {"greeting": "Hello World"},
    "reportingRecords": [],
}


class TestWrapper(unittest.TestCase):
    """End-to-end test that runs the wrapper against a sample input context."""

    def setUp(self):
        self.input_path = os.path.join(THIS_DIR, "input.json")
        self.output_path = os.path.join(THIS_DIR, "output.json")
        # Write the sample input context so the test is self-contained.
        with open(self.input_path, "w") as f:
            json.dump(SAMPLE_INPUT_CONTEXT, f)
        # Start from a clean slate so a stale file can never mask a failure.
        if os.path.exists(self.output_path):
            os.remove(self.output_path)

    def test_wrapper(self):
        """
        Runs the wrapper as a subprocess with the sample input context and verifies
        that it exits successfully and produces the expected output context.
        """
        env = dict(os.environ)
        env["INPUT_LOCATION"] = "input.json"
        env["OUTPUT_LOCATION"] = "output.json"
        env["RELEASE_URL"] = "http://localhost:5516"

        result = subprocess.run(
            [sys.executable, "-m", "digitalai.release.integration.wrapper"],
            cwd=THIS_DIR,
            env=env,
            capture_output=True,
            text=True,
        )

        self.assertEqual(
            result.returncode, 0,
            msg=f"wrapper exited with {result.returncode}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}",
        )
        self.assertTrue(os.path.exists(self.output_path), "wrapper did not produce output.json")

        with open(self.output_path, "r") as json_file:
            actual_output = json.load(json_file)

        self.assertEqual(EXPECTED_OUTPUT, actual_output)


if __name__ == '__main__':
    unittest.main()
