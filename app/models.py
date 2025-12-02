from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False)
    description: Optional[str] = Field(default=None)
    priority: str = Field(nullable=False)   # "high", "medium", "low"
    status: str = Field(nullable=False)     # "pending", "done", etc.
    created_at: datetime = Field(default_factory=datetime.utcnow)