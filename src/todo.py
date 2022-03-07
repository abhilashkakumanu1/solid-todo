from uuid import uuid4

from pydantic import BaseModel


class TodoDetails(BaseModel):
    id: str
    task: str
    isCompleted: bool


class Todo:
    id: str
    task: str
    is_completed: bool = False

    def __init__(self, task: str, id=None, is_completed=False):
        self.id = id or str(uuid4())
        self.task = task
        self.is_completed = is_completed

    def toggle(self):
        self.is_completed = not self.is_completed

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.task == other.task
            and self.is_completed == other.is_completed
        )

    def update_task(self, task: str):
        self.task = task
