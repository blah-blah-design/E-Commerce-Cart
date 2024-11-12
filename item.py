class Item:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name} (Price: ${self.price:.2f}, Quantity: {self.quantity})"
