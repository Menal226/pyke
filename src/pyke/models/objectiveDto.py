from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_bool, to_int

@dataclass(slots=True, frozen=True)
class ObjectiveDto:
    first: bool = False
    kills: int = 0

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "ObjectiveDto":
        payload = dict(data or {})
        return cls(
            first=to_bool(payload.get("first")),
            kills=to_int(payload.get("kills")),
        )


