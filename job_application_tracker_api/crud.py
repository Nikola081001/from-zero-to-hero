import sqlite3
from database import DB_NAME


def create_table():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY,
        company TEXT NOT NULL,
        position TEXT NOT NULL,
        status TEXT NOT NULL,
        applied_date TEXT NOT NULL,
        notes TEXT,
        contact_email TEXT
        )
    """)

    connection.commit()
    connection.close()
