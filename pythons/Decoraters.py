# decorators modify or enhance the behaviour of functions or methods.
# built-in decorators

# common example - staticmethod, classmethod
# property
class config:
    @property
    def database_url(self):
        return 'link'
    
config = config()
print(config.database_url)# Access without parentheses

# staticmethod - belongs to class rather any objects instance . it does not require access to class or instance
# it used for utility functions that are logically related to the class but don't need to interact wiht the class or instance data.

class Mathutils:
    @staticmethod
    def add_numbers(a,b):
        return a+ b
result = Mathutils.add_numbers(10,20)
print(result)
# used for formatting data or calucaltions unrelated to a specific instances.

class Datautils:
    @staticmethod
    def format_date(data_str):
        return data_str.replace('/','-')
formatted = Datautils.format_date('2025/01/15')
print(formatted)

# classmethods- a class belongs to the class and has the access ti the class itself via the cls paramater
# it can modify the class state or interact with class level attributes
#takes class as the first argument instead of self.
# can be used using the class name

class Employee:
    company_name = 'TechCrop'
    def __init__(self,name):
        self.name = name
    
    @classmethod
    def change_company (cls,new_name):
        cls.company_name = new_name
Employee.change_company('Innovatech')
print(Employee.company_name)

# or 
 
class Employees:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(clas,emp_str):
        name,age = emp_str.split(',')
        return clas(name,int(age))
    
employee = Employees.from_string('alice,30')
print(employee.name)
print(employee.age)

class Config:
    def __init__(self, db_host, db_port):
        self.db_host = db_host
        self.db_port = db_port

    @classmethod
    def from_dict(cls, config_dict):
        return cls(config_dict["db_host"], config_dict["db_port"])

# Create a Config object using a dictionary
config_data = {"db_host": "localhost", "db_port": 5432}
config = Config.from_dict(config_data)
print(config.db_host)  # Output: localhost


# custom decorators
# usages - wrapping functions like logging, timing or authentication

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}")
        return func(*args, **kwargs)
    return wrapper

@logger
def process_data(data):
    return [x**2 for x in data]

process_data([1, 2, 3])


def timing_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")
        return result
    return wrapper

@timing_decorator
def process_data(data):
    return [x**2 for x in data]

process_data(range(1000000))
