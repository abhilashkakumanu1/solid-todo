from .models import Todo, TodoList
from ..interfaces import ITodoListRepo
from .mappers import TodoMapper, TodoListMapper


class TodoListRepoImp(ITodoListRepo):
    def get(self, id):
        todo_list = TodoList.objects.with_id(id)
        return TodoListMapper.to_domain(todo_list)

    def create(self, todo_list):
        todo_list_details = TodoListMapper.to_db(todo_list)
        saved_todo_list = TodoList(**todo_list_details).save()
        return saved_todo_list.id

    def add_todo(self, todo_list_id, todo):
        todo = Todo(**TodoMapper.to_db(todo))
        todo_list = TodoList.objects.with_id(todo_list_id)
        todo_list.todos.append(todo)
        todo_list.save()
        return todo.id

    def toggle_todo(self, todo_list_id, todo_id):
        todo_list = TodoList.objects.with_id(todo_list_id)
        for todo in todo_list.todos:
            if todo.id == todo_id:
                todo.isCompleted = not todo.isCompleted
        todo_list.save()

    def update_task(self, todo_list_id, todo_id, task):
        todo_list = TodoList.objects.with_id(todo_list_id)
        for todo in todo_list.todos:
            if todo.id == todo_id:
                todo.task = task
        todo_list.save()

    def delete_todo(self, todo_list_id, todo_id):
        todo_list = TodoList.objects.with_id(todo_list_id)
        for todo in todo_list.todos:
            if todo.id == todo_id:
                todo_list.todos.remove(todo)
        todo_list.save()


TodoListRepo = TodoListRepoImp()
