from uuid import uuid4
from typing import List, Union

from todo import ITodo, Todo


class TodoList:
    id: str
    list_name: str
    _todos: List[ITodo] = []

    def __init__(self, list_name):
        self.id = str(uuid4())
        self.list_name = list_name

    def add_todo(self, todo: ITodo):
        self._todos.append(todo)

    def get_todos(self) -> List[ITodo]:
        return self._todos

    def delete_todo(self, id):
        self._todos = [todo for todo in self._todos if todo.id != id]
