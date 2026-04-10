from ..models.championInfo import ChampionInfo

from .._base_riot_client import _BaseRiotClient
from ..enums.region import Region


class ChampionEndpoint:
    def __init__(self, client: _BaseRiotClient):
        self._client = client

    async def rotations(self, region: Region) -> ChampionInfo:
        """# Returns champion rotations, including free-to-play and low-level free-to-play rotations

        **Example:**  
            `rotations = await api.champion.rotations(Region.EUW)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  

        **Returns:**  
            `ChampionInfo`
        """  # fmt: skip

        path = "/lol/platform/v3/champion-rotations"
        data = await self._client._request(region=region, path=path)

        return ChampionInfo.from_dict(data)
