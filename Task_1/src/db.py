import sqlite3


def connect_db():
    db = sqlite3.connect('data.db')
    db.cursor().execute('CREATE TABLE IF NOT EXISTS users '
                        '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
                        'username TEXT, '
                        'password TEXT)')
    db.cursor().execute('CREATE TABLE IF NOT EXISTS comments '
                        '(id INTEGER PRIMARY KEY AUTOINCREMENT, '
                        'username TEXT, '
                        'comment TEXT, '
                        'time TEXT)')
    db.commit()
    return db


def add_user(username, password):
    db = connect_db()
    db.cursor().execute('INSERT INTO users (username, password) '
                        'VALUES (?, ?)', (username, password))
    db.commit()

def get_user(username, password):
    try:
        db = connect_db()
        cur = db.cursor()
        sql = f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}'"
        cur.execute(sql)
        result = cur.fetchone()
        return result
    except:
        return False

def add_comment(username, comment, time):
    db = connect_db()
    db.cursor().execute('INSERT INTO comments (username, comment, time) '
                        'VALUES (?, ?, ?)', (username, comment, time))
    db.commit()


def get_comments():
    db = connect_db()
    cur = db.cursor()
    cur.execute('SELECT username, comment, time FROM comments')
    results = cur.fetchall()
    return results

add_user('admin', 'admin')
add_comment('admin', 'Hello', '29-09-2023 At 02:23')