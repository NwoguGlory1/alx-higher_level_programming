#!/usr/bin/python3
"""
Python script that takes in URL, an email,
sends a POST request to the passed URL with the email
as a parameter, displays body of the response(decoded in utf-8)
"""
if __name__ == "__main__":
    """ ensures script does not run if imported """
    import urllib
    import sys

    try:
        url = sys.argv[1]
        eMail = {"email": sys.argv[2]}
        data = urllib.parse.urlencode(eMail).encode('utf-8')
        req_object = urllib.request.Request(url, data)
        with urllib.request.urlopen(req_object) as response:
            print("Your email is: {}".format(response.read().decode('utf-8')))
    except:
        pass
