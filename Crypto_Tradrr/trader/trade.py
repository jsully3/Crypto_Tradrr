import time
from datetime import datetime, timedelta
from kucoin.client import Client
# local file with api info
from local_const import *

client = Client(api_key, api_secret, api_passphrase)

# User input crypto currency of their choice
user_symbol = input("Enter the Cryptocurrency Abbreviation (ex. BTC) that you would like to trade: ")


def current_time():
    # datetime object containing current date and time
    now = datetime.now()
    return now


print("The current time is: ", current_time())


def trade(symbol):
    current_price = client.get_ticker(symbol + "-USDT")["price"]  # Grab the current price of the cryptocurrency as str
    now_time = datetime.now()  # Get the current time
    end_time = now_time + timedelta(seconds=30)  # Add 4 second interval to the current time
    current_price = float(current_price)  # Converts current_price from str to float
    trend_count = 0.0  # Initialize the trend count as an float
    profit = 0.0  # Initialize the profit as a float
    bought_price = 0.0
    bought_in = False
    print(f"Current price: {current_price}")
    while end_time > now_time:
        now_time = current_time()
        time.sleep(0.5)
        last_price = float(current_price)
        current_price = float(client.get_ticker(symbol + "-USDT")["price"])  # Get the most recent price as str
        print(f"Current price: {current_price}")
        trend_count = current_price - last_price + trend_count  # comparing current and last price
        print(f"Trend Count: {trend_count}")
        if trend_count < -5 and bought_in is False:  # Decide whether to buy, sell, or hold
            print("Buy")
            bought_in = True
            bought_price = current_price
        elif trend_count > 5 and bought_in is True:
            print("Sell")
            bought_in = False
            profit = current_price - bought_price
            trend_count = 0.0
        else:
            continue


trade(user_symbol)
