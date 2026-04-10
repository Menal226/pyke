from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_dict_list, to_str, to_str_list
from .statusDto import StatusDto


@dataclass(slots=True, frozen=True)
class PlatformDataDto:
    id: str = ""
    name: str = ""
    locales: list[str] = field(default_factory=list[str])
    maintenances: list[StatusDto] = field(default_factory=list[StatusDto])
    incidents: list[StatusDto] = field(default_factory=list[StatusDto])

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "PlatformDataDto":
        payload = dict(data or {})
        return cls(
            id=to_str(payload.get("id")),
            name=to_str(payload.get("name")),
            locales=to_str_list(payload.get("locales")),
            maintenances=[
                StatusDto.from_dict(item)
                for item in to_dict_list(payload.get("maintenances"))
            ],
            incidents=[
                StatusDto.from_dict(item)
                for item in to_dict_list(payload.get("incidents"))
            ],
        )