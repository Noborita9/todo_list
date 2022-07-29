import sqlite3 as sql
class TaskDAO():
    def __init__(self):
        pass

    def connect(self, db_name: str):
        connection = sql.connect(db_name)
        cursor = connection.cursor()
        return cursor

    def create_table(self, cursor: sql.Cursor, table_name: str, item_dict: dict):
        state = {
                "table_created" : False,
                "err" : None,
                }
        try:
            cursor.execute(table_name)
        except Exception:
            pass
        return state

