from .database import Base, db_session
from sqlalchemy import Column, Integer, String, Boolean
from time import strftime as stime
from assignment import Assignment
from user import User


class Submission(Base):
    """Holds assignments submitted by students"""

    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_ID = Column(Integer, nullable=False)
    submission_date = Column(String(10), nullable=True)
    project = Column(String, nullable=False)
    grade = Column(Integer, nullable=True)
    assignment_ID = Column(Integer, nullable=False)
    team_ID = Column(Integer, nullable=True)

    def __init__(self, user_id, submission_date, project, points, assignment_id, team_id):
        self.user_id = user_id
        self.submission_date = submission_date
        self.project = project
        self.assignment_id = assignment_id
        self.points = points
        self.team_id = team_id

    def grading(self, points):
        """Allows mentor to grade an assignment """
        self.points = points

    def get_table_info(self):
        """Gets data to to display it in table"""
        assignment_title = Assignment.get_by_id(self.assignment_id).title
        full_name = User.get_by_id(self.user_id).full_name
        date = self.submission_date
        project = self.project
        id_ = self.id
        return [assignment_title, full_name, date, project, id_]

    @staticmethod
    def get_by_user_id(user_id):
        """Returns user submitting an assignment"""
        submissions_list = db_session.query(Submission).filter(user_ID=user_id).all()
        return submissions_list

    @staticmethod
    def save(user_id, project, assignment_id, team_id):
        """Saves submitted assignment to database"""
        submission_date = stime("%d-%m-%Y")
        submission = Submission(user_id, submission_date, project, None, assignment_id, team_id)
        db_session.merge(submission)
        db_session.commit()

    @staticmethod
    def get_all():
        """Returns list of submissions"""
        submissions = db_session.query(Submission).all()
        return submissions
