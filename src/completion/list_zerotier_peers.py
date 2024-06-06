import sys
import typing
import json
from tabulate import tabulate
import requests
import re

import vyos.opmode
from vyos.utils.process import cmd
from vyos.configquery import ConfigTreeQuery



def zt_api(url, api_token, api_type):
    if api_type == "service":
        headers = {
            "X-ZT1-Auth": api_token
        }
    elif api_type == "central":
        headers = {
            'Authorization': f'token {api_token}'
        }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx and 5xx)
        return response  # Assuming you want to return the parsed JSON data directly
    except requests.exceptions.HTTPError as http_err:
        exit(f'HTTP error occurred: {http_err}')
    except Exception as err:
        exit(f'Other error occurred: {err}')
    return None  # Return None in case of an error

localNodeList = []

try:
    with open(f'/config/vyos-zerotier/zt1/authtoken.secret', 'r') as file:
        authtoken = file.read()
except FileNotFoundError:
    print('authtoken.secret not found! This should have been created when installing ZeroTier')

network_data = zt_api(f'http://127.0.0.1:9993/peer', authtoken, 'service').json()
for peers in network_data:
    print(json.dumps(peers, indent=4))
    localNodeList.append(peers['address'])
