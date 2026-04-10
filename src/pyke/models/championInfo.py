from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_int, to_int_list

@dataclass(slots=True, frozen=True)
class ChampionInfo:
    maxNewPlayerLevel: int = 0
    freeChampionIdsForNewPlayers: list[int] = field(default_factory=list[int])
    freeChampionIds: list[int] = field(default_factory=list[int])

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "ChampionInfo":
        payload = dict(data or {})
        return cls(
            maxNewPlayerLevel=to_int(payload.get("maxNewPlayerLevel")),
            freeChampionIdsForNewPlayers=to_int_list(
                payload.get("freeChampionIdsForNewPlayers")
            ),
            freeChampionIds=to_int_list(payload.get("freeChampionIds")),
        )