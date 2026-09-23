# QFT route notes

These notes describe the current Flask routes. See [README.md](README.md) for setup and limitations.

| Route | Input / behavior |
| --- | --- |
| `GET /` | Fetches daily IBM data and renders a candlestick chart |
| `POST /` | Reads form fields `symbol`, `outputsize`, `function_interval`, and optional `intraday_interval` |
| `GET /trading` | Retrieves Alpaca paper-account and portfolio-history data |
| `POST /trading` | Submits an Alpaca paper order from form fields |
| `GET /cancel_order` | Attempts to cancel the most recent open paper order |

For chart requests, `function_interval` is `daily` or `intraday`. For intraday data, `intraday_interval` supplies the interval, such as `15min`. The route reads form data, not a JSON request body.

The order form supplies `symbol`, `qty`, `side`, `type`, and `time_in_force`. No automatic trading strategy is implemented by these routes.

The cancellation route changes state through a GET request. Changing that to a protected POST action, adding input validation, and handling external API errors are follow-up work. Keep this app local.
