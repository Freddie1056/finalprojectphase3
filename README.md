Inventory Management System

A robust Inventory Management System built with Python and SQLite, designed to manage stock effectively. This project offers a streamlined solution for adding, viewing, and managing items in a local database via a command-line interface.

Key Features
Add New Items: Insert new inventory items with details like name, price, and quantity.
View Inventory: List all items currently in stock with their respective details.
SQLite Integration: Persistent data storage through a local SQLite database.
Getting Started
To get the Inventory Management System up and running on your local machine, follow the steps outlined below.

Prerequisites
Ensure that you have the following installed:

Python 3.x: Download from python.org.
SQLite: Usually comes pre-installed with Python.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/inventory_proj.git
cd inventory_proj
Set up a Virtual Environment (recommended):

bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the SQLite Database: The SQLite database will be created automatically when you run the application for the first time.

Running the Application
Activate the virtual environment (if using):

bash
Copy code
source .venv/bin/activate
Run the main program:

bash
Copy code
python main.py
SQLite Database Operations: You can manually interact with the SQLite database using the following commands:

bash
Copy code
sqlite3 inventory.db
List available tables:

sql
Copy code
.tables
Query the items table:

sql
Copy code
SELECT * FROM items;
Application Usage
This system allows users to add and view items in their inventory.

Add an Item:

bash
Copy code
Enter item name: Laptop
Enter item price: 1500
Enter item quantity: 10
Item successfully added to inventory.
View Inventory:

bash
Copy code
ID  | Name    | Price | Quantity
--------------------------------
1   | Laptop  | 1500  | 10
2   | Mouse   | 20    | 50
Database Schema
The system stores inventory data in an SQLite database (inventory.db). The primary table, items, is structured as follows:

Column	Type	Description
id	INTEGER	Unique identifier for each item (auto-incremented)
name	TEXT	Name of the item
price	REAL	Price per unit of the item
quantity	INTEGER	Quantity available in stock
Project Structure
plaintext
Copy code
inventory_proj/
│
├── inventory/
│   ├── __init__.py
│   └── inventory.py      # Core logic for managing inventory
│
├── main.py               # Main application entry point
├── requirements.txt      # List of project dependencies
└── README.md             # Project documentation
Contributing
We welcome contributions to improve the system. If you would like to contribute, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Create a Pull Request.
License
This project is licensed under the MIT License. For more details, refer to the LICENSE file.