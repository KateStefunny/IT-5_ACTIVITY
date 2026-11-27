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
# I added a billing system that calculates the total cost of orders, applies discounts, and determines the customer's change.
total = 0

for item, quantity in orders.items():
    total += menu[item] * quantity

print("Total Cost: ", total)
discount = float(input("Enter discount amount: "))

final_total = total - discount

print("Final Total", final_total)

payment = float(input("Enter payment: "))

if payment >= final-total:
    change = payment - final_total
    print("Change: ", change)

else:
    print("Insuficient payment!")
