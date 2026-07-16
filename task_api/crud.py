import sqlite3
from database import DB_NAME


def create_table():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        completed INTEGER DEFAULT 0
    )
""")

    connection.commit()
    connection.close()


def add_task(title, description):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(""
                   "INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))

    new_task = cursor.lastrowid

    connection.commit()
    connection.close()

    return new_task


def get_all_tasks():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    connection.close()

    return tasks


def get_task_by_id(task_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))

    task = cursor.fetchone()
    connection.close()

    return task


def tasks_to_dict(task):
    return {
        "id": task[0],
        "title": task[1],
        "description": task[2],
        "completed": task[3]
    }


def tasks_to_dics(tasks):
    return [tasks_to_dict(task) for task in tasks]


def update_task_completed(task_id, completed):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?",
                   (completed, task_id))
    connection.commit()
    connection.close()


def delete_task(task_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    connection.commit()
    connection.close()
