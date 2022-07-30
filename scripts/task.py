import datetime
class Task():
    def __init__(self, title: str, desc: str, urgency: float, id: int, date_init: datetime.date = datetime.date.today(), date_end: datetime.date = datetime.date.today(), completed: bool = False) -> None:
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self.date_init = date_init
        self.date_end = date_end
        self.id = id
        self.completed = completed

    def set_title(self, new_title):
        self.title = new_title

    def set_text(self, new_text):
        self.text = new_text

    def set_urgency(self, urgency_level):
        self.urgency = urgency_level

    def set_date_end(self, end_date):
        self.date_end = end_date

    def print_task(self):
        print(f"{self.title}:   urgency: {self.urgency}\n{self.text}\ninitialized: {self.date_init} | finalization: {self.date_end}")

def main():
    task_1 = Task("Title", "Text", 0.5, 1)
    task_1.set_date_end(datetime.date(2022, 12, 28))
    task_1.print_task()
    print(type(task_1.date_init))
    print(type(task_1.date_end))


if __name__ == "__main__":
    main()


