import pandas as pd
from sqlalchemy import create_engine

def extract_data(file_path):
    return pd.read_csv(file_path)

def transform_data(df):
    df['Total'] = df['Quantity'] * df['Price']
    return df

def load_data(df,db_url,table_name):
    engine = create_engine(db_url)
    df.to_sql(table_name,engine,if_exists = 'replace',index = False)

# Usage
file_path = 'sales_data.csv'
db_uri = 'sqlite:///sales.db'
table_name = 'sales'


data = extract_data(file_path)
transformed_data = transform_data(data)
load_data(transformed_data, db_uri, table_name)
print("Pipeline executed successfully!")