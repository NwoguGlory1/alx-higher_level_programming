#!/usr/bin/python3
""" overwrites the content of the byte"""

def write_file(filename="", text=""):
    """write to file

    filename: the filename
    text: the text

    Returns:
    return the number of byte/character written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
