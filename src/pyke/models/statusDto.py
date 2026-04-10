from dataclasses import dataclass, field
from typing import Any, Mapping

from ..enums.incident_severity import IncidentSeverity
from ..enums.maintenance_status import MaintenanceStatus
from ..enums.platform import Platform
from ._coerce import to_dict_list, to_int, to_str, to_str_list
from .contentDto import ContentDto
from .updateDto import UpdateDto

@dataclass(slots=True, frozen=True)
class StatusDto:
    id: int = 0
    maintenance_status: MaintenanceStatus = MaintenanceStatus.COMPLETE
    incident_severity: IncidentSeverity = IncidentSeverity.INFO
    titles: list[ContentDto] = field(default_factory=list[ContentDto])
    updates: list[UpdateDto] = field(default_factory=list[UpdateDto])
    created_at: str = ""
    archive_at: str = ""
    updated_at: str = ""
    platforms: list[Platform] = field(default_factory=list[Platform])

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "StatusDto":
        payload = dict(data or {})

        maintenance_status_raw = to_str(payload.get("maintenance_status", MaintenanceStatus.COMPLETE.value))
        incident_severity_raw = to_str(payload.get("incident_severity", IncidentSeverity.INFO.value))

        try:
            maintenance_status = MaintenanceStatus(maintenance_status_raw)
        except ValueError:
            maintenance_status = MaintenanceStatus.COMPLETE

        try:
            incident_severity = IncidentSeverity(incident_severity_raw)
        except ValueError:
            incident_severity = IncidentSeverity.INFO

        platform_values = to_str_list(payload.get("platforms"))
        platforms: list[Platform] = []
        for value in platform_values:
            try:
                platforms.append(Platform(value))
            except ValueError:
                continue

        return cls(
            id=to_int(payload.get("id")),
            maintenance_status=maintenance_status,
            incident_severity=incident_severity,
            titles=[ContentDto.from_dict(item) for item in to_dict_list(payload.get("titles"))],
            updates=[UpdateDto.from_dict(item) for item in to_dict_list(payload.get("updates"))],
            created_at=to_str(payload.get("created_at")),
            archive_at=to_str(payload.get("archive_at")),
            updated_at=to_str(payload.get("updated_at")),
            platforms=platforms,
        )
