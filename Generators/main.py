# 1. Reading Large Files Lazily
# Instead of loading an entire file into memory, a generator reads one line at a time.

# def read_large_file(file_path):
#     with open(file_path,"r")as file:
#         for line in file:
#             yield line.strip()

# for line in read_large_file("large_datasets.csv"):
#     print(line)

# 2. Processing Streaming Data
# When processing real-time data streams (e.g., logs or message queues), generators help handle data efficiently.

# import time
# def stream_logs():
#     logs = [
#         "Log entry 1",
#         "Log entry 2",
#         "Log entry 3",
#     ]
#     for log in logs:
#         time.sleep(1)
#         yield log

# for log_entry in stream_logs():
#     print(f"processing :{log_entry}")


# . Chaining Generators for Data Pipelines
# def read_data(file_path):
#     with open(file_path,"r") as file:
#         for line in file:
#             yield line.strip()

# def filter_data(data, keyword):
#     for line in data:
#         if keyword in line:
#             yield line

# def transform_data(data):
#     for line in data:
#         yield line.upper()

# #  Pipeline
# data = read_data("large_dataset.csv")
# filtered_data = filter_data(data, "ERROR")
# transformed_data = transform_data(filtered_data)

# for record in transformed_data:
#     print(record)

#  chunk data
# def chunk_data(data,chunk_size):
#     chunk =[]
#     for items in data:
#         chunk.append(items)
#         if len(chunk) == chunk_size:
#             yield chunk
#             chunk = []
#     if chunk:
#         yield chunk
# data = range(1,101)
# for chunks in chunk_data(data,10):
#     print(chunks)

# def infinite_ids(start=1):
#     while True:
#         yield start
#         start +=1 
# id_generators = infinite_ids()
# for _ in range(10):
#     print(next(id_generators))

# import sqlite3

# def fetch_records(db_path,query,batch_size = 100):
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#     cursor.execute(query)
#     while rows:= cursor.fetchmany(batch_size):
#         for row in rows:
#             yield row
#         conn.close()

# for record in fetch_records("database.db","select * from large_data"):
#     print(record)

# #  single generators
# def extract_data():
#     for i in range(1, 1001):  # Simulated data extraction
#         yield {"id": i, "value": i * 10}

# def transform_data(data):
#     for record in data:
#         record["value"] = record["value"] / 2  # Transform logic
#         yield record

# def load_data(data):
#     for record in data:
#         print(f"Loading: {record}")  # Simulate loading

# # ETL Workflow
# data = extract_data()
# transformed_data = transform_data(data)
# load_data(transformed_data)


# real world- example data cleaning pipeline 
def extract_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

def clean_data(data):
    for line in data:
        if line and not line.startswith("#"):  # Remove empty lines and comments
            yield line


def split_fields(data, delimiter=","):
    for line in data:
        yield line.split(delimiter)


# Usage
raw_data = extract_file("large_dataset.csv")
cleaned_data = clean_data(raw_data)
records = split_fields(cleaned_data)

for record in records:
    print(record)