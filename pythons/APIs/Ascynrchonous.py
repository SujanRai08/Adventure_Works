# Asynchronous programming allows tasks to run concurrently, improving efficiency for I/O-bound operations. 
"""Key Concepts

Coroutine: Defined using async def.
Event Loop: Executes coroutines.
Task: Coroutine scheduled for execution.
"""
import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)
    print("World!")

# Run the coroutine
asyncio.run(say_hello())


# Using asyncio.gather for Concurrency

# Runs multiple coroutines concurrently.
import asyncio

async def task(name, delay):
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")

async def main():
    await asyncio.gather(
        task("Task 1", 2),
        task("Task 2", 3),
        task("Task 3", 1),
    )

asyncio.run(main())



Using Async with HTTP Requests
import aiohttp
import asyncio

async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ["https://example.com", "https://example.org"]
    async with aiohttp.ClientSession() as session:
        responses = await asyncio.gather(*(fetch_url(session, url) for url in urls))
        for response in responses:
            print(response[:100])  # Print first 100 characters

asyncio.run(main())


# Asynchronous Programming

# Fetching data concurrently from multiple APIs or databases.
# Running asynchronous ETL jobs for real-time data processing.