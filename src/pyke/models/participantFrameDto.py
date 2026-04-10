from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_dict, to_int
from .championStatsDto import ChampionStatsDto
from .damageStatsDto import DamageStatsDto
from .positionDto import PositionDto


@dataclass(slots=True, frozen=True)
class ParticipantFrameDto:
    championStats: ChampionStatsDto = field(default_factory=ChampionStatsDto)
    currentGold: int = 0
    damageStats: DamageStatsDto = field(default_factory=DamageStatsDto)
    goldPerSecond: int = 0
    jungleMinionsKilled: int = 0
    level: int = 0
    minionsKilled: int = 0
    participantId: int = 0
    position: PositionDto = field(default_factory=PositionDto)
    timeEnemySpentControlled: int = 0
    totalGold: int = 0
    xp: int = 0

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "ParticipantFrameDto":
        payload = dict(data or {})
        return cls(
            championStats=ChampionStatsDto.from_dict(to_dict(payload.get("championStats"))),
            currentGold=to_int(payload.get("currentGold")),
            damageStats=DamageStatsDto.from_dict(to_dict(payload.get("damageStats"))),
            goldPerSecond=to_int(payload.get("goldPerSecond")),
            jungleMinionsKilled=to_int(payload.get("jungleMinionsKilled")),
            level=to_int(payload.get("level")),
            minionsKilled=to_int(payload.get("minionsKilled")),
            participantId=to_int(payload.get("participantId")),
            position=PositionDto.from_dict(to_dict(payload.get("position"))),
            timeEnemySpentControlled=to_int(payload.get("timeEnemySpentControlled")),
            totalGold=to_int(payload.get("totalGold")),
            xp=to_int(payload.get("xp")),
        )
