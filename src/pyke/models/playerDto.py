from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_str
from ..enums.position import Position
from ..enums.role import Role

@dataclass(slots=True, frozen=True)
class PlayerDto:
    puuid: str = ""
    teamId: str = ""
    position: Position = Position.UNSELECTED
    role: Role = Role.MEMBER

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "PlayerDto":
        payload = dict(data or {})

        position_raw = to_str(payload.get("position"), Position.UNSELECTED.value)
        role_raw = to_str(payload.get("role"), Role.MEMBER.value)

        try:
            position = Position(position_raw)
        except ValueError:
            position = Position.UNSELECTED

        try:
            role = Role(role_raw)
        except ValueError:
            role = Role.MEMBER

        return cls(
            puuid=to_str(payload.get("puuid")),
            teamId=to_str(payload.get("teamId")),
            position=position,
            role=role,
        )