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

number = int(input("Enter number of order attemos: "))
for i in range (1, number + 1):
  print("Order", i)

  item = input("Enter item name: ").title()

  if item not in menu:
    print("Item not available!")
    continue

quantity = int(input("Enter quantity: "))

  if quantity <= 0:
    print("Invalid quantity!")
    continue

order[item] = orders.get(item, 0) + quantity

print("===== ORDER SUMMARY =====")

for item, quanttity in orders.items():
  print(item, "x", quantity)

total = 0

for item, quantity in orders.items():
  total += menu[item] * quantity 

print("Total Cost: ", total)

discount = float(input("Enter discount amount: "))

final_total = total - discount

print("Final Total", final_total)

payment = float(input("Enter payment: "))

if payment >= final-total:
  change = payment - final-total
  print("Change: ", change)

else:
  print("Insuficient payment!")
