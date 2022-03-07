import os
import logging

from dotenv import load_dotenv
from mongoengine import (
    connect,
)

from ..interfaces import IDB

# load environment variables
load_dotenv()
connection_str = os.environ.get("DB_CONNECTION_STRING")


class DBImp(IDB):
    def connect(self):
        connect(host=connection_str)
        logging.info("successfully connected to DB")


DB = DBImp()
