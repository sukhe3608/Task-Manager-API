from fastapi import FastAPI, HTTPException
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate
from app.crud import (
    get_all_tasks,
    get_task_by_id,
    create_task,
    update_task,
    delete_task,
)
from app.database import create_db_and_tables


app = FastAPI(title = "Task Manager API")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/tasks")
def list_tasks():
    return get_all_tasks()

@app.get("/tasks/{task_id}")
def get_tasks(task_id: int):
    task = get_task_by_id(task_id)
    if not task:
        raise HttpException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks", status_code=201)
def add_task(task: TaskCreate):
    task = Task(**task.dict())
    return create_task(task)

@app.put("/tasks/{task_id}")
def edit_task(task_id: id,int, task_data: TaskUpdate):
    updated_task = update_task(task_id, Task(**task_data.dict(exclude_unset=True)))
    if not updated_task:
        raise HttpException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    if not delete_task(task_id):
        raise HttpException(status_code=404, detail="Task not found")