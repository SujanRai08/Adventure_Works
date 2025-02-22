import pandas as pd

df = pd.read_csv("sales_data.csv")

# Convert to Parquet format
df.to_parquet("sales_data.parquet", engine="pyarrow", compression="snappy")

# Read Parquet file
df_parquet = pd.read_parquet("sales_data.parquet")
print(df_parquet.head())


#  Use case: Storing large datasets efficiently, using Parquet for big data analytics.