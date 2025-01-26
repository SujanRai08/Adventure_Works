# import logging
# logging.basicConfig(level=logging.INFO)

# def log_execution(func):
#     def wrapper(*args, **kwargs):
#         logging.info(f"exeution {func.__name__}with args: {args} kwargs:{kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"execution complicated. Result: {result}")
#         return result
#     return wrapper

# @log_execution
# def process_data(data):
#     return [x*2 for x in data]
# process_data([1, 2, 3])

# retry 

# import time 
# from functools import wraps

# def retry(retries = 3,delays=2,expections=(Exception,)):
#     def decorators(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             attempts = 0
#             while attempts < retries:
#                 try:
#                     return func(*args, **kwargs)
#                 except expections as e:
#                     attempts +=1 
#                     time.sleep(delays)
#                     if attempts == retries:
#                         raise
#         return wrapper
#     return decorators
# @retry(retries=3, delay=1)
# def connect_to_database():
#     raise ConnectionError("Database not reachable!")

# connect_to_database()

#  caching decorators
# import time
# from functools import lru_cache

# @lru_cache(maxsize=128)
# def fetch_data(query):
#     time.sleep(2)
#     return f"results for {query}"


# print(fetch_data("SELECT * FROM table"))
# print(fetch_data("SELECT * FROM table"))  # Cached result

 
# validations
# def validate_input(func):
#     def wrapper(*args, **kwargs):
#         if not all(isinstance(arg,int)for arg in args):
#             raise ValueError("All input must be integers")
#         return func(*args, **kwargs)
#     return wrapper

# @validate_input
# def add_numbers(a,b):
#     return a + b
# print(add_numbers(1, 2))


