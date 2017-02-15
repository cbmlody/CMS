import sqlite3 as sql

class Query:

    con = sql.connect('database.db')
    cur = con.cursor()

    @classmethod
    def get_user(cls, login, password):
        user = cls.cur.execute("SELECT ID, role_ID FROM `USERS` WHERE login=? AND password=?", (login, password))
        return user.fetchall()

    @classmethod
    def get_users_by_role(cls, role):
        users = cls.cur.execute("SELECT login, full_name, name FROM `USERS` u, `ROLES` r  WHERE u.role_ID = r.ID AND r.name=?", (role,))
        return users.fetchall()

    @classmethod
    def insert_user(cls, inp_login, inp_password, inp_full_name, inp_role_ID):
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
        data = cls.cur.execute("SELECT *FROM ?", (table_name,))
        return data.fetchall()
