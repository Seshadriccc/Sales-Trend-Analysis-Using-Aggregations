# Sales Trend Analysis - Task 6

## Objective
Analyze monthly revenue and order volume using SQL aggregations, as part of the Data Analyst Internship Task 6.

## Database Used
MySQL (via MySQL Workbench, version 8.0+)

## Task Requirements
- Analyze monthly revenue and order volume using the `online_sales` dataset (`orders` table).
- Tools: PostgreSQL/MySQL/SQLite (MySQL used).
- Deliverables: SQL scripts and results table.
- Address 7 interview questions (see below).

## Files Description
- `sql-scripts/`:
  - `01-create-table.sql`: Creates the `orders` table.
  - `02-insert-data.sql`: Inserts sample data for January to March 2024.
  - `03-main-analysis.sql`: Analyzes monthly revenue, order volume, and average order value.
  - `04-additional-queries.sql`: Includes top 3 months and growth rate analysis.
- `results/`:
  - `monthly-sales-results.csv`: Results of the main analysis query.
  - `top-3-months.csv`: Top 3 months by revenue.
  - `growth-rate-results.csv`: Month-over-month growth rate.
  - `analysis-summary.md`: Summary of key findings.
- `screenshots/`:
  - Screenshots of query execution and results in MySQL Workbench.

## Key Findings
- February 2024 had the highest revenue ($475.25) and average order value ($237.63).
- Revenue grew by 35.59% from January to February 2024 but declined by 14.62% from February to March.
- Each month had 2 orders, indicating consistent order volume.

## Interview Questions Answered
1. **Group by month and year**: Used `GROUP BY YEAR(order_date), MONTH(order_date)`.
2. **COUNT(*) vs COUNT(DISTINCT col)**: Used `COUNT(DISTINCT order_id)` for unique orders; `COUNT(*)` would count all rows.
3. **Monthly revenue**: Calculated using `SUM(amount)` grouped by year/month.
4. **Aggregate functions**: Used `SUM`, `COUNT`, `AVG` for analysis.
5. **Handle NULLs**: Used `COALESCE` and `NULLIF` in growth rate query to handle NULLs and zero-division.
6. **ORDER BY vs GROUP BY**: `GROUP BY` aggregates data; `ORDER BY` sorts results (e.g., `sales_year DESC, sales_month DESC`).
7. **Top 3 months**: Used `ORDER BY revenue DESC LIMIT 3`.

## How to Run
1. Open MySQL Workbench and connect to a MySQL 8.0+ server.
2. Create a schema (e.g., `sales_trend_analysis`).
3. Run scripts in order: `01-create-table.sql`, `02-insert-data.sql`, `03-main-analysis.sql`, `04-additional-queries.sql`.
4. Export results to CSV using MySQL Workbench's export feature.
5. Take screenshots of results for verification.

## Notes
- MySQL `YEAR` and `MONTH` functions were used instead of `EXTRACT` for compatibility.
- Sample data covers January to March 2024 with 6 orders.
- Error handling included for NULLs and division by zero.
