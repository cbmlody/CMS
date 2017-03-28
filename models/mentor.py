from models.employee import Employee


class Mentor(Employee):

    role = 1

    def __init__(self, *args):
        Employee.__init__(self, *args)
