import sqlite3
from database import DB_NAME


def create_table():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    """)

    connection.commit()
    connection.close()


def add_student(name, age):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students (name, age) VALUES (?, ?)",
        (name, age)
    )

    new_student_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return new_student_id


def get_all_students():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    connection.close()
    return rows


def get_student_by_id(student_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    row = cursor.fetchone()

    connection.close()
    return row


def update_student_age(student_id, new_age):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE students SET age = ? WHERE id = ?",
        (new_age, student_id)
    )

    connection.commit()
    connection.close()


def delete_student(student_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    connection.commit()
    connection.close()


def get_student_by_name(name):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students WHERE name LIKE ?", (f"%{name}%",))

    rows = cursor.fetchall()

    connection.close()
    return rows


def get_valid_number(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Please enter a valid number.")


def get_non_empty_input(message):
    while True:
        text = input(message)

        if text.strip():
            return text
        else:
            print("Input cannot be empty.")


def print_student(student):
    print(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]}")


def student_to_dict(student):
    return {
        "id": student[0],
        "name": student[1],
        "age": student[2]
    }


def students_to_dicts(students):
    students_list = []

    for student in students:
        students_list.append(student_to_dict(student))

    return students_list


def api_get_all_students():
    students = get_all_students()

    return {
        "status_code": 200,
        "data": students_to_dicts(students)
    }


def api_get_student_by_id(student_id):
    student = get_student_by_id(student_id)

    if student:
        return {
            "status_code": 200,
            "data": student_to_dict(student)
        }
    else:
        return {
            "status_code": 404,
            "error": "Student not found"
        }


def api_create_student(name, age):
    if not name.strip():
        return {
            "status_code": 400,
            "error": "Name cannot be empty"
        }
    if not isinstance(age, int):
        return {
            "status_code": 400,
            "error": "Age must be a number"
        }

    add_student(name, age)

    return {
        "status_code": 201,
        "message": "Student created successfully"
    }


def api_update_student_age(student_id, new_age):
    if not isinstance(student_id, int):
        return {
            "status_code": 400,
            "error": "Student ID must be a number"
        }

    if not isinstance(new_age, int):
        return {
            "status_code": 400,
            "error": "Age must be a number"
        }

    student = get_student_by_id(student_id)

    if not student:
        return {
            "status_code": 404,
            "error": "Student not found"
        }

    update_student_age(student_id, new_age)

    return {
        "status_code": 200,
        "message": "Student updated successfully"
    }


def api_delete_student(student_id):
    if not isinstance(student_id, int):
        return {
            "status_code": 400,
            "error": "Student ID must be a number"
        }

    student = get_student_by_id(student_id)

    if not student:
        return {
            "status_code": 404,
            "error": "Student not found"
        }

    delete_student(student_id)

    return {
        "status_code": 200,
        "message": "Student deleted successfully"
    }


def show_all_students():
    students = get_all_students()

    if students:
        for student in students:
            print_student(student)
        else:
            print("No students found")


def handle_add_student():
    name = get_non_empty_input("Enter student name: ")
    age = get_valid_number("Enter student age: ")

    add_student(name, age)
    print("Student added successfully.")


def handle_find_student():
    student_id = get_valid_number("Enter student ID: ")

    student = get_student_by_id(student_id)

    if student:
        print_student(student)
    else:
        print("Student not found.")


def handel_update_students():
    student_id = get_valid_number("Enter student ID: ")

    student = get_student_by_id(student_id)

    if student:
        new_age = get_valid_number("Enter new age: ")
        update_student_age(student_id, new_age)
        print("Student updated successfully.")
    else:
        print("Student not found")


def handle_delete_student():
    student_id = get_valid_number("Enter student ID: ")

    student = get_student_by_id(student_id)

    if student:
        delete_student(student_id)
        print("Student deleted successfully")
    else:
        print("Student nout found")


def handle_find_students_by_name():
    name = get_non_empty_input("Enter student name or part of name: ")

    students = get_student_by_name(name)

    if students:
        for student in students:
            print_student(student)
    else:
        print("Not student found with that name.")


def main_menu():
    print("\nStudent Manager")
    print("1. Add student")
    print("2. Show all students")
    print("3. Find student by ID")
    print("4. Find student by name")
    print("5. Update student age")
    print("6. Delete student")
    print("7. Exit")


def run_app():
    create_table()

    while True:
        main_menu()

        choice = input("Choose an option: ")

        if choice == "1":
            handle_add_student()

        elif choice == "2":
            show_all_students()

        elif choice == "3":
            handle_find_student()

        elif choice == "4":
            handle_find_students_by_name()

        elif choice == "5":
            handel_update_students()

        elif choice == "6":
            handle_delete_student()

        elif choice == "7":
            print("Goodbye!")
            break


if __name__ == "__main__":
    run_app()
