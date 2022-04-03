import sqlite3

import os

dir = os.path.dirname(os.path.abspath(__file__))


def get_db_connection():
    conn = sqlite3.connect('posts.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    connection = sqlite3.connect('posts.db')
    posts = connection.execute('SELECT name FROM sqlite_master WHERE type = \'table\' AND name = \'posts\'').fetchall()
    if len(posts) == 0:
        with open(dir + '/ddl.sql') as f:
            connection.executescript(f.read())
        connection.commit()
    connection.close()


def get_posts():
    connection = sqlite3.connect('posts.db')
    posts = connection.execute('SELECT id, title, created, content FROM posts WHERE status = 1').fetchall()
    connection.close()
    return posts


def get_post(id):
    connection = sqlite3.connect('posts.db')
    posts = connection.execute('SELECT id, title, created, content FROM posts WHERE id = ' + str(id)).fetchone()
    connection.close()
    return posts


def del_post(id):
    conn = get_db_connection()
    conn.execute('update posts set status = 0 where id = ' + str(id))
    conn.commit()
    conn.close()


def new_post(title: str, content: str):
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                 (title, content))
    conn.commit()
    conn.close()
