import asyncio
import os

from dotenv import load_dotenv

from pyke import Continent, Pyke, Region

load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")


async def main() -> None:
    async with Pyke(API_KEY) as api:
        account = await api.account.by_riot_id(Continent.EUROPE, "saves", "000")
        current_game = await api.spectator.by_puuid(
            Region.EUW,
            account["puuid"],
        )

        teams = {100: "Blue", 200: "Red"}

        for banned_champion in current_game["bannedChampions"]:
            team = teams[banned_champion["teamId"]]
            print(
                f"Team: {team} Pick: {banned_champion['pickTurn']} Banned champion: {banned_champion['championId']}"
            )


if __name__ == "__main__":
    asyncio.run(main())
