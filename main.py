
# ============================================================
# GROUP 4 PROJECT
# DYNAMIC E-COMMERCE CART
#
# Group Members:
# 1. Md Touseef Warsi
# 2. Aditya Kumar Singh
# 3. Md Ashif
#
# Programming Language: Python
# Concepts: Lists, Dictionaries and Functions
#
# Project Description:
# A menu-driven shopping cart application that allows users
# to view, search, add, remove and update products.
# It automatically calculates subtotal, demonstration tax
# and final payable amount.
# ============================================================


# ------------------------------------------------------------
# 1. PRODUCT DATABASE (NESTED DICTIONARY)
# ------------------------------------------------------------

products = {
    101: {"name": "Laptop", "price": 50000},
    102: {"name": "Mouse", "price": 500},
    103: {"name": "Keyboard", "price": 1200},
    104: {"name": "Headphones", "price": 2000},
    105: {"name": "Mobile Phone", "price": 15000},
    106: {"name": "Monitor", "price": 12000},
    107: {"name": "Printer", "price": 8000},
    108: {"name": "Webcam", "price": 2500}
}


# ------------------------------------------------------------
# 2. SHOPPING CART (LIST OF DICTIONARIES)
# ------------------------------------------------------------

cart = []


# ------------------------------------------------------------
# 3. DEMONSTRATION TAX CONFIGURATION
# ------------------------------------------------------------

# 5% is used only for academic demonstration.
# It is not a claim about the applicable GST rate.

TAX_RATE = 0.05
TAX_LABEL = "Demonstration Tax (5%)"


# ------------------------------------------------------------
# FUNCTION 1: DISPLAY PROJECT INTRODUCTION
# ------------------------------------------------------------

def display_intro():

    print("\n" + "=" * 65)
    print("             WELCOME TO OUR PROJECT")
    print("                DYNAMIC E-COMMERCE CART")
    print("=" * 65)

    print("\nPROJECT DEVELOPED BY GROUP 4")

    print("1. Md Touseef Warsi")
    print("2. Aditya Kumar Singh")
    print("3. Md Ashif")

    print("\nPROJECT DESCRIPTION")
    print("-" * 65)

    print("This application provides a simple shopping cart system.")
    print("Users can view, search, add, remove and update products.")
    print("It automatically calculates the shopping bill and tax.")

    print("\nHOW TO USE THE APPLICATION")
    print("-" * 65)

    print("1. Select an option from the main menu.")
    print("2. View products and their prices.")
    print("3. Enter a product ID to add items to your cart.")
    print("4. Update or remove products whenever required.")
    print("5. Calculate your bill and confirm checkout.")

    print("\nNOTE:")
    print("The application uses a 5% demonstration tax rate.")

    print("=" * 65)

    input("\nPress Enter to continue...")


# ------------------------------------------------------------
# FUNCTION 2: DISPLAY HEADER
# ------------------------------------------------------------

def display_header():

    print("\n" + "=" * 65)
    print("                    DYNAMIC E-COMMERCE CART")
    print("=" * 65)


# ------------------------------------------------------------
# FUNCTION 3: DISPLAY AVAILABLE PRODUCTS
# ------------------------------------------------------------

def display_products():

    display_header()

    print("\nAVAILABLE PRODUCTS")
    print("-" * 65)

    print(f"{'ID':<10}{'PRODUCT':<30}{'PRICE (Rs.)':>20}")

    print("-" * 65)

    for product_id, details in products.items():

        print(
            f"{product_id:<10}"
            f"{details['name']:<30}"
            f"{details['price']:>20,}"
        )

    print("-" * 65)


# ------------------------------------------------------------
# FUNCTION 4: SEARCH PRODUCTS
# ------------------------------------------------------------

