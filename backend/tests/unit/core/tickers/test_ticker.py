import pytest
from app.core.tickers.ticker import Ticker
from app.core.tickers.exceptions import NumOfTickersNegativeError, InitialPriceNegativeError


def test_tickers_make_movement():
    tickers = Ticker(num_of_tickers=10)
    for ticker, data in tickers.tickers.items():
        assert len(data['time']) == 1
    tickers.make_movement()
    for ticker, data in tickers.tickers.items():
        assert len(data['time']) == 2


def test_tickers_get_tickers():
    tickers = Ticker(num_of_tickers=10)
    assert tickers.get_tickers() == list(tickers.tickers.keys())


def test_tickers_get_state():
    tickers = Ticker(num_of_tickers=10)
    assert tickers.get_state() == tickers.tickers


def test_negative_num_of_tickers_exception():
    with pytest.raises(NumOfTickersNegativeError):
        tickers = Ticker(num_of_tickers=-1)


def test_negative_initial_price_exception():
    with pytest.raises(InitialPriceNegativeError):
        tickers = Ticker(initial_price=-100)
