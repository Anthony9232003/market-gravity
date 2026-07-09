
"""The purpose of this program is to have a main file for this project where 
I can cleanly organize code and maintain a main program. """


from data_loader import get_market_data
from data_cleaning import prepare_data 
from density_model import calculate_density
from center_of_mass import calculate_center_of_mass
from presentation import plot_market_density


def main(): 
    raw_data = get_market_data(
        tickers=["SPY", "^VIX"], 
        start_date="2018-01-01", 
        end_date="2026-01-01"
    )

    clean_data = prepare_data(raw_data)

    density = calculate_density(clean_data)

    clean_data["density"] = density 

    center_of_mass = calculate_center_of_mass(clean_data)

    print(clean_data.head())

    # print()
    # print("Center of Mass: ")
    # print(f'SPY Return: {center_x}')
    # print(f'VIX Changes: {center_y}')

    print(clean_data.columns)

    plot_market_density(
        clean_data, 
        x_col="spy_return", 
        y_col="vix_change", 
        density_col="density",
        center_of_mass=center_of_mass
    )


if __name__ == "__main__": 
    main()