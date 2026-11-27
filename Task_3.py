#Combine the corrected program from Task 1 and the developed program from 
# Task 2 into a complete Canteen Ordering and Billing Management System.

#TASK 1
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

number = int(input("\nEnter number of order attempts: "))

for i in range(1, number + 1): # skips the lastt order attemp so Add + 1

    print("\nOrder", i)

    item = input("Enter item name: ").title()

    if item not in menu: # changed to not in
        print("Item not available!")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0: #changed tto <= rather than < 
        print("Invalid quantity!")
        continue

    orders[item] = quantity

print("\n===== ORDER SUMMARY =====")

for item, quantity in orders.items():
    print(item, "x", quantity)


#TASK 2
total = 0

payment = float(input("Enter Your Payment: ")) 

for item, quantity in orders.items(): 
    total += menu[item] * quantity

for item, quantity in orders.items(): 
    print(item, "x", quantity, "=", menu[item] * quantity)

if total >=500:
    discount = total * 0.10
else:
    discount = 0

final_total = total - discount

if payment >= final_total:
    change = payment - final_total
else:
    change = 0
    print("Insufficient payment.")

print("===== BILLING SUMMARY =====")

print("Total: ", total)
print("Discount: ", discount)
print("Final Total: ", final_total)
print("Change: ", change)


