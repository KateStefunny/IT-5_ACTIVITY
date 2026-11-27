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

for i in range(1, number + 1):
    print("\nOrder", i)
    
    item = input("Enter item name: ").title()
    
    if item not in menu:
        print("Item not available!")
        continue
        
    quantity = int(input("Enter quantity: "))
    
    if quantity <= 0:
        print("Invalid quantity!")
        continue
        
    orders[item] = orders.get(item, 0) + quantity

print("\n===== RECEIPT / BILLING SUMMARY =====")

subtotal = 0

for item, quantity in orders.items():
    price = menu[item]
    item_total = price * quantity
    subtotal = subtotal + item_total
    print(item, "x", quantity, "=", item_total)

print("\nSubtotal:", subtotal)

discount = 0
if subtotal >= 500:
    discount = subtotal * 0.10
    print("Discount (10%):", discount)
else:
    print("Discount: 0")

total = subtotal - discount
print("Total Amount:", total)

payment = float(input("\nEnter payment amount: "))

if payment < total:
    print("Insufficient payment!")
else:
    change = payment - total
    print("Change:", change)
