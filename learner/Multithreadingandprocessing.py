# why? - speeds up data processing by utilizing cpu cores efficiently.EOFError 

# parallel data transformation using  multiprocessing 
import multiprocessing
import multiprocessing.pool
def tranformation(record):
    return {**record,"price":float(record["price"])*1.1} # increaing the price by 10%

sales_data = [
    {"product": "Laptop", "price": "1200.50"},
    {"product": "Mouse", "price": "25.99"},
    {"product": "Keyboard", "price": "45.99"}
]

if __name__ =="__main__":
    with multiprocessing.Pool(processes=2)as pool:
        tranformation = pool.map(tranformation,sales_data)
    print(tranformation)