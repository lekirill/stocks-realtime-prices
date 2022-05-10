import asyncio
import pytest
from fastapi import FastAPI

from app.core.tickers.ticker import Ticker
from app.api import realtimedata
from app.api import tickers

app = FastAPI()


@pytest.fixture()
def test_app():
    @app.on_event("startup")
    async def startup():
        app.tickers = Ticker()

    app.include_router(realtimedata.router)
    app.include_router(tickers.router)
    return app
