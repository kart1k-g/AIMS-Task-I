import pandas as pd
import numpy as np

def simple_imputer(df, strategy='mean', fill_value=None):
    if strategy not in ['mean', 'median', 'most_frequent', 'constant']:
        raise ValueError("Invalid imputation strategy. Choose from 'mean', 'median', 'most_frequent', or 'constant'.")

    for column in df.columns:
        if strategy == 'mean':
            imputation_value = df[column].mean()
        elif strategy == 'median':
            imputation_value = df[column].median()
        elif strategy == 'most_frequent':
            imputation_value = df[column].mode().iloc[0]
        elif strategy == 'constant':
            imputation_value = fill_value

        df[column].fillna(imputation_value, inplace=True)

    return df