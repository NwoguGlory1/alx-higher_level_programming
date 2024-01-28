#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL, displays body of the response
...(decoded in utf-8)
"""
if __name__ == "__main__":
    """ ensures script does not run if imported """
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    response.raise_for_status()
    """ raises and HTTP Error. Below is thecontent of response"""
    content = response.text
    print(content)

except requests.exceptions.HTTPError as e:
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        pass
