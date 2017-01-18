import time


class Attendance:

    def __init__(self, attendance, date=time.strftime("%d/%m/%Y")):
        self.date = date
        self.attendance = attendance

