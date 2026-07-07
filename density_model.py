
""" I take my data from data_cleaning.py module to create a graph where
sp 500 returns are on the x axis and vix changes are on the y axis. Then I can 
calculate the density of each combination to see how many times are these two 
values related (or how dense they are). """

import numpy as np 
from scipy.stats import gaussian_kde 


def calculate_density(clean_data): 

    x_values = clean_data["spy_return"].to_numpy()
    y_values = clean_data["vix_change"].to_numpy()

    points = np.vstack([x_values, y_values])

    kde = gaussian_kde(points)

    density = kde(points)

    return density 

    