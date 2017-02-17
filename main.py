from database import *
from user import *

LIST_TABLE_TITLES = ["Fullname", "username", "Status"]


def main():
    db = Database()
    db.import_sql()
    while True:
        username = input("Please provide a username: ")
        password = input("Please provide a password: ")
        log = db.get_user(username, password)
        login_type = db.login(log, username)
        time.sleep(2)
        if login_type == "Manager":
            while True:
                Manager.menu(log, username)
        elif login_type == "Mentor":
            while True:
                Mentor.menu(log, username)
        elif login_type == "Employee":
            while True:
                Employee.menu()
        elif login_type == "Student":
            while True:
                Student.menu(log, username)


if __name__ == '__main__':
    main()
