from sqlmodel import Session, select
from app.models import Task
from app.schemas import TaskCreate, TaskUpdate
from datetime import datetime


def get_all_tasks(db: Session):
    return db.exec(select(Task)).all()


def get_task_by_id(db: Session, task_id: int):
    return db.get(Task, task_id)


def create_task(db: Session, task: TaskCreate):
    created_at = task.created_at or datetime.utcnow()

    db_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        status=task.status,
        created_at=created_at,
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, updated_fields: dict):
    db_task = db.get(Task, task_id)
    if not db_task:
        return None

    for key, value in updated_fields.items():
        setattr(db_task, key, value)

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int):
    db_task = db.get(Task, task_id)
    if not db_task:
        return None

    db.delete(db_task)
    db.commit()
    return db_task
