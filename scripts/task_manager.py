from task import Task
from task_dao import State, Task_Dao as task_dao
class Task_Manager():
    def __init__(self, db_name: str) -> None:
        # self.order = order
        self.td = task_dao(db_name)

    def create_task(self, title: str, desc: str, urgency: float, id: int) -> State:
        state = self.td.insert_task(Task(title, desc, urgency, id))
        return state

    def select_task(self, id: int = -1) -> list:
        state = self.td.select_task(id)
        return state.val
            

    def save_task(self):
        pass

    def delete_task(self):
        pass
