from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_str

@dataclass(slots=True, frozen=True)
class AccountRegionDTO:
    puuid: str = ""
    game: str = ""
    region: str = ""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "AccountRegionDTO":
        payload = dict(data or {})
        return cls(
            puuid=to_str(payload.get("puuid")),
            game=to_str(payload.get("game")),
            region=to_str(payload.get("region")),
        )