import unittest

from todo import Todo
from todo_list import TodoList

task1 = "code for 2 hrs"
todo1 = Todo(task1)
task2 = "read clean code book for 30 mins"
todo2 = Todo(task2)
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

    def test_add_todo(self):
        todo_list.add_todo(todo1)
        self.assertTrue(todo_list._todos[-1] == todo1, "todos get added to todo-list")

    def test_get_todos(self):
        todo_list.add_todo(todo1)
        todo_list.add_todo(todo2)
        todos = todo_list.get_todos()
        self.assertEqual(todos, todo_list._todos, "can get all the todos")
