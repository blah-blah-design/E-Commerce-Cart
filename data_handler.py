import json

def save_cart_to_file(cart, filename):
    with open(filename, 'w') as f:
        json.dump({name: vars(item) for name, item in cart.items.items()}, f)

def load_cart_from_file(filename):
    cart = Cart()
    try:
        with open(filename, 'r') as f:
            items_data = json.load(f)
            for item_data in items_data.values():
                item = Item(**item_data)
                cart.add_item(item)
    except FileNotFoundError:
        pass
    return cart
