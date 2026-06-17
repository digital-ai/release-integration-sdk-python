import unittest

from com.xebialabs.xlrelease.release_api_client import (
    ReleaseAPIClient as ApiClientReleaseAPIClient,
)
from digitalai.release.release_api_client import ReleaseAPIClient


class TestReleaseAPIClientBackwardCompatibility(unittest.TestCase):
    """The old ``digitalai.release.release_api_client`` import path must keep
    working as a drop-in for the standalone api-client implementation."""

    def test_is_subclass_of_api_client_class(self):
        """The shim extends the standalone api-client class."""
        self.assertTrue(issubclass(ReleaseAPIClient, ApiClientReleaseAPIClient))

    def test_instance_is_recognized_as_api_client_class(self):
        """Instances created via the old path are instances of both classes."""
        client = ReleaseAPIClient("http://localhost:5516", "admin", "admin")
        try:
            self.assertIsInstance(client, ReleaseAPIClient)
            self.assertIsInstance(client, ApiClientReleaseAPIClient)
        finally:
            client.close()

    def test_constructor_behaves_like_base(self):
        """Construction, URL normalization, and auth match the base class."""
        with ReleaseAPIClient("http://localhost:5516/", "admin", "secret") as client:
            self.assertEqual(client.server_address, "http://localhost:5516")
            self.assertEqual(client.session.auth, ("admin", "secret"))

    def test_constructor_requires_credentials(self):
        """The base validation still applies through the shim."""
        with self.assertRaises(ValueError):
            ReleaseAPIClient("http://localhost:5516")


if __name__ == "__main__":
    unittest.main()
