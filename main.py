from cart import Cart
from checkout import checkout
from data_handler import save_cart_to_file, load_cart_from_file

def main():
    cart = load_cart_from_file('cart.json')
    filename = 'cart.json'

    while True:
        print("\nE-commerce Cart System")
        print("1. Add Item to Cart")
        print("2. Remove Item from Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Save & Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            item = Item(name, price, quantity)
            cart.add_item(item)
            print(f"Added: {item}")

        elif choice == '2':
            name = input("Enter item name to remove: ")
            cart.remove_item(name)
            print(f"Removed item: {name}")

        elif choice == '3':
            items = cart.view_cart()
            print("Items in cart:")
            for item in items:
                print(item)

        elif choice == '4':
            total = checkout(cart)
            print(f"Total amount due: ${total:.2f}")

        elif choice == '5':
            save_cart_to_file(cart, filename)
            print("Cart saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
