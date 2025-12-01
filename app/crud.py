from sqlmodel import SQLModel , Session
from app.models import Task
from app.database import engine

def get_all_tasks():
    with Session(engine) as session:
        return session.exec(select(Task)).all()

def get_task_by_id(task_id: int):
    with Session(engine) as session:
        return session.get(Task, task_id)

def create_task(task: Task):
    with Session(engine) as session:
        session.add(task)
        session.commit()
        session.refresh(task)
        return task

def update_task(task_id: int, updated_task: Task):
    with Session(engine) as session:
        db_task = session.get(Task, task_id)
        if not db_task:
            return None
        
        for key, value in updated_task.dict(execlude_unset=True).items():
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

        

