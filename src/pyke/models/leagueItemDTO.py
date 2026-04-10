from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_bool, to_dict, to_int, to_str
from .miniSeriesDTO import MiniSeriesDTO


@dataclass(slots=True, frozen=True)
class LeagueItemDTO:
    freshBlood: bool = False
    wins: int = 0
    miniSeries: MiniSeriesDTO = field(default_factory=MiniSeriesDTO)
    inactive: bool = False
    veteran: bool = False
    hotStreak: bool = False
    rank: str = ""
    leaguePoints: int = 0
    losses: int = 0
    puuid: str = ""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "LeagueItemDTO":
        payload = dict(data or {})
        return cls(
            freshBlood=to_bool(payload.get("freshBlood")),
            wins=to_int(payload.get("wins")),
            miniSeries=MiniSeriesDTO.from_dict(to_dict(payload.get("miniSeries"))),
            inactive=to_bool(payload.get("inactive")),
            veteran=to_bool(payload.get("veteran")),
            hotStreak=to_bool(payload.get("hotStreak")),
            rank=to_str(payload.get("rank")),
            leaguePoints=to_int(payload.get("leaguePoints")),
            losses=to_int(payload.get("losses")),
            puuid=to_str(payload.get("puuid")),
        )
