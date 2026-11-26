# Shopping Cart Management Module

from data import inventory, cart
from inventory import validate_quantity


# 1. Add Product to Cart
def add_to_cart():

    product_id = input("Enter Product ID: ").strip().upper()

    if product_id not in inventory:
        print("Product not found!")
        return

    try:
        quantity = int(input("Enter Quantity: "))

    except ValueError:
        print("Please enter a valid quantity!")
        return

    current_quantity = cart.get(product_id, 0)
    total_quantity = current_quantity + quantity

    if not validate_quantity(product_id, total_quantity):
        return

    cart[product_id] = total_quantity

    print("Product added to cart successfully!")


# 2. Remove Product from Cart
def remove_from_cart():

    product_id = input("Enter Product ID to remove: ").strip().upper()

    if product_id not in cart:
        print("Product not found in cart!")
        return

    del cart[product_id]

    print("Product removed from cart successfully!")


# 3. Update Cart Quantity
def update_cart():

    product_id = input("Enter Product ID: ").strip().upper()

    if product_id not in cart:
        print("Product not found in cart!")
        return

    try:
        quantity = int(input("Enter New Quantity: "))

    except ValueError:
        print("Invalid quantity!")
        return

    if not validate_quantity(product_id, quantity):
        return

    cart[product_id] = quantity

    print("Cart quantity updated successfully!")


# 4. Display Shopping Cart
def display_cart():

    if not cart:
        print("\nYour shopping cart is empty!")
        return

    print("\n========== SHOPPING CART ==========")

    print(
        f"{'ID':<10}"
        f"{'Product':<20}"
        f"{'Price':<12}"
        f"{'Quantity':<12}"
        f"{'Total'}"
    )

    print("-" * 64)

    for product_id, quantity in cart.items():

        product = inventory[product_id]

        price = product["price"]
        total = price * quantity

        print(
            f"{product_id:<10}"
            f"{product['name']:<20}"
            f"{price:<12.2f}"
            f"{quantity:<12}"
            f"{total:.2f}"
        )

    print("-" * 64)

    print(f"Subtotal: Rs. {calculate_subtotal():.2f}")


# 5. Calculate Cart Subtotal
def calculate_subtotal():

    subtotal = 0

    for product_id, quantity in cart.items():

        price = inventory[product_id]["price"]

        subtotal += price * quantity

    return subtotal
