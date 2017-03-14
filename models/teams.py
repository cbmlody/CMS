from models.database import Database
import sqlite3


class Team:

    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name

    def add(self):
        conn, cur = Database.db_connect()
        try:
            cur.execute("INSERT INTO `TEAMS`(name) VALUES(?)", (self.name,))
            conn.commit()
        except sqlite3.IntegrityError:
            return "Team exists!"
        finally:
            conn.close()

    @classmethod
    def get_all(cls):
        teams_list = []
        conn, cur = Database.db_connect()
        all_teams = cur.execute("SELECT * FROM `TEAMS`")
        for team in all_teams:
            teams_list.append(Team(*team))
        return teams_list