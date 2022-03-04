from uuid import uuid4
from typing import List, Union

from todo import ITodo, Todo


class TodoList:
    id: str
    list_name: str
    todos: List[ITodo] = []

    def __init__(self, list_name):
        self.id = str(uuid4())
        self.list_name = list_name

    def add_todo(self, todo: ITodo):
        self.todos.append(todo)
