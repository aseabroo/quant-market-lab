# Quantum Flux Toolkit

A Python/Flask sandbox for exploring financial market data, interactive candlestick charts, and synthetic OHLCV generation.

This repository is intentionally separate from [AiQuant](https://github.com/aseabroo/aiquant). **AiQuant is the trading/research system. QFT is a lightweight market-data and visualization playground.**

## What QFT is for

QFT focuses on:

- fetching market time-series data from Alpha Vantage,
- rendering interactive Plotly candlestick charts,
- experimenting with synthetic OHLCV generation,
- trying small data/visualization ideas without coupling them to a trading engine.

It does **not** contain a trading strategy, portfolio engine, backtester, execution system, or live-capital workflow.

## Main files

| File | Purpose |
| --- | --- |
| [app.py](app.py) | Flask market-data explorer |
| [data_fetch.py](data_fetch.py) | Alpha Vantage request handling |
| [url_builder.py](url_builder.py) | Daily/intraday request construction |
| [plot_stock_data.py](plot_stock_data.py) | Interactive candlestick visualization |
| [stock_spoof_generator.py](stock_spoof_generator.py) | Experimental synthetic OHLCV generator |
| [stock_spoof_data.json](stock_spoof_data.json) | Saved synthetic sample |

## Historical paper-trading experiment

The original 2023 prototype also included Alpaca paper-account and order endpoints. Those files are preserved under `legacy/` for provenance, but they are no longer part of the active Flask application.

That separation is deliberate: trading execution belongs in **AiQuant**, while QFT remains a safe experimentation surface for market data and visualization.

## Local setup

Use Python 3.12, create a virtual environment, and install the requirements.

```bash
git clone https://github.com/aseabroo/qft.git
cd qft
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export ALPHA_VANTAGE_API_KEY=your_key
python app.py
```

Then open http://127.0.0.1:8000.

## Current limitations

This remains a small experimental application rather than a production data service.

- External-data error handling is basic.
- Alpha Vantage rate limits can affect requests.
- The server starts in Flask debug mode for local development.
- The synthetic generator still needs stricter bounds and more deterministic fixtures.
- There is no automated test suite yet.

## Portfolio role

Keep QFT as an **early financial-data experimentation project**. Its value is different from AiQuant: it shows the earlier Flask/data-visualization work and a lightweight sandbox mentality, while AiQuant represents the more structured quantitative research and trading stack.

## Security note

Historical commits contained credentials. Current source uses environment variables, but removing credentials from current files does not revoke old credentials or erase them from Git history. Any previously exposed credentials should remain rotated.
