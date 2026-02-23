import asyncio
import os

from dotenv import load_dotenv

from pyke import Continent, Pyke

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")


async def main() -> None:
    async with Pyke(API_KEY) as api:
        account = await api.account.by_riot_id(Continent.EUROPE, "saves", "000")

        print(f"PUUID:     {account['puuid']}")
        print(f"Game name: {account['gameName']}")
        print(f"Tag line:  {account['tagLine']}")

        region = await api.account.region_by_puuid(Continent.EUROPE, account["puuid"])

        print(f"Region:    {region['region']}")


if __name__ == "__main__":
    asyncio.run(main())
