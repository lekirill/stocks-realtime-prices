import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.tickers.ticker import Ticker
from app.api import realtimedata
from app.api import tickers

logger = logging.getLogger("uvicorn")


def create_app() -> FastAPI:
    application = FastAPI()
    origins = [
        "*",
        "http://localhost",
        "http://0.0.0.0:8080",
        "http://0.0.0.0:8081",
        "http://localhost:8081",
        "http://localhost:3007",
    ]

    @application.on_event("startup")
    async def startup_event():
        application.tickers = Ticker()

    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
    application.include_router(realtimedata.router)
    application.include_router(tickers.router)
    return application


app = create_app()
