from os import stat
import sqlite3 as sql
from state import State
class Sqlite_Creator():
    def __init__(self, db_name: str) -> None:
        self.connection = sql.connect(db_name) 
        self.cursor = self.connection.cursor()

    def table_exists(self, table_name):
        try:
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='table_name';")
            self.connection.commit()
            state = State(True, "")
        except Exception as e:
            state = State(False, f"{e}")
            raise e 
        return state

    def create_table(self, table_name: str, query: str) -> State:
        try:
            if self.table_exists(table_name).completed:
                return State(False, "Table Already Exists")
            format_query = f"CREATE TABLE {table_name} ({query})"
            self.cursor.execute(format_query)
            self.connection.commit()
            print(format_query)
            state = State(True, "")
        except Exception as e:
            state = State(False, f"{e}")
            raise e
        return state

    def drop_table(self, table_name: str) -> State:
        try:
            format_query = f"DROP TABLE {table_name}"
            self.cursor.execute(format_query)
            self.connection.commit()
            state = State(True, "")
        except Exception as e:
            state = State(False, f"{e}")
            raise e
        return state

def main():
    pass
    sq_creator = Sqlite_Creator("../todos.db")
    sq_creator.create_table("todos", "id AUTOINCREMENT, title text, desc text , urgency real, date_init date, date_end date, completed int")


if __name__ == "__main__":
    main()
