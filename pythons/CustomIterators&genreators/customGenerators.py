# Functions that yield values using yield keyword.

def countdown(n):
    while n>0:
        yield n
        n -=1
    
for value in countdown(5):
    print(value)

# Generator Expressions 
# Similar to list comprehensions but produce items lazily. 
squares = (x * x for x in range(5))
print(list(squares))  # Output: [0, 1, 4, 9, 16]

#lazy evaluations
def generate_numbers():
    for i in range(1, 10):
        print(f"Yielding {i}")
        yield i

gen = generate_numbers()

print(next(gen))  # Output: Yielding 1, 1
print(next(gen))  # Output: Yielding 2, 2


numbers = (x * x for x in range(5))  # Generator expression

print(next(numbers))  # Output: 0
print(next(numbers))  # Output: 1



# exaple 
# Without Lazy Evaluation:
# Loads the entire file into memory
with open("large_file.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())


# With Lazy Evaluation: 
# Processes the file line by line
with open("large_file.txt", "r") as file:
    for line in file:
        print(line.strip())
