
import pandas as pd 

def prepare_data(raw_data):
    if "Adj Close" in raw_data.columns: 
        prices = raw_data["Adj Close"]
    else: 
        prices = raw_data["Close"]

    clean_data = pd.DataFrame()

    clean_data["spy_return"] = prices["SPY"].pct_change(21)
    clean_data["vix_change"] = prices["^VIX"].pct_change(21)

    clean_data = clean_data.dropna()

    return clean_data 

