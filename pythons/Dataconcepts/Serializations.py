# Serialization formats are crucial for storing and transferring structured data.
# Lightweight data exchange format.
# json
import json

data = {"name": "Alice", "age": 25, "city": "New York"}
json_data = json.dumps(data)  # Serialize
print(json_data)
deserialized_data = json.loads(json_data)  # Deserialize
print(deserialized_data)

# parquet:  Optimized for large datasets, commonly used in big data.
import pandas as pd
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df.to_parquet('data.parquet')
df_parquet = pd.read_parquet('data.parquet')
print(df_parquet)

# avro:  schema based serialzations.
# pip install fastavro 


#pickle - Python-specific object serialization.
import pickle

data = {"key": "value"}
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)
print(loaded_data)
