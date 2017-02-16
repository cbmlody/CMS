import time
from user import *

class Database:
    """
    Class represents list of objects
    """
    con = sql.connect('database.db')
    cur = con.cursor()


    def import_sql(self):
        """
        Method import csv with employees, mentors and students and returns list with all objects
        """
        with open('database.sql', 'r') as file:
            self.cur.executescript(file.read())


    @classmethod
    def login(cls, username, password):
        """
        Checks if user exists and can log in

        :param username: string with username
        :param password: string with password
        :return: message
        """
        log = cls.cur.execute("SELECT ID, role_ID FROM `USERS` WHERE login=? AND password=?", (username, password))
        if log:
            role_id = log.fetchall()[0][1]
            role_name = cls.cur.execute("SELECT name FROM `ROLES` r, `USERS` u  WHERE r.ID = ?", (role_id,))
            print("Welcome {}".format(username))
            return role_name.fetchall()[0][0]
        else:
            print("Incorrect username or password")


    @classmethod
    def add(cls, login, password, full_name, role_ID):
        """

        :param login:
        :param password:
        :param full_name:
        :param role_ID:
        :return:
        """
        users = cls.con.execute("SELECT * FROM `USERS`")
        if login not in users.fetchall():
            cls.cur.execute("INSERT INTO `USERS`(login, password, full_name, role_ID) VALUES (?, ?, ?, ?)",
                            (login, password, full_name, role_ID), )
            cls.con.commit()
            return "User successfully added!"
        else:
            return "User exists in database"


    @classmethod
    def remove(cls, username):
        """
        :param username:
        :return: None
        """
        cls.cur.execute("DELETE FROM `USERS` WHERE login = ?", (username,))
        cls.con.commit()
        return "User deleted"


    def update(self):
        self.con.commit()
