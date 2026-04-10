from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_dict, to_dict_list, to_int, to_str
from .bannedChampionDto import BannedChampionDto
from .currentGameParticipantDto import CurrentGameParticipantDto
from .observerDto import ObserverDto


@dataclass(slots=True, frozen=True)
class CurrentGameInfoDto:
    gameId: int = 0
    """The ID of the game"""
    gameType: str = ""
    """The game type"""
    gameStartTime: int = 0
    """The game start time represented in epoch milliseconds"""
    mapId: int = 0
    """The ID of the map"""
    gameLength: int = 0
    """The amount of time in seconds that has passed since the game started"""
    platformId: str = ""
    """The ID of the platform on which the game is being played"""
    gameMode: str = ""
    """The game mode"""
    bannedChampions: list[BannedChampionDto] = field(
        default_factory=lambda: list[BannedChampionDto]()
    )
    """Banned champion information"""
    gameQueueConfigId: int = 0
    """The queue type (queue types are documented on the Game Constants page)"""
    observers: ObserverDto = field(default_factory=ObserverDto)
    """The observer information"""
    participants: list[CurrentGameParticipantDto] = field(
        default_factory=lambda: list[CurrentGameParticipantDto]()
    )
    """The participant information"""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "CurrentGameInfoDto":
        payload = dict(data or {})
        return cls(
            gameId=to_int(payload.get("gameId")),
            gameType=to_str(payload.get("gameType")),
            gameStartTime=to_int(payload.get("gameStartTime")),
            mapId=to_int(payload.get("mapId")),
            gameLength=to_int(payload.get("gameLength")),
            platformId=to_str(payload.get("platformId")),
            gameMode=to_str(payload.get("gameMode")),
            bannedChampions=[
                BannedChampionDto.from_dict(item)
                for item in to_dict_list(payload.get("bannedChampions"))
            ],
            gameQueueConfigId=to_int(payload.get("gameQueueConfigId")),
            observers=ObserverDto.from_dict(to_dict(payload.get("observers"))),
            participants=[
                CurrentGameParticipantDto.from_dict(item)
                for item in to_dict_list(payload.get("participants"))
            ],
        )
