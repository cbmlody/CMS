import sqlite3
from models.database import Database


class Person:

    def __init__(self, id_, login, password, full_name, role_id, team_id):

        self.id_ = id_
        self.login = login
        self.password = password
        self.full_name = full_name
        self.role_id = role_id
        self.team_id = team_id

    @classmethod
    def get_all(cls, role=None):
        conn, cur = Database.db_connect()
        query = "SELECT * FROM `USERS`"
        values = ()
        if role:
            query += "WHERE role_id=(?)"
            values = (role,)
        all_users = cur.execute(query, values)
        user_list = []
        for user in all_users:
            user_list.append(cls(*user))
        return user_list

    def add(self):
        conn, cur = Database.db_connect()
        try:
            cur.execute("INSERT INTO `USERS`(login,password,full_name,role_id,team_id) VALUES(?,?,?,?,?)",
                        (self.login, self.password, self.full_name, self.role_id, self.team_id))
            conn.commit()
        except sqlite3.IntegrityError:
            return "User exists!"
        finally:
            conn.close()

    def delete(self):
        conn, cur = Database.db_connect()
        try:
            cur.execute("DELETE FROM `USERS` WHERE login=?", (self.login,))
            conn.commit()
        finally:
            conn.close()

    def update(self):
        conn, cur = Database.db_connect()
        try:
            cur.execute("UPDATE `USERS` SET password=?, full_name=?, role_id=?, team_id=? WHERE login=?",
                        (self.password, self.full_name, self.role_id, self.team_id, self.login))
            conn.commit()
        finally:
            conn.close()

    def change_password(self, password, repeat_password):
        conn, cur = Database.db_connect()
        error = None
        try:
            if password == repeat_password:
                cur.execute("UPDATE `USERS` SET password=? WHERE login=?", (password, self.login))
                error = "Password successfully changed!"
                conn.commit()
            else:
                error = "Passwords don't match!"
        finally:
            conn.close()
        return error

    @classmethod
    def get_by_id(cls, id):
        conn, cur = Database.db_connect()
        user = cur.execute("SELECT * FROM `USERS` WHERE ID = ?", (id,)).fetchone()
        return cls(*user)

    @classmethod
    def get_by_login(cls, login):
        conn, cur = Database.db_connect()
        user = cur.execute("SELECT * FROM `USERS` WHERE login=(?)", (login,)).fetchone()
        return cls(*user)

