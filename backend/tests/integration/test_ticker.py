from fastapi.testclient import TestClient


def test_get_tickers(test_app):
    with TestClient(test_app) as client:
        test_app.tree_cache = {}
        response = client.get(
            'tickers/',
        )
        assert response.status_code == 200
        assert 'ticker_list' in response.json()
        response_data = response.json()
        assert isinstance(response_data['ticker_list'], list)
