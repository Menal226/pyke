from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_bool, to_dict, to_dict_list, to_int
from .banDto import BanDto
from .objectivesDto import ObjectivesDto

@dataclass(slots=True, frozen=True)
class TeamDto:
    bans: list[BanDto] = field(default_factory=list[BanDto])
    objectives: ObjectivesDto = field(default_factory=ObjectivesDto)
    teamId: int = 0
    win: bool = False

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "TeamDto":
        payload = dict(data or {})
        return cls(
            bans=[BanDto.from_dict(item) for item in to_dict_list(payload.get("bans"))],
            objectives=ObjectivesDto.from_dict(to_dict(payload.get("objectives"))),
            teamId=to_int(payload.get("teamId")),
            win=to_bool(payload.get("win")),
        )


