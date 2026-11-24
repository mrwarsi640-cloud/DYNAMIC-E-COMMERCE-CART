# 🛒 DYNAMIC E-COMMERCE CART
### Group 4 – Python Programming Project

---

## 1. Project Information

**Project Title:** Dynamic E-Commerce Cart

**Project Type:** Python Console-Based Application

**Programming Language:** Python 3

**Development Environment:** Visual Studio Code

**Project Domain:** E-Commerce / Shopping Cart Management

**Group Number:** 4

### Group Members

1. Md Touseef Warsi
2. Aditya Kumar Singh
3. Md Ashif

---

## 2. Project Overview

Dynamic E-Commerce Cart is a Python-based shopping cart management application developed as a group project.

The main purpose of this project is to develop a simple and user-friendly shopping cart system that allows customers to view available products, search for products, add items to their shopping cart, remove products, update product quantities, and calculate the final shopping bill.

The application uses Python data structures such as lists and dictionaries to store and manage product information and shopping cart details.

It also uses functions, loops, conditional statements, and exception handling to perform different operations efficiently.

The system automatically calculates the subtotal, demonstration tax, and final payable amount.

This project demonstrates the practical implementation of Python programming concepts in a real-world e-commerce application.

---

## 3. Project Objectives

The main objectives of this project are:

- To develop a simple shopping cart management system using Python.
- To understand the practical implementation of Python lists and dictionaries.
- To store product information using nested dictionaries.
- To manage shopping cart items using lists.
- To implement functions for different shopping operations.
- To allow users to add, remove, and update products.
- To calculate the total shopping amount automatically.
- To implement demonstration tax calculation.
- To handle invalid user inputs using exception handling.
- To improve programming, logical thinking, and problem-solving skills.

---

## 4. Features of the Project

The Dynamic E-Commerce Cart provides the following features:

### 4.1 Project Introduction
Displays the project title, group member names, project description, and instructions for using the application.

### 4.2 View Available Products
Displays all available products with their product IDs, names, and prices.

### 4.3 Search Products
Allows users to search for products using their names.

### 4.4 Add Products to Cart
Allows users to select products using their product IDs and specify quantities.

If a product already exists in the cart, its quantity is increased instead of creating a duplicate entry.

### 4.5 Remove Products from Cart
Allows users to remove selected products from their shopping cart.

### 4.6 Update Product Quantity
Allows users to modify the quantity of an existing cart item.

### 4.7 View Shopping Cart
Displays the products currently added to the cart, including product ID, product name, price, quantity, and individual subtotal.

It also displays the total number of distinct products and total quantity.

### 4.8 Automatic Bill Calculation
Calculates the shopping subtotal, demonstration tax, and final payable amount automatically.

### 4.9 Checkout System
Allows users to confirm or cancel their orders.

After successful confirmation, the application displays an order success message and clears the shopping cart.

### 4.10 Input Validation
Handles invalid numerical inputs, incorrect product IDs, invalid quantities, and incorrect checkout confirmations.

---

## 5. Technologies and Tools Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| Visual Studio Code | Code editor |
| Python Lists | Shopping cart management |
| Python Dictionaries | Product database |
| Functions | Modular programming |
| Loops | Repeated operations |
| Conditional Statements | Decision-making |
| Exception Handling | Handling invalid inputs |
| GitHub | Source code hosting (optional) |

No external Python libraries are required for the current version.

---

## 6. Python Concepts Used

### 6.1 Dictionaries

Dictionaries are used to store product information in key-value pairs.

Example:

```python
products = {
    101: {"name": "Laptop", "price": 50000},
    102: {"name": "Mouse", "price": 500}
}
```

Each product ID acts as a key, while the product name and price are stored as values.

### 6.2 Nested Dictionaries

A dictionary inside another dictionary is used to organize product details.

This makes it easy to retrieve product names and prices using product IDs.

### 6.3 Lists

A list is used to store shopping cart items.

```python
cart = []
```

Users can add multiple products to this list.

### 6.4 List of Dictionaries

Each shopping cart item is represented as a dictionary stored inside a list.

Example:

```python
cart.append({
    "product_id": 102,
    "name": "Mouse",
    "price": 500,
    "quantity": 2
})
```

### 6.5 Functions

Functions divide the application into smaller and reusable operations.

The project contains functions for displaying products, searching products, adding products, removing products, updating quantities, viewing the cart, calculating bills, checkout, and displaying menus.

### 6.6 Loops

For loops are used to display products and process shopping cart items.

While loops are used to keep the application menu running until the user chooses to exit.

### 6.7 Conditional Statements

If, elif, and else statements are used to execute different operations according to user choices.

### 6.8 Exception Handling

Try and except statements are used to handle invalid numerical inputs and prevent unexpected program termination.

---

## 7. Product Database

The application contains the following sample products:

| Product ID | Product Name | Price (Rs.) |
|---|---|---:|
| 101 | Laptop | 50,000 |
| 102 | Mouse | 500 |
| 103 | Keyboard | 1,200 |
| 104 | Headphones | 2,000 |
| 105 | Mobile Phone | 15,000 |
| 106 | Monitor | 12,000 |
| 107 | Printer | 8,000 |
| 108 | Webcam | 2,500 |

These products are stored in a nested Python dictionary.

---

## 8. Tax and Bill Calculation

The application uses a 5% demonstration tax rate for academic purposes.

This is a project assumption and does not represent a universal or officially applicable GST rate.

The bill is calculated using the following formulas:

**Subtotal:**

Subtotal = Sum of (Product Price × Quantity)

