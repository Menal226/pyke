from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_str


@dataclass(slots=True, frozen=True)
class MetadataTimeLineDto:
    dataVersion: str = ""
    matchId: str = ""
    participants: list[str] = field(default_factory=list[str])

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "MetadataTimeLineDto":
        payload = dict(data or {})
        return cls(
            dataVersion=to_str(payload.get("dataVersion")),
            matchId=to_str(payload.get("matchId")),
            participants=[to_str(item) for item in payload.get("participants", [])],
        )
