from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_int

@dataclass(slots=True, frozen=True)
class MissionsDto:
    playerScore0: int = 0
    playerScore1: int = 0
    playerScore2: int = 0
    playerScore3: int = 0
    playerScore4: int = 0
    playerScore5: int = 0
    playerScore6: int = 0
    playerScore7: int = 0
    playerScore8: int = 0
    playerScore9: int = 0
    playerScore10: int = 0
    playerScore11: int = 0

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "MissionsDto":
        payload = dict(data or {})
        return cls(
            playerScore0=to_int(payload.get("playerScore0")),
            playerScore1=to_int(payload.get("playerScore1")),
            playerScore2=to_int(payload.get("playerScore2")),
            playerScore3=to_int(payload.get("playerScore3")),
            playerScore4=to_int(payload.get("playerScore4")),
            playerScore5=to_int(payload.get("playerScore5")),
            playerScore6=to_int(payload.get("playerScore6")),
            playerScore7=to_int(payload.get("playerScore7")),
            playerScore8=to_int(payload.get("playerScore8")),
            playerScore9=to_int(payload.get("playerScore9")),
            playerScore10=to_int(payload.get("playerScore10")),
            playerScore11=to_int(payload.get("playerScore11")),
        )


