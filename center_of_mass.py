
import pandas as pd 

def calculate_center_of_mass(
    df: pd.DataFrame,
    x_col: str = "spy_return",
    y_col: str = "vix_change", 
    density_col: str = "density"
) -> tuple[float, float]: 

    df = df.dropna(subset=[x_col, y_col, density_col])

    total_mass = df[density_col].sum()

    if total_mass == 0: 
        raise ValueError("Total density is zero, so center of mass cannot be calculated")

    center_x = (df[x_col] * df[density_col]).sum() / total_mass

    center_y = (df[y_col] * df[density_col]).sum() / total_mass

    return center_x, center_y



    