# Inventory Management Module

from data import inventory


# 1. Display Available Stock
def display_stock():

    if not inventory:
        print("Inventory is empty!")
        return

    print("\n========== INVENTORY STATUS ==========")

    print(f"{'Product ID':<15}{'Product Name':<20}{'Stock'}")
    print("-" * 45)

    for product_id, details in inventory.items():

        print(
            f"{product_id:<15}"
            f"{details['name']:<20}"
            f"{details['stock']}"
        )

    print("=" * 45)


# 2. Check Stock Availability
def check_stock(product_id, quantity):

    if product_id not in inventory:
        return False

    if quantity <= 0:
        return False

    available_stock = inventory[product_id]["stock"]

    return available_stock >= quantity


# 3. Get Available Quantity
def get_available_stock(product_id):

    if product_id not in inventory:
        return 0

    return inventory[product_id]["stock"]


# 4. Validate Product Quantity
def validate_quantity(product_id, quantity):

    if product_id not in inventory:
        print("Product does not exist!")
        return False

    if quantity <= 0:
        print("Quantity must be greater than zero!")
        return False

    if not check_stock(product_id, quantity):

        print("Insufficient stock!")

        print(
            "Available quantity:",
            get_available_stock(product_id)
        )

        return False

    return True


# 5. Check Low Stock Products
def check_low_stock():

    threshold = 5

    print("\n========== LOW STOCK ALERT ==========")

    found = False

    for product_id, details in inventory.items():

        if details["stock"] <= threshold:

            print(
                product_id,
                "-",
                details["name"],
                "| Stock:",
                details["stock"]
            )

            found = True

    if not found:
        print("No low-stock products!")

    print("=" * 40)
