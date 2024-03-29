#!/usr/bin/python3
""" A  Python script that fetches a url using urllib """

if __name__ == "__main__":
    """ ensures that code will not run if imported """
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
