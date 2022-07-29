import sqlite3 as sql
from state import State
class Sqlite_Creator():
    def __init__(self, db_name: str) -> None:
        self.connection = sql.connect(db_name) 
        self.cursor = self.connection.cursor()

    def create_table(self, table_name: str, query: str) -> State:
        try:
            format_query = f"CREATE TABLE {table_name} ({query})"
            self.cursor.execute(format_query)
            self.connection.commit()
            state = State(True, "")
        except Exception as e:
            state = State(False, f"{e}")
            raise e
        return state

def main():
    sq_creator = Sqlite_Creator("todos.db")
    sq_creator.create_table("todos", "id AUTOINCREMENT, title text, desc text ,date_init date, date_end date")


if __name__ == "__main__":
    main()
