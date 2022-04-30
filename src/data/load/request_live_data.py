import requests
import os
import pandas as pd

# TODO: make a class that has all this data with the api keys

def request_to_alpha_vantage(function="CRYPTO_INTRADAY", symbol="BTC", market="USD", interval="60min"):
    """
    ask the data from alpha vantage per day in the interval for 30 min
    the daly for this api is 3 days

    COLUMNS
        INDEX - Date      1. open      2. high       3. low     4. close 5. volume

    intervals -> 1min, 5min, 15min, 30min, 60min

    Returns:
        _type_: _description_
    """
    api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
    if not api_key:
        print("Not property request")
        return None

    url = "https://www.alphavantage.co/query"

    main_url = \
        f"{url}?function={function}&symbol={symbol}&market={market}&interval={interval}&apikey={api_key}"

    response = requests.get(main_url)
    if response.status_code != 200:
        print(f"Not status code good [{response.status_code}]")
        return None

    try:
        data = response.json()[f"Time Series Crypto ({interval})"]

    except Exception as e:
        print("Data malformed")

        return None

    df = pd.DataFrame.from_dict(data).T  # For transposed

    df = df.reset_index().rename(columns={"index": "Date"})
    df['Date'] = pd.to_datetime(df['Date'])

    return df


def coinmarket_api():
    """_summary_
    """

    api_url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=1&convertId=2781&timeStart=1632441600&timeEnd=1637712000'
    r = requests.get(api_url)
    data = []
    for item in r.json()['data']['quotes']:
        close = item['quote']['close']
        volume = item['quote']['volume']
        date = item['quote']['timestamp']
        high = item['quote']['high']
        low = item['quote']['low']
        data.append([close, volume, date, high, low])

    cols = ["close", "volume", "date", "high", "low"]

    df = pd.DataFrame(data, columns=cols)
    print(df)
