from fastapi import FastAPI
from crud import create_table


app = FastAPI()


create_table()


@app.get("/")
def home():
    return {"message": "Job Application Tracker API is running"}
