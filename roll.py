import time
import csv


class Attendance:
    """
    Attendance which contains information of date and status of attendance
    """
    attendance_list = []

    def __init__(self, name, attendance, who):
        self.date = time.strftime("%d/%m/%Y")
        self.name = name
        self.attendance = attendance
        self.who = who
        self.attendance_list.append([self.date, self.attendance, self.name, self.who])

    @classmethod
    def save_roll_to_file(cls):
        with open("attendance.ccms", "a+") as att:
            data_writer = csv.writer(att)
            for row in Attendance.attendance_list:
                data_writer.writerow(row)

