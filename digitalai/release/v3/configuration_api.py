from typing import Any, Dict
from digitalai.release.release_api_client import ReleaseAPIClient
from digitalai.release.v3.global_variable import GlobalVariable


class ConfigurationApi:

    def __init__(self, client: ReleaseAPIClient) -> None:
        self.client: ReleaseAPIClient = client

    def create_global_variable(self, global_variable: GlobalVariable) -> GlobalVariable:
        json_data = self.client.request_json(
            method='POST',
            endpoint='/api/v1/config/Configuration/variables/global',
            json=global_variable.to_dict()
        )
        return GlobalVariable(json_data)

    def update_global_variable(self, variable_id: str, global_variable: GlobalVariable) -> GlobalVariable:
        json_data = self.client.request_json(
            method='PUT',
            endpoint=f'/api/v1/config/{variable_id}',
            json=global_variable.to_dict()
        )
        return GlobalVariable(json_data)

    def get_global_variable(self, variable_id: str) -> GlobalVariable:
        json_data = self.client.request_json(
            method='GET',
            endpoint=f'/api/v1/config/{variable_id}'
        )
        return GlobalVariable(json_data)

    def delete_global_variable(self, variable_id: str) -> None:
        response = self.client.delete(f'/api/v1/config/{variable_id}')
        response.raise_for_status()

