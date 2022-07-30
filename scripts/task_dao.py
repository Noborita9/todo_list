import sqlite3 as sql
from state import State
from task import Task
class Task_Dao():
    def __init__(self, db_name: str) -> None:
        self.connection = sql.connect(db_name, detect_types=sql.PARSE_DECLTYPES |
                                                            sql.PARSE_COLNAMES) 
        self.cursor = self.connection.cursor()

    def insert_todo(self, task: Task):
        try:
            query = "INSERT INTO todos (id, title, urgency, desc, date_init, date_end, completed) values (?, ?, ?, ?, ?, ?, ?);"
            data_tuple = (task.id, task.title, task.urgency, task.desc, task.date_init, task.date_end, task.completed)
            self.cursor.execute(query, data_tuple )
            self.connection.commit()
            state = State(True, "")
        except Exception as e:
            state = State(False, f"{e}")
            raise e
        return state

    def select_todo(self, id: int = -1) :# -> State:
        try:
            if id == -1 :
                select_string = "SELECT * from todos;"
            else:
                select_string = f""
            self.cursor.execute(select_string)
            rows = self.cursor.fetchall()
            self.connection.commit()
        except Exception as e:
            raise e

    def delete_todo(self, id: int) -> State:
        try:
            self.cursor.execute(f"DELETE FROM todos WHERE id={id}")
            self.connection.commit()
            state = State(True, "")
        except sql.Error as e:
            state = State(False, f"{e}")
            raise e
        return state
