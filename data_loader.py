
"""In this program I pull the needed data for my project. """

import yfinance as yf 

def get_market_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)
    return data

