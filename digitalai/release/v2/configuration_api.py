from typing import Any, Dict
from digitalai.release.release_api_client import ReleaseAPIClient

class ConfigurationApi:

    def __init__(self, client: ReleaseAPIClient) -> None:
        self.client: ReleaseAPIClient = client

    def create_global_variable(self, global_variable: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request_json(
            method='POST',
            endpoint='/api/v1/config/Configuration/variables/global',
            json=global_variable
        )

    def update_global_variable(self, variable_id: str, global_variable: Dict[str, Any]) -> Dict[str, Any]:
        return self.client.request_json(
            method='PUT',
            endpoint=f'/api/v1/config/{variable_id}',
            json=global_variable
        )

    def get_global_variable(self, variable_id: str) -> Dict[str, Any]:
        return self.client.request_json(
            method='GET',
            endpoint=f'/api/v1/config/{variable_id}'
        )

    def delete_global_variable(self, variable_id: str) -> None:
        response = self.client.delete(f'/api/v1/config/{variable_id}')
        response.raise_for_status()

