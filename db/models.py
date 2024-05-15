import enum
import logging

from peewee import *

db = SqliteDatabase("database.db")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    chat_id = BigIntegerField(null=False, primary_key=True)
    city = TextField(null=True, default=None)


try:
    db.create_tables([User])
except OperationalError as er:
    logging.warning(str(er))
