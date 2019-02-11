import re

class Student:
    def __init__(self, name=''):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (type(name) == str) and (re.match("^[A-Za-z ]+$", name)):
            self._name = name
        else:
            raise ValueError("Wrong value")
