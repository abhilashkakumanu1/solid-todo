from uuid import uuid4
from typing import List

from todo import Todo


class TodoList:
    id: str
    list_name: str
    _todos: List[Todo] = []

    def __init__(self, list_name):
        self.id = str(uuid4())
        self.list_name = list_name

    def add_todo(self, todo: Todo):
        self._todos.append(todo)

    def get_todos(self) -> List[Todo]:
        return self._todos

    def delete_todo(self, id):
        self._todos = [todo for todo in self._todos if todo.id != id]
