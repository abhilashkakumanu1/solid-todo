from uuid import uuid4
from typing import List
from abc import ABC, abstractmethod


from todo import ITodo


class ITodoList(ABC):
    id: str
    list_name: str
    _todos: List[ITodo]

    @abstractmethod
    def add_todo(self):
        """Add todo to the todo-list"""

    @abstractmethod
    def get_todos(self):
        """Get all todos on the todo-list"""

    @abstractmethod
    def delete_todo(self):
        """Delete todo on the todo-list"""


class TodoList(ITodoList):
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
