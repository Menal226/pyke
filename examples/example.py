import asyncio
import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, exceptions

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")


async def main() -> None:
    # Initialize the API
    async with Pyke(API_KEY, timeout=60, print_url=True) as api:
        # Every pyke method follows the same convention as the Riot API
        # For example account/v1/accounts/by-riot-id/{gameName}/{tagLine} becomes:
        account = await api.account.by_riot_id(Continent.EUROPE, "saves", "000")

        print(f"Riot ID: {account['gameName']}#{account['tagLine']}")
        print(f"PUUID:   {account['puuid']}")

        # pyke throws typed exceptions matching Riot API error codes
        try:
            region = await api.account.region_by_puuid(
                Continent.EUROPE, account["puuid"]
            )
        except exceptions.DataNotFound as e:
            print(e)  # Output: Data not found (Error Code: 404)
            quit()

        print(f"Region:  {region['region']}")


if __name__ == "__main__":
    asyncio.run(main())
