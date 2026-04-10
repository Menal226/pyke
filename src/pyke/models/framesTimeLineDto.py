from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_dict, to_int
from .eventsTimeLineDto import EventsTimeLineDto
from .participantFramesDto import ParticipantFramesDto


@dataclass(slots=True, frozen=True)
class FramesTimeLineDto:
    participantFrames: ParticipantFramesDto = field(default_factory=ParticipantFramesDto)
    """A frame contains all events that occurred during a particular timeframe"""
    events: list[EventsTimeLineDto] = field(default_factory=list[EventsTimeLineDto])
    """Event happened either at the beginning of the frame or during the frame."""
    timestamp: int = 0

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "FramesTimeLineDto":
        payload = dict(data or {})
        return cls(
            participantFrames=ParticipantFramesDto.from_dict(payload.get("participantFrames", {})),
            events=[
                EventsTimeLineDto.from_dict(to_dict(item))
                for item in payload.get("events", [])
                if isinstance(item, Mapping)
            ],
            timestamp=to_int(payload.get("timestamp")),
        )
