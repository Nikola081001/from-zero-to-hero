# Expense Tracker API

Simple FastAPI CRUD API for tracking personal expenses.

## Features

- Get all expenses
- Get expense by ID
- Create new expense
- Update existing expense
- Delete expense
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
expense_tracker_api/
├── main.py
├── schemas.py
├── database.py
├── crud.py
├── .gitignore
└── README.md
```

## Expense Data

Each expense has:

```text
id
date
category
amount
description
payment_method
```

Example expense:

```json
{
  "id": 1,
  "date": "2026-07-25",
  "category": "food",
  "amount": 65.5,
  "description": "Steak and rice",
  "payment_method": "cash"
}
```

## API Endpoints

```text
GET     /
GET     /expenses
GET     /expenses/{expense_id}
POST    /expenses
PUT     /expenses/{expense_id}
DELETE  /expenses/{expense_id}
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
  "date": "2026-07-25",
  "category": "food",
  "amount": 65.5,
  "description": "Steak and rice",
  "payment_method": "cash"
}
```

Example response:

```json
{
  "message": "Expense created successfully",
  "expense": {
    "id": 1,
    "date": "2026-07-25",
    "category": "food",
    "amount": 65.5,
    "description": "Steak and rice",
    "payment_method": "cash"
  }
}
```

## Example PUT request

```json
{
  "date": "2026-07-25",
  "category": "food",
  "amount": 70.5,
  "description": "Steak and rice updated",
  "payment_method": "card"
}
```

Example response:

```json
{
  "message": "Expense updated successfully",
  "expense": {
    "id": 1,
    "date": "2026-07-25",
    "category": "food",
    "amount": 70.5,
    "description": "Steak and rice updated",
    "payment_method": "card"
  }
}
```

## Example DELETE response

```json
{
  "message": "Expense deleted successfully",
  "expense": {
    "id": 1
  }
}
```

## Status

This project is a learning project for practicing Python, SQLite, FastAPI, CRUD operations, project structure, API validation, error handling, and GitHub workflow.