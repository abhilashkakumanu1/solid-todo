import unittest

from todo import Todo
from todo_list import TodoList

todo1 = Todo("code for 2 hrs")
todo2 = Todo("read clean code book for 30 mins")
list_name = "work-todos"
todo_list = TodoList(list_name)


class TestTodoList(unittest.TestCase):
    def test_todo_list_init(self):
        self.assertAlmostEqual(
            todo_list.list_name,
            list_name,
            "correctly saves the given list name on initialization",
        )

    def test_todo_list_id(self):
        self.assertIsNotNone(todo_list.id, "todo-list has non-none id")
        todo_list2 = TodoList("personal-todos")
        self.assertNotEqual(
            todo_list.id, todo_list2.id, "every todo-list has unique id"
        )
