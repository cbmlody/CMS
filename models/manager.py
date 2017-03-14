from employee import Employee


class Manager(Employee):

    def __init__(self, *args):
        Employee.__init__(self, *args)