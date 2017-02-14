from user import *
import csv


class PeopleList:
    """
    Class represents list of objects
    """


    def __init__(self):
        self.people_list = []


    def import_csv(self):
        """
        Method import csv with employees, mentors and students and returns list with all objects
        """

        with open("employees.csv", 'r') as f:
            data = csv.reader(f)
            for person in data:
                self.people_list.append(Employee(person[0], person[1], person[2], person[3]))

        with open("mentors.csv", 'r') as f:
            data = csv.reader(f)
            for person in data:
                self.people_list.append(Mentor(person[0], person[1], person[2], person[3]))

        with open("students.csv", 'r') as f:
            data = csv.reader(f)
            for person in data:
                self.people_list.append(Student(person[0], person[1], person[2], person[3], person[4]))
        return self.people_list


    @staticmethod
    def export_to_csv(filename, data):
        """
        Writeas data to csv file
        :param filename: string with path to file
        :param data: data to write
        :return: None
        """

        with open(filename, 'w') as f:
            data_writer = csv.writer(f)
            for row in data:
                data_writer.writerow([row.username, row.password, row.name, row.status])


    def login(self, username, password):
        """
        Checks if user exists and can log in

        :param username: string with username
        :param password: string with password
        :return: message
        """

        for x in self.people_list:
            if x.username == username and x.password == password:
                if x.status == "1":
                    return x
                else:
                    return "Inactive user"


    def get_list(self, person_type, status="1"):
        """
        Returns list of objects of input type
        :param person_type: str
        :param status: str status of person to get
        :return: list of objects
        """

        if status == "1":
            return [x for x in self.people_list if x.__class__.__name__ == person_type and x.status == "1"]
        elif status == "0":
            return [x for x in self.people_list if x.__class__.__name__ == person_type and x.status == "0"]
        elif status == None:
            return [x for x in self.people_list if x.__class__.__name__ == person_type]


    def add(self, person_type, inputs):
        """
        Add new person to database

        :param person_type: class name
        :param inputs: list of inputs
        :return: None
        """

        if person_type == "Manager":
            mentor_to_add = Mentor(*inputs)
            self.people_list.append(mentor_to_add)
        elif person_type == "Mentor":
            student_to_add = Student(*inputs)
            self.people_list.append(student_to_add)


    def remove(self, person_type, username):
        """
        Set user status=0, user is inactive
        :param person_type:
        :param username:
        :return: None
        """
        for person in self.get_list(person_type):
            if person.username == username:
                person.status = "0"


    def update(self):
        pass
