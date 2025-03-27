#!/usr/bin/env python

import requests
import getpass

# Base URL
base_url = "https://amcr.aiscr.cz"

# Authentication
username = input("Enter your username: ")
password = getpass.getpass("Enter your password: ")

# POST request to obtain token
response = requests.post(
    f"{base_url}/api/token-auth/",
    json={
        "username": username,
        "password": password
    }
)

# Extract token from response
token = response.json()['token']

print(token)
