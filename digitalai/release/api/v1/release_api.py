from typing import Any, Dict, List
from digitalai.release.release_api_client import ReleaseAPIClient

class ReleaseApi:

    def __init__(self, release_api_client: ReleaseAPIClient) -> None:
        self.api = release_api_client

    def getRelease(self, releaseId: str) -> List[Dict[str, Any]]:
        response = self.api.get(f"/api/v1/releases/{releaseId}")
        return response.json()