import pandas as pd
from sqlalchemy import create_engine

# Extract
data = pd.read_csv("data.csv")

# Transform
data['New_Column'] = data['Old_Column'] * 2

# Load
engine = create_engine('sqlite:///data.db')
data.to_sql("table_name", engine, if_exists='replace', index=False)



import pandas as pd
import sqlite3

# Extract
data = pd.read_csv('data.csv')

# Transform
data['processed_column'] = data['raw_column'].apply(lambda x: x.strip().upper())

# Load
conn = sqlite3.connect('database.db')
data.to_sql('processed_data', conn, if_exists='replace', index=False)
conn.close()
