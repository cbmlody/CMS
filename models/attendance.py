from models.database import Base , db_session
from sqlalchemy import Column, Integer, String, Boolean


class Attendance(Base):
    """Holds attendance data"""
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    date = Column(String(10), nullable=False)
    status = Column(Boolean, nullable=False)

    """
    Attendance which contains information of date and status of attendance
    """
    def __init__(self, user_id, date, status):
        self.user_id = user_id
        self.date = date
        self.status = status

    def add(self):
        """Adds attendance to database"""
        db_session.add(self)
        db_session.commit()

    @classmethod
    def get_all(cls):
        """Get all attendances from db"""
        attendances = cls.query.all()
        return attendances

    @classmethod
    """Get all attendances from specified user"""
    def get_by_id(cls,student_id):
        selected = cls.query(cls).filter_by(user_id=student_id).all()
        return selected
