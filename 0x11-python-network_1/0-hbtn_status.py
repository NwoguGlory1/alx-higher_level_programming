#!/usr/bin/python3
import urllib.request
if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen('url') as response:
        response.read()
