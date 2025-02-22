from sqlalchemy import create_engine
import pandas as pd

# Create database connection
engine = create_engine("postgresql://username:password@localhost:5432/mydatabase")

# Read CSV and insert into PostgreSQL
df = pd.read_csv("sales_data.csv")
df.to_sql("sales", engine, if_exists="replace", index=False)
