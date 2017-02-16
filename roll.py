import database


class Attendance:
    """
    Attendance which contains information of date and status of attendance
    """
    attendance_list = []

    def __init__(self, name, date, status, day_of_school):
        self.name = name
        self.date = date
        self.status = status
        self.day_of_school = day_of_school
        self.attendance_list.append([self.name, self.date, self.status, self.day_of_school])

    @staticmethod
    def import_from_db():
        attendances = database.Database.cur.execute("SELECT * FROM ATTENDANCES").fetchall()
        for attendance in attendances:
            Attendance(*attendance)

