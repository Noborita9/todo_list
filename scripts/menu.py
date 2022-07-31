import getch
import os
from task_manager import Task_Manager
from task import Task
class Menu():
    def __init__(self, db_name: str) -> None:
        self.number = 0
        self.task_quantity = 0
        self.is_opened = False
        self.td = Task_Manager(db_name)

    def format_task(self, task: tuple) -> Task:
        new_task = Task(task[0], task[1], task[2], task[3], task[4], task[5], task[6] )
        return new_task
        

    def print_task(self, task: Task, is_selected: bool = False) -> None:
        line1 = f"{task.urgency} | {task.title} | {task.completed} | #{task.id} "
        if is_selected:
            line1 = "(*) " + line1 
            if self.is_opened:
                line1 = line1 + f"\n{task.desc}"
        else:
            line1 =  "( ) " + line1 
        print(line1)


    def open_task(self, actual: int = 0):
        pass

    def show(self, actual: int = 0):
        tasks = self.td.select_task()
        self.task_quantity = len(tasks)
        for index, task in enumerate(tasks):
            formated_task = self.format_task(task)
            if actual == index:
                self.print_task(formated_task, True)
            else:
                self.print_task(formated_task)
    
    def start(self):
        while True:
            os.system("clear")
            self.show(self.number % 2)
            ans = getch.getch()
            self.is_opened = False
            if ans == "q":
                break
            if ans == "j":
                self.number += 1
                continue
            elif ans == "k":
                self.number -= 1
                continue
            elif ans == " ":
                self.is_opened = True
                continue
