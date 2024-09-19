from inventory.inventory import Inventory, Item

def main():
    inventory = Inventory()
    item1 = Item(1, "Apples", 0.5, 50)
    item2 = Item(2, "Oranges", 0.75, 30)
    inventory.add_item(item1)
    inventory.add_item(item2)

    while True:
        print("Inventory Management System")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update item")
        print("4. Generate report")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            id = int(input("Enter item ID: "))
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            item = Item(id, name, price, quantity)
            inventory.add_item(item)
            print("Item added successfully!")
        elif choice == "2":
            id = int(input("Enter item ID: "))
            inventory.remove_item(id)
        elif choice == "3":
            id = int(input("Enter item ID: "))
            field = input("Enter field to update (name/price/quantity): ")
            value = input("Enter new value: ")
            if field in ["price", "quantity"]:
                value = float(value)
            inventory.update_item(id, field, value)
        elif choice == "4":
            inventory.generate_report()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
