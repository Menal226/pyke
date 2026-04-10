from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_dict_list, to_int, to_str
from .perkStyleSelectionDto import PerkStyleSelectionDto

@dataclass(slots=True, frozen=True)
class PerkStyleDto:
    description: str = ""
    selections: list[PerkStyleSelectionDto] = field(
        default_factory=list[PerkStyleSelectionDto]
    )
    style: int = 0

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "PerkStyleDto":
        payload = dict(data or {})
        return cls(
            description=to_str(payload.get("description")),
            selections=[
                PerkStyleSelectionDto.from_dict(item)
                for item in to_dict_list(payload.get("selections"))
            ],
            style=to_int(payload.get("style")),
        )


