from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_dict, to_dict_list
from .perkStatsDto import PerkStatsDto
from .perkStyleDto import PerkStyleDto

@dataclass(slots=True, frozen=True)
class PerksDto:
    statPerks: PerkStatsDto = field(default_factory=PerkStatsDto)
    styles: list[PerkStyleDto] = field(default_factory=list[PerkStyleDto])

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "PerksDto":
        payload = dict(data or {})
        return cls(
            statPerks=PerkStatsDto.from_dict(to_dict(payload.get("statPerks"))),
            styles=[PerkStyleDto.from_dict(item) for item in to_dict_list(payload.get("styles"))],
        )


