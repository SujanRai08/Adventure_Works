# Python does not have a built-in interface keyword like Java or C#. However, we can achieve interface-like behavior using abstract classes with only abstract methods.

# 🔹 Why Use Interfaces?
# Ensures that multiple unrelated classes follow a common structure.
# Encourages polymorphism (different classes with the same methods).
# Helps decouple implementation from design.

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class PayPal(PaymentGateway):
    def process_payment(self, amount):
        return f"Processing PayPal payment of {amount}"

    def refund(self, amount):
        return f"Refunding PayPal payment of {amount}"


class Stripe(PaymentGateway):
    def process_payment(self, amount):
        return f"Processing Stripe payment of {amount}"

    def refund(self, amount):
        return f"Refunding Stripe payment of {amount}"


paypal = PayPal()
stripe = Stripe()

print(paypal.process_payment(100))  
print(stripe.refund(50))            
