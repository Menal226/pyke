from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_int, to_str


@dataclass(slots=True, frozen=True)
class EventsTimeLineDto:
    timestamp: int = 0
    realTimestamp: int = 0
    type: str = ""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "EventsTimeLineDto":
        payload = dict(data or {})
        return cls(
            timestamp=to_int(payload.get("timestamp")),
            realTimestamp=to_int(payload.get("realTimestamp")),
            type=to_str(payload.get("type")),
        )
