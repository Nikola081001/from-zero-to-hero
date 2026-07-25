from pydantic import BaseModel


class ExpanseCreate(BaseModel):
    date: str
    category: str
    amount: float
    description: str
    payment_method: str


class ExpenseUpdate(BaseModel):
    date: str
    category: str
    amount: float
    description: str
    payment_method: str
