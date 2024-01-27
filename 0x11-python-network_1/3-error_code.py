#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL, displays body of the response
...(decoded in utf-8)
"""
if __name__ == "__main__":
    """ ensures script does not run if imported """
    import urllib.request
    import sys

    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            value = response.read().decode('utf-8')

    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
