import sqlite3
from database import DB_NAME


def create_table():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT,
            payment_method TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_expense(date, category, amount, description, payment_method):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO expenses (date, category, amount, description, payment_method)
        VALUES (?, ?, ?, ?, ?)
    """, (date, category, amount, description, payment_method))

    new_expense_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return new_expense_id


def get_all_expenses():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    connection.close()
    return expenses


def expense_to_dict(expense):
    return {
        "id": expense[0],
        "date": expense[1],
        "category": expense[2],
        "amount": expense[3],
        "description": expense[4],
        "payment_method": expense[5]
    }


def expense_to_dicts(expenses):
    return [expense_to_dict(expense) for expense in expenses]


def get_expense_by_id(expense_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
    expenses = cursor.fetchone()

    connection.close()
    return expenses


def update_expense(expense_id, date, category, amount, description, payment_method):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE expenses
        SET date = ?, category = ?, amount = ?, description = ?, payment_method = ?
        WHERE id = ?
    """, (date, category, amount, description, payment_method, expense_id))

    connection.commit()
    connection.close()


def delete_expense(expense_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    connection.commit()
    connection.close()


def get_total_expenses():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    connection.close()
    return total or 0


def get_expenses_by_category(category):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))

    expenses = cursor.fetchall()

    connection.close()

    return expenses
