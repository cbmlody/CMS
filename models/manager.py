from employee import Employee


class Manager(Employee):

    role = 0

    def __init__(self, *args):
        Employee.__init__(self, *args)
