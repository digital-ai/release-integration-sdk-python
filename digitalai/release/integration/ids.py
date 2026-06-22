"""
Helpers for parsing Release object ids.

Release object ids are slash-separated paths, e.g.
    Applications/Folder.../Release.../Phase.../Task...
The server derives the enclosing phase/folder by walking up that path (see
com.xebialabs.xlrelease.repository.Ids). A task only receives its own task and
release ids, so we reproduce the same walk to resolve the phase and folder.
"""

_ID_SEPARATOR = '/'
_PHASE_PREFIX = 'Phase'
_FOLDER_PREFIX = 'Folder'


class Ids:
    """Path-based parsing of Release object ids (mirrors the server's Ids)."""

    @staticmethod
    def segment_name(object_id: str) -> str:
        """Return the last path segment of an id (Ids.getName)."""
        if _ID_SEPARATOR not in object_id:
            return object_id
        return object_id[object_id.rfind(_ID_SEPARATOR) + 1:]

    @staticmethod
    def parent_id(object_id: str) -> str:
        """Return the id with its last path segment removed (Ids.getParentId)."""
        return object_id[:object_id.rfind(_ID_SEPARATOR)]

    @staticmethod
    def is_root(object_id: str) -> bool:
        """True when the id has no parent, i.e. no separator (Ids.isRoot)."""
        return _ID_SEPARATOR not in object_id

    @staticmethod
    def phase_id_from(object_id: str) -> str:
        """Return the enclosing phase id of ``object_id`` (Ids.phaseIdFrom)."""
        ancestry = object_id
        while not Ids.segment_name(ancestry).startswith(_PHASE_PREFIX):
            if Ids.is_root(ancestry):
                raise ValueError(f"No phase found in id '{object_id}'")
            ancestry = Ids.parent_id(ancestry)
        return ancestry

    @staticmethod
    def find_folder_id(object_id: str) -> str:
        """Return the enclosing folder id of ``object_id`` (Ids.findFolderId)."""
        parent = object_id
        while not Ids.segment_name(parent).startswith(_FOLDER_PREFIX) and not Ids.is_root(parent):
            parent = Ids.parent_id(parent)
        return parent
