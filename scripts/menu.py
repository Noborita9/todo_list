import os
from task_manager import Task_Manager
from task import Task
class Menu():
    def __init__(self, db_name: str) -> None:
        self.options = {}
        self.td = Task_Manager(db_name)

    def format_task(self, task: tuple) -> Task:
        new_task = Task(task[0], task[1], task[2], task[3], task[4], task[5], task[6] )
        return new_task
        

    def show(self):
        tasks = self.td.select_task()
        for task in tasks:
            formated_task = self.format_task(task)
            print(type(formated_task))
    
    def start(self):
        os.system("clear")
        self.show()
