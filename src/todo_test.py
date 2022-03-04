import unittest

from todo import Todo


task = "Code for 10 hrs"


class TestTodo(unittest.TestCase):
    def test_todo_init(self):
        todo = Todo(task)
        self.assertAlmostEqual(
            todo.task, task, "correctly saves the given task on initialization"
        )

    def test_default_state_of_todo(self):
        todo = Todo(task)
        self.assertFalse(todo.is_completed, "by default, todo should be incomplete")
