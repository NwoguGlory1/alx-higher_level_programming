#!/usr/bin/python3

def text_indentation(text):
    """
    This is a module that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
    text: This must be a string

    Raises:
    TypeError: text must be a string
    There should be no space at the beginning
    or at the end of each printed line

    Returns:
    text with 2 new lines after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()  # Remove leading and trailing spaces

    if len(text) == 0:
        return None

    result = ""
    newline = False  # To track if a newline is added

    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
            newline = True
        else:
            newline = False

    # If there's no space at the beginning of the line
    if not newline:
        result += "\n"

    print(result, end='')
