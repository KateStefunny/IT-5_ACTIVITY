#Combine the corrected program from Task 1 and the developed program from 
# Task 2 into a complete Canteen Ordering and Billing Management System.

menu = {
    "Burger": 85,
    "Fries": 45,
    "Drink": 30,
    "Chicken": 120
}

orders = {}

print("===== CANTEEN MENU =====")
for item, price in menu.items():
    print(f"{item} - {price}")

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

    orders[item] = orders.get(item, 0) + quantity

print("\n===== ORDER SUMMARY & BILLING =====")

if not orders:
    print("No valid items ordered.")
else:
    subtotal = 0

    for item, quantity in orders.items():
        price = menu[item]
        item_total = price * quantity
        subtotal += item_total
        print(f"{item} x {quantity} = {item_total}")

    print(f"\nSubtotal: {subtotal:.2f}")

    # Apply 10% discount if subtotal is 500 or above
    if subtotal >= 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    total_amount = subtotal - discount
    print(f"Discount: {discount:.2f}")
    print(f"Total Amount: {total_amount:.2f}")

    payment = float(input("\nEnter payment amount: "))

    if payment < total_amount:
        print("Insufficient payment!")
    else:
        change = payment - total_amount
        print(f"Change: {change:.2f}")
