import datetime


class Task():
    def __init__(self, id: int,
                 title: str,
                 desc: str, 
                 urgency: float,
                 date_init: datetime.date = datetime.date.today(),
                 date_end: datetime.date = datetime.date.today(),
                 completed: bool = False) -> None:
        self.id = id
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self.date_init = date_init
        self.date_end = date_end
        self.completed = completed
