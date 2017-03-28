from models.database import db_session
from models.database import Base
from sqlalchemy import Column, Integer, String, Boolean
import datetime


class Checkpoint(Base):
    """Holds checkpoints data"""
    __tablename__ = 'checkpoint'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(120), nullable=False)
    date = Column(String(50), nullable=False)


    def __init__(self, description, date):
        self.description = description
        self.date = date

    def add(self):
        db_session.add(self)
        db_session.commit()

    @classmethod
    def list_checkpoints(cls):
        list_checkpoints = cls.query.all()
        return list_checkpoints