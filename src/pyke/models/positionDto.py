from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_int


@dataclass(slots=True, frozen=True)
class PositionDto:
    x: int = 0
    y: int = 0

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "PositionDto":
        payload = dict(data or {})
        return cls(
            x=to_int(payload.get("x")),
            y=to_int(payload.get("y")),
        )
