from fastapi import FastAPI, HTTPException
from schemas import ExpanseCreate, ExpenseUpdate
from crud import create_table, add_expense, get_all_expenses, expense_to_dicts, expense_to_dict, get_expense_by_id, update_expense, delete_expense, get_total_expenses


app = FastAPI()

create_table()


@app.get("/")
def home():
    return {"message": "Expense Tracker API is running successfully!"}


@app.post("/expenses", status_code=201)
def create_expense(expense: ExpanseCreate):
    if not expense.category.strip():
        raise HTTPException(status_code=400, detail="Category cannot be empty")

    if expense.amount < 0:
        raise HTTPException(
            status_code=400, detail="Amount cannot be less than 0")

    if not expense.payment_method.strip():
        raise HTTPException(
            status_code=400, detail="Payment method cannot be empty")

    new_expense_id = add_expense(
        expense.date,
        expense.category,
        expense.amount,
        expense.description,
        expense.payment_method
    )

    return {
        "message": "Expense created successfully",
        "expense": {
            "id": new_expense_id,
            "date": expense.date,
            "category": expense.category,
            "amount": expense.amount,
            "description": expense.description,
            "payment_method": expense.payment_method
        }
    }


@app.get("/expenses")
def get_expenses():
    expenses = get_all_expenses()
    return expense_to_dicts(expenses)


@app.get("/expenses/total")
def get_total_expenses_endpoint():
    total = get_total_expenses()
    return {"total_expenses": total}


@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):
    expense = get_expense_by_id(expense_id)

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense_to_dict(expense)


@app.put("/expenses/{expense_id}")
def update_expense_endpoint(expense_id: int, expense_update: ExpenseUpdate):
    expense = get_expense_by_id(expense_id)

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    if not expense_update.category.strip():
        raise HTTPException(status_code=400, detail="Category cannot be empty")

    if expense_update.amount < 0:
        raise HTTPException(
            status_code=400, detail="Amount cannot be less than 0")

    if not expense_update.payment_method.strip():
        raise HTTPException(
            status_code=400, detail="Payment method cannot be empty")

    update_expense(
        expense_id,
        expense_update.date,
        expense_update.category,
        expense_update.amount,
        expense_update.description,
        expense_update.payment_method
    )

    return {
        "message": "Expense updated successfully",
        "expense": {
            "id": expense_id,
            "date": expense_update.date,
            "category": expense_update.category,
            "amount": expense_update.amount,
            "description": expense_update.description,
            "payment_method": expense_update.payment_method
        }
    }


@app.delete("/expenses/{expense_id}")
def delete_expense_endpoint(expense_id: int):
    expense = get_expense_by_id(expense_id)

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    delete_expense(expense_id)

    return {"message": "Expense deleted successfully",
            "expense": {
                "id": expense_id, }}
