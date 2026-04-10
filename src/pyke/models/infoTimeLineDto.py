from dataclasses import dataclass, field
from typing import Any, Mapping, cast

from ._coerce import to_int
from .framesTimeLineDto import FramesTimeLineDto
from .participantTimeLineDto import ParticipantTimeLineDto


@dataclass(slots=True, frozen=True)
class InfoTimeLineDto:
    frameInterval: int = 0
    """Number of milliseconds between each frame therein"""
    frames: list[FramesTimeLineDto] = field(default_factory=list[FramesTimeLineDto])
    participants: list[ParticipantTimeLineDto] = field(default_factory=list[ParticipantTimeLineDto])

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "InfoTimeLineDto":
        payload = dict(data or {})
        return cls(
            frameInterval=to_int(payload.get("frameInterval")),
            frames=[
                FramesTimeLineDto.from_dict(cast(Mapping[str, Any], item))
                for item in payload.get("frames", [])
                if isinstance(item, Mapping)
            ],
            participants=[
                ParticipantTimeLineDto.from_dict(cast(Mapping[str, Any], item))
                for item in payload.get("participants", [])
                if isinstance(item, Mapping)
            ],
        )
