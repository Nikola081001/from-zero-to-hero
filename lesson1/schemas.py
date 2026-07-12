from pydantic import BaseModel


class StudentUpdateAge(BaseModel):
    new_age: int


class StudentCreate(BaseModel):
    name: str
    age: int
