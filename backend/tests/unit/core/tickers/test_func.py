from app.core.tickers.func import generate_movement


def test_generate_movement():
    movement_value = generate_movement()
    assert movement_value in (1, -1)
