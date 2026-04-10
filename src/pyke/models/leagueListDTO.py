from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_dict_list, to_str
from .leagueItemDTO import LeagueItemDTO

@dataclass(slots=True, frozen=True)
class LeagueListDTO:
    leagueId: str = ""
    entries: list[LeagueItemDTO] = field(default_factory=list[LeagueItemDTO])
    tier: str = ""
    name: str = ""
    queue: str = ""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "LeagueListDTO":
        payload = dict(data or {})
        return cls(
            leagueId=to_str(payload.get("leagueId")),
            entries=[
                LeagueItemDTO.from_dict(entry)
                for entry in to_dict_list(payload.get("entries"))
            ],
            tier=to_str(payload.get("tier")),
            name=to_str(payload.get("name")),
            queue=to_str(payload.get("queue")),
        )