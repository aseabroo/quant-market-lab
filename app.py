import os
from flask import Flask, render_template, request

from data_fetch import get_json_data
from plot_stock_data import create_interactive_candlestick_with_timezone

app = Flask(__name__)

API_KEY = os.environ["ALPHA_VANTAGE_API_KEY"]
DEFAULT_SYMBOL = "IBM"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symbol = request.form["symbol"]
        outputsize = request.form["outputsize"]
        function_interval = request.form["function_interval"]
        intraday_interval = request.form.get("intraday_interval")
    else:
        symbol = DEFAULT_SYMBOL
        outputsize = "compact"
        function_interval = "daily"
        intraday_interval = None

    data = get_json_data(
        symbol,
        outputsize,
        API_KEY,
        function_interval,
        intraday_interval,
    )
    candlestick_html = create_interactive_candlestick_with_timezone(
        data,
        "America/New_York",
    )
    return render_template("index.html", candlestick_html=candlestick_html)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
