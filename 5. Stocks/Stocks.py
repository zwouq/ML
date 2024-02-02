import pandas as pd
import numpy as np

def limit_gmv(df: pd.DataFrame) -> pd.DataFrame:
    """
     Adjust the GMV in the DataFrame based on available stock.

     Parameters:
     df (pd.DataFrame): DataFrame containing sku, gmv, price, and stock columns.

     Returns:
     pd.DataFrame: DataFrame with adjusted GMV values.
     """
    # Create a copy of the DataFrame
    df_copy = df.copy()

    # Calculate the predicted number of units sold and round down
    predicted_units = np.floor(df_copy['gmv'] / df_copy['price'])

    # Use numpy.minimum to efficiently find the minimum between predicted units and stock
    limited_units = np.minimum(predicted_units, df_copy['stock'])

    # Update the GMV based on limited units
    df_copy['gmv'] = limited_units * df_copy['price']

    return df_copy
