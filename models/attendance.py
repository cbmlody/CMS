from models.database import Database


class Attendance:
    """
    Attendance which contains information of date and status of attendance
    """
    def __init__(self, id_, date, status):
        self.id_ = id_
        self.date = date
        self.status = status

    def add(self):
        conn, cur = Database.db_connect()
        try:
            cur.execute("INSERT OR IGNORE INTO `ATTENDANCES` VALUES (?,?,?)", (self.id_, self.date, self.status))
            cur.execute("UPDATE `ATTENDANCES` SET status=(?) WHERE user_ID = (?)", (self.status, self.id_))
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

    @staticmethod
    def get_by_id(student_id):
        attendance_list = []
        conn, cur = Database.db_connect()
        try:
            attendances = cur.execute("SELECT * FROM `ATTENDANCES` WHERE user_ID=(?)", (student_id,)).fetchall()
            for attendance in attendances:
                attendance_list.append(Attendance(*attendance))
        finally:
            conn.close()
        return attendance_list

