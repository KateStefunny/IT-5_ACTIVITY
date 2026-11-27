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

# number + 1 for range to include the last order attempt
for i in range(1, number + 1):

    print("\nOrder", i)

    item = input("Enter item name: ").title()
    
    #item not in menu
    if item not in menu:
        print("Item not available!")
        continue

    quantity = int(input("Enter quantity: "))
    
    #quantity < 0 to quantity <= 0 to include 0 as invalid quantity
    if quantity <= 0:
        print("Invalid quantity!")
        continue

    orders[item] = quantity

print("\n===== ORDER SUMMARY =====")

for item, quantity in orders.items():
    print(item, "x", quantity)