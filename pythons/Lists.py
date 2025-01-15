# python's advanced data types provide the foundation for efficient data manipulations.
# list: ordered, mutable collections of items. usages in data engineering - used to stores sequences of data, like rows from a file or query results.
data = [1,2,3,4,5]
squared = [x**2 for x in data]
print(squared)

# tuple: ordered, immutable collections of items used for fixed data structures, like database keys or configurations.
data = (1,2,3,4)
print(data[0])

db_config = ('localhost', 5432 , 'my_database')
print(db_config)

# set: unordered, unique collections of items usages - use for eliminating duplicates in datasets.
id =[1,1,2,3,4,4,3,3,5]
unique_id = set(id)
print(unique_id)

# Dictionary : key value pairs, unordered - ideal for mapping configurations, caching or column to data mappings.
data_mappings = {'id':1,'name':'alice'}
print(data_mappings['name'])

# comprehension - efficent way to create list, dictionary, or sets
square_dict = {x:x**2 for x in range(5)}
print(square_dict)