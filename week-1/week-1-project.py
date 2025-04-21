'''
A command-line tool to manage warehouse inventory and process orders.

Core Features:

1. add: Add new items to inventory

2. update: Modify item details

3. remove: Delete items from inventory

4. view: Display current inventory with low-stock warnings

5. order: Process orders and update stock

6. exit: Close the program

'''



class WarehouseOrderingSystem:
    def __init__(self, low_stock_threshold=5):
        self.inventory = {}
        self.low_stock_threshold = low_stock_threshold

    def add_item(self, item_id, name, quantity, price):
        if item_id in self.inventory:
            print(f"❌ Error: Item ID '{item_id}' already exists.")
            return
        self.inventory[item_id] = {'name': name, 'quantity': quantity, 'price': price}
        print(f"✅ Item '{name}' added successfully.")

    def update_item(self, item_id, name=None, quantity=None, price=None):
        if item_id not in self.inventory:
            print(f"❌ Error: Item ID '{item_id}' not found.")
            return
        if name:
            self.inventory[item_id]['name'] = name
        if quantity is not None:
            self.inventory[item_id]['quantity'] = quantity
        if price is not None:
            self.inventory[item_id]['price'] = price
        print(f"🔄 Item ID '{item_id}' updated.")

    def remove_item(self, item_id):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print(f"🗑️ Item ID '{item_id}' removed.")
        else:
            print(f"❌ Error: Item ID '{item_id}' not found.")

    def view_inventory(self):
        if not self.inventory:
            print("📦 Inventory is empty.")
            return
        print("\n📦 Current Inventory:")
        for item_id, details in self.inventory.items():
            warning = "⚠️ LOW STOCK" if details['quantity'] <= self.low_stock_threshold else ""
            print(f"{item_id} | {details['name']} | Qty: {details['quantity']} | ${details['price']:.2f} {warning}")
        print()

    def process_order(self, item_id, order_quantity):
        if item_id not in self.inventory:
            print(f"❌ Error: Item ID '{item_id}' not found.")
            return
        item = self.inventory[item_id]
        if item['quantity'] < order_quantity:
            print(f"❌ Not enough stock. Available: {item['quantity']}")
            return
        item['quantity'] -= order_quantity
        total_price = order_quantity * item['price']
        print(f"✅ Order placed: {order_quantity} x '{item['name']}' for ${total_price:.2f}")
        if item['quantity'] <= self.low_stock_threshold:
            print(f"⚠️ Warning: '{item['name']}' stock low (Qty: {item['quantity']})")


def main():
    system = WarehouseOrderingSystem()

    print("\n🔧 Warehouse Ordering System CLI\n")
    print("Commands: add, update, remove, order, view, exit\n")

    while True:
        command = input("\n> Enter command: ").strip().lower()

        if command == "add":
            try:
                item_id = input("Item ID: ").strip()
                name = input("Name: ").strip()
                quantity = int(input("Quantity: "))
                price = float(input("Price: "))
                system.add_item(item_id, name, quantity, price)
            except ValueError:
                print("❌ Invalid input. Quantity must be an integer, and price must be a number.")

        elif command == "update":
            item_id = input("Item ID to update: ").strip()
            name = input("New Name (leave blank to keep current): ").strip()
            q = input("New Quantity (leave blank to keep current): ").strip()
            p = input("New Price (leave blank to keep current): ").strip()
            quantity = int(q) if q else None
            price = float(p) if p else None
            system.update_item(item_id, name=name or None, quantity=quantity, price=price)

        elif command == "remove":
            item_id = input("Item ID to remove: ").strip()
            system.remove_item(item_id)

        elif command == "order":
            try:
                item_id = input("Item ID: ").strip()
                quantity = int(input("Order Quantity: "))
                system.process_order(item_id, quantity)
            except ValueError:
                print("❌ Invalid quantity. Must be an integer.")

        elif command == "view":
            system.view_inventory()

        elif command == "exit":
            print("👋 Exiting system. Goodbye!")
            break

        else:
            print("❌ Unknown command. Try: add, update, remove, order, view, exit")


if __name__ == "__main__":
    main()
