from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_int, to_str

@dataclass(slots=True, frozen=True)
class RewardConfigDto:
    rewardValue: str = ""
    rewardType: str = ""
    maximumReward: int = 0

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "RewardConfigDto":
        payload = dict(data or {})
        return cls(
            rewardValue=to_str(payload.get("rewardValue")),
            rewardType=to_str(payload.get("rewardType")),
            maximumReward=to_int(payload.get("maximumReward")),
        )
