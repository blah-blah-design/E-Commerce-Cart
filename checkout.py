from cart import Cart

def checkout(cart: Cart):
    total = cart.total_price()
    print("Checkout Summary:")
    for item in cart.view_cart():
        print(item)
    print(f"Total Amount: ${total:.2f}")
    return total
