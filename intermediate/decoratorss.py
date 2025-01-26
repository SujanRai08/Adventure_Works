# import functools
# def start_end_decorators(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("start")
#         result = func(*args, **kwargs)
#         print("end")
#         return result
#     return wrapper

# @start_end_decorators
# def print_name():
#     print("Sujan")
# @start_end_decorators
# def add5(x):
#     return x+5
# result = add5(10)
# print(result)

# # print_name = start_end_decorators(print_name)
# print_name()


# import functools 

# def repeat(num_fields):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_fields):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decorator_repeat
# @repeat()
# def great(name):
#     greeting = f'Hello{name}'
#     print(greeting)
#     return greeting
# great("Alex")
