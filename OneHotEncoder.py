import pandas as pd

def one_hot_encoder(df, columns):
    encoded_df = df.copy()

    for column in columns:
        # Get unique categories in the column
        unique_categories = df[column].unique()

        # Create binary columns for each category
        for category in unique_categories:
            new_column_name = f"{column}_{category}"
            encoded_df[new_column_name] = (df[column] == category).astype(int)

        # Drop the original categorical column
        encoded_df.drop(column, axis=1, inplace=True)

    return encoded_df
