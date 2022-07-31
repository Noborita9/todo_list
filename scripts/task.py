import datetime
import uuid


class Task():
    def __init__(self, id: int = 0 ,
                 title: str = "UNNAMED",
                 desc: str = "UNDEFINED", 
                 urgency: float = 0.0,
                 date_init: datetime.date = datetime.date.today(),
                 date_end: datetime.date = datetime.date.today(),
                 completed: bool = False) -> None:
        self.id = self.generate_id(id) 
        self.title = title
        self.desc = desc
        self.urgency = urgency
        self.date_init = date_init
        self.date_end = date_end
        self.completed = completed

    def generate_id(self, eid: int = 0):
        if not eid:
            id = int(str(uuid.uuid1().int)[:8])
        else:
            id = eid
        return id
