class State():
    def __init__(self, type: str) -> None:
        self.completed = False
        self.err = None
        self.number = 0
        self.set_state(type)

    def set_state(self, type: str):
        states = {
                "OK": {
                    "completed": True,
                    "err": None,
                    "number": 200,
                    },
                "CREATED": {
                    "completed": True,
                    "err": None,
                    "number": 200,
                    },
                "FAILED": {
                    "completed": False,
                    "err": "Action Failed",
                    "number": 400,
                    },
                "NOTFOUND": {
                    "completed": False,
                    "err": "Instance Not Found",
                    "number": 400,
                    },
                }
        if type in states:
            self.completed = states[type]["completed"]
            self.err = states[type]["err"]
            self.number = states[type]["number"]
