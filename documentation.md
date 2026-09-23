# QFT notes

QFT is a market-data and visualization sandbox. The active Flask application exposes one route:

| Route | Input / behavior |
| --- | --- |
| `GET /` | Fetches daily IBM data by default and renders a candlestick chart |
| `POST /` | Reads `symbol`, `outputsize`, `function_interval`, and optional `intraday_interval` to render another chart |

For intraday data, `intraday_interval` supplies an interval such as `15min`.

## Legacy material

The original prototype included Alpaca paper-account and order routes. Those artifacts now live under `legacy/` and are not imported or exposed by the active application.

Trading execution belongs in the separate AiQuant project; QFT is intentionally limited to data exploration and visualization.
