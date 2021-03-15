# todo: come up with trading algo

from datetime import datetime


def current_time():
    # datetime object containing current date and time
    now = datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    return str(now)


print("Enter the Currency rate: ")
currency = float(input())


def trade_algo():
    if currency > 5:
        return print("Sell Sell Sell")
    if currency < 1:
        return print("Buy Buy Buy")
    else:
        return print("Stay In")

trade_algo()
