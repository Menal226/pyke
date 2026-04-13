from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_str


@dataclass(slots=True, frozen=True)
class GameCustomizationObjectDto:
    category: str = ""
    """Category identifier for Game Customization"""
    content: str = ""
    """Game Customization content"""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "GameCustomizationObjectDto":
        payload = dict(data or {})
        return cls(
            category=to_str(payload.get("category")),
            content=to_str(payload.get("content")),
        )
