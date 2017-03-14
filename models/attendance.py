from database import Database


class Attendance:
    """
    Attendance which contains information of date and status of attendance
    """
    def __init__(self, name, date, status, day_of_school):
        self.name = name
        self.date = date
        self.status = status
        self.day_of_school = day_of_school

    def add(self, user_id):
        conn, cur = Database.db_connect()
        try:
            cur.execute("INSERT INTO `ATTENDANCES` VALUES (?,?,?,?,?)",
                        (user_id, self.name, self.date, self.status, self.day_of_school,))
            conn.commit()
        except Exception:
            return "Record already exists"
        finally:
            conn.close()

    @staticmethod
    def get_all():
        attendance_list = []
        conn, cur = Database.db_connect()
        try:
            attendances = cur.execute("SELECT * FROM `ATTENDANCES`")
            for attendance in attendances:
                attendance_list.append(Attendance(*attendance))
        finally:
            conn.close()
        return attendance_list

