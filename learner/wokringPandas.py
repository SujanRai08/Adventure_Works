# why ? - optimizing pandas operations can speed up data transformations 
# chunk wise processing of large csv files

import pandas as pd

chunkSize = 10_000
for chunk in pd.read_csv("large_dataset.csv",chunksize=chunkSize):
    chunk["new_columns"] = chunk["exisiting_data"].apply(lambda x:x*2)
    print(chunk.head())