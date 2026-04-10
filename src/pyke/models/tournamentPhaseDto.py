from dataclasses import dataclass
from typing import Any, Mapping

from pyke.models._coerce import to_bool, to_int

@dataclass(slots=True, frozen=True)
class TournamentPhaseDto:
    id: int = 0
    registrationTime: int = 0
    startTime: int = 0
    cancelled: bool = False
    
    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "TournamentPhaseDto":
        payload = dict(data or {})
        return cls(
            id=to_int(payload.get("id")),
            registrationTime=to_int(payload.get("registrationTime")),
            startTime=to_int(payload.get("startTime")),
            cancelled=to_bool(payload.get("cancelled"))
        )