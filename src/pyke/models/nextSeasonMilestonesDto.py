from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_bool, to_dict, to_int
from .rewardConfigDto import RewardConfigDto

@dataclass(slots=True, frozen=True)
class NextSeasonMilestonesDto:
    requireGradeCounts: dict[str, Any] = field(default_factory=dict[str, Any])
    rewardMarks: int = 0
    bonus: bool = False
    rewardConfig: RewardConfigDto = field(default_factory=RewardConfigDto)

    @classmethod
    def from_dict(
        cls, data: Mapping[str, Any] | None
    ) -> "NextSeasonMilestonesDto":
        payload = dict(data or {})
        return cls(
            requireGradeCounts=to_dict(payload.get("requireGradeCounts")),
            rewardMarks=to_int(payload.get("rewardMarks")),
            bonus=to_bool(payload.get("bonus")),
            rewardConfig=RewardConfigDto.from_dict(to_dict(payload.get("rewardConfig"))),
        )