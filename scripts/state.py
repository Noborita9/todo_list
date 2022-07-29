class State():
    def __init__(self, completed: bool = False, err: "str" = "", number: int = 0) -> None:
        self.completed = completed
        self.err = err
        self.number = number 
        self.init_number()

    def init_number(self):
        if self.completed :
            self.number = 200
        else:
            self.number = 404
