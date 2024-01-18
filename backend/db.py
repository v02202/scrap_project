import click
from flask import current_app, g
from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy


def get_db():
    db = getattr(g, "_database", None)
    if db is None:

        db = g._database = PyMongo(current_app).db
       
    return db

# 代理模式是程序设计的一种结构模式，其目的是使调用者和执行者之间不发生直接的关系，而是使用一个代理人，这样调用者和执行者就进行了解耦，可以避免许多的问题。
db = LocalProxy(get_db)
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()