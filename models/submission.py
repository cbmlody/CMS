from .database import Base, db_session
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from time import strftime as stime


class Submission(Base):
    """Holds assignments submitted by students"""

    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    submission_date = Column(String(10), nullable=True)
    project = Column(String, nullable=False)
    grade = Column(Integer, nullable=True)
    assignment_id = Column(Integer, ForeignKey('assignments.id'))
    team_id = Column(Integer, ForeignKey('team.id'))

    assignment = relationship('Assignment', backref='submissions')
    user = relationship('User', backref = 'submissions')
    team = relationship('Team', backref = 'submissions')

    def __init__(self, user_id, submission_date, project, assignment_id, team_id):
        self.user_id = user_id
        self.submission_date = submission_date
        self.project = project
        self.assignment_id = assignment_id
        self.team_id = team_id

    def grading(self, points):
        """Allows mentor to grade an assignment """
        self.grade = points
        db_session.merge(self)
        db_session.commit()

    @classmethod
    def get_by_user_id(cls, user_id):
        """Returns user submitting an assignment"""
        submissions_list = cls.query.filter_by(user_id=user_id).all()
        return submissions_list

    @classmethod
    def get_by_id(cls, id):
        """Returns user submitting an assignment"""
        submission = cls.query.filter_by(id=id).one()
        return submission

    @classmethod
    def save(cls, user_id, project, assignment_id, team_id):
        """Saves submitted assignment to database"""
        submission_date = stime("%d-%m-%Y")
        submission = cls(user_id, submission_date, project, assignment_id, team_id)
        db_session.merge(submission)
        db_session.commit()

    @classmethod
    def get_all(cls):
        """Returns list of submissions"""
        submissions = cls.query.all()
        return submissions
