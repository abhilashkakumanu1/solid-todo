class Todo:
    task: str
    is_completed: bool = False

    def __init__(self, task: str):
        self.task = task
