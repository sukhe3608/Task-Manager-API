from sqlmodel import SQLModel
from typing import Optional

class TaskCreate(SQLModel):
    title: str
    descriptio: str
    priority: str

class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None

