import sys

# Product catalog (Product Name: [Price, Stock Quantity])
products = {
    "Lasco":       [650.0, 20],
    "Brown Bread": [725.0, 10],
    "Oats":        [550.0, 18],
    "Cornflakes":  [650.0, 12],
    "Soda":        [120.0, 30],
    "Broom":      [1000.0, 25],
    "Betty Milk":  [250.0, 18],
    "Bun":         [200.0, 20],
    "Cheese":      [100.0, 12],
    "Pancake":     [2450.0, 6]
}

# Shopping cart starts empty
default_cart = {}


def display_products():
    ##Show the available products along with price and stock quantity
    print("\nAvailable Products:")
    for product, details in products.items():
        stock_status = "LOW STOCK ON ITEM!" if details[1] < 5 else ""
        print(f"{product}: ${details[0]:.2f} (Stock: {details[1]}) {stock_status}")


def add_to_cart(cart):
    ##Allows the user to add an item to their cart
    display_products()
    product_name = input("Enter the product name: ").title()
    if product_name in products:
        try:
            quantity = int(input("Enter quantity: "))
            ##Check if requested quantity is within available stock
            if 0 < quantity <= products[product_name][1]:
                cart[product_name] = cart.get(product_name, 0) + quantity ##Add to cart (or increase quantity)
                products[product_name][1] -= quantity ##Reduce stock
                print(f"{quantity} {product_name}(s) added to cart.")
            else:
                print("Invalid quantity or insufficient stock!")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("Product not found!")


def remove_from_cart(cart):##Removes an item from the cart and restores the stock quantity
    if not cart:
        print("Cart is empty!")
        return

    product_name = input("Enter the product name to remove: ").title()
    if product_name in cart:
        products[product_name][1] += cart[product_name] ##Restore stock
        del cart[product_name] ##Remove from cart
        print(f"{product_name} removed from cart.")
    else:
        print("Product is no longer in cart!")


def view_cart(cart): ##Displays the contents of the cart along with the total cost
    if not cart:
        print("The cart is empty!")
        return
    print("\nShopping Cart:")
    total = 0
    for product, quantity in cart.items():
        price = products[product][0] * quantity
        print(f"{product}: {quantity} x ${products[product][0]:.2f} = ${price:.2f}")
        total += price
    print(f"Subtotal: ${total:.2f}")


def checkout(cart): ##This handles the checkout process, applying discounts and calculating the tax
    if not cart:
        print("The cart is empty! Please Add items before checkout.")
        return

    subtotal = sum(products[item][0] * qty for item, qty in cart.items())
    discount = 0.05 * subtotal if subtotal > 5000 else 0 ##5% discount for orders over $5k
    tax = 0.10 * (subtotal - discount) ##10% tax applied after discount
    total = (subtotal - discount) + tax

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax (10%): +${tax:.2f}")
    print(f"Total Amount Due: ${total:.2f}")

    while True:
        try:
            amount_paid = float(input("Enter amount paid: "))
            if amount_paid >= total:
                change = amount_paid - total
                print(f"Change: ${change:.2f}")
                generate_receipt(cart, subtotal, discount, tax, total, amount_paid, change)
                cart.clear() ##Empty cart after successful checkout
                break
            else:
                print("Insufficient funds. Try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def generate_receipt(cart, subtotal, discount, tax, total, amount_paid, change):

    import datetime
        ##Prints receipt with the current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  #Get current date & time

    ##Prints a detailed receipt for the customer's purchase
    print("\n---------------- BEST BUY RETAIL STORE------------------------")
    print(f"Date & Time: {current_time}")  ##Displays the date and time
    print("Items:")
    for product, quantity in cart.items():
        price = products[product][0] * quantity
        print(f"{product}: {quantity} x ${products[product][0]:.2f} = ${price:.2f}")
    print("______________________________________________________________")
    print(f"Subtotal:                                ${subtotal:.2f}")
    print(f"Discount:                                 -${discount:.2f}")
    print(f"Tax (10%):                               +${tax:.2f}")
    print(f"Total:                                   ${total:.2f}")
    print("_______________________________________________________________")
    print(f"Amount Paid:                            ${amount_paid:.2f}")
    print(f"Change:                                 ${change:.2f}")
    print("_______________________________________________________________")
    print("\n   Thank You for Shopping with BEST BUY RETAIL STORE 😁")



def main():
    ##Main function that controls the shopping system menu
    cart = default_cart.copy() #Create a fresh cart for each session
    while True:
        print("\n1. View Products\n2. View Cart \n3. Add to Cart\n4. Remove from Cart\n5. Checkout\n6. Exit")
        choice = input("Choose an option 1-6: ")
        if choice == "1":
            display_products()
        elif choice == "2":
            view_cart(cart)
        elif choice == "3":
            add_to_cart(cart)
        elif choice == "4":
            remove_from_cart(cart)
        elif choice == "5":
            checkout(cart)
        elif choice == "6":
            print("Exiting system......")
            sys.exit()
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()