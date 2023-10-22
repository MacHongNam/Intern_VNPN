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

def get_users(username):
    db = connect_db()
    cur = db.cursor()
    cur.execute('SELECT * FROM users where username = ?', (username,))
    results = cur.fetchall()
    return results

def edit_userPassword(username, new_password):
    db = connect_db()
    db.cursor().execute('UPDATE users SET password = ? WHERE username = ?', (new_password, username))
    db.commit()

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
