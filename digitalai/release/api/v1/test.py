from digitalai.release.api.v1.release_api import ReleaseApi
from digitalai.release.release_api_client import ReleaseAPIClient

client = ReleaseAPIClient("http://localhost:5516", "admin", "admin")

api = ReleaseApi(client)

print(api.getRelease("Releaseed825e506e944b16b050bf4af5f9402a"))