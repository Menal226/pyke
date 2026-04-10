from dataclasses import dataclass, field
from typing import Any, Mapping

from ._coerce import to_bool, to_dict, to_dict_list, to_int, to_str
from .gameCustomizationObjectDto import GameCustomizationObjectDto
from .spectatorPerksDto import SpectatorPerksDto


@dataclass(slots=True, frozen=True)
class CurrentGameParticipantDto:
    championId: int = 0
    """The ID of the champion played by this participant"""
    perks: SpectatorPerksDto = field(default_factory=SpectatorPerksDto)
    """Perks/Runes Reforged Information"""
    profileIconId: int = 0
    """The ID of the profile icon used by this participant"""
    bot: bool = False
    """Flag indicating whether or not this participant is a bot"""
    teamId: int = 0
    """The team ID of this participant, indicating the participant's team"""
    puuid: str = ""
    """The encrypted puuid of this participant. null when the player is anonym."""
    spell1Id: int = 0
    """The ID of the first summoner spell used by this participant"""
    spell2Id: int = 0
    """The ID of the second summoner spell used by this participant"""
    gameCustomizationObjects: list[GameCustomizationObjectDto] = field(
        default_factory=lambda: list[GameCustomizationObjectDto]()
    )
    """List of Game Customizations"""

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "CurrentGameParticipantDto":
        payload = dict(data or {})
        return cls(
            championId=to_int(payload.get("championId")),
            perks=SpectatorPerksDto.from_dict(to_dict(payload.get("perks"))),
            profileIconId=to_int(payload.get("profileIconId")),
            bot=to_bool(payload.get("bot")),
            teamId=to_int(payload.get("teamId")),
            puuid=to_str(payload.get("puuid")),
            spell1Id=to_int(payload.get("spell1Id")),
            spell2Id=to_int(payload.get("spell2Id")),
            gameCustomizationObjects=[
                GameCustomizationObjectDto.from_dict(item)
                for item in to_dict_list(payload.get("gameCustomizationObjects"))
            ],
        )
