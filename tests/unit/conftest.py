from typing import AsyncGenerator

import pytest_asyncio
import respx

from pyke import Pyke


@pytest_asyncio.fixture(scope="session")
async def pyke_client() -> AsyncGenerator[Pyke, None]:
    async with Pyke("RGAPI-000000000000000000000000000000000000") as client:
        yield client


@pytest_asyncio.fixture(autouse=True)
async def respx_mock() -> AsyncGenerator[respx.MockRouter, None]:
    with respx.mock(assert_all_called=False) as mock:
        yield mock
