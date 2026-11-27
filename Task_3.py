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

  orders[item] = orders.get(item, 0) + quantity

print("===== ORDER SUMMARY =====")

total = 0

for item, quantity in orders.items():
  subtotal = menu[item] * quantity
  print(item, "x", quantity, "=", subtotal)
  total += subtotal
if total >= 500:
    discount = total * 0.10
else:
    discount = 0
  
final_amount = total - discount

print("Subtotal: ", total)
print("Discount: ", discount)
print("Total Amount: ", final_amount)

if total > 0:

    payment = float(input("Enter payment amount: "))

    if payment >= final_amount:
        change = payment - final_amount

        print("===== PAYMENT RECEIPT =====")
        print("Total Amount: ", final_amount)
        print("Change: ", change)

    else:
        balance = final_amount - payment

        print("Insufficient payment!")
        print("Remaining Balance: ", balance)

else:
     print("No valid order found.")
