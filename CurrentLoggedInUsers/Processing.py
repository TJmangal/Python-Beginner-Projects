
class Processing:

    def __init__(self):

        self.events = []
        self.machines_info = {}

    def add_events(self, event):

        self.events.append(event)

    def process_data(self, events):

        events.sort(key=lambda ev: ev.datetime)
        for event in events:
            if event.machine not in self.machines_info.keys():
                self.machines_info[event.machine] = {event.user}

            if event.event_type.lower() == "log in":
                self.machines_info[event.machine].add(event.user)
            elif event.event_type.lower() == "log out" and event.user in self.machines_info[event.machine]:
                self.machines_info[event.machine].remove(event.user)

        return self.machines_info

    def display_report(self):

        for machine, users in self.machines_info.items():
            if len(users) > 0:
                print(f"Following users are logged in {machine} - ")
                print(",".join(users))
                print()
