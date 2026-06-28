# Sales Trend Analysis Using Aggregations

A compact data-analysis project that demonstrates how to combine **SQLite + SQL aggregations + Python visualization** to produce a clean product-level sales summary.

## Project Overview

This repository contains two scripts:

1. `analyze_sales.py` – creates/initializes the SQLite database and inserts sample sales data.
2. `task7.py` – runs SQL aggregation queries, prints a tabular summary, and generates a revenue chart.

## Tech Stack

- Python 3
- SQLite (`sqlite3`)
- pandas
- matplotlib

## Repository Structure

- `analyze_sales.py` – database initialization script
- `task7.py` – sales summary and chart generation script
- `sales_data.db` – SQLite database file
- `sales_chart.png` – generated chart image

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## How to Run

### 1) Initialize database

```bash
python analyze_sales.py
```

### 2) Run analysis and generate chart

```bash
python task7.py
```

## Output

- Console summary of total quantity and revenue by product
- `sales_chart.png` bar chart for product-wise revenue

## SQL Aggregation Used

```sql
SELECT
    product,
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC;
```

## Notes

- `task7.py` safely handles empty datasets and prompts for database initialization.
- The scripts are intentionally small and beginner-friendly, while following clean structure and reusable function design.
