# using numpy and pandas 
# Powerful for data manipulation and analysis.
# Works well with structured data like CSV, Excel, or SQL tables.
import pandas as pd
sales_data = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'A', 'C'],
    'Quantity': [10, 15, 8, 12, 20],
    'Price': [100, 150, 120, 110, 130]
})
sales_data['Total'] = sales_data['Quantity'] * sales_data['Price']
grouped = sales_data.groupby('Product')['Total'].sum()
print(grouped)


# numpy for faster numerical computations on large datasets 
import numpy as np

data = np.array([[10, 15], [8, 12]])
print("Mean:", np.mean(data))
print("Sum:", np.sum(data))
