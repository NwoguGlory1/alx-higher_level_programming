#!/usr/bin/python3
"""
Python script that takes in a letter, sends a POST request
to http://0.0.0.0:5000/search_user with the letter as arg.
"""

if __name__ == "__main__":
    """ ensures script does not run if imported """
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    try:
        response = requests.post(url, data)
        js = response.json()
        if not js:
            print("No result")
        else:
            print("[{}] {}".format(js.get('id'), js.get('name')))
    except ValueError:
        print("Not a valid JSON")
