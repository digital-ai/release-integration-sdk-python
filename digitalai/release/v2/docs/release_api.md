# `ReleaseApi.find_releases_by_title`

Retrieves a list of releases whose title matches the specified query.

---

## Method Signature

```python
def find_releases_by_title(self, release_title: str) -> List[Dict[str, Any]]:
```

## Parameters

| Parameter       | Type  | Description                                   |
| --------------- | ----- | --------------------------------------------- |
| `release_title` | `str` | The exact title of the release to search for. |

## Returns

A list of release objects matching the given title. Each release is represented as a JSON-like dictionary containing its details.

**Return Type:** `List[Dict[str, Any]]`

## Example Usage

### Input

```python
release_title = "Find me"
```

### Output

```json
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
    "overdueNotified": false,
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
    "calendarPublished": false,
    "tutorial": false,
    "abortOnFailure": false,
    "archiveRelease": true,
    "allowPasswordsInAllFields": false,
    "disableNotifications": false,
    "allowConcurrentReleasesFromTrigger": true,
    "createdFromTrigger": false
  }
]
```

---

