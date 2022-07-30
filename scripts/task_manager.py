from task import Task
from task_dao import State, Task_Dao as task_dao
class Task_Manager():
    def __init__(self, db_name: str) -> None:
        # self.order = order
        self.td = task_dao(db_name)

    def create_task(self, title: str, desc: str, urgency: float, id: int) -> State:
        self.td.insert_todo(Task(title, desc, urgency, id))
        state = State(True, "")
        return state

    def select_task(self):
        self.td.select_todo()
        state = State(True, "")
        return state

    def save_task(self):
        pass

