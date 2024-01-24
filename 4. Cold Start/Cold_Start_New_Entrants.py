import pandas as pd
import numpy as np


def fillna_with_mean(
        df: pd.DataFrame, target: str, group: str
) -> pd.DataFrame:
    """
        Fills NaN values in the 'target' column of the DataFrame 'df' with the mean values of their respective groups defined by the 'group' column. Rounded down to the nearest whole number.

        Parameters:
        df (pd.DataFrame): DataFrame with data
        target (str): Name of the column in which to fill NaNs
        group (str): Name of the column to group by

        Returns:
        pd.DataFrame: DataFrame with NaNs filled
        """
    # Create a copy of the DataFrame to avoid changing the original df
    df_copy = df.copy()

    # Calculate the mean of the target column for each group
    group_means = df_copy.groupby(group)[target].mean()

    # Apply a function to fill NaN values with the group's mean, rounded down
    df_copy[target] = df_copy.apply(
        lambda row: np.floor(group_means[row[group]]) if pd.isnull(row[target]) else row[target],
        axis=1
    )

    return df_copy

    return df_copy