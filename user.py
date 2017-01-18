import random
import string


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
        self.password = args[1]
        self.name = args[2]
        self.status = args[3]

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

    def __init__(self, username, password, name, status=1):
        Person.__init__(self, username, password, name, status)


class Mentor(Employee):
    """
    Class represents every Mentor
    """

    def __init__(self, username, password, name, status=1):
        Employee.__init__(self, username, password, name, status)


class Manager(Employee):
    """
    Class represents every Manager
    """

    def __init__(self, username, password, name, status=1):
        Person.__init__(self, username, password, name, status)
        self.username = "Jerry"
        self.password = "123wer"
        self.name = "Jerzy Mardaus"


class Student(Person):
    """
    Class represents every Student
    """

    def __init__(self, username, password, name, grades, status=1):
        Person.__init__(self, username, password, name, status)
        self.grades = grades.split(';')
