import os
import logging

from mongoengine import (
    connect,
)

# MONGO DB SETTINGS
DB_HOST = os.environ.get("DB_HOST")
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_DATABASE = os.environ.get("DB_DATABASE")

connect(
    host=f"mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:27017/{DB_DATABASE}",
)
