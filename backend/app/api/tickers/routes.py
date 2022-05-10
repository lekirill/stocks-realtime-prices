from fastapi import Request, APIRouter

from app.api.tickers.models import TickerListBase

router = APIRouter()


@router.get('/tickers', response_model=TickerListBase)
async def get_tickers_list(request: Request):
    response = TickerListBase(ticker_list=request.app.tickers.get_tickers())
    return response
