from models.employee import Employee


class Mentor(Employee):

    def __init__(self, *args):
        Employee.__init__(self, *args)