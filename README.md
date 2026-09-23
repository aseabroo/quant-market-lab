# Quantum Flux Trading

An early Python/Flask experiment with stock-price charts and Alpaca paper-trading API calls.

The web app fetches time-series data from Alpha Vantage and renders a Plotly candlestick chart. A separate page retrieves an Alpaca paper account and submits paper orders. The repository also contains a synthetic-data experiment.

## Main files

| File | Purpose |
| --- | --- |
| [app.py](app.py) | Flask routes and form handling |
| [data_fetch.py](data_fetch.py), [url_builder.py](url_builder.py) | Alpha Vantage requests |
| [plot_stock_data.py](plot_stock_data.py) | Candlestick chart creation |
| [alpaca_trading.py](alpaca_trading.py), [cancel_order.py](cancel_order.py) | Alpaca paper account and order requests |
| [stock_spoof_generator.py](stock_spoof_generator.py) | Experimental synthetic data generator |
| [stock_spoof_data.json](stock_spoof_data.json) | Saved sample data |

## Local setup

Use Python 3.12, create a virtual environment, and install `requirements.txt`. Configure these environment variables before starting:

- `ALPHA_VANTAGE_API_KEY`
- `APCA_API_KEY_ID` and `APCA_API_SECRET_KEY` from an Alpaca **paper** account
- `FLASK_SECRET_KEY`, a locally generated random value

`.env.example` lists the names. Export them in your shell; `python app.py` does not automatically load that file.

```bash
git clone https://github.com/aseabroo/qft.git
cd qft
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
# Export the four environment variables listed above, then:
python app.py
```

The local address is http://127.0.0.1:8000. The order modules use Alpaca's paper API. Do not substitute live-trading endpoints.

## Current limitations

This is a development prototype. The home page depends on an external data response, error handling is incomplete, and the server starts in debug mode. There is no verified trading strategy, backtest, or performance result here.

The synthetic-data script is separate from the web app; there is no JSON upload route. Its intraday branch needs fixes for interval keys and termination when no month is given. Its imports also include Faker, which is absent from the current requirements. Avoid running that branch until it is repaired.

The portfolio-history request contains a fixed 2023 end date, and order cancellation needs better response handling. There is no automated test suite in the repository.

## Next steps

Make charting work from a saved sample response, handle missing or rate-limited data, and repair the synthetic generator with a bounded output size. Keep external paper-account tests separate from local checks.

Historical commits contained credentials. Removing them from the current source does not revoke them or remove them from Git history; affected credentials need rotation.
