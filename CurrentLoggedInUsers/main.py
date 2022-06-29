import datetime
import Processing
from Event import Event as Ev

if __name__ == "__main__":

    event1 = Ev("aws_d03", "Tejasvi", datetime.datetime.now(), "Log In")
    event2 = Ev("aws_d03", "Chirag", datetime.datetime.now(), "Log In")
    event3 = Ev("aws_d04", "Teja", datetime.datetime.now(), "Log in")
    event4 = Ev("aws_d03", "Chir", datetime.datetime.now(), "Log In")
    event5 = Ev("aws_d05", "Tej", datetime.datetime.now(), "Log In")
    event6 = Ev("aws_d05", "Tej", datetime.datetime.now(), "Log out")

    processing = Processing.Processing()
    processing.add_events(event1)
    processing.add_events(event2)
    processing.add_events(event3)
    processing.add_events(event4)
    processing.add_events(event5)
    processing.add_events(event6)

    processing.process_data(processing.events)
    processing.display_report()
