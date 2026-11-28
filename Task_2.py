# The canteen billing system calculates the total cost,
# applies discounts, and determines the customer's change.

menu = {
    "Burger": 85,
    "Fries": 45,
    "Drink": 30,
    "Chicken": 120
}

orders = {
    "Burger": 3,
    "Fries": 3,
    "Chicken": 1,
    "Drink": 2
}

total = 0

print("===== ORDER SUMMARY =====")
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
