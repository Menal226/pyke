from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_dict
from .infoTimeLineDto import InfoTimeLineDto
from .metadataTimeLineDto import MetadataTimeLineDto


@dataclass(slots=True, frozen=True)
class TimelineDto:
	metadata: MetadataTimeLineDto = field(default_factory=MetadataTimeLineDto)
	info: InfoTimeLineDto = field(default_factory=InfoTimeLineDto)

	@classmethod
	def from_dict(cls, data: Mapping[str, Any]) -> "TimelineDto":
		payload = dict(data or {})
		return cls(
			metadata=MetadataTimeLineDto.from_dict(to_dict(payload.get("metadata"))),
			info=InfoTimeLineDto.from_dict(to_dict(payload.get("info"))),
		)