**Demonstration Tax:**

Tax = Subtotal × 5 / 100

**Final Amount:**

Final Amount = Subtotal + Tax

### Example Calculation

Suppose a customer purchases:

- Mouse: 2 × Rs. 500 = Rs. 1,000
- Keyboard: 1 × Rs. 1,200 = Rs. 1,200
- Webcam: 1 × Rs. 2,500 = Rs. 2,500

Subtotal = Rs. 4,700

Demonstration Tax = Rs. 235

Final Amount = Rs. 4,935

---

## 9. Main Menu Options

The application provides the following menu:

1. View All Products
2. Search Products
3. Add Product to Cart
4. Remove Product from Cart
5. Update Product Quantity
6. View Shopping Cart
7. Calculate Final Bill
8. Checkout
9. Exit

Users can select any operation by entering its corresponding menu number.

---

## 10. Project File Structure

The project folder is organized as follows:

```text
Dynamic_Ecommerce_Cart/
│
├── main.py
│
├── README.md
│
└── Screenshots/
    │
    ├── 01_intro.png
    ├── 02_product_list.png
    ├── 03_add_to_cart.png
    ├── 04_shopping_cart.png
    ├── 05_final_bill.png
    └── 06_checkout.png
```

### File Description

- **main.py:** Contains the complete Python source code.
- **README.md:** Contains project information, features, instructions, and documentation.
- **Screenshots:** Contains screenshots of the application's actual execution and output.

---

## 11. System Requirements

### Hardware Requirements

- Computer or laptop
- Minimum 2 GB RAM recommended
- Keyboard and monitor
- Sufficient storage space

### Software Requirements

- Windows, Linux, or macOS
- Python 3
- Visual Studio Code or another Python editor

---

## 12. Installation and Execution

Follow these steps to run the project.

### Step 1: Install Python

Download and install Python 3 from:

https://www.python.org/downloads/

### Step 2: Install Visual Studio Code

Download VS Code from:

https://code.visualstudio.com/

### Step 3: Open the Project

Open the Dynamic_Ecommerce_Cart folder in Visual Studio Code.

### Step 4: Open the Terminal

Select Terminal → New Terminal.

### Step 5: Run the Application

Execute the following command:

```bash
python main.py
```

If the above command does not work on Windows, try:

```bash
py main.py
```

### Step 6: Use the Application

After execution, the project introduction and main menu will appear.

Select the desired operation by entering a menu number.

---

## 13. Testing and Validation

The application should be tested using different inputs to verify its functionality.

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| TC01 | Display products | All products displayed |
| TC02 | Search for Laptop | Laptop details displayed |
| TC03 | Search unknown product | No matching product message |
| TC04 | Add a valid product | Product added successfully |
| TC05 | Add an existing product | Quantity increased |
| TC06 | Enter invalid product ID | Error message displayed |
| TC07 | Enter zero quantity | Quantity rejected |
| TC08 | View shopping cart | Cart details displayed |
| TC09 | Update quantity | Quantity updated |
| TC10 | Remove product | Product removed |
| TC11 | Calculate bill | Subtotal, tax and final amount displayed |
| TC12 | Invalid checkout confirmation | User asked to enter yes or no |
| TC13 | Cancel checkout | Cart remains unchanged |
| TC14 | Confirm checkout | Order placed and cart cleared |
| TC15 | Exit application | Application terminates |

Note: These are the planned test cases. Actual test results should be recorded after executing the corresponding tests.

---

## 14. Advantages of the Project

- Simple and user-friendly interface.
- Easy product management.
- Automatic bill calculation.
- Supports adding and removing products.
- Supports quantity modification.
- Uses basic Python programming concepts.
- Handles several invalid inputs.
- Easy to understand and maintain.
- Does not require external libraries.

---

## 15. Limitations of the Project

The current version has some limitations:

1. Product information is predefined in the Python source code.
2. Shopping cart information is stored temporarily in memory.
3. Cart information is lost when the application closes or the cart is cleared after checkout.
4. The application does not have a user registration or login system.
5. No real online payment gateway is integrated.
6. No database is connected.
7. The application currently uses a console-based interface.
8. The 5% tax rate is only a demonstration assumption.

---

## 16. Future Scope

The project can be improved further by introducing:

- Graphical User Interface using Tkinter.
- Database integration using SQLite or MySQL.
- User registration and login.
- Product stock management.
- Product categories and filtering.
- Order history management.
- Online payment gateway integration.
- Product ratings and reviews.
- Invoice generation in PDF format.
- Web-based shopping cart functionality.

---

## 17. Conclusion

The Dynamic E-Commerce Cart project demonstrates the practical implementation of Python programming concepts in a shopping cart management application.

The project successfully combines lists, dictionaries, functions, loops, conditional statements, and exception handling to perform different shopping operations.

Users can view and search products, add items to their shopping cart, remove products, update quantities, calculate the final bill, and complete checkout.

Through this project, the group has gained practical experience in developing a menu-driven application, managing structured data, writing reusable functions, and handling user inputs.

This project provides a foundation for developing more advanced e-commerce applications in the future.

---

## 18. References

1. Python Official Documentation: https://docs.python.org/3/
2. Python Data Structures: https://docs.python.org/3/tutorial/datastructures.html
3. Python Functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
4. Visual Studio Code Documentation: https://code.visualstudio.com/docs

---

**PROJECT DEVELOPED BY GROUP 4**

Md Touseef Warsi | Aditya Kumar Singh | Md Ashif

**Project Title: Dynamic E-Commerce Cart**

**Programming Language: Python 3**