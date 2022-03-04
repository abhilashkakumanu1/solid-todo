from uuid import uuid4
from typing import List

from todo import Todo


class TodoList:
    id: str
    list_name: str
    todos: List[Todo]

    def __init__(self, list_name):
        self.id = str(uuid4())
        self.list_name = list_name
