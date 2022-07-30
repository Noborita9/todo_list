import sqlite3 as sql
from state import State
from task import Task
class Task_Dao():
    def __init__(self, db_name: str) -> None:
        self.connection = sql.connect(db_name) 
        self.cursor = self.connection.cursor()

    def insert_todo(self, task: Task):
        try:
            task_string = f"{task.id}, '{task.title}', {task.urgency}, '{task.desc}', {task.date_init}, {task.date_end}, {task.completed}"
            query = f"INSERT INTO todos (id, title, urgency, desc, date_init, date_end, completed) values ({task_string})"
            print(f"Task String = {task_string}\nQuery = {query}")
            self.cursor.execute(query)
            self.connection.commit()
            state = State(True, "")
        except Exception as e:
            state = State(False, f"{e}")
            raise e
        return state

    def select_todo(self):
        try:
            self.cursor.execute("SELECT * from todos")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
            self.connection.commit()

        except Exception as e:
            raise e

# dao = Task_Dao("todos.db")

dao = Task_Dao("../todos.db")
dao.select_todo()
