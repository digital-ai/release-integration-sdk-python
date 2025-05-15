from typing import Any, Dict

class GlobalVariable:
    """
    Domain model representing a GlobalVariable. Initializes attributes from a dict.
    """
    def __init__(self, data: Dict[str, Any]) -> None:
        for key, value in data.items():
            setattr(self, key, value)

    def __repr__(self) -> str:
        attrs = ', '.join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"GlobalVariable({attrs})"

    def to_dict(self) -> Dict[str, Any]:
        return dict(self.__dict__)