def search_product():

    keyword = input(
        "\nEnter product name to search: "
    ).strip().lower()

    if not keyword:

        print("Please enter a valid product name.")
        return

    found = False

    print("\nSEARCH RESULTS")
    print("-" * 45)

    for product_id, details in products.items():

        if keyword in details["name"].lower():

            print("Product ID:", product_id)
            print("Product Name:", details["name"])
            print("Price: Rs.", f"{details['price']:,}")

            print("-" * 45)

            found = True

    if not found:

        print("No matching product found.")


# ------------------------------------------------------------
# FUNCTION 5: ADD PRODUCT TO CART
# ------------------------------------------------------------

def add_to_cart():

    display_products()

    try:

        product_id = int(
            input("\nEnter Product ID: ")
        )

        if product_id not in products:

            print("\nInvalid Product ID!")
            return

        quantity = int(
            input("Enter Quantity: ")
        )

        if quantity <= 0:

            print("\nQuantity must be greater than zero!")
            return

        # Check whether the product already exists in cart.

        for item in cart:

            if item["product_id"] == product_id:

                item["quantity"] += quantity

                print("\nProduct quantity updated successfully!")

                print("New Quantity:", item["quantity"])

                return

        # Add a new product as a nested dictionary.

        cart.append({

            "product_id": product_id,

            "name": products[product_id]["name"],

            "price": products[product_id]["price"],

            "quantity": quantity

        })

        print("\nProduct added to cart successfully!")

        print("Product:", products[product_id]["name"])

        print("Quantity:", quantity)

    except ValueError:

        print("\nPlease enter valid numeric values!")


# ------------------------------------------------------------
# FUNCTION 6: REMOVE PRODUCT FROM CART
# ------------------------------------------------------------

def remove_from_cart():

    if not cart:

        print("\nYour shopping cart is empty!")
        return

    view_cart()

    try:

        product_id = int(
            input("\nEnter Product ID to remove: ")
        )

        for item in cart:

            if item["product_id"] == product_id:

                cart.remove(item)

                print("\nProduct removed successfully!")

                return

        print("\nProduct not found in cart!")

    except ValueError:

        print("\nPlease enter a valid Product ID!")


# ------------------------------------------------------------
# FUNCTION 7: UPDATE PRODUCT QUANTITY
# ------------------------------------------------------------

def update_quantity():

    if not cart:

        print("\nYour shopping cart is empty!")
        return

    view_cart()

    try:

        product_id = int(
            input("\nEnter Product ID: ")
        )

        # Find the product before asking for quantity.

        selected_item = None

        for item in cart:

            if item["product_id"] == product_id:

                selected_item = item
                break

        if selected_item is None:

            print("\nProduct not found in cart!")
            return

        quantity = int(
            input("Enter New Quantity: ")
        )

        if quantity <= 0:

            print("\nQuantity must be greater than zero!")
            return

        selected_item["quantity"] = quantity

        print("\nProduct quantity updated successfully!")

        print("New Quantity:", quantity)

    except ValueError:

        print("\nPlease enter valid numeric values!")


# ------------------------------------------------------------
# FUNCTION 8: VIEW SHOPPING CART
# ------------------------------------------------------------

def view_cart():

    display_header()

    print("\nYOUR SHOPPING CART")
    print("-" * 75)

    if not cart:

        print("Your shopping cart is currently empty!")

        print("-" * 75)

        return

    print(
        f"{'ID':<8}"
        f"{'PRODUCT':<22}"
        f"{'PRICE':>12}"
        f"{'QTY':>8}"
        f"{'TOTAL':>15}"
    )

    print("-" * 75)

    total_amount = 0

    total_quantity = 0

    for item in cart:

        subtotal = item["price"] * item["quantity"]

        total_amount += subtotal

        total_quantity += item["quantity"]

        print(
            f"{item['product_id']:<8}"
            f"{item['name']:<22}"
            f"{item['price']:>12,}"
            f"{item['quantity']:>8}"
            f"{subtotal:>15,}"
        )

    print("-" * 75)

    print("Distinct Products:", len(cart))

    print("Total Quantity:", total_quantity)

    print("Cart Subtotal: Rs.", f"{total_amount:,.2f}")

    print("-" * 75)


