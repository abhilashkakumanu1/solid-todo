from src.db.interfaces import ITodoListRepo
from todo import Todo
from todo_list import TodoList, TodoListDetails


class Services:
    TodoListRepo: ITodoListRepo

    def __init__(self, TodoListRepo):
        self.TodoListRepo = TodoListRepo

    def create_todo_list(self, list_name: str) -> str:
        todo_list = TodoList(list_name=list_name)
        return self.TodoListRepo.create(todo_list)

    def add_todo(self, todo_list_id: str, task: str) -> str:
        todo = Todo(task=task)
        return self.TodoListRepo.add_todo(todo_list_id=todo_list_id, todo=todo)

    def get_todo_list(self, todo_list_id: str) -> TodoListDetails:
        return self.TodoListRepo.get(id=todo_list_id)

    def toggle_todo(self, todo_list_id: str, todo_id: str):
        self.TodoListRepo.toggle_todo(todo_list_id=todo_list_id, todo_id=todo_id)

    def update_todo_task(self, todo_list_id: str, todo_id: str, task: str):
        self.TodoListRepo.update_task(
            todo_list_id=todo_list_id, todo_id=todo_id, task=task
        )

    def delete_todo(self, todo_list_id: str, todo_id: str):
        self.TodoListRepo.delete_todo(todo_list_id=todo_list_id, todo_id=todo_id)
