from ..models.summonerDTO import SummonerDTO

from .._base_riot_client import _BaseRiotClient
from ..enums.region import Region


class SummonerEndpoint:
    def __init__(self, client: _BaseRiotClient):
        self._client = client

    async def by_puuid(self, region: Region, puuid: str) -> SummonerDTO:
        """# Get a summoner by PUUID.

        **Example:**  
            `summoner = await api.summoner.by_puuid(Region.EUW, "some puuid")`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  
            `puuid (str)` Encrypted PUUID. Exact length of 78 characters.  

        **Returns:**  
            `SummonerDTO`
        """  # fmt: skip

        path = f"/lol/summoner/v4/summoners/by-puuid/{puuid}"
        data = await self._client._request(region=region, path=path)

        return SummonerDTO.from_dict(data)
