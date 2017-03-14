from person import Person


class Student(Person):

    def __init__(self, *args):
        Person.__init__(self, *args)