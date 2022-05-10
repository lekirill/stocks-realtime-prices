from typing import Dict, List
from datetime import datetime

from app.core.tickers.func import generate_movement
from app.core.tickers.exceptions import NumOfTickersNegativeError, InitialPriceNegativeError


class Ticker:

    def __init__(self, num_of_tickers: int = 100, initial_price: int = 0):
        if num_of_tickers <= 0:
            raise NumOfTickersNegativeError
        if initial_price < 0:
            raise InitialPriceNegativeError
        self.tickers = {
            f'ticker_{str(x).zfill(len(str(num_of_tickers)) - 1)}':
                {
                    'time': [datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), ],
                    'price': [initial_price, ],
                }
            for x in range(num_of_tickers)
        }

    def make_movement(self):
        for ticker, data in self.tickers.items():
            self.tickers[ticker]['time'].append(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))
            self.tickers[ticker]['price'].append(self.tickers[ticker]['price'][-1] + generate_movement())

    def get_state(self) -> Dict:
        return self.tickers

    def get_tickers(self) -> List:
        return list(self.tickers.keys())
