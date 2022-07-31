import getch
import os
from task_manager import Task_Manager
from task import Task

# TODO: Cache system so its faster :D

class Menu():
    def __init__(self, db_name: str) -> None:
        self.task_number = 0
        self.task_quantity = 1
        self.is_opened = False
        self.tm = Task_Manager(db_name)
        self.actual_tasks = []
        self.cached = False

    def get_tasks(self):
        self.actual_tasks = self.tm.select_task()
        self.task_quantity = len(self.actual_tasks)
        self.cached = True

    def format_task(self, task: tuple) -> Task:
        new_task = Task(task[0], task[1], task[2],
                        task[3], task[4], task[5], task[6])
        return new_task

    def print_task(self, task: Task, is_selected: bool = False) -> None:
        line1 = f"{task.urgency} | {task.title} | {task.completed} | #{task.id} "
        if is_selected:
            line1 = "(*) " + line1
            if self.is_opened:
                line1 = line1 + f"\n{task.desc}"
        else:
            line1 = "( ) " + line1
        print(line1)

    def create_task(self):
        os.system("clear")
        title = input("Task's Title: ")
        desc = input("Task's Content:\n")
        urgency = float(input("Task's Urgency: "))
        self.tm.create_task(5, title, desc, urgency)
        self.cached = False

    def delete_task(self):
        self.tm.delete_task(self.task_number)
        self.cached = False

    def show(self, actual: int = 0):
        if not self.cached:
            self.get_tasks()
        for index, task in enumerate(self.actual_tasks):
            formated_task = self.format_task(task)
            if actual == index:
                self.print_task(formated_task, True)
            else:
                self.print_task(formated_task)

    def start(self):
        while True:
            os.system("clear")
            self.show(self.task_number % self.task_quantity)
            ans = getch.getch()
            self.is_opened = False
            if ans == "q":
                break
            if ans == "j":
                self.task_number += 1
                continue
            elif ans == "k":
                self.task_number -= 1
                continue
            elif ans == " ":
                self.is_opened = True
                continue
            elif ans == "c":
                self.create_task()
                continue
            elif ans == "d":
                self.delete_task()
                self.task_number -= 1
