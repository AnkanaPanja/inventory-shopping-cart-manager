# Billing Management Module

from data import inventory, cart
from shopping_cart import calculate_subtotal


# 1. Calculate Total Bill
def calculate_bill():

    if not cart:
        return 0.0

    total_amount = calculate_subtotal()

    return total_amount


# 2. Display Item-wise Bill
def display_bill():

    if not cart:
        print("\nShopping cart is empty!")
        print("Cannot generate bill.")
        return

    print("\n")
    print("=" * 65)
    print("                 CUSTOMER BILL")
    print("=" * 65)

    print(
        f"{'Product ID':<13}"
        f"{'Product Name':<20}"
        f"{'Price':<10}"
        f"{'Quantity':<10}"
        f"{'Amount'}"
    )

    print("-" * 65)

    for product_id, quantity in cart.items():

        product = inventory[product_id]

        name = product["name"]
        price = product["price"]

        amount = price * quantity

        print(
            f"{product_id:<13}"
            f"{name:<20}"
            f"{price:<10.2f}"
            f"{quantity:<10}"
            f"{amount:.2f}"
        )

    print("-" * 65)

    subtotal = calculate_bill()

    print(f"\nSubtotal: Rs. {subtotal:.2f}")

    print("-" * 65)

    print(f"TOTAL AMOUNT: Rs. {subtotal:.2f}")

    print("=" * 65)

    print("Thank you for shopping with us!")


# 3. Generate Billing Summary
def generate_bill():

    if not cart:
        print("No items available for billing!")
        return

    total = calculate_bill()

    print("\n========== BILLING SUMMARY ==========")

    print("Total Items:", sum(cart.values()))

    print("Total Products:", len(cart))

    print(f"Total Amount: Rs. {total:.2f}")

    print("=====================================")
