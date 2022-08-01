import getch
import os
from task_manager import Task_Manager
from task import Task

# TODO: Cache system so its faster :D


class Menu():
    def __init__(self, db_name: str) -> None:
        self.tm = Task_Manager(db_name)
        self.task_number = 0
        self.task_quantity = 1
        self.is_opened = False
        self.actual_tasks = []
        self.cached = False
        self.order = "urgency"
        self.is_ordered = False

    def get_tasks(self):
        self.actual_tasks = self.tm.select_task()
        self.task_quantity = len(self.actual_tasks)
        if self.task_quantity == 0:
            self.task_quantity = 1
        self.cached = True

    def order_tasks(self):
        self.actual_tasks = sorted(
            self.actual_tasks, key=lambda task: task[3], reverse=True)
        self.is_ordered = True

    def format_task(self, task: tuple) -> Task:
        new_task = Task(task[0], task[1], task[2],
                        task[3], task[4], task[5], task[6])
        return new_task

    def print_task(self, task: Task, is_selected: bool = False) -> None:
        line_init = f"{task.urgency} | {task.title}"
        line1 = f"{line_init}{' ' * (40 - len(line_init))}| {task.completed} | #{task.id} "
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
        urgency = float(input("Task's Urgency: ").replace(",", "."))
        self.tm.create_task(0, title=title, desc=desc, urgency=urgency)
        self.cached = False
        self.is_ordered = False

    def delete_task(self):
        del_task_num = self.actual_tasks[self.task_number][0]
        self.tm.delete_task(del_task_num)
        self.cached = False
        self.is_ordered = False

    def show(self, actual: int = 0):
        print("Your Tasks: [c]reate [d]elete [ ]open [q]exit")
        if not self.cached:
            self.get_tasks()
        if not self.is_ordered:
            self.order_tasks()
        for index, task in enumerate(self.actual_tasks):
            formated_task = self.format_task(task)
            if actual == index:
                self.print_task(formated_task, True)
            else:
                self.print_task(formated_task)

    def start(self):
        while True:
            os.system("clear")
            self.show(self.task_number)
            ans = getch.getch()
            self.is_opened = False
            if ans == "q":
                break
            if ans == "j":
                self.task_number = (self.task_number + 1) % self.task_quantity
                continue
            elif ans == "k":
                self.task_number = (self.task_number - 1) % self.task_quantity
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
