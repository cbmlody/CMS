from database import *
import getpass
import ui
import os
import hashlib
import datetime
from user import *
import time


LIST_TABLE_TITLES = ["Fullname", "username", "Status"]


def main():
    date = str(datetime.date.today())
    db = Database()
    db.import_sql()
    # list_all.people_list = list_all.import_sql()
    # list_all.people_list.append(Manager())
    # Attendance.import_roll_from_file()
    while True:
        username = input("Please provide a username: ")
        password = input("Please provide a password: ")
        log = db.get_user(username, password)
        login_type = db.login(log, username)
        if login_type == "Manager":
            while True:
                Manager.menu(log, username)
        elif login_type == "Mentor":
            while True:
                print("Mentor")
        elif login_type == "Employee":
            while True:
                print("Employee")
        elif login_type == "Student":
            while True:
                Student.menu(log, username)


            # while True:
            #
            #     if login.__class__.__name__ == "Manager":
            #         list_options = ["List mentors", "List students", "Add mentor", "Remove mentor", "Check attendance"]
            #         ui.print_menu("What would you like to do", list_options, "Exit CcMS")
            #         user_input = input("-> ")
            #
            #         if user_input == "1":
            #             mentors_list = list_all.get_list("Mentor", None)
            #             mentor_data = [[x.name, x.username, x.status] for x in mentors_list]
            #             print(ui.print_table(mentor_data, LIST_TABLE_TITLES))
            #             input("Press enter to go back")
            #
            #         elif user_input == "2":
            #             students_list = list_all.get_list("Student", None)
            #             student_data = [[x.name, x.username, x.status] for x in students_list]
            #             print((ui.print_table(student_data, LIST_TABLE_TITLES)))
            #             input("Press enter to go back")
            #
            #         elif user_input == "3":
            #             inputs = ui.get_inputs(["username: ", "Fullname: "], "Provide personal information")
            #             inputs.insert(1, hashlib.md5("1234".encode('utf-8')).hexdigest())
            #             inputs.insert(3, "1")
            #             list_all.add("Manager", inputs)
            #             PeopleList.export_to_csv("mentors.csv", list_all.get_list("Mentor", None))
            #             input("Press enter to go back")
            #
            #         elif user_input == "4":
            #             inputs = ui.get_inputs(["username: "], "Provide username to remove")
            #             list_all.remove("Mentor", *inputs)
            #             input("Press enter to go back")
            #
            #         elif user_input == "5":
            #             print(Mentor.check_attendance(list_all.get_list("Student"), login.name))
            #             roll.Attendance.save_roll_to_file()
            #             input("Press enter to go back")
            #
            #         elif user_input == "0":
            #             os.system("clear")
            #             break
            #
            #         else:
            #             print("There is no such option")
            #
            #     elif login.__class__.__name__ == "Student":
            #         list_options = ["View my grades", "Submit assignment", "View attendance"]
            #         ui.print_menu("What would you like to do", list_options, "Exit CcMS")
            #         user_input = input("-> ")
            #
            #         if user_input == "1":
            #             print('My grades:')
            #             with open("submited.ccms", "r") as grades:
            #                 for line in grades:
            #                     graded = line.split(":")
            #                     if username == graded[1]:
            #                         print(graded[5])
            #
            #             input("Click to continue")
            #
            #         elif user_input == "2":
            #             dict_assignment = {}
            #             os.system("clear")
            #             with open("assignment_m.ccms", "r") as assign:
            #                 counter = 1
            #                 for line in assign:
            #                     splitted = line.split(";")
            #                     print(counter, ".)", splitted[0])
            #                     dict_assignment[counter] = splitted[0]
            #                     counter += 1
            #
            #             print("Type 0 to exit")
            #             option = int(input("Which assignment do you want to send?: -> "))
            #             link_git = input("Type link to your's project: ")
            #             with open("submited.ccms", "a+") as submited:
            #                 if 0 < option < counter:
            #                     submited.write("0:" + username + ":" + dict_assignment[
            #                         option] + ":" + date + ":" + link_git + "\n")
            #                 elif option == 0:
            #                     break
            #
            #         elif user_input == "3":
            #             print("Roll call: {}".format(x.date for x in login.view_attendance()))
            #             input("Click to continue")
            #
            #         elif user_input == "0":
            #             os.system("clear")
            #             break
            #         else:
            #             print("There is no such option")
            #
            #     elif login.__class__.__name__ == "Mentor":
            #         list_options = ["List students", "Add assignment", "Grade Assignment", "Add student",
            #                         "Remove student", "Check Attendance"]
            #         ui.print_menu("What would you like to do", list_options, "Exit CcMS")
            #         user_input = input("-> ")
            #
            #         if user_input == "1":
            #             students_list = list_all.get_list("Student")
            #             student_data = [[x.name, x.username, x.status] for x in students_list]
            #             print((ui.print_table(student_data, LIST_TABLE_TITLES)))
            #             input("Press enter to go back")
            #
            #         elif user_input == "2":
            #             inputs = ui.get_inputs(["Title: ", "Submission date: ", "Project: ", "Max points: "],
            #                                    "Provide info about assignment")
            #             with open("assignment_m.ccms", "a+") as assign:
            #                 for item in inputs:
            #                     assign.write(item + ";")
            #                 assign.write("\n")
            #
            #         elif user_input == "3":
            #             graded = []
            #             f = open('submited.ccms', 'r')
            #             for line in f:
            #                 to_check = line.split(":")
            #                 if to_check[0] == "0":
            #                     print(to_check[1], "sent", to_check[2], "on", to_check[3], "link: ", to_check[4])
            #                     grade = input("Score: ")
            #                     to_check[0] = "1"
            #                     to_check[4] = to_check[4].rstrip()
            #                     to_check.append(grade)
            #                     line = ":".join(to_check)
            #                     graded.append(line)
            #             f.close()
            #             with open('submited.ccms', 'w') as f:
            #                 for element in graded:
            #                     f.write(element)
            #                     f.write("\n")
            #             input("Ok!")
            #
            #         elif user_input == "4":
            #             inputs = ui.get_inputs(["username: ", "Fullname: "], "Provide personal information")
            #             inputs.insert(1, hashlib.md5("1234".encode('utf-8')).hexdigest())
            #             inputs.insert(3, "1")
            #             list_all.add("Mentor", inputs)
            #             PeopleList.export_to_csv("mentors.csv", list_all.get_list("Mentor", None))
            #             input("Press enter to go back")
            #
            #         elif user_input == "5":
            #             inputs = ui.get_inputs(["username: "], "Provide username to remove")
            #             list_all.remove("Student", *inputs)
            #             input("Press enter to go back")
            #
            #         elif user_input == "6":
            #             print(Mentor.check_attendance(list_all.get_list("Student"), login.name))
            #             roll.Attendance.save_roll_to_file()
            #             input("Press enter to go back")
            #
            #         elif user_input == "0":
            #             os.system("clear")
            #             break
            #
            #         else:
            #             print("There is no such option")
            #
            #     elif login.__class__.__name__ == "Employee":
            #         list_options = ["List students"]
            #         ui.print_menu("What would you like to do", list_options, "Exit CcMS")
            #         user_input = input("-> ")
            #
            #         if user_input == "1":
            #             students_list = list_all.get_list("Student", None)
            #             student_data = [[x.name, x.username, x.status] for x in students_list]
            #             print((ui.print_table(student_data, LIST_TABLE_TITLES)))
            #             input("Press enter to go back")
            #
            #         elif user_input == "0":
            #             os.system("clear")
            #             break
            #
            #         else:
            #             print("There is no such option")


if __name__ == '__main__':
    main()
