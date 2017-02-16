import time
from query import *
from database import *


class Attendance:
    """
    Attendance which contains information of date and status of attendance
    """
    attendance_list = []

    def __init__(self, name, attendance, who, date=time.strftime("%d/%m/%Y")):
        self.date = date
        self.name = name
        self.attendance = attendance
        self.attendance_list.append([self.date, self.attendance, self.name])

    # @classmethod
    # def save_roll_to_file(cls):
    #     with open("attendance.ccms", "a+") as att:
    #         data_writer = csv.writer(att)
    #         for row in Attendance.attendance_list:
    #             data_writer.writerow(row)
    #
    # @classmethod
    # def import_roll_from_sql(cls):
    #     with open("attendance.ccms", "r") as att:
    #         data_reader = csv.reader(att)
    #         for row in data_reader:
    #             Attendance(*row)
    @classmethod
    def list_init(cls):
        for elem  in Query.get_data_by_table_name('ATTENDANCES'):
            Attendance(*elem)

    @classmethod
    def add_attendance(cls, user_id, date, status):
        Database.cur.execute("INSERT INTO `ATTENDANCES` VALUES (?,?,?)", (user_id, date, status,))
