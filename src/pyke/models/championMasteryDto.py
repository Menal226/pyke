from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_bool, to_dict, to_int, to_str, to_str_list
from .nextSeasonMilestonesDto import NextSeasonMilestonesDto

@dataclass(slots=True, frozen=True)
class ChampionMasteryDto:
    puuid: str = ""
    championPointsUntilNextLevel: int = 0
    chestGranted: bool = False
    championId: int = 0
    lastPlayTime: int = 0
    championLevel: int = 0
    championPoints: int = 0
    championPointsSinceLastLevel: int = 0
    markRequiredForNextLevel: int = 0
    championSeasonMilestone: int = 0
    nextSeasonMilestone: NextSeasonMilestonesDto = field(
        default_factory=NextSeasonMilestonesDto
    )
    tokensEarned: int = 0
    milestoneGrades: list[str] = field(default_factory=list[str])

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "ChampionMasteryDto":
        payload = dict(data or {})
        return cls(
            puuid=to_str(payload.get("puuid")),
            championPointsUntilNextLevel=to_int(
                payload.get("championPointsUntilNextLevel")
            ),
            chestGranted=to_bool(payload.get("chestGranted")),
            championId=to_int(payload.get("championId")),
            lastPlayTime=to_int(payload.get("lastPlayTime")),
            championLevel=to_int(payload.get("championLevel")),
            championPoints=to_int(payload.get("championPoints")),
            championPointsSinceLastLevel=to_int(
                payload.get("championPointsSinceLastLevel")
            ),
            markRequiredForNextLevel=to_int(payload.get("markRequiredForNextLevel")),
            championSeasonMilestone=to_int(payload.get("championSeasonMilestone")),
            nextSeasonMilestone=NextSeasonMilestonesDto.from_dict(
                to_dict(payload.get("nextSeasonMilestone"))
            ),
            tokensEarned=to_int(payload.get("tokensEarned")),
            milestoneGrades=to_str_list(payload.get("milestoneGrades")),
        )