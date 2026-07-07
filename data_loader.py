
"""In this program I pull the needed data for my project. """

import yfinance as yf 

def get_market_data(tickers, start_date, end_date):
    raw_data = yf.download(tickers, start_date, end_date)
    return raw_data

