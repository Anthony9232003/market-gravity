
"""The purpose of this program is to have a main file for this project where 
I can cleanly organize code and maintain a main program. """


from data_loader import get_market_data
from data_cleaning import prepare_data 
from density_model import calculate_density


def main(): 
    raw_data = get_market_data(
        tickers=["SPY", "^VIX"], 
        start_date="2018-01-01", 
        end_date="2026-01-01"
    )

    clean_data = prepare_data(raw_data)

    print(clean_data.head())

    density = calculate_density(clean_data)
    print(density[:5])

    

if __name__ == "__main__": 
    main()