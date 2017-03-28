from models.database import Base, db_session
from sqlalchemy import Column, Integer, String, Boolean


class Assignment(Base):
    """Holds assignments, created by mentors"""

    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    due_date = Column(String(10), nullable=True)
    max_points = Column(Integer, nullable=False)
    as_team = Column(Boolean(), nullable=False)

    def __init__(self, title, due_date, max_points, as_team=0):
        self.title = title
        self.due_date = due_date
        self.max_points = max_points
        self.as_team = as_team

    @classmethod
    def get_all(cls):
        """Returns list of assignments"""
        assignments = db_session.query(cls).all()
        return assignments

    @staticmethod
    def add(title, due_date, max_points, as_team):
        """Adds assignment to database"""
        assignment = Assignment(title, due_date, max_points, as_team)
        db_session.add(assignment)
        db_session.commit()

    @classmethod
    def get_by_id(cls, id):
        """ Retrieves assignment with given id from database.
        Args:
            id(int): item id
        Returns:
            Assignment: Assignment object with a given id
        """
        assignment = db_session.query(cls).filter(id=id).one()
        return assignment

    @classmethod
    def get_by_ids(cls, id_list):
        """Gets list of assignments with certain ids"""
        assignment_list = cls.query.filter(cls.id.in_(id_list)).all()
        return assignment_list
