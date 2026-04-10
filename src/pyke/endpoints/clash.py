from ..models.playerDto import PlayerDto
from ..models.teamDto import TeamDto
from ..models.tournamentDto import TournamentDto

from .._base_riot_client import _BaseRiotClient
from ..enums.region import Region


class ClashEndpoint:
    def __init__(self, client: _BaseRiotClient):
        self._client = client

    async def by_puuid(self, region: Region, puuid: str) -> list[PlayerDto]:
        """# Get players by puuid

        **Example:**  
            `players = await api.clash.by_puuid(Region.EUW, "some puuid")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `list[PlayerDto]`
        """  # fmt: skip

        path = f"/lol/clash/v1/players/by-puuid/{puuid}"
        data = await self._client._request(region=region, path=path)

        return [PlayerDto.from_dict(entry) for entry in data]

    async def by_team_id(self, region: Region, team_id: str) -> TeamDto:
        """# Get team by ID

        **Example:**  
            `team = await api.clash.by_team_id(Region.EUW, "some team id")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `team_id (str)` Team id of the clash team.  

        **Returns:**  
            `TeamDto`
        """  # fmt: skip

        path = f"/lol/clash/v1/teams/{team_id}"
        data = await self._client._request(region=region, path=path)

        return TeamDto.from_dict(data)

    async def tournaments(self, region: Region) -> list[TournamentDto]:
        """# Get all active or upcoming tournaments

        **Example:**  
            `tournaments = await api.clash.tournaments(Region.EUW)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  

        **Returns:**  
            `list[TournamentDto]`
        """  # fmt: skip

        path = "/lol/clash/v1/tournaments"
        data = await self._client._request(region=region, path=path)

        return [TournamentDto.from_dict(entry) for entry in data]

    async def tournament_by_team_id(
        self, region: Region, team_id: str
    ) -> TournamentDto:
        """# Get tournament by team ID

        **Example:**  
            `tournament = await api.clash.tournament_by_team_id(Region.EUW, "some team id")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `team_id (str)` Team id of the clash team.  

        **Returns:**  
            `TournamentDto`
        """  # fmt: skip

        path = f"/lol/clash/v1/tournaments/by-team/{team_id}"
        data = await self._client._request(region=region, path=path)

        return TournamentDto.from_dict(data)

    async def tournament_by_tournament_id(
        self, region: Region, tournament_id: int
    ) -> TournamentDto:
        """# Get tournament by ID

        **Example:**  
            `tournament = await api.clash.tournament_by_tournament_id(Region.EUW, 12345)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `tournament_id (int)` Tournament id of the clash.  

        **Returns:**  
            `TournamentDto`
        """  # fmt: skip

        path = f"/lol/clash/v1/tournaments/{tournament_id}"
        data = await self._client._request(region=region, path=path)

        return TournamentDto.from_dict(data)
