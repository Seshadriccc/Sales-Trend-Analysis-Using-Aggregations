from __future__ import annotations

import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATABASE_PATH = Path("sales_data.db")
CHART_PATH = Path("sales_chart.png")


QUERY = """
SELECT
    product,
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
"""


def fetch_sales_summary(db_path: Path = DATABASE_PATH) -> pd.DataFrame:
    with sqlite3.connect(db_path) as connection:
        return pd.read_sql_query(QUERY, connection)


def create_revenue_chart(data: pd.DataFrame, output_file: Path = CHART_PATH) -> None:
    ax = data.plot(kind="bar", x="product", y="revenue", legend=False, color="#2563eb")
    ax.set_title("Revenue by Product")
    ax.set_xlabel("Product")
    ax.set_ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()


def main() -> None:
    summary = fetch_sales_summary()

    if summary.empty:
        print("No sales data found. Run analyze_sales.py first.")
        return

    print("=== SALES SUMMARY ===")
    print(summary.to_string(index=False))

    create_revenue_chart(summary)
    print(f"\nChart saved to: {CHART_PATH}")


if __name__ == "__main__":
    main()
