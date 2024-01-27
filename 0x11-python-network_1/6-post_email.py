#!/usr/bin/python3
"""
Script that takes in a URL and an email address,
sends a POST request to the passed URL with email as a parameter,
finally displays the body of the response.
"""

if __name__ == "__main__":
    """ ensures script does not run if imported """
    import requests
    import sys
    url = sys.argv[1]
    eMail_value = {"email": sys.argv[2]}
    response = requests.post(url, eMail_value)
    content = response.text
    print(content)
