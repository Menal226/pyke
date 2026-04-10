from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_int, to_str


@dataclass(slots=True, frozen=True)
class ParticipantTimeLineDto:
    puuid: str = ""
    participantId: int = 0

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "ParticipantTimeLineDto":
        payload = dict(data or {})
        return cls(
            puuid=to_str(payload.get("puuid")),
            participantId=to_int(payload.get("participantId")),
        )
