from task import Task

class Task_Manager():
    def __init__(self, order: str = "urg"):
        self.order = order

    def get_task(self):
        pass

    def create_task(self, title: str, text: str, urgency: float) -> Task:
        new_task = Task(title, text, urgency)
        return new_task

    def save_task(self):
        pass

