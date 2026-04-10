from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_str, to_str_list

@dataclass(slots=True, frozen=True)
class MetadataDto:
    dataVersion: str = ""
    """Match data version."""
    matchId: str = ""
    """Match id."""
    participants: list[str] = field(default_factory=list[str])
    """A list of participant PUUIDs."""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "MetadataDto":
        payload = dict(data or {})
        return cls(
            dataVersion=to_str(payload.get("dataVersion")),
            matchId=to_str(payload.get("matchId")),
            participants=to_str_list(payload.get("participants")),
        )


