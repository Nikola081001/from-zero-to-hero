from fastapi import FastAPI, HTTPException
from schemas import StudentCreate, StudentUpdateAge
from crud import get_all_students, get_student_by_id,  students_to_dicts, student_to_dict, add_student, update_student_age, delete_student


app = FastAPI()


@app.put("/students/{student_id}")
def update_student(student_id: int, student_update: StudentUpdateAge):
    student = get_student_by_id(student_id)

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    update_student_age(student_id, student_update.new_age)

    return {
        "message": "Student age updated successfully",
        "student": {
            "id": student_id,
            "age": student_update.new_age
        }
    }


@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    if not student.name.strip():
        raise HTTPException(status_code=400, detail="Name cannot be empty")

    new_student_id = add_student(student.name, student.age)

    return {
        "message": "Student created successfully",
        "student": {
            "id": new_student_id,
            "name": student.name,
            "age": student.age
        }
    }


@app.get("/")
def home():
    return {"message": "Student API is running"}


@app.get("/students")
def get_students():
    students = get_all_students()
    return students_to_dicts(students)


@app.get("/students/{student_id}")
def get_student(student_id: int):
    student = get_student_by_id(student_id)

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    return student_to_dict(student)


@app.delete("/students/{student_id}")
def delete_student_endpoint(student_id: int):
    student = get_student_by_id(student_id)

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    delete_student(student_id)

    return {
        "message": "Student deleted successfully",
        "student": {
            "id": student_id
        }
    }
