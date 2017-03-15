from models.person import Person
import sqlite3 as sql

class Student(Person):

    def __init__(self, *args):
        Person.__init__(self, *args)
