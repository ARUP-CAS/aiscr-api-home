#!/usr/bin/env python
import requests

# Base URL
base_url = "https://amcr.aiscr.cz"

# Token auth
token = input("Enter token: ")

# Headers
headers = {
    "Authorization": f"Bearer {token}"
}

# GET request to obtain user info
response = requests.get(
    f"{base_url}/api/uzivatel-info/",
    headers=headers
)

# Check if the request was successful
if response.status_code == 200:
    # Print the raw XML
    print(response.text)
else:
    print(f"Failed to retrieve user info. Status code: {response.status_code}")
    print(f"Response: {response.text}")
