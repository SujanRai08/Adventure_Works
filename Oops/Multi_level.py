# Base class
class Product:
    def __init__(self, ProductID, Productname, category, Quantity):
        self.ProductID = ProductID
        self.Productname = Productname
        self.category = category
        self.Quantity = Quantity

    def show_product(self):
        return f"Product ID: {self.ProductID}, Name: {self.Productname}, Category: {self.category}"

class Sales(Product):
    def __init__(self, ProductID, Productname, category, Quantity, SalesID, SalesPrice):
        super().__init__(ProductID, Productname, category, Quantity)
        self.SalesID = SalesID
        self.SalesPrice = float(SalesPrice)

    def Revenue(self):
        total_revenue = self.Quantity * self.SalesPrice
        return f"Total Revenue: {total_revenue}"

class DiscountedSales(Sales):
    def __init__(self, ProductID, Productname, category, Quantity, SalesID, SalesPrice, Discount):
        super().__init__(ProductID, Productname, category, Quantity, SalesID, SalesPrice)
        self.Discount = float(Discount)

    def Revenue(self):
        discounted_price = self.SalesPrice - (self.SalesPrice * self.Discount / 100)
        total_revenue = self.Quantity * discounted_price
        return f"Discounted Revenue: {total_revenue}"

d1 = DiscountedSales(1, "Vaseline", "Moisturizer", 5, "122x21", 340, 10)
print(d1.show_product()) 
print(d1.Revenue())     
