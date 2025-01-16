# Using multiprocessing

# Distributes work across multiple CPU cores.

from multiprocessing import Pool
def square(n):
    return n *n
numbers = [1,2,3,4,5]
with Pool(4) as pool:
    results = pool.map(square,numbers)
print(results)


# Using concurrent.futures

# Simpler interface for multithreading and multiprocessing.

import requests 
from concurrent.futures import ThreadPoolExecutor
urls = ["https://example.com", "https://example.org", "https://example.net"]
def fetch_urls(url):
    response = requests.get(url)
    return url,response.status_code

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch_urls,urls))

for url, status in results:
    print(f'{url}, {status}')