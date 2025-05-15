Module configuration_api
========================

Classes
-------

`ConfigurationApi(client: digitalai.release.release_api_client.ReleaseAPIClient)`
:   

    ### Methods

    `create_global_variable(self, global_variable: Dict[str, Any]) ‑> Dict[str, Any]`
    :   Creates a new global variable in the Release configuration.
        
        Args:
            global_variable (Dict[str, Any]): A dict representing the global variable to create. Example:
                {
                    "id": None,
                    "key": "global.newVar",
                    "type": "xlrelease.StringVariable",
                    "requiresValue": False,
                    "showOnReleaseStart": False,
                    "value": "new value",
                    "label": None,
                    "description": None,
                    "multiline": False,
                    "referencedType": None,
                    "inherited": False,
                    "preventInterpolation": False,
                    "externalVariableValue": None,
                    "valueProvider": None
                }
        
        Returns:
            Dict[str, Any]: The created global variable resource. Example:
                {
                    "id": "Configuration/variables/global/Variable46146adfe1a444cab8ff722f3ec432ef",
                    "type": "xlrelease.StringVariable",
                    "key": "global.newVar",
                    "requiresValue": False,
                    "showOnReleaseStart": False,
                    "inherited": False,
                    "value": "new value",
                    "multiline": False,
                    "preventInterpolation": False
                }
        
        Raises:
            requests.HTTPError: If the API request fails with an HTTP error status.

    `delete_global_variable(self, variable_id: str) ‑> None`
    :

    `get_global_variable(self, variable_id: str) ‑> Dict[str, Any]`
    :

    `update_global_variable(self, variable_id: str, global_variable: Dict[str, Any]) ‑> Dict[str, Any]`
    :