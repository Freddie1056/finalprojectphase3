
Inventory Management System
A command-line based Inventory Management System built in Python, utilizing SQLite for database management. This system enables users to efficiently manage inventory by adding, viewing, and tracking items in stock.

Features
Add Items: Insert new items into the inventory with details such as name, price, and quantity.
View Items: Retrieve a list of all items in the inventory.
Data Persistence: Items are stored in a SQLite database for persistent storage.
Installation
Follow these steps to install and run the Inventory Management System on your local machine.

Prerequisites
Python 3.x: Ensure you have Python 3 installed. You can download it from python.org.
SQLite3: SQLite is required to manage the database. It comes pre-installed with Python.
Virtual Environment: It's recommended to use a virtual environment to manage dependencies.
Steps
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/inventory_proj.git
cd inventory_proj
Create a virtual environment (optional but recommended):

bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database: The database will automatically be created and populated when you run the program.

Usage
Activate the virtual environment (if using one):

bash
Copy code
source .venv/bin/activate
Run the main program:

bash
Copy code
python main.py
Working with SQLite:

To open and inspect your inventory.db:
bash
Copy code
sqlite3 inventory.db
List all tables:
bash
Copy code
.tables
Query the items table:
sql
Copy code
SELECT * FROM items;
Database Schema
The system uses an SQLite database to store information. The primary table, items, has the following structure:

Column	Type	Description
id	INTEGER	Unique identifier for each item
name	TEXT	Name of the item
price	REAL	Price per unit of the item
quantity	INTEGER	Number of units available in inventory
Example Output
When you run the program, you will be able to perform the following actions:

Add an item:

bash
Copy code
Enter item name: Apples
Enter item price: 0.5
Enter item quantity: 50
Item added successfully!
View items in the inventory:

bash
Copy code
ID  | Name    | Price | Quantity
--------------------------------
1   | Apples  | 0.5   | 50
2   | Oranges | 0.75  | 30
Project Structure
plaintext
Copy code
inventory_proj/
│
├── inventory/
│   ├── __init__.py
│   └── inventory.py      # Logic for managing the inventory
│
├── main.py               # Entry point for running the program
├── requirements.txt      # List of Python dependencies
└── README.md             # This file
Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

License
This project is licensed under the MIT License. See the LICENSE file for details.