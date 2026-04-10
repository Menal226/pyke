from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_int

@dataclass(slots=True, frozen=True)
class PerkStyleSelectionDto:
    perk: int = 0
    var1: int = 0
    var2: int = 0
    var3: int = 0

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "PerkStyleSelectionDto":
        payload = dict(data or {})
        return cls(
            perk=to_int(payload.get("perk")),
            var1=to_int(payload.get("var1")),
            var2=to_int(payload.get("var2")),
            var3=to_int(payload.get("var3")),
        )


