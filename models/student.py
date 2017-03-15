from models.person import Person
from models.database import Database


class Student(Person):

    role = 3

    def __init__(self, *args):
        Person.__init__(self, *args)

    def assign_team(self, team_id_to_assign):
        self.team_id = team_id_to_assign
        con, cur = Database.db_connect()
        try:
            cur.execute("UPDATE `USERS` SET team_id=(?) WHERE id=(?)", (self.team_id, self.id_,))
            con.commit()
        finally:
            con.close()

    def get_team_name(self):
        con, cur = Database.db_connect()
        try:
            team_name = cur.execute("SELECT name FROM `TEAMS` WHERE ID=(?)", (self.team_id,)).fetchone()[0]
        except Exception:
            team_name = None
        finally:
            con.close()
        return team_name
