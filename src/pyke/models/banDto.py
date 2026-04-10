from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_int

@dataclass(slots=True, frozen=True)
class BanDto:
    championId: int = 0
    pickTurn: int = 0

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "BanDto":
        payload = dict(data or {})
        return cls(
            championId=to_int(payload.get("championId")),
            pickTurn=to_int(payload.get("pickTurn")),
        )


