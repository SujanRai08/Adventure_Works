# hashing maps data to fixed size value using a hash functions. it's fast for lookups

# for dictionary
data = {'alice':25,'bob':30,'charlie':35}
print(data['alice'])

# sets store unique elements 
items = {1,2,3,4}
print(3 in items)

data = ["apple", "banana", "cherry", "apple", "banana"]
frequency = {}
for items in data:
    frequency[items] = frequency.get(items,0) + 1
print(frequency)

