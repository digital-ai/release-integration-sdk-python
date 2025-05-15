from typing import Any, Dict, List
from digitalai.release.release_api_client import ReleaseAPIClient
from digitalai.release.v3.release import Release


class ReleaseApi:

    def __init__(self, client: ReleaseAPIClient) -> None:
        self.client: ReleaseAPIClient = client

    def find_releases_by_title(self, release_title: str) -> List[Release]:
        params = {"releaseTitle": release_title}
        json_list =  self.client.request_json(
            method="GET",
            endpoint="/api/v1/releases/byTitle",
            params=params
        )
        return [Release(item) for item in json_list]

