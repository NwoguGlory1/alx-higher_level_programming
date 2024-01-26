#!/usr/bin/python3
"""
 Python script that fetches https://alx-intranet.hbtn.io/status
 using package, requests
"""
if __name__ == "__main__":
    """ ensures script does not run if imported """
    import requests
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)
    print("Body response:")
    print(f"\t - type: {type(response.text)}")
    print(f"\t - content: {response.text}")
