import unittest

from todo import Todo


task = "Code for 10 hrs"
todo = Todo(task)


class TestTodo(unittest.TestCase):
    def test_todo_init(self):
        self.assertAlmostEqual(
            todo.task, task, "correctly saves the given task on initialization"
        )

    def test_todo_id(self):
        self.assertIsNotNone(todo.id, "todo has non-none id")
        todo2 = Todo("read clean code book for 30 mins")
        self.assertNotEqual(todo.id, todo2.id, "every todo has unique id")

    def test_default_state_of_todo(self):
        todo = Todo(task)
        self.assertFalse(todo.is_completed, "by default, todo should be incomplete")

    def test_toogle_todo_state(self):
        todo = Todo(task)
        todo.toggle()
        self.assertTrue(todo.is_completed, "toggle False -> True")
        todo.toggle()
        self.assertFalse(todo.is_completed, "toggle True -> False")
