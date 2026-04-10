from dataclasses import dataclass, field
from typing import Any, Mapping

from ..enums.publish_location import PublishLocation
from ._coerce import to_bool, to_dict_list, to_int, to_str, to_str_list
from .contentDto import ContentDto


@dataclass(slots=True, frozen=True)
class UpdateDto:
    id: int = 0
    author: str = ""
    publish: bool = False
    publish_locations: list[PublishLocation] = field(default_factory=list[PublishLocation])
    """Publish targets. Legal values: riotclient, riotstatus, game."""
    translations: list[ContentDto] = field(default_factory=list[ContentDto])
    created_at: str = ""
    updated_at: str = ""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "UpdateDto":
        payload = dict(data or {})

        location_values = to_str_list(payload.get("publish_locations"))
        publish_locations: list[PublishLocation] = []
        for value in location_values:
            try:
                publish_locations.append(PublishLocation(value))
            except ValueError:
                continue

        return cls(
            id=to_int(payload.get("id")),
            author=to_str(payload.get("author")),
            publish=to_bool(payload.get("publish")),
            publish_locations=publish_locations,
            translations=[
                ContentDto.from_dict(item)
                for item in to_dict_list(payload.get("translations"))
            ],
            created_at=to_str(payload.get("created_at")),
            updated_at=to_str(payload.get("updated_at")),
        )