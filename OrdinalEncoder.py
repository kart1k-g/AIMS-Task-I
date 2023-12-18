import pandas as pd
def ordinal_encode(df, columns):
  encoded_df = df.copy()
  for col in columns:
    categories = df[col].unique()
    category_map = {c: i for i, c in enumerate(categories)}
    encoded_df[col] = df[col].map(category_map)
  return encoded_df