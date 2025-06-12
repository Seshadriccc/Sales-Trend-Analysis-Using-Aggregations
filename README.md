# 📊 Task 7 – Basic Sales Summary using SQLite and Python

## 🧠 Objective
To create a basic SQLite database and use Python with SQL to:
- Summarize total quantity sold and revenue per product
- Display the result using a bar chart

---

## 🧰 Tools & Libraries Used
- Python 3
- SQLite3 (built-in with Python)
- pandas (for SQL data handling)
- matplotlib (for bar chart visualization)
- Visual Studio Code

---

## 📁 Project Files

| File Name         | Description                                      |
|------------------|--------------------------------------------------|
| `sales_data.db`   | SQLite database file containing sales data       |
| `task7.py`        | Python script that creates DB, runs analysis     |
| `sales_chart.png` | Bar chart of revenue by product (auto-generated)|
| `README.md`       | Task explanation and instructions                |

---

## ⚙️ How It Works

### 🔹 Step 1: Database Creation (in `task7.py`)
```python
import sqlite3

# Connect to or create the database
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
''')

# Insert sample data
sample_data = [
    ('Pen', 10, 5.0),
    ('Notebook', 5, 15.0),
    ('Pencil', 20, 2.5),
    ('Pen', 7, 5.0),
    ('Notebook', 3, 15.0),
    ('Pencil', 10, 2.5)
]
cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)

conn.commit()
conn.close()
print("Database created and data inserted successfully!")
