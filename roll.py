import time


class Attendance:
    """
    Attendance which contains information of date and status of attendance
    """

    def __init__(self, attendance, date=time.strftime("%d/%m/%Y")):
        self.date = date
        self.attendance = attendance

