from digitalai.release.release_api_client import ReleaseAPIClient
from digitalai.release.v2.configuration_api import ConfigurationApi

client = ReleaseAPIClient(
    server_address="http://localhost:5516",
    username="admin", password="admin"
)
config_api = ConfigurationApi(client)

# 1. Create
new_var = {
    "id": None,
    "key": "global.newVar",
    "type": "xlrelease.StringVariable",
    "requiresValue": "false",
    "showOnReleaseStart": "false",
    "value": "new value"
}
created = config_api.create_global_variable(new_var)

print("Created Global Variable:", created)

# 2. Update
created["value"] = "updated value"
updated = config_api.update_global_variable(created["id"], created)

# 3. Retrieve
fetched = config_api.get_global_variable(created["id"])

# 4. Delete
config_api.delete_global_variable(created["id"])

client.close()