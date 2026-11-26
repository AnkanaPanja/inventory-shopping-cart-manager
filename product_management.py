# Product Management Module

from data import inventory, cart


# 1. Add New Product
def add_product():

    product_id = input("Enter Product ID: ").strip().upper()

    if product_id in inventory:
        print("Product ID already exists!")
        return

    name = input("Enter Product Name: ").strip()

    if not name:
        print("Product name cannot be empty!")
        return

    try:
        price = float(input("Enter Product Price: "))
        stock = int(input("Enter Initial Stock: "))

        if price < 0 or stock < 0:
            print("Price and stock cannot be negative!")
            return

    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return

    inventory[product_id] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    print("Product added successfully!")


# 2. Display All Products
def display_products():

    if not inventory:
        print("No products available!")
        return

    print("\n========== PRODUCT LIST ==========")

    print(f"{'ID':<10}{'Name':<20}{'Price':<12}{'Stock'}")
    print("-" * 52)

    for product_id, details in inventory.items():

        print(
            f"{product_id:<10}"
            f"{details['name']:<20}"
            f"{details['price']:<12.2f}"
            f"{details['stock']}"
        )

    print("=" * 52)


# 3. Search Product
def search_product():

    search = input("Enter Product ID or Name: ").strip()

    found = False

    for product_id, details in inventory.items():

        if (product_id.lower() == search.lower()
                or search.lower() in details["name"].lower()):

            print("\nProduct Found!")
            print("Product ID:", product_id)
            print("Name:", details["name"])
            print("Price:", details["price"])
            print("Available Stock:", details["stock"])

            found = True

    if not found:
        print("Product not found!")


# 4. Update Product
def update_product():

    product_id = input("Enter Product ID to update: ").strip().upper()

    if product_id not in inventory:
        print("Product not found!")
        return

    print("\n1. Update Name")
    print("2. Update Price")
    print("3. Update Stock")

    choice = input("Enter your choice: ")

    if choice == "1":

        new_name = input("Enter New Name: ").strip()

        if not new_name:
            print("Name cannot be empty!")
            return

        inventory[product_id]["name"] = new_name

    elif choice == "2":

        try:
            new_price = float(input("Enter New Price: "))

            if new_price < 0:
                print("Price cannot be negative!")
                return

            inventory[product_id]["price"] = new_price

        except ValueError:
            print("Invalid price!")
            return

    elif choice == "3":

        try:
            new_stock = int(input("Enter New Stock: "))

            if new_stock < 0:
                print("Stock cannot be negative!")
                return

            inventory[product_id]["stock"] = new_stock

        except ValueError:
            print("Invalid stock!")
            return

    else:
        print("Invalid choice!")
        return

    print("Product updated successfully!")


# 5. Delete Product
def delete_product():

    product_id = input("Enter Product ID to delete: ").strip().upper()

    if product_id not in inventory:
        print("Product not found!")
        return

    if product_id in cart:
        print("Cannot delete! Product exists in shopping cart.")
        return

    confirm = input("Are you sure? (yes/no): ").strip().lower()

    if confirm == "yes":

        del inventory[product_id]

        print("Product deleted successfully!")

    else:
        print("Deletion cancelled.")
