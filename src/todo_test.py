import unittest

from todo import Todo


task1 = "code for 2 hrs"
todo1 = Todo(task1)
task2 = "read clean code book for 30 mins"
todo2 = Todo(task2)


class TestTodo(unittest.TestCase):
    def test_todo_init(self):
        self.assertAlmostEqual(
            todo1.task, task1, "correctly saves the given task1 on initialization"
        )

    def test_todo_id(self):
        self.assertIsNotNone(todo1.id, "todo1 has non-none id")
        self.assertNotEqual(todo1.id, todo2.id, "every todo has unique id")

    def test_default_state_of_todo(self):
        todo1 = Todo(task1)
        self.assertFalse(todo1.is_completed, "by default, todo should be incomplete")

    def test_toogle_todo_state(self):
        todo1.toggle()
        self.assertTrue(todo1.is_completed, "toggle False -> True")
        todo1.toggle()
        self.assertFalse(todo1.is_completed, "toggle True -> False")

    def test_equality_of_todos(self):
        self.assertTrue(todo1 == todo1, "a todo is equal to itself")

    def test_inequality_of_todos(self):
        # todo3 has same task as todo1, but its a different todo -> diff id
        todo3 = Todo(task1)
        self.assertTrue(todo1 != todo3, "diff in id leads to inequality")

        todo4 = Todo(task1)
        todo4.id = todo1.id
        todo4.toggle()
        self.assertTrue(todo1 != todo4, "diff in is_completed leads to inequality")

        todo5 = Todo(task1)
        todo5.id = todo1.id
        todo5.task = "tada-tada-tada"
        self.assertTrue(todo1 != todo5, "diff in tasks leads to inequality")
