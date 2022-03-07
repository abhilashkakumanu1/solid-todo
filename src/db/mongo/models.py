import os
import logging

from mongoengine import (
    connect,
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    StringField,
    BooleanField,
    ListField,
)

# DB connection env variables
MONGO_HOST = os.environ.get("MONGO_HOST")
MONGO_DB = os.environ.get("MONGO_DB")
MONGO_PORT = int(os.environ.get("MONGO_PORT"))

# Connect to DB
connect(db=MONGO_DB, host=MONGO_HOST, port=MONGO_PORT)
logging.info("Connected to DB")


class Todo(EmbeddedDocument):
    id = StringField(primary_key=True)
    task = StringField(required=True)
    isCompleted = BooleanField(default=False)


class TodoList(Document):
    id = StringField(primary_key=True)
    listName = StringField(required=True)
    todos = ListField(EmbeddedDocumentField(Todo))

    meta = {"collection": "todoList"}
