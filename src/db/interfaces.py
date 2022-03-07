from abc import ABC, abstractmethod

from todo import Todo
from todo_list import TodoList


class ITodoListRepo(ABC):
    @abstractmethod
    def get(self, id: str) -> TodoList:
        """Get the todo-list with given id"""

    @abstractmethod
    def create(self, todo_list: TodoList) -> str:
        """Create new todo-list with given name"""

    @abstractmethod
    def add_todo(self, todo_list_id: str, todo: Todo) -> str:
        """add todo to the todo-list with given id"""

    @abstractmethod
    def toggle_todo(self, todo_list_id: str, todo_id: str):
        """toogle is_completed field of the given todo"""

    @abstractmethod
    def update_task(self, todo_list_id: str, todo_id: str, task: str):
        """update task details of the given todo"""

    @abstractmethod
    def delete_todo(self, todo_list_id: str, todo_id: str):
        """Delete a todo with given id from todo-list"""
