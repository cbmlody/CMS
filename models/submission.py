from .database import Base, db_session
from sqlalchemy import Column, Integer, String, Boolean
from time import strftime as stime
from assignment import Assignment
from user import User


class Submission:
    """Holds assignments submitted by students"""

    def __init__(self, id_, user_id, submission_date, project, points, assignment_id, team_id):
        self.id_ = id_
        self.user_id = user_id
        self.submission_date = submission_date
        self.project = project
        self.assignment_id = assignment_id
        self.points = points
        self.team_id = team_id

    def grade(self, points):
        """Allows mentor to grade an assignment """
        self.points = points

    def get_table_info(self):
        """Gets data to to display it in table"""
        assignment_title = Assignment.get_by_id(self.assignment_id).title
        full_name = Person.get_by_id(self.user_id).full_name
        date = self.submission_date
        project = self.project
        id_ = self.id_
        return [assignment_title, full_name, date, project, id_]

    @staticmethod
    def get_by_user_id(user_id):
        """Returns user submitting an assignment"""
        con, cur = Database.db_connect()
        submissions_list = []
        try:
            submissions = cur.execute("SELECT * FROM `SUBMISSIONS` WHERE user_ID=(?)", (user_id,)).fetchall()
            for submission in submissions:
                submissions_list.append(Submission(*submission))
        finally:
            con.close()
        return submissions_list

    @staticmethod
    def save(user_id, project, assignment_id, team_id):
        """Saves submitted assignment to database"""
        con, cur = Database.db_connect()
        submission_date = stime("%d-%m-%Y")
        try:
            cur.execute(
                "INSERT OR IGNORE INTO `SUBMISSIONS` (user_ID, submission_date, content, grade, assignment_ID,team_ID) VALUES (?,?,?,?,?,?)",
                (user_id, submission_date, project, None, assignment_id, team_id,))
            cur.execute(
                "UPDATE `SUBMISSIONS` SET user_ID =? , submission_date = ?, content =?, grade =?, assignment_ID =?, team_ID =? WHERE user_ID = ? AND assignment_id =?",
                (user_id, submission_date, project, None, assignment_id, team_id, user_id, assignment_id))
            con.commit()
        except Exception:
            return "Record already exists"
        finally:
            con.close()

    @staticmethod
    def get_all():
        """Returns list of submissions"""
        submissions = []
        conn, cur = Database.db_connect()
        submission_list = cur.execute("SELECT * FROM `SUBMISSIONS`")
        for submit in submission_list:
            submissions.append(Submission(*submit))
        return submissions