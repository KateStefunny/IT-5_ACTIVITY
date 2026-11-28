1. Canteen Menu (Item Code: [Item Name, Price])
menu = {
    "1": ["Rice Meal (Chicken Adobo)", 65.00],
    "2": ["Rice Meal (Pork Sisig)", 75.00],
    "3": ["Pancit Canton", 35.00],
    "4": ["Burger", 45.00],
    "5": ["Bottled Water", 15.00],
    "6": ["Iced Tea", 20.00]
}

def display_menu():
    print("\n" + "=" * 42)
    print("        CANTEEN MENU & PRICE LIST")
    print("=" * 42)
    print(f"{'Code':<6} {'Item':<26} {'Price':>8}")
    print("-" * 42)
    for code, details in menu.items():
        print(f"{code:<6} {details[0]:<26} ₱{details[1]:>7.2f}")
    print("=" * 42)

def take_order():
    orders = []
    while True:
        display_menu()
        choice = input("\nEnter item code to order (or '0' to finish): ").strip()
        
        if choice == '0':
            break
        elif choice in menu:
            try:
                qty = int(input(f"Enter quantity for {menu[choice][0]}: "))
                if qty <= 0:
                    print("Quantity must be at least 1.")
                    continue
                
                item_name = menu[choice][0]
                price = menu[choice][1]
                subtotal = price * qty
                orders.append([item_name, qty, price, subtotal])
                print(f"Added {qty}x {item_name} to your order.")
            except ValueError:
                print("Invalid input. Please enter a valid number for quantity.")
        else:
            print("Invalid item code. Please try again.")
            
    return orders

def generate_bill(orders):
    if not orders:
        print("\nNo items ordered. Transaction cancelled.")
        return

    print("\n" + "=" * 50)
    print("                 OFFICIAL RECEIPT")
    print("=" * 50)
    print(f"{'Item':<25} {'Qty':>4} {'Price':>9} {'Subtotal':>10}")
    print("-" * 50)
    
    total_amount = 0.0
    for item in orders:
        name, qty, price, subtotal = item
        total_amount += subtotal
        print(f"{name:<25} {qty:>4} ₱{price:>8.2f} ₱{subtotal:>9.2f}")
        
    print("-" * 50)
   
    discount_choice = input("Apply 10% Student/Senior Discount? (y/n): ").strip().lower()
    discount = total_amount * 0.10 if discount_choice == 'y' else 0.0
    final_total = total_amount - discount

    print(f"{'Gross Total:':<39} ₱{total_amount:>9.2f}")
    if discount > 0:
        print(f"{'Discount (10%):':<39} -₱{discount:>8.2f}")
    print(f"{'TOTAL AMOUNT DUE:':<39} ₱{final_total:>9.2f}")
    print("=" * 50)

    while True:
        try:
            payment = float(input("Enter cash payment: ₱"))
            if payment < final_total:
                print(f"Insufficient amount. You still need ₱{final_total - payment:.2f}.")
            else:
                change = payment - final_total
                print(f"Change: ₱{change:.2f}")
                print("\nThank you for ordering! Have a great day!")
                break
        except ValueError:
            print("Invalid input. Please enter a valid cash amount.")

def main():
    print("Welcome to the Canteen Ordering and Billing System!")
    while True:
        orders = take_order()
        generate_bill(orders)
        
        again = input("\nProcess another customer? (y/n): ").strip().lower()
        if again != 'y':
            print("System shutting down. Goodbye!")
            break

if _name_ == "_main_":
    main()
