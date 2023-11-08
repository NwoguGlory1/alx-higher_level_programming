#!/usr/bin/python3
"""
A  function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    prints content of the text file to stdout

    Args:
    filename: the file name
    """
    with open(filename, encoding="utf-8") as myfile:
        line = myfile.readlines()
        for line in myfile:
            print(line, end='')
