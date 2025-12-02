from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

from app.models import Task
from app.schemas import TaskCreate, TaskUpdate
from app.crud import get_all_tasks, get_task_by_id, create_task, update_task, delete_task
from app.database import Base, engine, get_db

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")


@app.get("/tasks")
def list_tasks(db: Session = Depends(get_db)):
    return get_all_tasks(db)


@app.get("/tasks/{task_id}")
def get_tasks(task_id: int, db: Session = Depends(get_db)):
    task = get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks", status_code=201)
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)


@app.put("/tasks/{task_id}")
def edit_task(task_id: int, task_data: TaskUpdate, db: Session = Depends(get_db)):
    updated_task = update_task(
        db,
        task_id,
        task_data.dict(exclude_unset=True)
    )

    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")

    return updated_task


@app.delete("/tasks/{task_id}")
def remove_task(task_id: int, db: Session = Depends(get_db)):
    if not delete_task(db, task_id):
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}
