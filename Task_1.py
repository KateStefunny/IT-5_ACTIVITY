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

#ERROR 1: Add +1 because range stops before the ending number.
for i in range(1, number + 1):
    print("order", i)

    item = input("Enter item name: ").title()

# ERROR 2: Use "not in" to check if the item is not available in the menu.
   if item not in menu:
       print("Item not available!")
       continue

    quantity = int(input("Enter quantity: "))
# ERROR 3: Use <= 0 because quantity must be greater than zero.
    if quantity <= 0:
        print("Invalid quantity!")
        continue

    orders[item] = quantity

print("\n===== ORDER SUMMARY =====")

for item, quantity in orders.items():
    print(item, "x", quantity)
