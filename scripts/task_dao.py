import sqlite3 as sql
from state import State
from task import Task
class Task_Dao():
    def __init__(self, db_name: str) -> None:
        self.connection = sql.connect(db_name, detect_types=sql.PARSE_DECLTYPES |
                                                            sql.PARSE_COLNAMES) 
        self.cursor = self.connection.cursor()

    def insert_task(self, task: Task):
        try:
            query = "INSERT INTO todos (id, title, urgency, desc, date_init, date_end, completed) values (?, ?, ?, ?, ?, ?, ?);"
            data_tuple = (task.id, task.title, task.desc, task.urgency, task.date_init, task.date_end, task.completed)
            self.cursor.execute(query, data_tuple )
            self.connection.commit()
            state = State("OK")
        except sql.Error as e:
            state = State("FAILED", [e])
            raise e
        return state

    def select_task(self, id: int = -1) :# -> State:
        try:
            if id == -1 :
                select_string = "SELECT * from todos;"
            else:
                select_string = f"SELECT * FROM todos WHERE id = {id}"
            self.cursor.execute(select_string)
            rows = self.cursor.fetchall()
            self.connection.commit()
            state = State("OK", rows)
        except sql.Error as e:
            state = State("NOTFOUND", [e])
            raise e
        return state
            

    def delete_task(self, id: int) -> State:
        try:
            self.cursor.execute(f"DELETE FROM todos WHERE id={id}")
            self.connection.commit()
            state = State("OK")
        except sql.Error as e:
            state = State("FAILED", [e])
            raise e
        return state

