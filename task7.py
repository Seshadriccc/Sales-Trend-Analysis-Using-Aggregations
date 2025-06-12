import sqlite3

# Connect to or create the database
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
''')

# Insert data
sample_data = [
    ('Pen', 10, 5.0),
    ('Notebook', 5, 15.0),
    ('Pencil', 20, 2.5),
    ('Pen', 7, 5.0),
    ('Notebook', 3, 15.0),
    ('Pencil', 10, 2.5)
]
cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)

# Save and close
conn.commit()
conn.close()

print("Database created and data inserted successfully!")
