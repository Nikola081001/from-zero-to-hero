from fastapi import FastAPI, HTTPException
from crud import create_table, add_task, get_all_tasks, tasks_to_dics, tasks_to_dict, get_task_by_id, update_task_completed, delete_task
from schemas import TaskCreate, TaskUpdateCompleted


app = FastAPI()

create_table()


@app.get("/")
def home():
    return {"message": "Task API is running"}


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    if not task.title.strip():
        raise HTTPException(status_code=400, detail="Title cannot be empty")

    new_task_id = add_task(task.title, task.description)

    return {
        "message": "Task created succesfully",
        "task": {
            "id": new_task_id,
            "title": task.title,
            "description": task.description,
            "completed": 0
        }
    }


@app.get("/tasks")
def get_tasks():
    tasks = get_all_tasks()
    return tasks_to_dics(tasks)


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = get_task_by_id(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return tasks_to_dict(task)


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdateCompleted):
    task = get_task_by_id(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task_update.completed not in [0, 1]:
        raise HTTPException(status_code=400, detail="Completed must be 0 or 1")

    update_task_completed(task_id, task_update.completed)

    return {
        "message": "Task updated successfully",
        "task": {
            "id": task_id,
            "completed": task_update.completed
        }
    }


@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int):
    task = get_task_by_id(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    delete_task(task_id)
    return {
        "message": "Task deleted successfully",
        "task": {
            "id": task_id
        }
    }
