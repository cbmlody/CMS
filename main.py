from database import *
import getpass
import ui
import os
import user
from time import sleep


def main():
    list_all = PeopleList()
    list_all.people_list = list_all.import_csv()
    list_all.people_list.append(Manager())
    students_list = []
    students_values = []
    mentors_list = []
    employees_list = []

    for obj in list_all.people_list:
        if obj.__class__.__name__ == "Student":
            students_list.append(obj)

    for obj in list_all.people_list:
        if obj.__class__.__name__ == "Employee":
            employees_list.append(obj)

    for obj in list_all.people_list:
        if obj.__class__.__name__ == "Mentor":
            mentors_list.append(obj)

    for person in students_list:
        students_values.append(person.name)

    while True:
        username = input("Please provide a username: ")
        password = getpass.getpass("Please provide a password: ")
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
                for person in mentors_list:
                    print(person.name)
                input("Press enter to go back")
            elif user_input == "2":
                for person in students_list:
                    print(person.name)
                input("Press enter to go back")
            elif user_input == "3":
                inputs = ui.get_inputs(["username: ", "Fullname: "], "Provide personal information")
                inputs.insert(1, "")
                print(inputs)
                list_all.add("Manager", inputs)
                input("Press enter to go back")
            elif user_input == "4":
                inputs = ui.get_inputs(["username: "], "Provide username to remove")
                list_all.remove("Mentor", inputs[0])
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
                pass
            elif user_input == "2":
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

        if isinstance(login, Mentor):
            list_options = ["List students", "Add assignment", "Grade Assignment","Add student", "Remove student"]
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
        # for person in list_all.people_list:
        #     if person.username == username and person.password == password:
        #         print("Welcome {}".format(person.name))
        # person.__class__.__name__ == "Manager":

    # sleep(5)
    # for person in list_all.people_list:
    #     if person.username == username and person.__class__.__name__ == "Manager":
    #         ui.print_menu("What would you like to do", manager_options, "Exit CcMS")
    #         inputs = ui.get_inputs(["Option: "], "")
    #         option = inputs[0]
    #         if option == "1":
    #             for person in list_all.people_list:
    #                 if person.__class__.__name__ == "Mentor":
    #                     print(person.name)
    #             pass
    #         elif option == "3":
    #             pass

    # inputs = ui.get_inputs(["username: ", "Fullname: "], "Provide personal information")
    # print(inputs)
    # list_all.add("Mentor", inputs)

    # print(list_all.get_list("Student"))
    # print(list_all.people_list)

if __name__ == '__main__':
    main()
