from dataclasses import dataclass, field
from typing import Any, Mapping

from pyke.models._coerce import to_dict, to_int, to_str
from ..models.tournamentPhaseDto import TournamentPhaseDto

@dataclass(slots=True, frozen=True)
class TournamentDto:
    id: int = 0
    themeId: int = 0
    nameKey: str = ""
    nameKeySecondary: str = ""
    schedule: TournamentPhaseDto = field(default_factory=TournamentPhaseDto)

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "TournamentDto":
        payload = dict(data or {})
        return cls(
            id=to_int(payload.get("id")),
            themeId=to_int(payload.get("themeId")),
            nameKey=to_str(payload.get("nameKey")),
            nameKeySecondary=to_str(payload.get("nameKeySecondary")),
            schedule=TournamentPhaseDto.from_dict(to_dict(payload.get("schedule")))
        )