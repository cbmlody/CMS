import time
import ui
import roll
import sys
import database
from roll import *
from query import *
import os
from assignment import *


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
        self.id = args[0]
        self.username = args[1]
        self.password = args[2]
        self.name = args[3]
        self.status = args[4]  # status = role

    @classmethod
    def get_all(cls):
        data = Query.get_data_by_table_name("USERS")
        all_users = []
        for person in data:
            all_users.append(Manager(data[0], data[1], data[2], data[3]))
        return all_users

    @staticmethod
    def check_password(log, username, user_input_old_password):
        log_value = log.fetchall()
        print(log_value)
        query = database.Database.cur.execute("SELECT password FROM `USERS` WHERE ID = ?", (log_value[0][0]))
        if user_input_old_password == query.fetchall()[0][0]:
            return "correct"
        else:
            return "incorrect"

    @classmethod
    def change_password(cls, new_pass, new_pass2, username):
        """
        Method return password

        :return: password(str)
        """
        if new_pass == new_pass2:
            database.Database.cur.execute("UPDATE `USERS` SET password=? WHERE login=?", (new_pass, username,))
            database.Database.con.commit()
            return "Password changed"
        else:
            return "Passwords don't match"
            # inputs = ui.get_inputs(["password: "], "Type in new password: ")
            # self.password = inputs[0]
            # self.password = hashlib.md5(self.password.encode('utf-8')).hexdigest()

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
        while True:
            list_options = ["List students"]
            ui.print_menu("What would you like to do", list_options, "Exit CcMS")
            user_input = input("-> ")
            if user_input == "1":
                students = Query.get_full_name_login('3')
                list_students = [list(row) for row in students.fetchall()]
                print((ui.print_table(list_students, ['full_name', 'login'])))
                input("Press enter to go back")
            elif user_input == "0":
                sys.exit(0)
            else:
                print("There is no such option")


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
    def check_attendance():
        """
        Checks class attendance
        :param student_list: list of students as objects
        :param who: name of person checking attendance as string
        :return: None
        """
        current_date = time.strftime("%d-%m-%Y")
        try:
            Attendance.import_from_db()
            last_date = database.Database.cur.execute("SELECT date, day_of_school FROM `ATTENDANCES`").fetchone()
            day = last_date[1]
            if last_date[0] != current_date:
                day += 1
        except TypeError:
            day = 1
        students_list = database.Database.cur.execute("SELECT ID, login, password, full_name, role_ID FROM `USERS` WHERE role_ID=3")
        for student in students_list.fetchall():
            student_obj = Student(*student)
            inputs = ui.get_inputs(["Attendance [ 0 / 1 ]: "], "{} is present?".format(student_obj.name))
            att = Attendance(student_obj.name, current_date, int(*inputs), day)
            database.Database.cur.execute("INSERT INTO ATTENDANCES VALUES (?,?,?,?)", (student_obj.id, att.date, att.status, att.day_of_school,))
            database.Database.con.commit()

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

    @staticmethod
    def create_teams(name):
        database.Database.cur.execute("INSERT INTO `TEAMS`(name) VALUES (?)", (name,))
        return "Team added"

    @staticmethod
    def list_teams():
        teams = database.Database.cur.execute("SELECT name FROM `TEAMS`")
        return teams

    @staticmethod
    def grade_checkpoint(username, grade):
        student_id = database.Database.cur.execute("SELECT ID FROM USERS WHERE login = ?", (username,)).fetchall()[0][0]
        database.Database.cur.execute("INSERT INTO `Checkpoints`(`user_ID`, `card`) VALUES (?,?);", (student_id, grade))
        database.Database.con.commit()
        return "Checkpoint graded"

    @staticmethod
    def add_assignment(inp_title, inp_due_date, inp_max_points, inp_as_team):
        database.Database.cur.execute("INSERT INTO `ASSIGNMENTS`(title,due_date,max_points,as_team) VALUES (?, ?, ?, ?)",
                        (inp_title, inp_due_date, inp_max_points, inp_as_team), )
        database.Database.con.commit()
        return "Assignment successfully added!"

    @staticmethod
    def menu(log, username):
        while True:
            list_options = ["List students", "Add assignment", "Grade Assignment", "Add student", "Remove student",
                            "Check Attendance", "Change password", "Create teams", "List teams", "Grade checkpoint",
                            "Students performance"]
            ui.print_menu("What would you like to do", list_options, "Exit CcMS")
            user_input = input("-> ")

            if user_input == "1":
                students = Query.get_full_name_login('3')
                list_students = [list(row) for row in students.fetchall()]
                print((ui.print_table(list_students, ['full_name', 'login'])))
                input("Press enter to go back")
            elif user_input == "2":
                inputs = ui.get_inputs(["Title: ", "Due date: ", "Max points: ", "As team: "], "Provide info about assignment")
                Mentor.add_assignment(inputs[0], inputs[1], inputs[2], inputs[3])
            elif user_input == "3":
                graded = []
                f = open('submited.ccms', 'r')
                for line in f:
                    to_check = line.split(":")
                    if to_check[0] == "0":
                        print(to_check[1], "sent", to_check[2], "on", to_check[3], "link: ", to_check[4])
                        grade = input("Score: ")
                        to_check[0] = "1"
                        to_check[4] = to_check[4].rstrip()
                        to_check.append(grade)
                        line = ":".join(to_check)
                        graded.append(line)
                f.close()
                with open('submited.ccms', 'w') as f:
                    for element in graded:
                        f.write(element)
                        f.write("\n")
                input("Ok!")

            elif user_input == "4":
                data = ui.get_inputs(["login: ", "password: ", "full_name: "], "Please insert all data about student")
                print(database.Database.add(data[0], data[1], data[2], 3))
                input("Press enter to go back")

            elif user_input == "5":
                username_to_del = input("Please insert username to delete: ")
                print(database.Database.remove(username_to_del))
                input("Press enter to go back")

            elif user_input == "6":
                Mentor.check_attendance()
                input("Press enter to go back")

            elif user_input == '7':
                input1 = input("Please enter a new password: ")
                input2 = input("Please repeat your new password: ")
                Person.change_password(input1, input2, username)
                input("Press enter to go back")

            elif user_input == '8':
                team_name = input("What is the name of the new team? ")
                print(Mentor.create_teams(team_name))
                input("Press enter to go back")

            elif user_input == '9':
                teams = Mentor.list_teams()
                list_teams = [list(row) for row in teams.fetchall()]
                print((ui.print_table(list_teams, ['Team name'])))
                input("Press enter to go back")
            elif user_input == '10':
                students = Query.get_full_name_login('3').fetchall()
                logins = []
                for row in students:
                    logins.append(row[1])
                while True:
                    student = input('Whose checkpoint would you like to grade? ')
                    if student not in logins:
                        input('No such student')
                    else:
                        break
                while True:
                    grade = input('Green, yellow or red card? ').lower()
                    if grade not in ['green', 'yellow', 'red']:
                        input("Wrong grade")
                    else:
                        input(Mentor.grade_checkpoint(student, grade))
                        break

            elif user_input == '11':
                students = Query.get_full_name_login('3').fetchall()
                logins = []
                for row in students:
                    logins.append(row[1])
                while True:
                    student = input('Whose performance would you like to see? ')
                    if student not in logins:
                        input('No such student')
                    else:
                        break
                input("Really good performance")

            elif user_input == "0":
                os.system("clear")
                sys.exit(0)

            else:
                print("There is no such option")


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
    def menu(log, username):
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
                Mentor.check_attendance()
                input("Press enter to go back")
            elif user_input == '6':
                pass
            elif user_input == '7':
                pass
            elif user_input == '8':
                input1 = input("Please enter a new password: ")
                input2 = input("Please repeat your new password: ")
                Person.change_password(input1, input2, username)
                input("Press enter to go back")
            elif user_input == '0':
                sys.exit(0)


