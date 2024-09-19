import sqlite3

class Item:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self, db_name='inventory.db'):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    quantity INTEGER NOT NULL
                )
            ''')
            conn.commit()

    def add_item(self, item):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO items (id, name, price, quantity)
                VALUES (?, ?, ?, ?)
            ''', (item.id, item.name, item.price, item.quantity))
            conn.commit()

    def remove_item(self, item_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
            conn.commit()
            if cursor.rowcount:
                print("Item removed successfully!")
            else:
                print("Item not found.")

    def update_item(self, item_id, field, value):
        if field not in ['name', 'price', 'quantity']:
            print("Invalid field.")
            return

        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(f'''
                UPDATE items
                SET {field} = ?
                WHERE id = ?
            ''', (value, item_id))
            conn.commit()
            if cursor.rowcount:
                print("Item updated successfully!")
            else:
                print("Item not found.")

    def generate_report(self):
        total_value = 0
        print("Inventory Report")
        print("-----------------")
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM items')
            items = cursor.fetchall()
            for item in items:
                item_id, name, price, quantity = item
                value = price * quantity
                total_value += value
                print(f"{name} - {quantity} units - ${value:.2f}")
        print("-----------------")
        print(f"Total value of inventory: ${total_value:.2f}")
