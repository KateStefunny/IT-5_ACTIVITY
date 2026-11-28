#Final
#Combine the corrected program from Task 1 and the developed program from 
# Task 2 into a complete Canteen Ordering and Billing Management System.

menu = {
    "Burger": 85,
    "Fries": 45,
    "Drink": 30,
    "Chicken": 120
}

orders = {}

# ===== PART 1: ORDERING (from Task 1) =====
print("===== CANTEEN MENU =====")

for item, price in menu.items():
    print(item, "-", price)

number = int(input("\nEnter number of order attempts: "))

for i in range(1, number + 1):

    print("\nOrder", i)

    item = input("Enter item name: ").title()

    if item not in menu:
        print("Item not available!")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Invalid quantity!")
        continue

    orders[item] = quantity

print("\n===== ORDER SUMMARY =====")

for item, quantity in orders.items():
    print(item, "x", quantity)

# ===== PART 2: BILLING (from Task 2) =====
if len(orders) == 0:
    print("\nNo valid orders. Nothing to bill.")
else:
    print("\n===== BILL =====")

    total = 0

    for item, quantity in orders.items():
        price = menu[item]
        subtotal = price * quantity
        total = total + subtotal
        print(item, "x", quantity, "@", price, "=", subtotal)

    print("\nTotal:", total)

    # Discount: 10% off if the total is 500 or more
    if total >= 500:
        discount = total * 0.10
    else:
        discount = 0

    amount_due = total - discount

    print("Discount:", discount)
    print("Amount Due:", amount_due)

    payment = float(input("\nEnter payment: "))

    while payment < amount_due:
        print("Insufficient payment! You still need", amount_due - payment)
        payment = float(input("Enter payment: "))

    change = payment - amount_due

    print("Change:", change)
    print("\nThank you for your purchase!")