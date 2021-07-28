import sqlite3
from sqlite3.dbapi2 import Cursor

class CreateUser:
    def __init__(self, username):
        self.username = username

    def AddUserToDB(self):
        db = sqlite3.connect('olx-parser-bot.db')
        sql = db.cursor()

        sql.execute("""CREATE TABLE IF NOT EXISTS users (
        username TEXT,
        mailing BOOL,
        language TEXT
        )""")

        db.commit()

        sql.execute("SELECT username FROM users WHERE username = '{0}'".format(self.username))


        if sql.fetchone() is None:
            sql.execute(
                "INSERT INTO users VALUES ('{0}', {1}, '{2}')".format(self.username, True, 'ru'))
            db.commit()

        return 'Success'