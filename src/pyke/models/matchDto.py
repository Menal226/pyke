from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_dict
from .infoDto import InfoDto
from .metadataDto import MetadataDto

@dataclass(slots=True, frozen=True)
class MatchDto:
    metadata: MetadataDto = field(default_factory=MetadataDto)
    """Match metadata."""
    info: InfoDto = field(default_factory=InfoDto)
    """Match info."""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "MatchDto":
        payload = dict(data or {})
        return cls(
            metadata=MetadataDto.from_dict(to_dict(payload.get("metadata"))),
            info=InfoDto.from_dict(to_dict(payload.get("info"))),
        )


