# List of classes

class Order:
    def __init__(self, orderName, quantity):
        self.orderName = orderName
        self.quantity = quantity

    def __str__(self):
        return f'Your order is {self.quantity} of {self.orderName}'