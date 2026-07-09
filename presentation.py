
import matplotlib.pyplot as plt 
from center_of_mass import calculate_center_of_mass

def plot_market_density(df, x_col, y_col, density_col, center_of_mass):

    x_center, y_center = center_of_mass

    plt.figure(figsize=(10, 7))

    scatter = plt.scatter(
        df[x_col], 
        df[y_col], 
        c=df[density_col],
        cmap="viridis", 
        alpha=0.7
    )

    plt.scatter(
        x_center, 
        y_center, 
        color="red", 
        marker="x", 
        s=150, 
        label="Center of Mass"
    )

    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title("Market Gravity Model: Density and Center of Mass")
    plt.colorbar(scatter, label="Density")
    plt.legend()
    plt.grid(True)
    plt.show()