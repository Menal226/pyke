from dataclasses import dataclass
from typing import Any, Mapping

from ._coerce import to_str


@dataclass(slots=True, frozen=True)
class ObserverDto:
    encryptionKey: str = ""
    """Key used to decrypt the spectator grid game data for playback"""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "ObserverDto":
        payload = dict(data or {})
        return cls(encryptionKey=to_str(payload.get("encryptionKey")))
