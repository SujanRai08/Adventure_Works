class Product:
    def __init__(self, ProductID, Productname):
        self.ProductID = ProductID
        self.Productname = Productname

    def show_product(self):
        return f"Product ID: {self.ProductID}, Name: {self.Productname}"
class Brand:
    def __init__(self, brand_name):
        self.brand_name = brand_name

    def show_brand(self):
        return f"Brand: {self.brand_name}"

class Sales(Product, Brand):
    def __init__(self, ProductID, Productname, brand_name, SalesPrice):
        Product.__init__(self, ProductID, Productname)  
        Brand.__init__(self, brand_name) 
        self.SalesPrice = float(SalesPrice)

    def Revenue(self, quantity):
        return f"Total Revenue: {self.SalesPrice * quantity}"

s1 = Sales(2, "Nivea Lotion", "Nivea", 400)
print(s1.show_product()) 
print(s1.show_brand())   
print(s1.Revenue(10))   
