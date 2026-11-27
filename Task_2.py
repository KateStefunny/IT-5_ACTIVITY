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
total = 0

for item, quantity in order.items():
    subtotal = menu[item] * quantity
    total += subtotal

if total >= 500:
    discount = total * 0.10
else:
    discount = 0

final_amount = total - discount

payment = float(input("Enter payment amount: ))

change = payment - final_amount

print("=== CANTEEN BILL ===")
for item, quantity in orders.items():
    print(item, "x", quantity, "=", menu[item] * quantity)

print("Subtotal: ₱", total)
print("Discount: ₱", discount)
print("Total Amount: ₱", final amount)

if payment >= final_amount:
    print("Payment: ₱", payment)
    print("Change: ₱", change)

else:
    print("Insufficient payment!")
    print("Remaining Balance: ₱", abs(change))
