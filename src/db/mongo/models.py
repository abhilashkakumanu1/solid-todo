from mongoengine import (
    Document,
    EmbeddedDocument,
    EmbeddedDocumentField,
    StringField,
    BooleanField,
    ListField,
)


class Todo(EmbeddedDocument):
    id = StringField(primary_key=True)
    task = StringField(required=True)
    isCompleted = BooleanField(default=False)


class TodoList(Document):
    id = StringField(primary_key=True)
    listName = StringField(required=True)
    todos = ListField(EmbeddedDocumentField(Todo))

    meta = {"collection": "todoList"}
