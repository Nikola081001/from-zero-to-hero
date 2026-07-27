# Expense Tracker API

Simple FastAPI CRUD API for tracking personal expenses.

This project was built as a learning project to practice Python, FastAPI, SQLite, CRUD operations, API routes, validation, error handling, filtering, totals, and Git/GitHub workflow.

---

## Features

- Create new expenses
- Get all expenses
- Get expense by ID
- Update existing expense
- Delete expense
- Get total amount of all expenses
- Filter expenses by category
- Filter expenses by payment method
- Get total amount by category
- SQLite database
- Pydantic validation
- Automatic API documentation with FastAPI Swagger UI

---

## Tech Stack

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn
- Git / GitHub

---

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

---

## Expense Data

Each expense contains:

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

---

## API Endpoints

### Basic endpoints

```text
GET     /
GET     /expenses
GET     /expenses/{expense_id}
POST    /expenses
PUT     /expenses/{expense_id}
DELETE  /expenses/{expense_id}
```

### Advanced endpoints

```text
GET     /expenses/total
GET     /expenses/category/{category}
GET     /expenses/payment-method/{payment_method}
GET     /expenses/category/{category}/total
```

---

## Run the Project

Start the server with:

```bash
uvicorn main:app --reload
```

Open API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Root Endpoint

### Request

```text
GET /
```

### Example response

```json
{
  "message": "Expense Tracker API is running"
}
```

---

## Create Expense

### Request

```text
POST /expenses
```

### Example request body

```json
{
  "date": "2026-07-25",
  "category": "food",
  "amount": 65.5,
  "description": "Steak and rice",
  "payment_method": "cash"
}
```

### Example response

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

---

## Get All Expenses

### Request

```text
GET /expenses
```

### Example response

```json
[
  {
    "id": 1,
    "date": "2026-07-25",
    "category": "food",
    "amount": 65.5,
    "description": "Steak and rice",
    "payment_method": "cash"
  },
  {
    "id": 2,
    "date": "2026-07-26",
    "category": "gym",
    "amount": 50.0,
    "description": "Gym membership",
    "payment_method": "card"
  }
]
```

If there are no expenses, the API returns:

```json
[]
```

---

## Get Expense by ID

### Request

```text
GET /expenses/{expense_id}
```

Example:

```text
GET /expenses/1
```

### Example response

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

### If expense does not exist

```json
{
  "detail": "Expense not found"
}
```

---

## Update Expense

### Request

```text
PUT /expenses/{expense_id}
```

Example:

```text
PUT /expenses/1
```

### Example request body

```json
{
  "date": "2026-07-25",
  "category": "food",
  "amount": 70.5,
  "description": "Steak and rice updated",
  "payment_method": "card"
}
```

### Example response

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

### If expense does not exist

```json
{
  "detail": "Expense not found"
}
```

---

## Delete Expense

### Request

```text
DELETE /expenses/{expense_id}
```

Example:

```text
DELETE /expenses/1
```

### Example response

```json
{
  "message": "Expense deleted successfully",
  "expense": {
    "id": 1
  }
}
```

### If expense does not exist

```json
{
  "detail": "Expense not found"
}
```

---

## Get Total Expenses

### Request

```text
GET /expenses/total
```

### Example response

```json
{
  "total": 135.5
}
```

If there are no expenses, the API returns:

```json
{
  "total": 0
}
```

---

## Get Expenses by Category

### Request

```text
GET /expenses/category/{category}
```

Example:

```text
GET /expenses/category/food
```

### Example response

```json
[
  {
    "id": 1,
    "date": "2026-07-25",
    "category": "food",
    "amount": 65.5,
    "description": "Steak and rice",
    "payment_method": "cash"
  }
]
```

If no expenses exist for that category, the API returns:

```json
[]
```

This is not an error. It means the request was successful, but there are no matching results.

---

## Get Expenses by Payment Method

### Request

```text
GET /expenses/payment-method/{payment_method}
```

Example:

```text
GET /expenses/payment-method/cash
```

### Example response

```json
[
  {
    "id": 1,
    "date": "2026-07-25",
    "category": "food",
    "amount": 65.5,
    "description": "Steak and rice",
    "payment_method": "cash"
  }
]
```

If no expenses exist for that payment method, the API returns:

```json
[]
```

---

## Get Total by Category

### Request

```text
GET /expenses/category/{category}/total
```

Example:

```text
GET /expenses/category/food/total
```

### Example response

```json
{
  "category": "food",
  "total": 65.5
}
```

If the category does not exist or has no expenses, the API returns:

```json
{
  "category": "nepostoji",
  "total": 0
}
```

---

## Validation Rules

The API validates expense data before saving or updating.

Rules:

```text
category cannot be empty
amount must be greater than 0
payment_method cannot be empty
```

Example error:

```json
{
  "detail": "Amount must be greater than 0"
}
```

---

## Important Learning Points

### FastAPI routes

Specific routes must be placed before dynamic routes.

Correct order:

```python
@app.get("/expenses/total")
@app.get("/expenses/category/{category}")
@app.get("/expenses/{expense_id}")
```

Why?

Because this route:

```text
/expenses/{expense_id}
```

can catch many values after `/expenses/`.

If `/expenses/{expense_id}` is placed before `/expenses/total`, FastAPI may try to read `"total"` as an integer ID and return an error.

---

### SQLite parameterized queries

Correct:

```python
cursor.execute(
    "SELECT * FROM expenses WHERE category = ?",
    (category,)
)
```

The SQL query and the values must be separated.

Wrong:

```python
cursor.execute("SELECT * FROM expenses WHERE category = ?, (category,)")
```

---

### Single-item tuple

Correct:

```python
(category,)
```

Wrong:

```python
(category)
```

The comma is required because Python needs to know it is a tuple.

---

### fetchone vs fetchall

```text
fetchone() → returns one result
fetchall() → returns a list of results
```

Examples:

```python
expense = cursor.fetchone()
expenses = cursor.fetchall()
```

---

### Converter functions

SQLite returns tuples.

Example tuple:

```python
(1, "2026-07-25", "food", 65.5, "Steak and rice", "cash")
```

The API should return dictionaries / JSON.

Example dictionary:

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

That is why converter functions are used.

---

## Project Status

Completed.

This project includes:

```text
CRUD operations
SQLite database
FastAPI endpoints
Pydantic schemas
validation
error handling
filtering
total calculations
README documentation
GitHub workflow
```

---

## Author

Nikola Milakovic