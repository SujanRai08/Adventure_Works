# handle concurrent tasks for better performance in data pipelines
# multithreading 
import threading
def print_number():
    for i in range(5):
        print(i)

thread = threading.Thread(target=print_number)
thread.start()
thread.join()

# multiprocessing
from multiprocessing import Pool
def square(n):
    return n*n
with Pool(4) as pool:
    result = pool.map(square,range(10))
    print(result)


#Concurrent Futures
# High-level API for threading or multiprocessing.
from concurrent.futures import ThreadPoolExecutor
def fetch_data(url):
    return f'fetched data from {url}'
urls = ['url1','url2','url3']
with ThreadPoolExecutor() as executor:
    results = executor.map(fetch_data,urls)
    for result in results:
        print(result)

# Advanced Data Types: Handle complex data transformations and mappings.
# Decorators: Modularize and reuse common logic like logging or error handling.
# Context Managers: Ensure resources (files, databases) are managed efficiently.
# Error Handling: Prevent crashes and ensure pipeline robustness.
# File Handling: Process large datasets stored in files.
# Concurrency: Optimize performance in ETL processes and APIs.

import threading 
import requests
def fetch_weather(api_urls):
    response = requests.get(api_urls)
    print(f'data from {api_urls}:{response.json()}')

# List of API URLs

api_urls = [
    "https://api.weatherapi.com/v1/current.json?key=YOUR_KEY&q=London",
    "https://api.weatherapi.com/v1/current.json?key=YOUR_KEY&q=New York",
    "https://api.weatherapi.com/v1/current.json?key=YOUR_KEY&q=Tokyo",
]
thread = []
for url in api_urls:
    thread = threading.Thread(target=fetch_weather,args=(urls,))
    thread.append(thread)
    thread.start()
for threads in thread:
    threads.join()
print('all api callas completed')