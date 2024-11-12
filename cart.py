from item import Item

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.name in self.items:
            self.items[item.name].quantity += item.quantity
        else:
            self.items[item.name] = item

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def view_cart(self):
        return list(self.items.values())

    def total_price(self):
        return sum(item.price * item.quantity for item in self.items.values())
