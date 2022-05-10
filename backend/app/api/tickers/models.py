from pydantic import BaseModel
from typing import List


class TickerListBase(BaseModel):
    ticker_list: List[str] = []
