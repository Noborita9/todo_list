from os import stat
import sqlite3 as sql
from state import State
from task import Task
class Task_Dao():
    def __init__(self, db_name: str) -> None:
        self.connection = sql.connect(db_name) 
        self.cursor = self.connection.cursor()

    def insert_todo(self, task: Task):
        try:
            query = f"INSERT INTO todos (id, title, desc, date_init, date_end, completed)"
            self.cursor.execute(query)
            self.connection.commit()
            state = State(True, "")
        except Exception as e:
            state = State(False, f"{e}")
            raise e
        return state

dao = Task_Dao("todos.db")
