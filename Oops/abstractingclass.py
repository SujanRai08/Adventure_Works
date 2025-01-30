from abc import ABC,abstractmethod

# An abstract class is a class that cannot be instantiated and is meant to be inherited by other classes. It contains one or more abstract methods, which must be implemented by any derived class.

# 🔹 Why Use Abstract Classes?
# Enforces that certain methods must be implemented in derived classes.
# Provides a template for child classes.
# Promotes code reusability and better design.

class Product(ABC):
    def __init__(self,ProductID,Productname):
        self.ProductID = ProductID
        self.Productname = Productname

    @abstractmethod
    def calculate_price(self):
        pass
    def show_product(self):
        return f"Product ID: {self.ProductID}, Name: {self.Productname}"
    

class Sales(Product):
    def __init__(self, ProductID, Productname, SalesPrice):
        super().__init__(ProductID, Productname)
        self.SalesPrice = SalesPrice

    def calculate_price(self):
        return f"Price of {self.Productname} is {self.SalesPrice}"

s1 = Sales(1, "Vaseline", 340)
print(s1.show_product())  
print(s1.calculate_price())  