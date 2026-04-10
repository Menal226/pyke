from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any, cast

from .participantFrameDto import ParticipantFrameDto


@dataclass(slots=True, frozen=True)
class ParticipantFramesDto:
    frames: dict[str, ParticipantFrameDto] = field(
        default_factory=lambda: cast(dict[str, ParticipantFrameDto], {})
    )
    """Key value mapping for each participant"""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "ParticipantFramesDto":
        payload = dict(data or {})
        frames: dict[str, ParticipantFrameDto] = {}
        for key, value in payload.items():
            if isinstance(value, Mapping):
                frames[str(key)] = ParticipantFrameDto.from_dict(cast(Mapping[str, Any], value))

        return cls(frames=frames)
