import unittest
from types import SimpleNamespace
from unittest import mock

from digitalai.release.integration.base_task import BaseTask
from digitalai.release.integration.exceptions import AbortException
from digitalai.release.integration.ids import Ids
from digitalai.release.integration.input_context import (
    AutomatedTaskAsUserContext,
    ReleaseContext,
)

# Realistic ids, matching the sample input context.
FOLDER_ID = 'Applications/Folder1f65c7220b394afbb941154342fd9fc6'
RELEASE_ID = f'{FOLDER_ID}/Release31de09e95c8e4ebb95aaed29a8082d0b'
PHASE_ID = f'{RELEASE_ID}/Phase723a601c78804f7dbcaa8b05b83708f5'
TASK_ID = f'{PHASE_ID}/Task3a35b67b42b6428b854857fba470b39a'


class _StubTask(BaseTask):
    """Minimal concrete task so BaseTask can be instantiated in tests."""

    def execute(self) -> None:  # pragma: no cover - never run
        pass


class TestIdParsing(unittest.TestCase):

    def test_phase_id_from_task_id(self):
        self.assertEqual(Ids.phase_id_from(TASK_ID), PHASE_ID)

    def test_find_folder_id_from_release_id(self):
        self.assertEqual(Ids.find_folder_id(RELEASE_ID), FOLDER_ID)

    def test_phase_id_from_raises_when_absent(self):
        with self.assertRaises(ValueError):
            Ids.phase_id_from('Applications/Folder1/Release1')

    def test_segment_name_and_parent_id(self):
        self.assertEqual(Ids.segment_name(TASK_ID), 'Task3a35b67b42b6428b854857fba470b39a')
        self.assertEqual(Ids.parent_id(TASK_ID), PHASE_ID)
        self.assertTrue(Ids.is_root('Applications'))
        self.assertFalse(Ids.is_root(RELEASE_ID))


class TestBaseTaskIds(unittest.TestCase):

    def _task(self):
        task = _StubTask()
        task.task_id = TASK_ID
        task.release_context = SimpleNamespace(id=RELEASE_ID)
        return task

    def test_get_phase_id_derives_from_task_id(self):
        self.assertEqual(self._task().get_phase_id(), PHASE_ID)

    def test_get_folder_id_derives_from_release_id(self):
        self.assertEqual(self._task().get_folder_id(), FOLDER_ID)


class TestBaseTaskOutput(unittest.TestCase):
    """Robustness coverage for output handling and credential validation."""

    def _task(self):
        task = _StubTask()
        task.task_id = TASK_ID
        return task

    def test_execute_task_sets_success_output(self):
        task = self._task()
        task.execute_task()
        ctx = task.get_output_context()
        self.assertEqual(ctx.exit_code, 0)
        self.assertEqual(ctx.job_error_message, "")

    def test_execute_task_captures_unexpected_error(self):
        class _Boom(_StubTask):
            def execute(self) -> None:
                raise RuntimeError("boom")

        task = _Boom()
        task.execute_task()
        ctx = task.get_output_context()
        self.assertEqual(ctx.exit_code, 1)
        self.assertEqual(ctx.job_error_message, "boom")

    def test_execute_task_handles_abort(self):
        class _Abort(_StubTask):
            def execute(self) -> None:
                raise AbortException()

        task = _Abort()
        with self.assertRaises(SystemExit) as cm:
            task.execute_task()
        self.assertEqual(cm.exception.code, 1)
        ctx = task.get_output_context()
        self.assertEqual(ctx.exit_code, 1)
        self.assertEqual(ctx.job_error_message, "Abort requested")

    def test_set_output_property_rejects_empty_name(self):
        task = self._task()
        task.execute_task()
        with self.assertRaises(ValueError):
            task.set_output_property("", "value")

    def test_set_output_property_rejects_unsupported_type(self):
        task = self._task()
        task.execute_task()
        with self.assertRaises(ValueError):
            task.set_output_property("name", object())

    def test_get_input_properties_requires_value(self):
        task = self._task()
        with self.assertRaises(ValueError):
            task.get_input_properties()

    def test_get_task_user_returns_none_without_release_context(self):
        task = self._task()
        self.assertIsNone(task.get_task_user())

    def test_get_release_api_client_raises_without_task_user(self):
        task = self._task()
        task.release_server_url = "http://localhost:5516"
        with self.assertRaises(ValueError):
            task.get_release_api_client()


class TestAutomatedTaskAsUser(unittest.TestCase):
    """Coverage for the 'Run as user' (automatedTaskAsUser) username/password."""

    SERVER_URL = "http://localhost:5516"

    def _task(self, username, password):
        task = _StubTask()
        task.task_id = TASK_ID
        task.release_server_url = self.SERVER_URL
        task.release_context = ReleaseContext(
            id=RELEASE_ID,
            automated_task_as_user=AutomatedTaskAsUserContext(username=username, password=password),
        )
        return task

    def test_get_task_user_returns_credentials(self):
        task = self._task("admin", "secret")
        user = task.get_task_user()
        self.assertEqual(user.username, "admin")
        self.assertEqual(user.password, "secret")

    def test_get_release_api_client_passes_credentials(self):
        task = self._task("admin", "secret")
        with mock.patch("digitalai.release.integration.base_task.ReleaseAPIClient") as fake_client:
            client = task.get_release_api_client()
        fake_client.assert_called_once_with(self.SERVER_URL, "admin", "secret", timeout=None)
        self.assertIs(client, fake_client.return_value)

    def test_get_release_api_client_raises_when_password_missing(self):
        task = self._task("admin", None)
        with self.assertRaises(ValueError):
            task.get_release_api_client()

    def test_get_release_api_client_uses_password_as_token_when_username_missing(self):
        task = self._task(None, "secret")
        with mock.patch("digitalai.release.integration.base_task.ReleaseAPIClient") as fake_client:
            client = task.get_release_api_client()
        fake_client.assert_called_once_with(
            self.SERVER_URL, personal_access_token="secret", timeout=None)
        self.assertIs(client, fake_client.return_value)

    def test_get_release_api_client_raises_when_credentials_blank(self):
        task = self._task("", "")
        with self.assertRaises(ValueError):
            task.get_release_api_client()

    def test_get_release_api_client_raises_without_server_url(self):
        task = self._task("admin", "secret")
        task.release_server_url = None
        with self.assertRaises(ValueError):
            task.get_release_api_client()


if __name__ == '__main__':
    unittest.main()
