from dataclasses import dataclass
from typing import Any, Mapping

from pyke.models._coerce import to_str, to_int

@dataclass(slots=True, frozen=True)
class SummonerDTO:
    profileIconId: int = 0
    """ID of the summoner icon associated with the summoner."""
    revisionDate: int = 0
    """Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: profile icon change, playing the tutorial or advanced tutorial, finishing a game, summoner name change."""
    puuid: str = ""
    """Encrypted PUUID. Exact length of 78 characters."""
    summonerLevel: int = 0
    """Summoner level associated with the summoner."""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any] | None) -> "SummonerDTO":
        payload = dict(data or {})
        return cls(
            profileIconId=to_int(payload.get("profileIconId")),
            revisionDate=to_int(payload.get("revisionDate")),
            puuid=to_str(payload.get("puuid")),
            summonerLevel=to_int(payload.get("summonerLevel"))
        )