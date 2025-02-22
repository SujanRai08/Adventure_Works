# why? -> Functionak programming makes data trandofrmations, etl pipelines, and parallel processing more efiicient. 
# using map, filter, reduce for data transformations 
# - imagine you are procssing sales data where prices are in different format as and need to be converted to float. 

from functools import reduce
sales_data = [
        {"product": "Laptop", "price": "1200.50"},
        {"product": "Mouse", "price": "25.99"},
        {"product": "Keyboard", "price": "45.99"}
]
# Convert price to float using map
sales_data = list(map(lambda item:{**item,"price":float(item["price"])},sales_data))

# filter out expensive items
affordable_items = list(filter(lambda item: item["price"] < 100, sales_data))

#  calculate total revenue using reduce
total_revenue = reduce(lambda acc, item:acc + item["price"],sales_data, 0)

print("Transformed Data:", sales_data)
print("Affordable Items: ", affordable_items)
print("Total Revenue",total_revenue)
