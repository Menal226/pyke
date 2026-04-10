from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_int

@dataclass(slots=True, frozen=True)
class PerkStatsDto:
    defense: int = 0
    flex: int = 0
    offense: int = 0

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "PerkStatsDto":
        payload = dict(data or {})
        return cls(
            defense=to_int(payload.get("defense")),
            flex=to_int(payload.get("flex")),
            offense=to_int(payload.get("offense")),
        )


