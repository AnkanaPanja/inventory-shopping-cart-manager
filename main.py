# Inventory and Shopping Cart Manager
# Main Menu Program

from product_management import (
    add_product,
    display_products,
    search_product,
    update_product,
    delete_product
)

from inventory import display_stock, check_low_stock

from shopping_cart import (
    add_to_cart,
    remove_from_cart,
    update_cart,
    display_cart
)

from billing import generate_bill, display_bill

from checkout import checkout


def display_menu():
    print("\n")
    print("=" * 50)
    print("       INVENTORY AND SHOPPING CART MANAGER")
    print("=" * 50)

    print("\n--- PRODUCT MANAGEMENT ---")
    print("1. Add Product")
    print("2. Display All Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")

    print("\n--- INVENTORY MANAGEMENT ---")
    print("6. Display Inventory")
    print("7. Check Low Stock")

    print("\n--- SHOPPING CART ---")
    print("8. Add Product to Cart")
    print("9. Remove Product from Cart")
    print("10. Update Cart Quantity")
    print("11. Display Shopping Cart")

    print("\n--- BILLING AND CHECKOUT ---")
    print("12. Generate Bill")
    print("13. Billing Summary")
    print("14. Checkout")

    print("\n0. Exit")
    print("=" * 50)


def main():

    print("\nWelcome to Inventory and Shopping Cart Manager!")

    while True:

        display_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_product()

        elif choice == "2":
            display_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            display_stock()

        elif choice == "7":
            check_low_stock()

        elif choice == "8":
            add_to_cart()

        elif choice == "9":
            remove_from_cart()

        elif choice == "10":
            update_cart()

        elif choice == "11":
            display_cart()

        elif choice == "12":
            display_bill()

        elif choice == "13":
            generate_bill()

        elif choice == "14":
            checkout()

        elif choice == "0":
            print("\nThank you for using our application!")
            print("Exiting the program...")
            break

        else:
            print("\nInvalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
