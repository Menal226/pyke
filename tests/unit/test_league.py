import pytest
from httpx import Response
from respx import MockRouter

from pyke import Pyke, Queue, Region


@pytest.mark.asyncio
async def test_challenger_leagues_by_queue(pyke_client: Pyke, respx_mock: MockRouter):
    respx_mock.get(
        "https://euw1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5"
    ).mock(return_value=Response(200, json={"entries": [{"summonerName": "Test"}]}))

    result = await pyke_client.league.challenger_leagues_by_queue(
        Region.EUW, Queue.SOLO_DUO
    )

    assert result["entries"][0]["summonerName"] == "Test"


@pytest.mark.asyncio
async def test_by_puuid(pyke_client: Pyke, respx_mock: MockRouter):
    respx_mock.get(
        "https://euw1.api.riotgames.com/lol/league/v4/entries/by-puuid/{puuid}"
    ).mock(return_value=Response(200, json=[{"tier": "GOLD"}]))

    result = await pyke_client.league.by_puuid(Region.EUW, "{puuid}")

    assert result[0]["tier"] == "GOLD"


# @pytest.mark.asyncio
# async def test_by_queue_tier_division(pyke_client: Pyke):
#     by_queue_tier_division = await pyke_client.league.by_queue_tier_division(
#         Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II, page=2
#     )

#     assert isinstance(by_queue_tier_division, list)

#     for league_entry in by_queue_tier_division:
#         assert isinstance(league_entry, dict)

#     by_queue_tier_division = await pyke_client.league.by_queue_tier_division(
#         Region.EUW, Queue.SOLO_DUO, Tier.GOLD, Division.II
#     )

#     assert isinstance(by_queue_tier_division, list)

#     for league_entry in by_queue_tier_division:
#         assert isinstance(league_entry, dict)


# @pytest.mark.asyncio
# async def test_grandmaster_leagues_by_queue(pyke_client: Pyke):
#     grandmaster_leagues_by_queue = (
#         await pyke_client.league.grandmaster_leagues_by_queue(
#             region=Region.EUW, queue=Queue.SOLO_DUO
#         )
#     )

#     league_list = grandmaster_leagues_by_queue["entries"]

#     assert isinstance(grandmaster_leagues_by_queue, dict)
#     assert isinstance(league_list, list)

#     for league_entry in grandmaster_leagues_by_queue["entries"]:
#         assert isinstance(league_entry, dict)


# @pytest.mark.asyncio
# async def test_by_league_id(pyke_client: Pyke):
#     if not TEST_LEAGUE_ID:
#         quit()

#     by_league_id = await pyke_client.league.by_league_id(
#         region=Region.EUW, league_id=TEST_LEAGUE_ID
#     )

#     league_list = by_league_id["entries"]

#     assert isinstance(by_league_id, dict)
#     assert isinstance(league_list, list)

#     for league_entry in by_league_id["entries"]:
#         assert isinstance(league_entry, dict)


@pytest.mark.asyncio
async def test_master_leagues_by_queue(pyke_client: Pyke, respx_mock: MockRouter):
    respx_mock.get(
        "https://euw1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5"
    ).mock(return_value=Response(200, json={"entries": [{"summonerName": "Test"}]}))

    result = await pyke_client.league.master_leagues_by_queue(
        Region.EUW, Queue.SOLO_DUO
    )

    assert result["entries"][0]["summonerName"] == "Test"
