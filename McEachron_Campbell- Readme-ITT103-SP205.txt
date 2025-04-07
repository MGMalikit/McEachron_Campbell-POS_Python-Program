Authors: Kyle Campbell & Malik McEachron
Date Created: 30/03/2025
Course: ITT103
URL Code: https://github.com/Kylo73/McEachron_Campbell-POS_Python-Program.git


Purpose of the Program

This Python code Point of Sale (POS) System is designed to facilitate the sale of products at a retail store. It allows users to:

- View available products along with their prices and stock levels.
- Add and remove items from a shopping cart.
- Apply discounts and calculate taxes at checkout.
- Generate a detailed receipt after a successful purchase.
- Handle stock updates dynamically as items are purchased.


How to Run the Program

- Ensure you have Python 3.x installed on your system or any other application.
- No additional libraries are required as the program uses built-in Python modules.


Required Modifications

-Persistent Storage: Modify the program to store product data in a file or database so stock levels remain updated between sessions.
-Stock Management: Add an option to restock products dynamically instead of restarting the script.
-User Authentication: Implement login/logout functionality for staff management.


Assumptions & Limitations

-Stock updates only within session:Currently, stock levels reset when the program is restarted.
-Limited Payment Handling: The program assumes cash transactions only and does not handle card payments.
-No Refunds or Returns: Once an item is purchased, there is no option for a return or refund.
-Discount Application: Only a 5% discount is applied on purchases above $5000.
-Fixed Tax Rate: The program assumes a flat 10% tax rate.



