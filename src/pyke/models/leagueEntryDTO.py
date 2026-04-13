from dataclasses import dataclass, field
from typing import Any, Mapping

from ..enums.queue import Queue
from ..enums.division import Division
from ..enums.tier import Tier

from ._coerce import to_bool, to_dict, to_int, to_str
from .miniSeriesDTO import MiniSeriesDTO

@dataclass(slots=True, frozen=True)
class LeagueEntryDTO:
    leagueId: str = ""
    summonerId: str = ""
    puuid: str = ""
    queueType: Queue = Queue.FLEX
    tier: Tier = Tier.IRON
    rank: Division = Division.I
    leaguePoints: int = 0
    wins: int = 0
    losses: int = 0
    hotStreak: bool = False
    veteran: bool = False
    freshBlood: bool = False
    inactive: bool = False
    miniSeries: MiniSeriesDTO = field(default_factory=MiniSeriesDTO)

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "LeagueEntryDTO":
        payload = dict(data or {})
        return cls(
            leagueId=to_str(payload.get("leagueId")),
            summonerId=to_str(payload.get("summonerId")),
            puuid=to_str(payload.get("puuid")),
            queueType=Queue(payload.get("queueType")),
            tier=Tier(payload.get("tier")),
            rank=Division(payload.get("rank")),
            leaguePoints=to_int(payload.get("leaguePoints")),
            wins=to_int(payload.get("wins")),
            losses=to_int(payload.get("losses")),
            hotStreak=to_bool(payload.get("hotStreak")),
            veteran=to_bool(payload.get("veteran")),
            freshBlood=to_bool(payload.get("freshBlood")),
            inactive=to_bool(payload.get("inactive")),
            miniSeries=MiniSeriesDTO.from_dict(to_dict(payload.get("miniSeries"))),
        )