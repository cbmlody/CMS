import random
import string
import roll


class Person:
    """
    Class represents every user
    """

    def __init__(self, *args):
        """
        Person class constructor

        :param username(str): person's username
        :param password: randomly generated password
        :param name: person's full name
        """
        self.username = args[0]
        self.password = Person.get_password()
        self.name = args[1]
        self.status = 1

    @staticmethod
    def get_password():
        """
        Method return random, safe password

        :return: password(str) randomly generated password
        """

        password = ''
        to_shuffle = []
        lower_letter = string.ascii_lowercase
        upper_letter = string.ascii_uppercase
        digits = string.digits
        for i in range(2):
            to_shuffle.append(random.choice(lower_letter))
            to_shuffle.append(random.choice(upper_letter))
            to_shuffle.append(random.choice(digits))
        random.shuffle(to_shuffle)
        password = ''.join(to_shuffle)
        return password

    def __str__(self):
        return self.username


class Employee(Person):
    """
    Class represents every Employee
    """

    def __init__(self, *args):
        Person.__init__(self, *args)


class Mentor(Employee):
    """
    Class represents every Mentor
    """

    def __init__(self, *args):
        Employee.__init__(self, *args)


class Manager(Employee):
    """
    Class represents every Manager
    """

    def __init__(self, username,name, status, password):
        Person.__init__(self, username, password, name, status)
        self.username = "Jerry"
        self.password = "123wer"
        self.name = "Jerzy Mardaus"


class Student(Person):
    """
    Class represents every Student
    """

    def __init__(self, *args, grades=""):
        Person.__init__(self, *args, grades)
        self.grades = grades.split(';')
        self.attendance = Attendance()

    def check_grades(self):
        return "Dear {}, your grades are: {}".format(self.name, self.grades)