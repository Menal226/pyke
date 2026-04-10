from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_int, to_str

@dataclass(slots=True, frozen=True)
class MiniSeriesDTO:
    losses: int = 0
    progress: str = ""
    target: int = 0
    wins: int = 0

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "MiniSeriesDTO":
        payload = dict(data or {})
        return cls(
            losses=to_int(payload.get("losses")),
            progress=to_str(payload.get("progress")),
            target=to_int(payload.get("target")),
            wins=to_int(payload.get("wins")),
        )
