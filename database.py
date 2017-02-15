from query import *


class Database:
    """
    Class represents list of objects
    """

    # def __init__(self):
    #     self.people_list = []

    def import_sql(self):
        """
        Method import csv with employees, mentors and students and returns list with all objects
        """
        con = sql.connect('database.db')
        with open('database.sql', 'r') as file:
            with con:
                cur = con.cursor()
                for line in file:
                    cur.execute(line)
        con.close()


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

    def login(self, username, password):
        """
        Checks if user exists and can log in

        :param username: string with username
        :param password: string with password
        :return: message
        """
        log = Query.get_user(username, password)
        if log:
            return log
        else:
            return "Incorrect username or password"

        # for x in self.people_list:
        #     if x.username == username and x.password == password:
        #         if x.status == "1":
        #             return x
        #         else:
        #             return "Inactive user"


    def get_list(self, person_type):
        """
        Returns list of objects of input type
        :param person_type: str
        :param status: str status of person to get
        :return: list of objects
        """

        # if status == "1":
        #     return [x for x in self.people_list if x.__class__.__name__ == person_type and x.status == "1"]
        # elif status == "0":
        #     return [x for x in self.people_list if x.__class__.__name__ == person_type and x.status == "0"]
        # elif status == None:
        #     return [x for x in self.people_list if x.__class__.__name__ == person_type]


    def add(self, login, password, full_name, role_ID):
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


    def remove(self, username):
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
