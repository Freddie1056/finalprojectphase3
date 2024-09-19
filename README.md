Inventory Management System
This is a simple Inventory Management System implemented in Python using SQLite as the database. The system allows users to add, view, and manage inventory items in a SQLite database through a command-line interface (CLI).

Table of Contents
Project Overview
Features
Installation
Usage
Database Structure
Contributing
License
Project Overview
This project provides a basic inventory management system that can be used to track items in stock. The CLI allows users to:

Add new items to the inventory
View all items in the inventory
Handle item details like name, price, and quantity
Features
Add Items: Add new items to the inventory with unique IDs, names, prices, and quantities.
View Inventory: View all items in the inventory.
SQLite Integration: Uses SQLite as the database for persistent storage of inventory data.
Installation
Prerequisites
Python 3.x
SQLite3
Virtual environment (optional but recommended)
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
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database: The database will automatically be created when you run the program.

Usage
Activate the virtual environment (if using one):

bash
Copy code
source .venv/bin/activate
Run the program:

bash
Copy code
python main.py
SQLite Commands:

To open the SQLite shell and inspect your inventory.db file:
bash
Copy code
sqlite3 inventory.db
Use .tables to see all tables in the database.
Use SQL queries like SELECT * FROM items; to view data.
Database Structure
The inventory.db SQLite database contains the following table:

Table: items
Column	Type	Description
id	INTEGER	Unique identifier for each item
name	TEXT	Name of the item
price	REAL	Price of the item
quantity	INTEGER	Quantity of the item in stock
Contributing
Feel free to contribute by opening issues or creating pull requests. Contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for more details.

