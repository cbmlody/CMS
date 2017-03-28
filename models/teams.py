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
