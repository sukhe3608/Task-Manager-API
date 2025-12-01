from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    priority: str
    status: str = "Pending"
    created_at: datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")