# ------------------------------------------------------------
# FUNCTION 9: CALCULATE FINAL BILL
# ------------------------------------------------------------

def calculate_bill():

    if not cart:

        print("\nYour shopping cart is empty!")

        return None

    display_header()

    print("\n                    FINAL BILL")

    print("-" * 65)

    subtotal = 0

    total_quantity = 0

    for item in cart:

        amount = item["price"] * item["quantity"]

        subtotal += amount

        total_quantity += item["quantity"]

        print(
            f"{item['name']} x {item['quantity']} "
            f"= Rs. {amount:,.2f}"
        )

    # Calculate demonstration tax.

    tax = round(subtotal * TAX_RATE, 2)

    # Calculate final amount.

    final_amount = round(subtotal + tax, 2)

    print("-" * 65)

    print("Distinct Products :", len(cart))

    print("Total Quantity    :", total_quantity)

    print(f"Subtotal          : Rs. {subtotal:,.2f}")

    print(f"{TAX_LABEL:<20}: Rs. {tax:,.2f}")

    print("-" * 65)

    print(f"FINAL AMOUNT      : Rs. {final_amount:,.2f}")

    print("=" * 65)

    return final_amount


# ------------------------------------------------------------
# FUNCTION 10: CHECKOUT
# ------------------------------------------------------------

def checkout():

    if not cart:

        print("\nYour shopping cart is empty!")

        print("Please add products before checkout.")

        return

    print("\n========== CHECKOUT ==========")

    # Generate the final bill.

    final_amount = calculate_bill()

    if final_amount is None:

        return

    # Accept only valid confirmation.

    while True:

        confirmation = input(
            "\nConfirm your order? (yes/no): "
        ).strip().lower()

        if confirmation in ("yes", "no"):

            break

        print("\nInvalid confirmation!")

        print("Please enter only 'yes' or 'no'.")

    if confirmation == "yes":

        print("\n" + "=" * 50)

        print("          ORDER PLACED SUCCESSFULLY!")

        print("Amount Paid: Rs.", f"{final_amount:,.2f}")

        print("Thank you for shopping with us!")

        print("=" * 50)

        # Clear the cart after successful checkout.

        cart.clear()

        print("\nYour shopping cart is now empty.")

    else:

        print("\nOrder cancelled.")

        print("Your products are still in the cart.")


# ------------------------------------------------------------
# FUNCTION 11: DISPLAY MAIN MENU
# ------------------------------------------------------------

def display_menu():

    display_header()

    print("\nMAIN MENU")

    print("-" * 65)

    print("1. View All Products")

    print("2. Search Products")

    print("3. Add Product to Cart")

    print("4. Remove Product from Cart")

    print("5. Update Product Quantity")

    print("6. View Shopping Cart")

    print("7. Calculate Final Bill")

    print("8. Checkout")

    print("9. Exit")

    print("-" * 65)


# ------------------------------------------------------------
# FUNCTION 12: MAIN PROGRAM
# ------------------------------------------------------------

def main():

    # Display project introduction first.

    display_intro()

    while True:

        display_menu()

        choice = input(
            "Enter Your Choice (1-9): "
        ).strip()

        if choice == "1":

            display_products()

        elif choice == "2":

            search_product()

        elif choice == "3":

            add_to_cart()

        elif choice == "4":

            remove_from_cart()

        elif choice == "5":

            update_quantity()

        elif choice == "6":

            view_cart()

        elif choice == "7":

            calculate_bill()

        elif choice == "8":

            checkout()

        elif choice == "9":

            print("\n" + "=" * 50)

            print("Thank you for using our application!")

            print("Have a nice day!")

            print("=" * 50)

            break

        else:

            print("\nInvalid choice!")

            print("Please select a number between 1 and 9.")


# ------------------------------------------------------------
# START THE APPLICATION
# ------------------------------------------------------------

if __name__ == "__main__":

    main()

# ============================================================
# END OF GROUP 4 PROJECT
# ============================================================
