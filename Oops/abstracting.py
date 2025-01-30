class Product:
    def __init__(self, ProductID, Productname, category, Quantity):
        self.ProductID = ProductID
        self.Productname = Productname
        self.category = category
        self.Quantity = Quantity  

    def Companies(self):
        return f"The product ID: {self.ProductID}, Product Name: {self.Productname}"

    def Categories(self):
        categories = self.category  
        print("The total product categories: ", categories)


class Sales(Product):
    def __init__(self, ProductID, Productname, category, Quantity, SalesID, SalesPrice):
        super().__init__(ProductID, Productname, category, Quantity)
        self.SalesID = SalesID
        self.SalesPrice = float(SalesPrice)  

    def Revenue(self):
        total_revenue = self.Quantity * self.SalesPrice
        return f"The total sales quantity is {self.Quantity}, total sales price {self.SalesPrice} = {total_revenue}"
        
s1 = Sales(1, "Vaseline", "Moisturizer", 5, "122x21", 340)
print(s1.Revenue())  
