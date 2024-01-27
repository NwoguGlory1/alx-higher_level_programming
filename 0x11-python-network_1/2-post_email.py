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
        eMail_value = {"email": sys.argv[2]}
        data = urllib.parse.urlencode(eMail_value)
        data = data.encode('ascii')
        req_object = urllib.request.Request(url, data)
        with urllib.request.urlopen(req_object) as response:
            value = response.read().decode('utf-8')
            print(value)
    except:
        pass
