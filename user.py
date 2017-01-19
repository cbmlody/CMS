import ui
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
        self.password = args[1]
        self.name = args[2]
        self.status = "1"

    def change_password(self):
        """
        Method return password

        :return: password(str)
        """
        inputs = ui.get_inputs(["password: "], "Type in new password: ")
        self.password = inputs[0]

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

    @staticmethod
    def check_attendance(student_list):
        """
        Checks class attendance
        :param student_list: list of students as objects
        :return: None
        """

        for student in student_list:
            inputs = ui.get_inputs(["Attendance [ 0 / 1 ]: "], "{} is present?".format(student.name))
            student.attendance.append(roll.Attendance(inputs))

    @staticmethod
    def view_attendance(student, student_list):
        """
        Shows student attendance list
        :param student: student full name
        :param student_list: list of students
        :return student.attendance: list of attendance
        :return: error message
        """
        if student in [stud.name for stud in student_list]:
            return student.attendance
        return "Could not find {} in database, are you sure it's correct value?".format(student)


class Manager(Employee):
    """
    Class represents every Manager
    """

    def __init__(self, username="Jerzy", password="qwe123", name="Jerzy Mardaus", status="1"):
        Person.__init__(self, username, password, name, status)
        self.username = username
        self.password = password
        self.name = name
        self.status = status


class Student(Person):
    """
    Class represents every Student
    """

    def __init__(self, *args, grades=""):
        Person.__init__(self, *args, grades)
        self.grades = grades.split(';')
        self.attendance = []

    def check_grades(self):
        return "Dear {}, your grades are: {}".format(self.name, self.grades)

    def view_attendance(self):
        """
        Shows attendance
        :return self.attendance: list of Attendance objects
        """
        return self.attendance
