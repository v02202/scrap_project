import click
from flask import current_app, g
from werkzeug.local import LocalProxy
from pymongo import MongoClient


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        client = MongoClient(host='db',
                            port=27017, 
                            username='root', 
                            password='pass')
        db = client["scrapy"]
    return db


# 代理模式是程序设计的一种结构模式，其目的是使调用者和执行者之间不发生直接的关系，而是使用一个代理人，这样调用者和执行者就进行了解耦，可以避免许多的问题。
# db = LocalProxy(get_db)
def close_db(e=None):
    db = g.pop('_database', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    # with current_app.open_resource('schema.sql') as f:
    #     db.executescript(f.read().decode('utf8'))
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    print('<------ Initialized the database -------->')
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)