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

    orders[item] = orders.get(item, 0) + quantity

print("\n===== ORDER SUMMARY =====")

total = 0

for item, quantity in orders.items():
    subtotal = menu[item] * quantity
    total += subtotal

    print(item, "x", quantity, "=", subtotal)

print("\nTotal Cost:", total)

if total >= 500:
    discount = total * 0.10
    print("Discount: 10%")
else:
    discount = 0
    print("Discount: None")

final_total = total - discount

print("Discount Amount:", discount)
print("Final Total:", final_total)

payment = float(input("\nEnter payment: "))

if payment >= final_total:
    change = payment - final_total
    print("Change:", change)
else:
    print("Insufficient payment!")
