from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_int


@dataclass(slots=True, frozen=True)
class DamageStatsDto:
    magicDamageDone: int = 0
    magicDamageDoneToChampions: int = 0
    magicDamageTaken: int = 0
    physicalDamageDone: int = 0
    physicalDamageDoneToChampions: int = 0
    physicalDamageTaken: int = 0
    totalDamageDone: int = 0
    totalDamageDoneToChampions: int = 0
    totalDamageTaken: int = 0
    trueDamageDone: int = 0
    trueDamageDoneToChampions: int = 0
    trueDamageTaken: int = 0

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "DamageStatsDto":
        payload = dict(data or {})
        return cls(
            magicDamageDone=to_int(payload.get("magicDamageDone")),
            magicDamageDoneToChampions=to_int(payload.get("magicDamageDoneToChampions")),
            magicDamageTaken=to_int(payload.get("magicDamageTaken")),
            physicalDamageDone=to_int(payload.get("physicalDamageDone")),
            physicalDamageDoneToChampions=to_int(payload.get("physicalDamageDoneToChampions")),
            physicalDamageTaken=to_int(payload.get("physicalDamageTaken")),
            totalDamageDone=to_int(payload.get("totalDamageDone")),
            totalDamageDoneToChampions=to_int(payload.get("totalDamageDoneToChampions")),
            totalDamageTaken=to_int(payload.get("totalDamageTaken")),
            trueDamageDone=to_int(payload.get("trueDamageDone")),
            trueDamageDoneToChampions=to_int(payload.get("trueDamageDoneToChampions")),
            trueDamageTaken=to_int(payload.get("trueDamageTaken")),
        )
