from models.database import db_session
from models.database import Base
from sqlalchemy import Column, Integer, String


class CheckpointGrades(Base):
    """Holds checkpoints user grades"""

    __tablename__ = 'checkpoint_grade'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    checkpoint_id = Column(Integer, nullable=False)
    card = Column(String(50), nullable=False)

    def __init__(self, user_id, checkpoint_id, card):
        self.user_id = user_id
        self.checkpoint_id = checkpoint_id
        self.card = card

    def grade(self):
        try:
            exists = CheckpointGrades.query.filter_by(user_id=self.user_id, checkpoint_id=self.checkpoint_id).one()
            exists.card = self.card
            db_session.merge(exists)
        except:
            db_session.merge(self)
            db_session.commit()

    @classmethod
    def get_user_checkpoints(cls, user_id):
        user_grades = cls.query.filter_by(user_id=user_id).all()
        return user_grades
