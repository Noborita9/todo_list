import sqlite3 as sql
class TaskDAO():
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self, db_name: str) -> sql.Connection:
        connection = sql.connect(db_name)
        self.connection = connection
        return connection

    def cursorize(self, connection: sql.Connection) -> sql.Cursor:
        cursor = connection.cursor()
        self.cursor = cursor
        return cursor

task = TaskDAO()
connection = task.connect("todos.db")
