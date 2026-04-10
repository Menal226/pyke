from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_dict_list, to_int, to_str
from .participantDto import ParticipantDto
from .teamDto import TeamDto

@dataclass(slots=True, frozen=True)
class InfoDto:
    endOfGameResult: str = ""
    """Refer to indicate if the game ended in termination."""
    gameCreation: int = 0
    """Unix timestamp for when the game is created on the game server (i.e., the loading screen)."""
    gameDuration: int = 0
    """Prior to patch 11.20, this field returns the game length in milliseconds calculated from gameEndTimestamp - gameStartTimestamp. Post patch 11.20, this field returns the max timePlayed of any participant in the game in seconds, which makes the behavior of this field consistent with that of match-v4. The best way to handling the change in this field is to treat the value as milliseconds if the gameEndTimestamp field isn't in the response and to treat the value as seconds if gameEndTimestamp is in the response."""
    gameEndTimestamp: int = 0
    """Unix timestamp for when match ends on the game server. This timestamp can occasionally be significantly longer than when the match \"ends\". The most reliable way of determining the timestamp for the end of the match would be to add the max time played of any participant to the gameStartTimestamp. This field was added to match-v5 in patch 11.20 on Oct 5th, 2021."""
    gameId: int = 0
    gameMode: str = ""
    """Refer to the Game Constants documentation."""
    gameName: str = ""
    gameStartTimestamp: int = 0
    """Unix timestamp for when match starts on the game server."""
    gameType: str = ""
    gameVersion: str = ""
    """The first two parts can be used to determine the patch a game was played on."""
    mapId: int = 0
    """Refer to the Game Constants documentation."""
    participants: list[ParticipantDto] = field(default_factory=list[ParticipantDto])
    platformId: str = ""
    """Platform where the match was played."""
    queueId: int = 0
    """Refer to the Game Constants documentation."""
    teams: list[TeamDto] = field(default_factory=list[TeamDto])
    tournamentCode: str = ""
    """Tournament code used to generate the match. This field was added to match-v5 in patch 11.13 on June 23rd, 2021."""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "InfoDto":
        payload = dict(data or {})
        return cls(
            endOfGameResult=to_str(payload.get("endOfGameResult")),
            gameCreation=to_int(payload.get("gameCreation")),
            gameDuration=to_int(payload.get("gameDuration")),
            gameEndTimestamp=to_int(payload.get("gameEndTimestamp")),
            gameId=to_int(payload.get("gameId")),
            gameMode=to_str(payload.get("gameMode")),
            gameName=to_str(payload.get("gameName")),
            gameStartTimestamp=to_int(payload.get("gameStartTimestamp")),
            gameType=to_str(payload.get("gameType")),
            gameVersion=to_str(payload.get("gameVersion")),
            mapId=to_int(payload.get("mapId")),
            participants=[
                ParticipantDto.from_dict(item)
                for item in to_dict_list(payload.get("participants"))
            ],
            platformId=to_str(payload.get("platformId")),
            queueId=to_int(payload.get("queueId")),
            teams=[TeamDto.from_dict(item) for item in to_dict_list(payload.get("teams"))],
            tournamentCode=to_str(payload.get("tournamentCode")),
        )


