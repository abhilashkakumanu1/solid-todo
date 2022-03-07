import logging
from typing import Dict, Type

from pydantic import BaseModel

from ..interfaces import ITodoListRepo
from ..mongo.mappers import TodoMapper, TodoListMapper
from todo_list import TodoListDetails


class IDataBase(BaseModel):
    __root__: Dict[str, Type[TodoListDetails]]


class TodoListRepoImp(ITodoListRepo):

    # Mock DB
    db: IDataBase = {}

    def __init__(self, db={}):
        self.db = db

    def get(self, id):
        return self.db[id]

    def create(self, todo_list):
        id = todo_list.id
        todo_list_details = TodoListMapper.to_db(todo_list)
        self.db[id] = todo_list_details
        return id

    def add_todo(self, todo_list_id, todo):
        todo_details = TodoMapper.to_db(todo)
        self.db[todo_list_id]["todos"].append(todo_details)
        return todo_details["id"]

    def toggle_todo(self, todo_list_id, todo_id):
        todos = self.db[todo_list_id]["todos"]
        for todo in todos:
            if todo["id"] == todo_id:
                todo["isCompleted"] = not todo["isCompleted"]

    def update_task(self, todo_list_id, todo_id, task):
        todos = self.db[todo_list_id]["todos"]
        for todo in todos:
            if todo["id"] == todo_id:
                todo["task"] = task

    def delete_todo(self, todo_list_id, todo_id):
        todos = self.db[todo_list_id]["todos"]
        for i, todo in enumerate(todos):
            if todo["id"] == todo_id:
                todos.pop(i)

    def clearDB(self):
        self.db = {}


TodoListRepo = TodoListRepoImp()
