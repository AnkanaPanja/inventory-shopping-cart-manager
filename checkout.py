# Checkout Management Module

from data import inventory, cart
from billing import display_bill


# 1. Validate Shopping Cart
def validate_cart():

    if not cart:
        print("Shopping cart is empty!")
        return False

    for product_id, quantity in cart.items():

        if product_id not in inventory:
            print("Product not found:", product_id)
            return False

        if quantity <= 0:
            print("Invalid quantity for:", product_id)
            return False

        available_stock = inventory[product_id]["stock"]

        if quantity > available_stock:

            print("\nInsufficient stock for:",
                  inventory[product_id]["name"])

            print("Available Stock:", available_stock)
            print("Requested Quantity:", quantity)

            return False

    return True


# 2. Update Inventory After Purchase
def update_inventory():

    for product_id, quantity in cart.items():

        inventory[product_id]["stock"] -= quantity


# 3. Complete Checkout
def checkout():

    print("\n========== CHECKOUT ==========")

    # Validate cart before purchase
    if not validate_cart():
        print("Checkout cannot proceed!")
        return

    # Display final bill
    display_bill()

    # Ask for purchase confirmation
    confirm = input(
        "\nConfirm your purchase? (yes/no): "
    ).strip().lower()

    if confirm == "yes":

        # Reduce inventory stock
        update_inventory()

        # Clear shopping cart
        cart.clear()

        print("\nPurchase completed successfully!")
        print("Inventory updated successfully!")
        print("Shopping cart cleared.")

    else:

        print("\nPurchase cancelled.")
        print("Your shopping cart is unchanged.")

    print("==============================")
