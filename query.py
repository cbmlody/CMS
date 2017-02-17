import sqlite3 as sql
import hashlib


class Query:

    con = sql.connect('database.db')
    cur = con.cursor()

    @classmethod
    def get_user(cls, login, password):
        user = cls.cur.execute("SELECT ID, role_ID FROM `USERS` WHERE login=? AND password=?", (login, password))
        return user

    @classmethod
    def get_users_by_role(cls, role):
        users = cls.cur.execute("SELECT login, full_name, name FROM `USERS` u, `ROLES` r  WHERE u.role_ID = r.ID AND r.name=?", (role,))
        return users

    @classmethod
    def insert_user(cls, inp_login, inp_password, inp_full_name, inp_role_ID):
        inp_password = hashlib.md5(inp_password.encode('utf-8')).hexdigest()

        users = cls.con.execute("SELECT * FROM `USERS`")
        if inp_login not in users.fetchall():
            cls.cur.execute("INSERT INTO `USERS`(login, password, full_name, role_ID) VALUES (?, ?, ?, ?)",
                            (inp_login, inp_password, inp_full_name,inp_role_ID),)
            cls.con.commit()
            return "User successfully added!"
        else:
            return "User exists in database"

    @classmethod
    def remove_user(cls, username):
        cls.cur.execute("DELETE FROM `USERS` WHERE login = ?", (username,))
        cls.con.commit()
        return "User deleted"

    @classmethod
    def change_password(cls, username, password2):
        cls.cur.execute("UPDATE `USERS` SET password=? WHERE login=?"), (password2, username)
        cls.con.commit()
        return "Password changed"

    @classmethod
    def get_data_by_table_name(cls, table_name):
        data = cls.cur.execute("SELECT * FROM {}".format(table_name))
        return data

    @classmethod
    def get_role_by_id(cls, role_id):
        role_name = cls.cur.execute("SELECT name FROM `ROLES` r, `USERS` u  WHERE r.ID = ?", (role_id,))
        return role_name

    @classmethod
    def get_full_name_login(cls, role_ID):
        data = cls.cur.execute("SELECT full_name, login FROM `USERS` WHERE role_ID = ?", (role_ID, ))
        return data

    @classmethod
    def get_users_data_using_roleid(cls, roleid):
        data = cls.cur.execute("SELECT login FROM `USERS` WHERE role_ID = ?", (roleid, ))
        return data


