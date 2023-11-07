#!/usr/bin/python3

def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout

    Args:
    filename: the file name
    """
    with open(filename, encoding="utf-8") as myfile:
        line = myfile.readlines()
        for i in line:
            print(i, end='')
