import time
from datetime import datetime
from kucoin.client import Client
# local file with api info
from local_const import *

client = Client(api_key, api_secret, api_passphrase)

user_symbol = input("Enter the Cryptocurrency that you would like to trade: ")


def current_time():
    # datetime object containing current date and time
    now = datetime.now()
    return now


def trade(symbol):
    last_price = client.get_ticker(symbol + "-USDT")["price"]
    end_time = current_time() + 4
    now_time = current_time()
    trend_count = 0
    profit = 0.0
    while end_time > now_time:
        now_time = current_time()
        time.sleep(0.5)
        # getting the most recent price
        current_price = client.get_ticker(symbol + "-USDT")["price"]
        # comparing current and last price

        # deciding whether to buy, sell, or hold


# todo: come up with trading algo

trade(user_symbol)
