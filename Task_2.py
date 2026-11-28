#The canteen needs a billing system that calculates 
#the total cost of purchased items, applies discounts, 
#and determines the customer's change. Use the given dictionary

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

print("===== BILL =====")

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