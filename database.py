import time
from user import *

class Database:
    """
    Class represents list of objects
    """
    con = sql.connect('database.db')
    cur = con.cursor()
    # def __init__(self):
    #     self.people_list = []

    def import_sql(self):
        """
        Method import csv with employees, mentors and students and returns list with all objects
        """
        with open('database.sql', 'r') as file:
            self.cur.executescript(file.read())


    # @staticmethod
    # def export_to_csv(filename, data):
    #     """
    #     Writeas data to csv file
    #     :param filename: string with path to file
    #     :param data: data to write
    #     :return: None
    #     """
    #
    #     with open(filename, 'w') as f:
    #         data_writer = csv.writer(f)
    #         for row in data:
    #             data_writer.writerow([row.username, row.password, row.name, row.status])

    @classmethod
    def get_user(cls, username, password):
        log = cls.cur.execute("SELECT ID, role_ID FROM `USERS` WHERE login=? AND password=?",
                              (username, password))
        return log

    @classmethod
    def login(cls, log, username):
        """
        Checks if user exists and can log in

        :param username: string with username
        :param password: string with password
        :return: message
        """
        log = log.fetchall()
        if log:
            role_id = log[0][1]
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
        added_user = Query.insert_user(login, password, full_name, role_ID)
        return added_user
        # if person_type == "Manager":
        #     mentor_to_add = Mentor(*inputs)
        #     self.people_list.append(mentor_to_add)
        # elif person_type == "Mentor":
        #     student_to_add = Student(*inputs)
        #     self.people_list.append(student_to_add)

    @classmethod
    def remove(cls, username):
        """
        :param username:
        :return: None
        """
        to_remove = Query.remove_user(username)
        return to_remove
        # for person in self.get_list(person_type):
        #     if person.username == username:
        #         person.status = "0"


    def update(self):
        pass
