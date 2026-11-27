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
print("/n===== CANTEEN RECEIPT =====")
subtotal = 0

for item, quantity in orders.items():
    price = menu[item]
    item_total = price * quantity
    subtotal += item_toatl
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

# Determine customer's change
payment = float(input("\nEnter payment amount: "))

if payment < total_amount:
    print("Insufficient payment!")
else:
    change = payment - total_amount
    print(f"Change: {change:.2f}")

