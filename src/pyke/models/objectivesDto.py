from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_dict
from .objectiveDto import ObjectiveDto

@dataclass(slots=True, frozen=True)
class ObjectivesDto:
    baron: ObjectiveDto = field(default_factory=ObjectiveDto)
    champion: ObjectiveDto = field(default_factory=ObjectiveDto)
    dragon: ObjectiveDto = field(default_factory=ObjectiveDto)
    horde: ObjectiveDto = field(default_factory=ObjectiveDto)
    inhibitor: ObjectiveDto = field(default_factory=ObjectiveDto)
    riftHerald: ObjectiveDto = field(default_factory=ObjectiveDto)
    tower: ObjectiveDto = field(default_factory=ObjectiveDto)

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "ObjectivesDto":
        payload = dict(data or {})
        return cls(
            baron=ObjectiveDto.from_dict(to_dict(payload.get("baron"))),
            champion=ObjectiveDto.from_dict(to_dict(payload.get("champion"))),
            dragon=ObjectiveDto.from_dict(to_dict(payload.get("dragon"))),
            horde=ObjectiveDto.from_dict(to_dict(payload.get("horde"))),
            inhibitor=ObjectiveDto.from_dict(to_dict(payload.get("inhibitor"))),
            riftHerald=ObjectiveDto.from_dict(to_dict(payload.get("riftHerald"))),
            tower=ObjectiveDto.from_dict(to_dict(payload.get("tower"))),
        )


