from __future__ import annotations

import sqlite3
from pathlib import Path

DATABASE_PATH = Path("sales_data.db")

SAMPLE_DATA: list[tuple[str, int, float]] = [
    ("Pen", 10, 5.0),
    ("Notebook", 5, 15.0),
    ("Pencil", 20, 2.5),
    ("Pen", 7, 5.0),
    ("Notebook", 3, 15.0),
    ("Pencil", 10, 2.5),
]


def initialize_database(db_path: Path = DATABASE_PATH) -> None:
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
            """
        )

        cursor.execute("DELETE FROM sales")
        cursor.executemany(
            "INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)",
            SAMPLE_DATA,
        )


def main() -> None:
    initialize_database()
    print("Database initialized and sample sales records inserted.")


if __name__ == "__main__":
    main()
