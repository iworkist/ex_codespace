import requests

def get_binance_price(symbol):
    base_url = "https://api.binance.com/api/v3/ticker/price"
    params = {
        "symbol": symbol
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        bitcoin_price = data["price"]
        return bitcoin_price
    else:
        print("Error occurred while fetching Bitcoin price from Binance.")
        return None

def get_ethereum_price(symbol):
    base_url = "https://api.binance.com/api/v3/ticker/price"
    params = {
        "symbol": symbol
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        ethereum_price = data["price"]
        return ethereum_price
    else:
        print("Error occurred while fetching Ethereum price from Binance.")
        return None

# # Usage
# symbol = "BTCUSDT"  # Bitcoin symbol in USDT
# bitcoin_price = get_binance_price(symbol)
# if bitcoin_price:
#     print("Bitcoin Price (USDT):", bitcoin_price)


# get ethereum price
# Usage
symbol = "ETHUSDT"  # Ethereum symbol in USDT
ethereum_price = get_ethereum_price(symbol)
if ethereum_price:
    print("Ethereum Price (USDT):", ethereum_price)


# top 10 coin symbols
symbols = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "XRPUSDT", "DOGEUSDT", "DOTUSDT", "UNIUSDT", "BCHUSDT", "LTCUSDT"]

# get top 10 coin prices
for symbol in symbols:
    price = get_binance_price(symbol)
    if price:
        print(symbol, "Price (USDT):", price)


