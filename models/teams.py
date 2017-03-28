from models.database import db_session
from models.database import Base
from sqlalchemy import Column, Integer, String


class Team(Base):
    """Holds team objects"""
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120), nullable=False)

    def __init__(self, name):
        self.name = name

    def add(self):
        """Adds new team to database"""
        db_session.add(self)

    @classmethod
    def get_all(cls):
        all_teams = cls.query.all()
        return all_teams