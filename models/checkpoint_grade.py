from models.database import db_session
from models.database import Base
from sqlalchemy import Column, Integer, String, Boolean


class CheckpointGrades(Base):
    """Holds checkpoints user grades"""
    __tablename__ = 'checkpoint_grade'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    checkpoint_id = Column(Integer, nullable=False)
    card = Column(String(50), nullable=False)

    def __int__(self, user_id, checkpoint_id, card):
        self.user_id = user_id
        self.checkpoint_id = checkpoint_id
        self.card = card

    def grade(self):
        db_session.add(self)
        db_session.commit()