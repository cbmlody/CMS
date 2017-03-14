from .database import Database
from datetime import datetime
from .assignment import Assignment
class Submission:
    """Holds assignments submitted by students"""

    def __init__(self, id, user_id, submission_date, project, points, assignment_id, team_id):
        self.id = id
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
        assignment_title = Assignment.get_by_id(self.assignment_id).title


    @staticmethod
    def save(user_id, project,points,assignment_id,team_id):
        """Saves submitted assignment to database"""
        con, cur = Database.db_connect()
        submission_date = datetime.today()
        try:
            cur.execute("INSERT INTO `SUBMISSIONS` (user_ID, date, content, grade, assignment_ID,team_ID) VALUES (?,?,?,?,?,?)",
                        (user_id, submission_date, project, points, assignment_id, team_id,))
            con.commit()
        except Exception:
            return "Record already exists"
        finally:
            con.close()

    @classmethod
    def get_all(cls):
        submissions = []
        conn, cur = Database.db_connect()
        submission_list = cur.execute("SELECT * FROM `SUBMISSIONS`").fetchall()
        for submit in submission_list:
            submissions.append(Submission(*submit))
        return submissions
