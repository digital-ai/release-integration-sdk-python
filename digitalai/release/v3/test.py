from platform import release

from digitalai.release.release_api_client import ReleaseAPIClient
from digitalai.release.v3.configuration_api import ConfigurationApi
from digitalai.release.v3.release_api import ReleaseApi
from digitalai.release.v3.global_variable import GlobalVariable

client = ReleaseAPIClient(
    server_address="http://localhost:5516",
    username="admin", password="admin"
)

# Configuration API example
config_api = ConfigurationApi(client)

# Create global variable
new_var = GlobalVariable({
    "id": None,
    "key": "global.newVar",
    "type": "xlrelease.StringVariable",
    "requiresValue": "false",
    "showOnReleaseStart": "false",
    "value": "new value"
})
created_var = config_api.create_global_variable(new_var)

print("Created Global Variable Id:", created_var.id)

# Delete global variable
config_api.delete_global_variable(created_var.id)

# Release API example
release_api = ReleaseApi(client)

# Find releases by title
releases = release_api.find_releases_by_title("mytest")

print("Releases found with title 'mytest':")
for release in releases:
    print(f"Release ID: {release.id}, Title: {release.title}")


