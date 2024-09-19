Inventory Management System

A Python-based Inventory Management System using SQLite for effective stock management through a command-line interface.

Features
Add Items: Insert new items with name, price, and quantity.
View Inventory: List all current items with details.
SQLite Storage: Persistent data with SQLite database.
Getting Started
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/inventory_proj.git
cd inventory_proj
Set Up Virtual Environment:

bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Application:

bash
Copy code
python main.py
Usage
Add an Item:

yaml
Copy code
Enter item name: Laptop
Enter item price: 1500
Enter item quantity: 10
View Inventory:

bash
Copy code
sqlite3 inventory.db
.tables
SELECT * FROM items;
Project Structure
plaintext
Copy code
inventory_proj/
├── inventory/
│   └── inventory.py      # Inventory management logic
├── main.py               # Entry point
├── requirements.txt      # Dependencies
└── README.md             # Documentation
Contributing
Fork the repo.
Create a branch (git checkout -b feature/your-feature).
Commit changes (git commit -m 'Add feature').
Push (git push origin feature/your-feature).
Submit a Pull Request.

License
MIT License. See the LICENSE file for details.

