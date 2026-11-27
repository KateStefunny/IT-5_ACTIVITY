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

print("===== RECEIPT / BILLING SUMMARY =====")

subtotal = 0

for item, quantity in orders.items():
    price = menu[item]
    item_total = price * quantity
    subtotal = subtotal + item_total
    print(item, "x", quantity, "=", item_total)

print("\nSubtotal:", subtotal)

discount = 0
if subtotal >= 500:
    discount = subtotal * 0.10
    print("Discount (10%):", discount)
else:
    print("Discount: 0")

total = subtotal - discount
print("Total Amount:", total)

payment = float(input("\nEnter payment amount: "))

if payment < total:
    print("Insufficient payment!")
else:
    change = payment - total
    print("Change:", change)
