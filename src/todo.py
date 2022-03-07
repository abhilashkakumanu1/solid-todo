from uuid import uuid4


class Todo:
    id: str
    task: str
    is_completed: bool = False

    def __init__(self, task: str):
        self.id = str(uuid4())
        self.task = task

    def toggle(self):
        self.is_completed = not self.is_completed

    def __eq__(self, other):
        return (
            self.id == other.id
            and self.task == other.task
            and self.is_completed == other.is_completed
        )
