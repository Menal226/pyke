from typing import Any

from ..enums.region import Region

from .._base_client import _BaseApiClient


class StatusEndpoint:
    def __init__(self, client: _BaseApiClient):
        self._client = client

    async def platform_data(self, region: Region) -> dict[Any, Any]:
        """# Get League of Legends status for the given platform

        **Example:**  
            `status = await api.lol_status.platform_data(Region.EUW)`

        **Args:**  
            `region (Region)` [Region](/pyke/pyke.html#Region) to execute against.  

        **Returns:**  
            `dict[Any, Any]`
        """  # fmt: skip

        path = "/lol/status/v4/platform-data"
        data = await self._client._region_request(region=region, path=path)

        return data
