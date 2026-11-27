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

payment = float(input("Enter Your Payment: ")) 

for item, quantity in orders.items(): #calculates how much ordered in total
    total += menu[item] * quantity

for item, quantity in orders.items(): # displlay orders and calcullate subtottal
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

print("\n      BILLING SUMMARY      ")

print("Total: ", total)
print("Discount: ", discount)
print("Final Total: ", final_total)
print("Change: ", change)
