import asyncio
import os

from dotenv import load_dotenv

from pyke import Pyke, Region

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")


async def main() -> None:
    async with Pyke(API_KEY) as api:
        # Let's get the current champions in the free rotation
        rotations = await api.champion.rotations(Region.EUW)

        print(f"Max new player level: {rotations['maxNewPlayerLevel']}")

        # The free champions for new players are different
        print(
            f"Free champion ids for new players: {rotations['freeChampionIdsForNewPlayers']}"
        )

        print(f"Free champion ids: {rotations['freeChampionIds']}")


if __name__ == "__main__":
    asyncio.run(main())
