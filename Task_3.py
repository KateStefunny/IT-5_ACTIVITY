# Combine the corrected program from Task 1 and the developed program from
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
    print(item, "-", price)

# --- PART 1: ORDERING SYSTEM (From Task 1) ---
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

# --- PART 2: BILLING SYSTEM (From Task 2) ---
print("\n===== ORDER SUMMARY & RECEIPT =====")
total_cost = 0

for item, quantity in orders.items():
    subtotal = menu[item] * quantity
    total_cost += subtotal
    print(f"{item} x {quantity} = {subtotal}")

print("\nSubtotal:", total_cost)

discount = 0
if total_cost >= 500:
    discount = total_cost * 0.10
    print("Discount (10%):", discount)
else:
    print("Discount: 0")

final_total = total_cost - discount
print("Total Amount Due:", final_total)

if final_total > 0:
    cash = float(input("\nEnter cash payment: "))
    if cash < final_total:
        print("Insufficient payment!")
    else:
        change = cash - final_total
        print("Change:", change)