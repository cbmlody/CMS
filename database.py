from user import *
import csv


class PeopleList:
    """Class represents list of objects"""
    def __init__(self):
        self.people_list = []

    @staticmethod
    def import_csv():
        """Method import csv with employees, mentors and students and returns list with all objects"""
        imported_list = []
        with open("employees.csv", 'r') as f:
            data = csv.reader(f)
            for person in data:
                imported_list.append(Employee(person[0], person[1], person[2]))

        with open("mentors.csv", 'r') as f:
            data = csv.reader(f)
            for person in data:
                imported_list.append(Mentor(person[0], person[1], person[2]))

        with open("students.csv", 'r') as f:
            data = csv.reader(f)
            for person in data:
                imported_list.append(Student(person[0], person[1], person[2], person[3]))
        return imported_list

    @staticmethod
    def export_to_csv(filename, data):
        with open(filename, 'w') as f:
            data_writer = csv.writer(f)
            for each in data:
                data_writer.writerow(each)

    def get_list(self):


    def add(self):
        pass

    def remove(self):
        pass

    def update(self):
        pass