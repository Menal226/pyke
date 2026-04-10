from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_int


@dataclass(slots=True, frozen=True)
class BannedChampionDto:
    pickTurn: int = 0
    """The turn during which the champion was banned"""
    championId: int = 0
    """The ID of the banned champion"""
    teamId: int = 0
    """The ID of the team that banned the champion"""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "BannedChampionDto":
        payload = dict(data or {})
        return cls(
            pickTurn=to_int(payload.get("pickTurn")),
            championId=to_int(payload.get("championId")),
            teamId=to_int(payload.get("teamId")),
        )
