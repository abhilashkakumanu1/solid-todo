import unittest

from todo import Todo
from todo_list import TodoList

task1 = "code for 2 hrs"
todo1 = Todo(task1)
task2 = "read clean code book for 30 mins"
todo2 = Todo(task2)
list_name = "work-todos"


class TestTodoList(unittest.TestCase):
    def test_todo_list_init(self):
        todo_list = TodoList(list_name)
        self.assertAlmostEqual(
            todo_list.list_name,
            list_name,
            "correctly saves the given list name on initialization",
        )

    def test_todo_list_id(self):
        todo_list1 = TodoList(list_name)
        self.assertIsNotNone(todo_list1.id, "todo-list has non-none id")
        todo_list2 = TodoList("personal-todos")
        self.assertNotEqual(
            todo_list1.id, todo_list2.id, "every todo-list has unique id"
        )

    def test_add_todo(self):
        todo_list3 = TodoList(list_name)
        todo_list3.add_todo(todo1)
        self.assertTrue(todo_list3._todos[-1] == todo1, "todos get added to todo-list")

    def test_get_todos(self):
        todo_list4 = TodoList(list_name)
        todo_list4.add_todo(todo1)
        todo_list4.add_todo(todo2)
        todos = todo_list4.get_todos()
        self.assertEqual(todos, todo_list4._todos, "can get all the todos")

    def test_delete_todo(self):
        todo_list5 = TodoList(list_name)
        todo_list5.add_todo(todo1)
        todo_list5.delete_todo(todo1.id)
        self.assertTrue(todo_list5._todos == [], "should delete todo with given id")
