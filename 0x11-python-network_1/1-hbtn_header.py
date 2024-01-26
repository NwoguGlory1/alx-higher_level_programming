#!/usr/bin/python3
"""
Python script that takes in URL, sends a request to it,
displays the value of X-Request-Id variable found in header of the response.
"""
if __name__ == "__main__":
    """ ensures script does not run if imported """
    import urllib.request
    import sys

    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            displayed_value = response.info().get('X-Request-Id')
            print(displayed_value)

    except:
        pass
