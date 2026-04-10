from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_int, to_str_list

@dataclass(slots=True, frozen=True)
class ReplayDTO:
    total: int = 0
    matchFileURLs: list[str] = field(default_factory=list[str])

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "ReplayDTO":
        payload = dict(data or {})
        return cls(
            total=to_int(payload.get("total")),
            matchFileURLs=to_str_list(payload.get("matchFileURLs"))
        )