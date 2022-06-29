class Event:

    def __init__(self, machine, user, datetime, event_type):

        self.machine = machine
        self.user = user
        self.datetime = datetime
        self.event_type = event_type

    def __str__(self):

        return f"This event has following attributes - \n 1. machine = {self.machine} \n 2. user = {self.user} \n " \
               f"3. datetime = {self.datetime} \n 4. event_type = {self.event_type}"