class Student(Person):
    """
    Class represents every Student
    """

    def __init__(self, *args):
        Person.__init__(self, *args)

    @staticmethod
    def menu(log, username):

        while True:
            list_options = ["View my grades", "Submit assignment", "View attendance", "Submit assignment as a team",
                            "Change password"]
            ui.print_menu("What would you like to do", list_options, "Exit CcMS")
            user_input = input("Input -> ")
            if user_input == '1':
                print("View my grades")
                input("Press enter to go back")
            elif user_input == '2':
                Student.submit_assignment(username)
                input("Press enter to go back")
            elif user_input == '3':
                print("View attendance")
                input("Press enter to go back")
            elif user_input == '4':
                Student.submit_assign_as_team(username)
                input("Press enter to go back")
            elif user_input == '5':
                input1 = input("Please enter a new password: ")
                input2 = input("Please repeat your new password: ")
                Person.change_password(input1, input2, username)
                input("Press enter to go back")
            elif user_input == '0':
                sys.exit(0)

    @staticmethod
    def submit_assignment(username):
        student_id = database.Database.cur.execute("SELECT ID FROM USERS WHERE login = ?", (username,)).fetchall()[0][0]
        assignments_data = database.Database.cur.execute("SELECT * FROM `ASSIGNMENTS` WHERE as_team = 0")
        assignment_ids = []
        for assignment in assignments_data.fetchall():
            print("{}) Title:{} | Due Date: {} | Max points: {} ".format(assignment[0], assignment[1], assignment[2],
                                                                         assignment[3]))
            assignment_ids.append(assignment[0])
        choose = input("Please choose assignment from list -> ")
        if int(choose) in assignment_ids:
            data = ui.get_inputs(["content: ", "date: "], "")
            database.Database.cur.execute("INSERT INTO `SUBMISSIONS`(user_ID, content, date, assignment_ID, team_ID) "
                                          "VALUES(?,?,?,?,?)",(student_id, data[0], data[1], choose, None), )
            database.Database.con.commit()
            print("Assignment add successfully!")
        else:
            print("Your choice is incorrect!")

    @staticmethod
    def submit_assign_as_team(username):
        student_id = database.Database.cur.execute("SELECT ID FROM USERS WHERE login = ?", (username,)).fetchall()[0][0]
        student_team_id = database.Database.cur.execute("SELECT team_ID FROM `USERS` WHERE login = ?", (username,)).fetchall()[0][0]
        assignments_data = database.Database.cur.execute("SELECT * FROM `ASSIGNMENTS` WHERE as_team = 1")
        assignment_ids = []
        for assignment in assignments_data.fetchall():
            print("{}) Title:{} | Due Date: {} | Max points: {} ".format(assignment[0], assignment[1], assignment[2],
                                                                         assignment[3]))
            assignment_ids.append(assignment[0])
        choose = input("Please choose assignment from list -> ")
        if int(choose) in assignment_ids:
            data = ui.get_inputs(["content: ", "date: "], "")
            database.Database.cur.execute("INSERT INTO `SUBMISSIONS`(user_ID, content, date, assignment_ID, team_ID) "
                                          "VALUES(?,?,?,?,?)", (student_id, data[0], data[1], choose, student_team_id), )
            database.Database.con.commit()
            print("Assignment add successfully!")
        else:
            print("Your choice is incorrect!")

    def view_attendance(self):
        """
        Shows attendance
        :return self.attendance: list of Attendance objects
        """
        database.Database.cur.execute("SELECT user_ID FROM `ATTENDANCES` WHERE user_ID")
