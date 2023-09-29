#!/usr/bin/python3
"""
This bash script takes in a URL, sends a request to the URL and displays the body
of the response. It also handles and displays errors.
"""

import requests
import sys

if __name__ == "__main__":
    try:
        res = requests.get(sys.argv[1])
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.RequestException as e:
        if res.status_code >= 400:
            print("Error code:", res.status_code)
