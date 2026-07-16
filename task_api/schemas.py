from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str


class TaskUpdateCompleted(BaseModel):
    completed: int
