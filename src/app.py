from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services import Services
from db import TodoListRepo

# Initiate APP
app = FastAPI()

# Initiate Services
services = Services(TodoListRepo)

# Pydantic types for API request bodies
class CreateTodoListReqBody(BaseModel):
    listName: str


class AddTodoReqBody(BaseModel):
    todoListId: str
    task: str


class ToggleTodoReqBody(BaseModel):
    todoListId: str
    todoId: str


class UpdateTodoReqBody(BaseModel):
    todoListId: str
    todoId: str
    task: str


class DeleteTodoReqBody(BaseModel):
    todoListId: str
    todoId: str


# cross-origin reference
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return "This is working!"


@app.post("/todoList")
def create_todo_list(body: CreateTodoListReqBody):
    list_name = body.listName
    todo_list_id = services.create_todo_list(list_name)
    return {"ok": True, "todo_list_id": todo_list_id}


@app.post("/todo")
def add_todo(body: AddTodoReqBody):
    todoListId = body.todoListId
    task = body.task
    todo_id = services.add_todo(todo_list_id=todoListId, task=task)
    return {"ok": True, "todo_id": todo_id}


@app.get("/todoList/{todoListId}")
def get_todo_list(todoListId):
    todo_list = services.get_todo_list(todo_list_id=todoListId)
    return {"ok": True, "todo_list": todo_list}


@app.put("/todo/toggle")
def toggle_todo(body: ToggleTodoReqBody):
    todoListId = body.todoListId
    todoId = body.todoId
    services.toggle_todo(todo_list_id=todoListId, todo_id=todoId)
    return {"ok": True}


@app.put("/todo/updateTask")
def update_todo_task(body: UpdateTodoReqBody):
    todoListId = body.todoListId
    todoId = body.todoId
    task = body.task
    services.update_todo_task(todo_list_id=todoListId, todo_id=todoId, task=task)
    return {"ok": True}


@app.delete("/todo")
def delete_todo(body: DeleteTodoReqBody):
    todoListId = body.todoListId
    todoId = body.todoId
    services.delete_todo(todo_list_id=todoListId, todo_id=todoId)
    return {"ok": True}
