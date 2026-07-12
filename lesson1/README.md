## Obriši sve iz README.md i zalijepi ovo

````markdown
# Student API

Simple FastAPI CRUD API for managing students.

## Features

- Get all students
- Get student by ID
- Create new student
- Update student age
- Delete student
- SQLite database
- Pydantic validation
- Automatic API docs with FastAPI

## Tech Stack

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn



## Project Structure

```text
lesson1/
├── main.py
├── schemas.py
├── database.py
├── crud.py
├── .gitignore
└── README.md
```

## API Endpoints

```text
GET     /students
GET     /students/{student_id}
POST    /students
PUT     /students/{student_id}
DELETE  /students/{student_id}
```

## Run the project

```bash
uvicorn main:app --reload
```

Open API docs:

```text
http://127.0.0.1:8000/docs
```

## Example POST request

```json
{
  "name": "Ivan",
  "age": 25
}
```

Example response:

```json
{
  "message": "Student created successfully",
  "student": {
    "id": 1,
    "name": "Ivan",
    "age": 25
  }
}
```

## Status

This project is a learning project for practicing Python, SQLite, FastAPI, CRUD operations, and GitHub workflow.