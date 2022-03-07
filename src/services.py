from todo import Todo
from todo_list import TodoList, TodoListDetails

from db import TodoListRepo


def create_todo_list(list_name: str):
    todo_list = TodoList(list_name=list_name)
    TodoListRepo.create(todo_list)


def add_todo(todo_list_id: str, task: str):
    todo = Todo(task=task)
    TodoListRepo.add_todo(todo_list_id=todo_list_id, todo=todo)


def get_todo_list(todo_list_id: str) -> TodoListDetails:
    return TodoListRepo.get(todo_list_id=todo_list_id)


def toggle_todo(todo_list_id: str, todo_id: str):
    TodoListRepo.toggle_todo(todo_list_id=todo_list_id, todo_id=todo_id)


def update_todo_task(todo_list_id: str, todo_id: str, task: str):
    TodoListRepo.update_task(todo_list_id=todo_list_id, todo_id=todo_id, task=task)


def delete_todo(todo_list_id: str, todo_id: str):
    TodoListRepo.delete_todo(todo_list_id=todo_list_id, todo_id=todo_id)
