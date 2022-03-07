import os
from unittest import TestCase, mock

from db.testing import TodoListRepo
from todo import Todo
from todo_list import Todo, TodoList

from services import Services

services = Services(TodoListRepo)

task1 = "read book for 1 hr"
task2 = "work 8 hours everyday"
task3 = "workout atleast 5 times a week"

list_name1 = "work-list"
list_name2 = "personal-list"


@mock.patch.dict(os.environ, {"ENV": "testing"})
class TestServices(TestCase):
    # clear db before every test
    def setUp(self):
        TodoListRepo.db = {}

    def test_create_todo_list(self):
        todo_list_id1 = services.create_todo_list(list_name=list_name1)
        self.assertTrue(len(TodoListRepo.db) == 1, "a new todo-list gets added to db")
        self.assertEqual(
            TodoListRepo.db[todo_list_id1]["listName"],
            list_name1,
            "creates a todo-list with the given name in the db",
        )

    def test_add_todo(self):
        todo_list_id2 = services.create_todo_list(list_name=list_name1)
        services.add_todo(todo_list_id=todo_list_id2, task=task1)
        todos = TodoListRepo.db[todo_list_id2]["todos"]
        self.assertTrue(len(todos) == 1, "a new todo gets added to todo-list")
        self.assertEqual(
            todos[0]["task"],
            task1,
            "adds a todo with the given task in the db",
        )

    def test_get_todo_list(self):
        # create a todo-list, and add a todo to it in DB
        todo_list_id3 = services.create_todo_list(list_name=list_name2)
        services.add_todo(todo_list_id=todo_list_id3, task=task1)

        todo_list3 = services.get_todo_list(todo_list_id=todo_list_id3)
        self.assertEqual(
            todo_list3["id"],
            todo_list_id3,
            "get todo_list returns the todo-list with correct id",
        )
        self.assertEqual(
            todo_list3["listName"],
            list_name2,
            "get_todo_list returns todo-list with correct listName",
        )
        self.assertTrue(
            todo_list3["todos"] == TodoListRepo.db[todo_list_id3]["todos"],
            "get_todo_list returns todo-list with correct todos",
        )

    def test_toggle_todo(self):
        # create a todo-list, and add a todo to it in DB
        todo_list_id4 = services.create_todo_list(list_name=list_name1)
        todo_id4 = services.add_todo(todo_list_id=todo_list_id4, task=task1)

        services.toggle_todo(todo_list_id=todo_list_id4, todo_id=todo_id4)
        todos = TodoListRepo.db[todo_list_id4]["todos"]
        self.assertTrue(
            todos[0]["isCompleted"],
            "toggle_todo toggles the is_completed field correctly",
        )

    def test_update_todo_task(self):
        # create a todo-list, and add a todo to it in DB
        todo_list_id5 = services.create_todo_list(list_name=list_name1)
        todo_id5 = services.add_todo(todo_list_id=todo_list_id5, task=task1)

        services.update_todo_task(
            todo_list_id=todo_list_id5, todo_id=todo_id5, task=task2
        )
        todos = TodoListRepo.db[todo_list_id5]["todos"]
        self.assertEqual(
            todos[0]["task"],
            task2,
            "update_todo_task updates the task correctly",
        )

    def test_delete_todo(self):
        # create a todo-list, and add a todo to it in DB
        todo_list_id6 = services.create_todo_list(list_name=list_name1)
        todo_id6 = services.add_todo(todo_list_id=todo_list_id6, task=task1)

        services.delete_todo(todo_list_id=todo_list_id6, todo_id=todo_id6)
        todos = TodoListRepo.db[todo_list_id6]["todos"]
        self.assertTrue(
            len(todos) == 0,
            "delete_todo deletes the todo",
        )
