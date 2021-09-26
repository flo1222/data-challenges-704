"""Functions that return various financial info from iexcloud api"""

import requests
import numpy as np
import pandas as pd
import matplotlib

def get_stock(code, time):
    """Function that returns graph of stock over a given period of time"""
    url = f"http://iex.lewagon.com/stable/stock/{code}/chart/{time}"
    api_data = requests.get(url).json()
    stocks_df = pd.DataFrame(api_data)
    stocks_df["date"] = pd.to_datetime(stocks_df["date"])
    stocks_df = stocks_df.set_index('date')
    return stocks_df[["open", "close", "high", "low"]].plot(figsize=(12,6))

def get_info(code):
    url = f"http://iex.lewagon.com/stable/stock/{code}/advanced-stats"
    api_data = requests.get(url).json()
    return api_data