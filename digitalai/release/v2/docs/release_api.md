Module release_api
==================

Classes
-------

`ReleaseApi(client: digitalai.release.release_api_client.ReleaseAPIClient)`
:   

    ### Methods

    `find_releases_by_title(self, release_title: str) ‑> List[Dict[str, Any]]`
    :   Finds releases by title.
        
        Args:
            release_title (str): The title of the release to search for.
        
        Returns:
            List[Dict[str, Any]]: A list of releases matching the title. Each release is represented as a dict containing release details.
        
        Example:
            >>> api = ReleaseApi(client)
            >>> api.find_releases_by_title("Find me")
            [
                {
                    "id": "Applications/Release162151faba694d03aa3065665cf26f21",
                    "type": "xlrelease.Release",
                    "createdBy": "admin",
                    "createdAt": "2025-04-28T07:00:34.387+0000",
                    "lastModifiedBy": "admin",
                    "lastModifiedAt": "2025-04-28T07:00:34.387+0000",
                    "scmTraceabilityDataId": "0",
                    "title": "Find me",
                    "flagStatus": "OK",
                    "overdueNotified": False,
                    "maxConcurrentReleases": 100,
                    "releaseTriggers": [],
                    "teams": [],
                    "memberViewers": [],
                    "roleViewers": [],
                    "attachments": [],
                    "phases": [],
                    "realFlagStatus": "OK",
                    "status": "PLANNED",
                    "kind": "RELEASE",
                    "tags": [],
                    "categories": [],
                    "variables": [],
                    "calendarPublished": False,
                    "tutorial": False,
                    "abortOnFailure": False,
                    "archiveRelease": True,
                    "allowPasswordsInAllFields": False,
                    "disableNotifications": False,
                    "allowConcurrentReleasesFromTrigger": True,
                    "createdFromTrigger": False,
                }
            ]