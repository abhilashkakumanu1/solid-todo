class Todo:
    task: str
    is_completed: bool = False

    def __init__(self, task: str):
        self.task = task

    def toggle(self):
        self.is_completed = not self.is_completed
