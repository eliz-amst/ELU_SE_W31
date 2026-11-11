
"""Functions for calculating and displaying shopping cart totals."""

CART = [
    {'name': 'Item A', 'price': 10.99},
    {'name': 'Item B', 'price': 5.99},
    {'name': 'Item C', 'price': '8.49'}
]


def calculate_total(cart):
    """Calculate the total price of all items in the cart."""
    total = 0.0
    for cart_item in cart:
        total += float(cart_item['price'])
    return total


def display_total(total):
    """Display the total price."""
    print(f"Total price: ${total:.2f}")


def main():
    """Display cart items and their total."""
    for cart_item in CART:
        print(f"Item: {cart_item['name']} - Price: ${cart_item['price']}")

    shopping_cart_total = calculate_total(CART)
    display_total(shopping_cart_total)


if __name__ == "__main__":
    main()
