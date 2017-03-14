from models.person import Person


class Employee(Person):

    def __init__(self, *args):
        Person.__init__(self, *args)