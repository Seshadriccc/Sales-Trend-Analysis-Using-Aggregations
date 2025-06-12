import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the existing database
conn = sqlite3.connect('sales_data.db')

# SQL query to get total quantity and revenue
query = '''
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
'''

# Load data into pandas DataFrame
df = pd.read_sql_query(query, conn)

# Display summary
print("=== SALES SUMMARY ===")
print(df)

# Plot revenue bar chart
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.xlabel("Product")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Saves the chart as an image
plt.show()

# Close DB connection
conn.close()
