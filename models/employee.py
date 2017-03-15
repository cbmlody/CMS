from models.person import Person


class Employee(Person):

    role = 2

    def __init__(self, *args):
        Person.__init__(self, *args)
