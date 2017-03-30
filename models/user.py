from sqlalchemy import Column, String, Integer, Boolean
from models.database import db_session, Base
from models.teams import Team


class User(Base):
    """Abstract class holding all users"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    role_id = Column(Integer, nullable=False)
    team_id = Column(Integer, nullable=True)
    status = Column(Boolean, nullable=False)

    MANAGER_ROLE = 0
    MENTOR_ROLE = 1
    EMPLOYEE_ROLE = 2
    STUDENT_ROLE = 3

    def __init__(self, login, password, full_name, role_id, team_id, status=True):
        self.login = login
        self.password = password
        self.full_name = full_name
        self.role_id = role_id
        self.team_id = team_id
        self.status = status

    def add(self):
        """Adds new user to database"""
        db_session.add(self)
        db_session.commit()

    def delete(self):
        """Removes certain user from database"""
        self.status = False
        db_session.commit()

    def change_password(self, password, repeat_password):
        """Changes users password"""
        error = None
        if password == repeat_password and len(password) != 0 and len(repeat_password) != 0:
            self.password = password
            error = "Password successfully changed!"
            db_session.commit()
        else:
            error = "Passwords don't match!"
        return error

    def assign_team(self, team_id_to_assign):
        """ Assign user to team """
        self.team_id = team_id_to_assign
        db_session.commit()

    def get_team_name(self):
        """ get team name """
        if self.team_id:
            team = Team.query.filter_by(id=self.team_id).one()
            return team.name
        else:
            return "None"

    @classmethod
    def get_all(cls, role=None):
        """Gets list of all users"""
        if role:
            user_list = cls.query.filter_by(status=True, role_id=role).all()
        else:
            user_list = cls.query.filter_by(status=True).all()
        return user_list

    @classmethod
    def get_active_unactive_users(cls):
        user_list = cls.query.all()
        return user_list

    @classmethod
    def get_by_id(cls, id):
        """Gets user object by id"""
        user = cls.query.filter_by(id=id).one()
        return user

    @classmethod
    def get_by_login(cls, login):
        """Gets user object by login"""
        user = cls.query.filter_by(status=True, login=login).one()
        return user
