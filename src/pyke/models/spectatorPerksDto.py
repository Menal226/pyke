from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_int, to_int_list


@dataclass(slots=True, frozen=True)
class SpectatorPerksDto:
    perkIds: list[int] = field(default_factory=lambda: list[int]())
    """IDs of the perks/runes assigned."""
    perkStyle: int = 0
    """Primary runes path"""
    perkSubStyle: int = 0
    """Secondary runes path"""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "SpectatorPerksDto":
        payload = dict(data or {})
        return cls(
            perkIds=to_int_list(payload.get("perkIds")),
            perkStyle=to_int(payload.get("perkStyle")),
            perkSubStyle=to_int(payload.get("perkSubStyle")),
        )
