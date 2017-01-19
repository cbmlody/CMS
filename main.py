from database import *
import getpass
import ui
import os
import user
import hashlib
from time import sleep


def main():
    LIST_TABLE_TITLES = ["Fullname", "username", "Status"]
    list_all = PeopleList()
    list_all.people_list = list_all.import_csv()
    list_all.people_list.append(Manager())

    while True:
        username = input("Please provide a username: ")
        password = getpass.getpass("Please provide a password: ")
        password = hashlib.md5(password.encode('utf-8')).hexdigest()

        login = list_all.login(username, password)

        if login == None:
            print("Wrong username or password")

        elif login == "Inactive user":
            print("Your account is inactive")

        else:
            print("Welcome {}".format(login))
            break

    while True:

        if isinstance(login, Manager):
            list_options = ["List mentors", "List students", "Add mentor", "Remove mentor"]
            ui.print_menu("What would you like to do", list_options, "Exit CcMS")
            user_input = input("-> ")

            if user_input == "1":
                mentors_list = list_all.get_list("Mentor")
                mentor_data = [[x.name, x.username, x.status] for x in mentors_list]
                print(ui.print_table(mentor_data, LIST_TABLE_TITLES))
                input("Press enter to go back")

            elif user_input == "2":
                students_list = list_all.get_list("Student")
                student_data = [[x.name, x.username, x.status] for x in students_list]
                print((ui.print_table(student_data, LIST_TABLE_TITLES)))
                input("Press enter to go back")

            elif user_input == "3":
                inputs = ui.get_inputs(["username: ", "Fullname: "], "Provide personal information")
                inputs.insert(1, "")
                inputs.insert(3, "1")
                list_all.add("Manager", inputs)
                # PeopleList.export_to_csv("mentors.csv", list_all.get_list("Mentor"))
                input("Press enter to go back")

            elif user_input == "4":
                inputs = ui.get_inputs(["username: "], "Provide username to remove")
                list_all.remove("Mentor", *inputs)
                input("Press enter to go back")

            elif user_input == "0":
                os.system("clear")
                break

            else:
                print("There is no such option")

        elif isinstance(login, Student):
            list_options = ["View my grades", "Submit assignment"]
            ui.print_menu("What would you like to do", list_options, "Exit CcMS")
            user_input = input("-> ")

            if user_input == "1":
                print(login.check_grades())

            elif user_input == "2":
                pass

            elif user_input == "0":
                os.system("clear")
                break

            else:
                print("There is no such option")

        elif isinstance(login, Mentor):
            list_options = ["List students", "Add assignment", "Grade Assignment", "Add student", "Remove student"]
            ui.print_menu("What would you like to do", list_options, "Exit CcMS")
            user_input = input("-> ")

            if user_input == "1":
                pass

            elif user_input == "2":
                pass

            elif user_input == "3":
                pass

            elif user_input == "4":
                pass

            elif user_input == "5":
                pass

            elif user_input == "0":
                os.system("clear")
                break

            else:
                print("There is no such option")

        elif isinstance(login, Employee):
            list_options = ["List students"]
            ui.print_menu("What would you like to do", list_options, "Exit CcMS")
            user_input = input("-> ")

            if user_input == "1":
                pass

            elif user_input == "0":
                os.system("clear")
                break

            else:
                print("There is no such option")


if __name__ == '__main__':
    main()
