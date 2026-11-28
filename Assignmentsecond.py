# The canteen needs a billing system that calculates
# the total cost of purchased items, applies discounts,
# and determines the customer's change. Use the given dictionary

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


subtotal = 0
print("--- CANTEEN RECEIPT ---")
for item, quantity in orders.items():
    if item in menu:
        item_total = menu[item] * quantity
        subtotal += item_total
        print(f"{item} x{quantity}: ₱{item_total:.2f}")

print("-----------------------")
print(f"Subtotal: ₱{subtotal:.2f}")

discount = 0
if subtotal >= 500:
    discount = subtotal * 0.10

final_total = subtotal - discount
print(f"Discount: -₱{discount:.2f}")
print(f"Total Amount Due: ₱{final_total:.2f}")

# 3. Determine the customer's change
cash_paid = float(input("\nEnter cash payment: ₱"))

if cash_paid >= final_total:
    change = cash_paid - final_total
    print(f"Change: ₱{change:.2f}")
else:
    shortage = final_total - cash_paid
    print(f"Insufficient payment. Short by: ₱{shortage:.2f}")