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

for i in range(1, number + 1): # includes the last number

    print("\nOrder", i)

    item = input("Enter item name: ").title()

    if item not in menu: # checks if an item does not exist
        print("Item not available!")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0: # i added = to check if the value is zero or negative
        print("Invalid quantity!")
        continue

    orders[item] = quantity

print("\n===== ORDER SUMMARY =====")

for item, quantity in orders.items():
    print(item, "x", quantity)
