from abc import ABC, abstractmethod

from todo import Todo
from todo_list import TodoList


class mapper(ABC):
    @abstractmethod
    def to_db(self):
        """core -> infra"""

    @abstractmethod
    def to_domain(self):
        """infra -> core"""


class TodoMapperImp(mapper):
    def to_db(self, todo: Todo):
        return {"id": todo.id, "task": todo.task, "isCompleted": todo.is_completed}

    def to_domain(self, todo):
        return Todo(id=todo.id, task=todo.task, is_completed=todo.isCompleted)


TodoMapper = TodoMapperImp()


class TodoListMapperImp(mapper):
    def to_db(self, todo_list: TodoList):
        todos = [TodoMapper.to_db(todo) for todo in todo_list.get_todos()]
        return {"id": todo_list.id, "listName": todo_list.list_name, "todos": todos}

    def to_domain(self, todo_list):
        todos = [TodoMapper.to_domain(todo) for todo in todo_list.todos]
        return TodoList(id=todo_list.id, list_name=todo_list.listName, todos=todos)


TodoListMapper = TodoListMapperImp()
