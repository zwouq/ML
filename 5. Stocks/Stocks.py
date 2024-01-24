import pandas as pd
import numpy as np

def limit_gmv(df: pd.DataFrame) -> pd.DataFrame:
    # Calculate the predicted number of units sold
    df['predicted_units'] = df['gmv'] / df['price']

    # Round down the predicted units as sales cannot be fractional
    df['predicted_units'] = df['predicted_units'].apply(np.floor)

    # Adjust GMV if predicted units exceed stock
    df['gmv'] = df.apply(lambda row: min(row['predicted_units'], row['stock']) * row['price'], axis=1)

    # Drop the temporary 'predicted_units' column
    df.drop(columns=['predicted_units'], inplace=True)

    return df
