# Task API

Simple FastAPI CRUD API for managing tasks.

## Features

- Get all tasks
- Get task by ID
- Create new task
- Update task completed status
- Delete task
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
task_api/
├── main.py
├── schemas.py
├── database.py
├── crud.py
├── .gitignore
└── README.md
```

## API Endpoints

```text
GET     /
GET     /tasks
GET     /tasks/{task_id}
POST    /tasks
PUT     /tasks/{task_id}
DELETE  /tasks/{task_id}
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
  "title": "Learn FastAPI",
  "description": "Practice CRUD endpoints"
}
```

Example response:

```json
{
  "message": "Task created successfully",
  "task": {
    "id": 1,
    "title": "Learn FastAPI",
    "description": "Practice CRUD endpoints",
    "completed": 0
  }
}
```

## Example PUT request

```json
{
  "completed": 1
}
```

Example response:

```json
{
  "message": "Task updated successfully",
  "task": {
    "id": 1,
    "completed": 1
  }
}
```

## Status

This project is a learning project for practicing Python, SQLite, FastAPI, CRUD operations, project structure, and GitHub workflow.