"""
The old ``digitalai.release.release_api_client`` import path must keep working
as a drop-in for the standalone ``digitalai-release-api-client`` package.
"""
import pytest
from com.xebialabs.xlrelease.release_api_client import ReleaseAPIClient as StandaloneReleaseAPIClient

from digitalai.release.release_api_client import ReleaseAPIClient


def test_shim_is_a_subclass_of_the_standalone_client():
    assert issubclass(ReleaseAPIClient, StandaloneReleaseAPIClient)


def test_shim_normalizes_the_url_and_uses_basic_auth():
    with ReleaseAPIClient("http://localhost:5516/", "admin", "secret") as client:
        assert client.server_address == "http://localhost:5516"
        assert client.session.auth == ("admin", "secret")


def test_shim_requires_credentials():
    with pytest.raises(ValueError):
        ReleaseAPIClient("http://localhost:5516")
