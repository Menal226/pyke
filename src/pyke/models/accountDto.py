from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_str

@dataclass(slots=True, frozen=True)
class AccountDto:
    puuid: str = ""
    gameName: str = ""
    tagLine: str = ""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "AccountDto":
        payload = dict(data or {})
        return cls(
            puuid=to_str(payload.get("puuid")),
            gameName=to_str(payload.get("gameName")),
            tagLine=to_str(payload.get("tagLine")),
        )