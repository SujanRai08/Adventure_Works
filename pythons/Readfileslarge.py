# Combined Example: Reading Large Files and Writing to a Database
# Imagine you need to read multiple large files and insert their content into a database. Threading handles the database I/O, while multiprocessing processes the files.

import threading
import multiprocessing
import pandas as pd
import sqlite3
def write_to_DB(data):
    conn = sqlite3.connect('example.db',check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('create table if not exists data(value real)')
    for value in data:
        cursor.execute('insert into data (value) value(?)',(value,))
    conn.commit()
    conn.close()

# files processingd data
def process_and_store(file_name):
    df = pd.read_csv(file_name)
    mean_values = df['column1'].mean()
    thread = threading.Thread(target=write_to_DB,args=([mean_values]))
    thread.start()
    thread.join()

file_names = ["file1.csv", "file2.csv", "file3.csv"]

# Use multiprocessing for parallel processing of files
with multiprocessing.Pool(processes=3) as pool:
    pool.map(process_and_store,file_names)
print('all files processed and store stored in the database')