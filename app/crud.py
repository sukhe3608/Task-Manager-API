from sqlmodel import SQLModel, Session, select
from app.models import Task
from app.schemas import TaskCreate
from app.database import engine
from datetime import datetime


def get_all_tasks():
    with Session(engine) as session:
        return session.exec(select(Task)).all()


def get_task_by_id(task_id: int):
    with Session(engine) as session:
        return session.get(Task, task_id)


def create_task(task: TaskCreate):
    created_at = task.created_at
    if isinstance(created_at, str):
        created_at = datetime.fromisoformat(created_at)

    with Session(engine) as session:         # <-- FIXED
        db_task = Task(
            title=task.title,
            description=task.description,
            priority=task.priority,
            status=task.status,
            created_at=created_at
        )

        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return db_task


def update_task(task_id: int, updated_task: Task):
    with Session(engine) as session:
        db_task = session.get(Task, task_id)
        if not db_task:
            return None
        
        for key, value in updated_task.dict(exclude_unset=True).items():
            setattr(db_task, key, value)

        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return db_task


def delete_task(task_id: int):
    with Session(engine) as session:
        db_task = session.get(Task, task_id)
        if not db_task:
            return None

        session.delete(db_task)
        session.commit()
        return db_task
