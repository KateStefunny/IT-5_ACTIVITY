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

print("===== RECEIPT =====")
total_cost = 0

# Calculate subtotal for each ordered item
for item, quantity in orders.items():
    subtotal = menu[item] * quantity
    total_cost += subtotal
    print(f"{item} x {quantity} = {subtotal}")

print("\nSubtotal:", total_cost)

# Apply discount (e.g., 10% discount if total is 500 or above)
discount = 0
if total_cost >= 500:
    discount = total_cost * 0.10
    print("Discount (10%):", discount)
else:
    print("Discount: 0")

final_total = total_cost - discount
print("Total Amount Due:", final_total)

# Payment and change calculation
cash = float(input("\nEnter cash payment: "))

if cash < final_total:
    print("Insufficient payment!")
else:
    change = cash - final_total
    print("Change:", change)