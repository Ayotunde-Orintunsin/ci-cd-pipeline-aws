import uuid
from datetime import datetime

from pydantic import BaseModel

from app.models.task import TaskStatus


class TaskCreate(BaseModel):
    title: str
    description: str | None = None

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None

class TaskRead(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None
    status: TaskStatus
    created_at: datetime

    class Config:
        from_attributes = True
