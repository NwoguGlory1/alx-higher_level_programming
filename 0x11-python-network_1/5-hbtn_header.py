#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL,
displays the value of the variable X-Request-Id in the response header
"""
if __name__ == "__main__":
    """ ensures script does not run if imported """
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    displayed_value = response.headers.get('X-Request-Id')
    print(displayed_value)
