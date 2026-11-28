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

# FIX 1: Changed range(1, number) to range(1, number + 1) because range() stops before the end value
for i in range(1, number + 1):

    print("\nOrder", i)

    item = input("Enter item name: ").title()

    # FIX 2: Changed 'if item in menu:' to 'if item not in menu:' so valid items aren't rejected
    if item not in menu:
        print("Item not available!")
        continue

    quantity = int(input("Enter quantity: "))

    # FIX 3: Changed 'quantity < 0' to 'quantity <= 0' so an order of 0 is also rejected
    if quantity <= 0:
        print("Invalid quantity!")
        continue

    # FIX 4: Used .get() so ordering the same item twice adds to the quantity instead of overwriting it
    orders[item] = orders.get(item, 0) + quantity

print("\n===== ORDER SUMMARY =====")

for item, quantity in orders.items():
    print(item, "x", quantity)