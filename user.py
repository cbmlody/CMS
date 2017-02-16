import ui
import roll
import sys
import database
from roll import *
from query import *



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
        self.status = args[3] # status = role

    @classmethod
    def get_all(cls):
        data = Query.get_data_by_table_name("USERS")
        all_users = []
        for person in data:
            all_users.append(Manager(data[0], data[1], data[2], data[3]))
        return all_users

    def change_password(self, new_pass, new_pass2):
        """
        Method return password

        :return: password(str)
        """
        if new_pass == new_pass2:
            Query.change_password(self.username, new_pass)
        else:
            return "Passwords don't match"
        #inputs = ui.get_inputs(["password: "], "Type in new password: ")
        #self.password = inputs[0]
        #self.password = hashlib.md5(self.password.encode('utf-8')).hexdigest()



    def __str__(self):
        return self.username


class Employee(Person):
    """
    Class represents every Employee
    """

    def __init__(self, *args):
        Person.__init__(self, *args)

    @staticmethod
    def menu():
        list_options = ["List mentors", "List students", "Add mentor", "Remove mentor", "Check attendance",
                        "See student average grade", "See full statistics"]
        ui.print_menu("What would you like to do", list_options, "Exit CcMS")


class Mentor(Employee):
    """
    Class represents every Mentor
    """

    def __init__(self, *args):
        Employee.__init__(self, *args)

    @staticmethod
    def menu():
        list_options = ["List mentors", "List students", "Add mentor", "Remove mentor", "Check attendance",
                        "See student average grade", "See full statistics"]
        ui.print_menu("What would you like to do", list_options, "Exit CcMS")

    @staticmethod
    def check_attendance(student_list, who):
        """
        Checks class attendance
        :param student_list: list of students as objects
        :param who: name of person checking attendance as string
        :return: None
        """
        for student in student_list:
            inputs = ui.get_inputs(["Attendance [ 0 / 1 ]: "], "{} is present?".format(student.name))
            roll.Attendance(student.name, *inputs, who)
        all_students = Query.get_users_by_role(3)
        # for student in all_students:
        #     students_obj = Student()
        #     inputs = ui.get_inputs(["Attendance [ 0 / 1 ]: "], "{} is present?".format(student.))
        # pass

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

    def __init__(self, username, password, name, status):
        Person.__init__(self, username, password, name, status)
        self.username = username
        self.password = password
        self.name = name
        self.status = status

    @staticmethod
    def menu():
        while True:
            list_options = ["List mentors", "List students", "Add mentor", "Remove mentor", "Check attendance",
                            "See student average grade", "See full statistics", "Change your password"]
            ui.print_menu("What would you like to do", list_options, "Exit CcMS")
            user_input = input("Input -> ")
            if user_input == '1':
                mentors = Query.get_full_name_login('1')
                list_mentors = [list(row) for row in mentors.fetchall()]
                print((ui.print_table(list_mentors, ['full_name', 'login'])))
                input("Press enter to go back")
            elif user_input == '2':
                students = Query.get_full_name_login('3')
                list_students = [list(row) for row in students.fetchall()]
                print((ui.print_table(list_students, ['full_name', 'login'])))
                input("Press enter to go back")
            elif user_input == '3':
                data = ui.get_inputs(["login: ", "password: ", "full_name: "], "Please insert all data about mentor")
                print(database.Database.add(data[0], data[1], data[2], 1))
                input("Press enter to go back")
            elif user_input == '4':
                username_to_del = input("Please insert username to delete: ")
                print(database.Database.remove(username_to_del))
                input("Press enter to go back")
            elif user_input == '5':
                all_students = Query.get_users_data_using_roleid("3")
                print(all_students)
                Mentor.check_attendance(all_students)
                input("Press enter to go back")
            elif user_input == '6':
                pass
            elif user_input == '7':
                pass
            elif user_input == '8':
                pass
            elif user_input == '0':
                sys.exit(0)




class Student(Person):
    """
    Class represents every Student
    """

    def __init__(self, *args, grades):
        Person.__init__(self, *args)
        self.grades = grades

    @staticmethod
    def menu():
        list_options = ["List mentors", "List students", "Add mentor", "Remove mentor", "Check attendance",
                        "See student average grade", "See full statistics"]
        ui.print_menu("What would you like to do", list_options, "Exit CcMS")

    def check_grades(self):
        return "Dear {}, your grades are: {}".format(self.name, self.grades.split(";"))

    def view_attendance(self):
        """
        Shows attendance
        :return self.attendance: list of Attendance objects
        """
        return [x.date for x in Attendance.attendance_list if x.name == self.name]



