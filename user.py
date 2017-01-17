import random
import string


class Person:
    """Class represents every user"""
    def __init__(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name

    @staticmethod
    def get_password():

        password = ''
        to_shuffle = []
        lower_letter = string.ascii_lowercase
        upper_letter = string.ascii_uppercase
        digits = string.digits
        for i in range(2):
            to_shuffle.append(random.choice(lower_letter))
            to_shuffle.append(random.choice(upper_letter))
            to_shuffle.append(random.choice(digits))
        random.shuffle(to_shuffle)
        password = ''.join(to_shuffle)
        return password

    def __str__(self):
        return self.username

    def login(self, username, password):
        if username == self.username and password == self.password:
            return "Welcome {}!".format(self.username)
        else:
            return "Username or password is incorrect!"

