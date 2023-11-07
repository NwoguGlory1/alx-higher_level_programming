#!/usr/bin/python3

class MyList(list):
    """ defines a class """

    def __init__(self):
        """ initializer """
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
