from com.xebialabs.xlrelease.release_api_client import (
    ReleaseAPIClient as _ReleaseAPIClient,
)


class ReleaseAPIClient(_ReleaseAPIClient):
    """
    Backwards-compatible import path for ``ReleaseAPIClient``.

    The implementation now lives in the standalone
    ``digitalai-release-api-client`` package at
    ``com.xebialabs.xlrelease.release_api_client``. This thin subclass keeps the
    original ``digitalai.release.release_api_client.ReleaseAPIClient`` import
    path working, so existing integrations continue to run unchanged. Class
    name, constructor signature, methods, and behavior are identical to the
    base class.
    """
