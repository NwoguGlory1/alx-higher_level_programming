#!/usr/bin/python3
"""
Script that takes your GitHub credential(username and password)
and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    """ ensures script does not run if imported """
    import requests
    import sys
    from requests.auth import HTTPBasicAuth
    username = sys.argv[1]
    password = sys.argv[2]
    basic = HTTPBasicAuth(username, password)
    r = requests.get('https://api.github.com/user', auth=basic)
    print(r.text)
    try:
        content = r.json()
        print(content.get('id'))
    except ValueError:
        print("Not a valid JSON")
