from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_str


@dataclass(slots=True, frozen=True)
class ContentDto:
    locale: str = ""
    content: str = ""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "ContentDto":
        payload = dict(data or {})
        return cls(
            locale=to_str(payload.get("locale")),
            content=to_str(payload.get("content")),
        )
