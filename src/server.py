from db import (
    DB,
    TodoListRepo,
)

from todo import Todo
from todo_list import TodoList

# Connect to DB
DB.connect()


# Testing
# todo1 = Todo("read book for 1 hour")
# todo2 = Todo("stop using insta for 90 days")
# todo_list1 = TodoList(list_name="work-tasks", todos=[todo1])

# TodoListRepo.create(todo_list=todo_list1)

# TodoListRepo.toggle_todo(
#     todo_list_id="266ee31e-eda3-46e2-85f1-6f2833c0531e",
#     todo_id="455c1c94-35be-47b9-ab5f-a25accde7678",
# )

# TodoListRepo.add_todo(todo_list_id="266ee31e-eda3-46e2-85f1-6f2833c0531e", todo=todo2)

# TodoListRepo.delete_todo(
#     todo_list_id="266ee31e-eda3-46e2-85f1-6f2833c0531e",
#     todo_id="455c1c94-35be-47b9-ab5f-a25accde7678",
# )

# todo_list = TodoListRepo.get("266ee31e-eda3-46e2-85f1-6f2833c0531e")

# TodoListRepo.update_task(
#     todo_list_id="266ee31e-eda3-46e2-85f1-6f2833c0531e",
#     todo_id="a7ebf17c-056b-4f36-b43d-f29c4fbf2a7b",
#     task="stop wasting time",
# )
