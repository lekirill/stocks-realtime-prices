import asyncio
import logging
from fastapi import WebSocket, APIRouter
from websockets.exceptions import ConnectionClosedOK

router = APIRouter()
logger = logging.getLogger("uvicorn")


@router.websocket('/realtime')
async def get_realtime_data(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            await asyncio.sleep(1)
            websocket.app.tickers.make_movement()
            response_data = websocket.app.tickers.get_state()
            await websocket.send_json(response_data)
    except ConnectionClosedOK as e:
        logger.info('connection gracefully closed')
