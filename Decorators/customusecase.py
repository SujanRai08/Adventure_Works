# Performance Timer
# Measures the execution time of functions.
# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"{func.__name__} executed in {end_time - start_time:.2f}s")
#         return result
#     return wrapper

# @timer
# def transform_data(data):
#     time.sleep(2)  # Simulating a delay
#     return [x * 2 for x in data]

# transform_data([1, 2, 3])


#  etl workflow step decorators
# tracks each step in an etl pipeline 

# def etl_step(func):
#     def wrapper(*args, **kwargs):
#         print(f'starting step: {func.__name__}')
#         result = func(*args, **kwargs)
#         print(f'completed step: {func.__name__}')
#         return result
#     return wrapper

# @etl_step
# def extract():
#     return "Exacted data"

# @etl_step
# def transform(data):
#     return data.upper()

# @etl_step
# def load(data):
#     print(f'loading data:{data}')

# data = extract()
# transform_data = transform(data)
# load(transform_data)

# Error Logging Decorator
# Logs errors that occur during function execution.

# def error_logger(func):
#     def wrapper(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except Exception as e:
#             print(f'error in {func.__name__}: {e}')
#             raise
#     return wrapper

# @error_logger
# def divide(a, b):
#     divided = a/5
#     print(f'the divide of the {divided}')
# divide(0, 1)